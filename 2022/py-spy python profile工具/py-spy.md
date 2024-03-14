## 1. .1. py-spy

>【github项目】 <https://github.com/xiewendan/game-dev-doc/tree/master>

* [py-spy](https://github.com/benfred/py-spy)是一款python的profile工具

* 特性
  * dump：可以把当前堆栈打印出来，方便查死循环的问题
  * record：可以统计一段时间的消耗，并以火焰图的方式呈现，
  * top：可以实时看函数的消耗

* 安装
  * 在linux上，需要用管理员身份安装

    ~~~s
    pip install py-spy
    ~~~

  * windows下，也最好以管理员身份安装。如果安装后运行不了，可以卸载后再重新安装

    ~~~s
    pip uninstall py-spy
    pip install py-spy
    ~~~

* 使用
  * 按时刻截帧

    ~~~s
    py-spy record --pid $PID --rate 250 --native --format speedscope -o profile.speedscope.json
    ~~~

    * rate后面是帧的采样频率，默认是100
    * native表示包含c++的代码
    * pid表示进程id，需要替换
  * 将生成的文件上传到网站`https://www.speedscope.app/`即可查看

* 问题
  * 在python3.10版本是可以正常使用，在python3.11上会报错，报错如下
    Error: Failed to find a python interpreter in the .data section
    * 可能性1，自己编译的python导致的。调整编译方式，能够找到.data
    * 可能性2，py-spy不支持python3.11。确认，官方版本3.11.4存在该问题。 解决方案，切换为3.10来跑
    * 该问题在py-spy的后续版本中修复了
