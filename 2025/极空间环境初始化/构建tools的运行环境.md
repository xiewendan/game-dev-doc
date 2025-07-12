[TOC]

# 1. 问题

目前需要有一个linux环境，运行现有的tools工具环境，希望在家里的极空间上通过docker部署debian，然后运行tools项目

# 2. 思路

* 安装debian
  * bashrc
  * apt安装源
* 常用软件安装
  * git
  * zsh
  * just
  * tmux
* tools运行环境
  * python
  * supervisor

# 3. 解决方案

## 3.1. debian

* 由于docker hub访问问题，所以，国内找了一个可用的debian的镜像下载网站
  * <https://docker.aityp.com/image/docker.io/library/debian:12>

* apt安装源设置为国内

  ~~~sh
  # edit /etc/apt/sources.list， apt update 失败，需要将https替换成http试一下
  deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free non-free-firmware
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free non-free-firmware
  deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free non-free-firmware
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free non-free-firmware
  deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free non-free-firmware
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free non-free-firmware
  deb https://mirrors.tuna.tsinghua.edu.cn/debian-security/ bookworm-security main contrib non-free non-free-firmware
  # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security/ bookworm-security main contrib non-free non-free-firmware
  ~~~

  ~~~sh
  # 在安装这些后，，可以把http再改回https
  apt install openssl ca-certificates 
  apt install certbot 
  ~~~

* 中文显示问题
  * 需要安装中文包，并设置采用zh_CN.UTF-8

    ~~~sh
    # 安装中文包
    apt install locales
    apt install fonts-wqy-microhei fonts-wqy-zenhei
    
    # 配置local
    dpkg-reconfigure locales
    选择zh_CN.UTF-8 UTF-8
    # 设置环境变量：~/.bashrc添加下面配置
    export LANG=zh_CN.UTF-8 
    export LC_ALL=zh_CN.UTF-8
    ~~~

    > 设置完需要重启ssh控制台

## 3.2. 安装常用软件

* git

  ~~~sh
  apt install git
  ~~~

* zsh
  [安装配置zsh](../../2023/阿里云服务器初始化/初始化debian%20on%20阿里云.md)
  
* just
  [安装just](../../2025/just/just.md)

* tmux
  [安装tmux](../../2025/tmux/tmux.md)
  
  * 极空间中tmux的窗口太小的问题

    ~~~sh
    stty rows 50 cols 225
    export LINES=50
    export COLUMNS=225
    export TERM=xterm-256color
    ~~~

## 3.3. tools运行环境

* python
  [安装python](../../2023/阿里云服务器初始化/初始化debian%20on%20阿里云.md)

* supervisor

  ~~~sh
  apt install supervisor
  ~~~
