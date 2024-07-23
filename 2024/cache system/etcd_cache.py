import asyncio
import aetcd


async def Main():
    async with aetcd.Client() as EtcdClientObj:
        async for EventObj in await EtcdClientObj.watch(b'key'):
            print(f"watch key value: {EventObj.kv.value}", )


async def Main2():
    async with aetcd.Client() as EtcdClientObj:
        nCount = 0
        while True:
            await asyncio.sleep(1)
            print(f"put key value {nCount}")
            await EtcdClientObj.put(b'key', str(nCount).encode("utf-8"))
            nCount += 1


asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(asyncio.gather(Main(), Main2()))
