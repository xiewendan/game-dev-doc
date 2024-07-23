import time
import asyncio
import aioredis
import motor.motor_asyncio as motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import functools
import msgpack
import uuid
import json
import base64


# redis

# 1 basic command：SET, GET, DEL, EXISTS, EXPIRE
# 2 diff type: value, int, list, set, hash, sorted set
# 3 transactions, pub sub channel, watch key

"""
modify_event--------------------
                                |
                                V
queryloop --> app cache --> redis cache --> mongo
                                ^
                                |
queryloop1 --> app cahce 1 -----



_queryloop：query by 4s interval
_queryloop1：query by 8s interval
_modify_event：clear the redis cache

see the exec log at the end.
"""

REDIS_FILED_VALUE = "value"
REDIS_FILED_VERSION = "version"

_g_RedisClientObj = None
_g_MongoClientObj = None
_g_MongoDbObj = None


_g_AppCacheObj = {}
_g_AppCacheObj1 = {}

_g_nSecond = 0


async def _Init():
    bInitRedis = await _InitRedisClient()
    if not bInitRedis:
        print("init redis failed")
        exit()
        return False

    bConnected = await _InitDb()
    if not bConnected:
        print("init db failed")
        exit()
        return False

    asyncio.get_event_loop().create_task(_QueryLoop())
    asyncio.get_event_loop().create_task(_QueryLoop1())


async def _InitRedisClient():
    global _g_RedisClientObj
    _g_RedisClientObj = await aioredis.from_url(
        "redis://localhost:6379", encoding="utf-8", decode_responses=True
    )
    if _g_RedisClientObj is None:
        return False

    # print("redis client query value", await _g_RedisClientObj.get("name"))

    return _g_RedisClientObj is not None


async def _InitDb():
    '''init db'''
    global _g_MongoClientObj, _g_MongoDbObj
    szMongoDbIp = "localhost"
    szMongoDbPort = 27017
    szMongoUri = f"mongodb://{szMongoDbIp}:{szMongoDbPort}/"
    print("init db: ", szMongoUri)
    _g_MongoClientObj = AsyncIOMotorClient(szMongoUri, serverSelectionTimeoutMS=2000)
    _g_MongoDbObj = _g_MongoClientObj["test_cache"]

    async def _CheckDbConnected(MongoDbObj: motor_asyncio.AsyncIOMotorDatabase):
        try:
            await MongoDbObj.command("ping")
            return True
        except Exception as e:
            return False

    bDbConnected = await _CheckDbConnected(_g_MongoDbObj)
    if not bDbConnected:
        return False

    # print("db query", await _g_MongoDbObj["cache"].find_one({"name": "xjc"}, {"_id": 0}))

    return True


async def _CheckVersion(dictAppCache, szFunName, args, szVersion):
    print("app cache check version")
    bytesKey = _Pack((szFunName, *args))
    try:
        ResponseObj = await _g_RedisClientObj.hget(bytesKey, REDIS_FILED_VERSION)
    except:
        ResponseObj = None

    bSucceed = ResponseObj == szVersion

    if bSucceed:
        print("check version succeed")
    else:
        print("check version failed")
        if szFunName not in dictAppCache:
            return

        if args in dictAppCache[szFunName]:
            dictAppCache[szFunName].pop(args)


def AppCacheName(dictAppCache):
    def AppCache(funObj):
        @functools.wraps(funObj)
        async def _Wapper(*args, **kwargs):
            szFunName = _GetFuncName(funObj)
            if szFunName not in dictAppCache:
                dictAppCache[szFunName] = {}

            tupleCacheInfo = dictAppCache[szFunName].get(args, None)
            if tupleCacheInfo is not None:
                ValueObj = tupleCacheInfo[0]
                szVersion = tupleCacheInfo[1]
                print("cache hit")
                if szVersion:
                    # 命中，需要远程请求校验版本
                    asyncio.get_event_loop().create_task(_CheckVersion(dictAppCache, szFunName, args, szVersion))
                return ValueObj

            print("cache miss")
            tupleCacheInfo = await funObj(*args, **kwargs)

            dictAppCache[szFunName][args] = tupleCacheInfo

            ValueObj = tupleCacheInfo[0]
            return ValueObj

        return _Wapper

    return AppCache


def _Pack(ValueObj):
    bytesValue = msgpack.packb(ValueObj)
    szValue = base64.b64encode(bytesValue).decode('utf-8')
    return szValue


def _Unpack(szValue: str):
    bytesValue = base64.b64decode(szValue)
    return msgpack.unpackb(bytesValue)


def _GetFuncName(funObj):
    return "__name__"
    # return funObj.__name__  # xjctodo 替换


def RedisCache(funObj):
    @functools.wraps(funObj)
    async def _Wapper(*args, **kwargs):
        szFunName = _GetFuncName(funObj)
        bytesKey = _Pack((szFunName, *args))
        try:
            ResponseValueObj = await _g_RedisClientObj.hgetall(bytesKey)
        except Exception as e:
            ResponseValueObj = None
            print("hget exception:", e)

        if ResponseValueObj:
            print("redis cache hit", bytesKey, ResponseValueObj)
            bytesValue = ResponseValueObj[REDIS_FILED_VALUE]
            ValueObj = _Unpack(bytesValue)
            return ValueObj, ResponseValueObj.get(REDIS_FILED_VERSION, None)

        print("redis cache miss:", bytesKey)
        ValueObj = await funObj(*args, **kwargs)
        print("query from db", ValueObj)
        szVersion = str(uuid.uuid4())
        bytesValue = _Pack(ValueObj)
        print("hset in redis:", bytesKey, {REDIS_FILED_VALUE: bytesValue, REDIS_FILED_VERSION: szVersion})
        await _g_RedisClientObj.hset(bytesKey, mapping={REDIS_FILED_VALUE: bytesValue, REDIS_FILED_VERSION: szVersion})

        return ValueObj, szVersion

    return _Wapper


