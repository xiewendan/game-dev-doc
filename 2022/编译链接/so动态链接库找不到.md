#! https://zhuanlan.zhihu.com/p/637854965

# 1. so动态链接库找不到
[TOC]
>【github项目】 https://github.com/xiewendan/game-dev-doc/tree/master

# 2. 问题背景

* 目录结构
  ~~~
  Server/Logic/main.py
  Server/GameCpp/Binary/libGameCore.so
  Server/GameCpp/Binary/Physx.so
  Server/GameCpp/Binary/PxFoundation.so
  ~~~

* 相关依赖
  main.py在运行的时候会加载libGameCore.so，libGameCore.so依赖Physx.so和PxFoundation.so

* 启动
  当前目录是在`Server/Logic/`目录下

  运行`main.py`，用cffi加载libGameCore.so，加载过程报错，说Physx.so文件找不到或不存在

# 3. 解决过程

* 利用ldd找so文件
  ~~~
  cd Server/GameCpp/Binary

  ldd libGameCore.so
  ~~~

  显示他依赖的库，并且可以找到

  ~~~
  Physx.so->./Physx.so
  PxFoundation.so->./PxFoundation.so
  ~~~

* 这里就很奇怪，为啥ldd找的到，cffi就找不到呢，实在不是很清楚，这里一开始怀疑是Physx.so编译有问题，路子就错了

* 这里的问题，本质是涉及共享库查找过程存在问题，去chatgpt查找对应的信息
  * linux so库的查找顺序是怎么样
    1、去程序已经指定的路径中查找，即so文件中的runpath，可以通过readelf so文件 | grep runpath
    2、环境变量LD_LIBRARY_PATH中查找
    3、去系统默认的路径中查找
       ~~~
       /lib
       /usr/lib
       /ect/ld.so.conf
       ~~~
    4、去缓存路径中查找 /etc/ld.so.cache
    * so中的runpath可以在编译的时候指定rpath制定，修改cmake即可。其中\$ORIGIN，表示和so同目录查找动态链接库
      set_target_properties(libGameCore PROPERTIES LINK_FLAGS "-Wl,-rpath,\$ORIGIN")

* 基于以上的知识，有几种解决方案

  * 1、修改cmake，加上ORIGIN，如上
  * 2、在LD\_LIBRARY\_PATH中添加so的路径
  * 3、去修改ld.so.cache

  最后，选择cmake，比较合适

