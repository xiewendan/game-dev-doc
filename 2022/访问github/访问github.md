#! https://zhuanlan.zhihu.com/p/595739702

# 1. 访问github

[TOC]
>【github项目】 https://github.com/xiewendan/game-dev-doc/tree/master

# 2. 问题

国内访问github非常不方便

# 3. 思路

* 用代理
* 用加速器

# 4. 解决方案

## 4.1. 加速器
* 加速器: [Watt Toolkit](https://steampp.net/)，原名叫steam++，发现可以用来加速github，果断下载并试用，可以访问，就是速度慢一点。
  * 当前文档目录放了一个已经下载好的版本 `Steam  _win_x64_v2.8.6.exe`

* 直接试用gitee替换掉github
  * gitee国内访问很快，可以方便用来提交和下载
  * gitee提供了[仓库镜像功能](https://gitee.com/help/articles/4336#article-header0)，可以将gitee的仓库，自动同步到github上

* 使用[fastgithub](https://github.com/dotnetcore/FastGithub)

## 4.2. 代理

### 4.2.1. 机场推荐列表

* [clashnode](https://clashnode.xyz/) 五星推荐 
  * 包含了各种机场
  * 翻墙后可以访问的网站

* [爱机场](https://aijichang.com/)
  * 翻墙机场评测网站

### 4.2.2. 代理软件
* [v2rayN](https://github.com/2dust/v2rayN)
* wgetcloud自带的软件

### 4.2.3. wsl配置
* 在wsl中希望访问github，需要额外配置，以便wsl中可以利用windows上的代理，访问github
  [wsl2配置代理](https://www.cnblogs.com/tuilk/p/16287472.html)

  * windows：代理软件，允许局域网
  * windows：开启防火墙
  * wsl：配置协议
    ~~~
    export hostip=$(cat /etc/resolv.conf |grep -oP '(?<=nameserver\ ).*')
    export https_proxy="http://${hostip}:7890";
    export http_proxy="http://${hostip}:7890";
    ~~~
    > 这里设置端口和代理软件，允许局域网的端口要一致
### 4.2.4. 阿里linux 配置
* [linux下配置V2ray作为客户端来访问GitHub、G*le等服务](https://www.witersen.com/?p=1408)
  * 启动v2ray
    ~~~
    ./v2ray -config config.json
    ~~~

  * 配置代理 .bashrc
    ~~~sh
    # set proxy
    function setproxy() {
        export http_proxy=socks5://127.0.0.1:10808
        export https_proxy=socks5://127.0.0.1:10808
        export ftp_proxy=socks5://127.0.0.1:10808
        export no_proxy="172.16.x.x"
    }
    ​
    # unset proxy
    function unsetproxy() {
        unset http_proxy https_proxy ftp_proxy no_proxy
    }
    ~~~

# 5. 结论

* &#9733;&#9733;&#9733;&#9733;&#9733; 通过代理访问github
* &#9733;&#9733;&#9733;&#9733;&#9734; 暂时利用Watt Toolkit去访问github上别人的项目
* &#9733;&#9733;&#9734;&#9734;&#9734; 自己的项目提交到gitee，并自动同步到github上