@AppCacheName(_g_AppCacheObj)
@RedisCache
async def _GetName(szGid):
    DataDocumentObj = await _g_MongoDbObj["cache"].find_one({"id": szGid}, {"_id": 0})
    if DataDocumentObj is None:
        return None
    return DataDocumentObj["name"]


@AppCacheName(_g_AppCacheObj1)
@RedisCache
async def _GetName1(szGid):
    DataDocumentObj = await _g_MongoDbObj["cache"].find_one({"id": szGid}, {"_id": 0})
    if DataDocumentObj is None:
        return None
    return DataDocumentObj["name"]


async def _QueryLoop():
    nLoopCount = 0
    while True:
        await asyncio.sleep(4)
        print(f"{_g_nSecond}=========queryloop, count=", nLoopCount)
        print("name=", await _GetName("1101"))
        nLoopCount += 1


async def _QueryLoop1():
    nLoopCount = 0
    while True:
        await asyncio.sleep(8)
        print(f"{_g_nSecond}=========queryloop1, count=", nLoopCount)
        print("name=", await _GetName1("1101"))
        nLoopCount += 1


async def _ModifyEvent():
    while True:
        await asyncio.sleep(17)
        print(f"{_g_nSecond}================modify event")
        szFunName = _GetFuncName(_GetName)
        args = "1101"
        bytesKey = _Pack((szFunName, args))

        await _g_RedisClientObj.delete(bytesKey)

        # await _g_RedisClientObj.delete('["_GetName", "1101"]')


async def _ClearAppCache():
    while True:
        await asyncio.sleep(20)
        print("================clear app cache")
        _g_AppCacheObj.clear()
        _g_AppCacheObj1.clear()
        print("clear cache")


def _Main():
    global _g_nSecond
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.get_event_loop().create_task(_Init())
    asyncio.get_event_loop().create_task(_ModifyEvent())
    # asyncio.get_event_loop().create_task(_ClearAppCache())

    nStartTime = int(time.time())

    while True:
        time.sleep(0.001)
        _g_nSecond = int(time.time()) - nStartTime
        asyncio.get_event_loop().run_until_complete(asyncio.sleep(0))


if __name__ == "__main__":
    _Main()


"""
4=========queryloop, count= 0
cache miss
redis cache miss kqhfX25hbWVfX6QxMTAx
query from db xjc
hset in redis: kqhfX25hbWVfX6QxMTAx {'value': 'o3hqYw==', 'version': '7d4d5fa7-82b4-4a65-8745-1a73f3fde2ad'}
name= xjc
8=========queryloop1, count= 0
cache miss
redis cache hit kqhfX25hbWVfX6QxMTAx {'value': 'o3hqYw==', 'version': '7d4d5fa7-82b4-4a65-8745-1a73f3fde2ad'}
name= xjc
8=========queryloop, count= 1
cache hit
name= xjc
app cache check version
check version succeed
12=========queryloop, count= 2
cache hit
name= xjc
app cache check version
check version succeed
16=========queryloop1, count= 1
cache hit
name= xjc
app cache check version
check version succeed
16=========queryloop, count= 3
cache hit
name= xjc
app cache check version
check version succeed
17================modify event
20=========queryloop, count= 4
cache hit
name= xjc
app cache check version
check version failed
24=========queryloop1, count= 2
cache hit
name= xjc
app cache check version
check version failed
24=========queryloop, count= 5
cache miss
redis cache miss kqhfX25hbWVfX6QxMTAx
query from db xjc
hset in redis: kqhfX25hbWVfX6QxMTAx {'value': 'o3hqYw==', 'version': 'bb921863-d13c-4ea9-b28b-f0566b8ca63d'}
name= xjc
28=========queryloop, count= 6
cache hit
name= xjc
app cache check version
check version succeed
32=========queryloop1, count= 3
cache miss
redis cache hit kqhfX25hbWVfX6QxMTAx {'value': 'o3hqYw==', 'version': 'bb921863-d13c-4ea9-b28b-f0566b8ca63d'}
name= xjc
32=========queryloop, count= 7
cache hit
name= xjc
app cache check version
check version succeed
34================modify event
36=========queryloop, count= 8
cache hit
name= xjc
app cache check version
check version failed
40=========queryloop1, count= 4
cache hit
name= xjc
app cache check version
check version failed
40=========queryloop, count= 9
cache miss
redis cache miss kqhfX25hbWVfX6QxMTAx
query from db xjc
hset in redis: kqhfX25hbWVfX6QxMTAx {'value': 'o3hqYw==', 'version': '8ce5e786-217c-4227-871d-124968e10f18'}
name= xjc
44=========queryloop, count= 10
cache hit
name= xjc
app cache check version
check version succeed
48=========queryloop1, count= 5
cache miss
redis cache hit kqhfX25hbWVfX6QxMTAx {'value': 'o3hqYw==', 'version': '8ce5e786-217c-4227-871d-124968e10f18'}
name= xjc
48=========queryloop, count= 11
cache hit
name= xjc
app cache check version
check version succeed

"""
