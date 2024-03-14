# 1. 初始化debian

[TOC]

------------------------------------------------------------------------------

## 1.1. 问题

* 新申请的阿里云服务器，希望启动一个python相关的服务，需要配置相关环境，这里做简要介绍

------------------------------------------------------------------------------

## 1.2. 思路

* 强大的shell工具--zsh
* 多版本的python管理方案
* supervisor的配置

------------------------------------------------------------------------------

## 1.3. 解决方案

### 1.3.1. 安装源管理

  ~~~sh
  # update source, update source, can easily install app
  apt update
  ~~~

### 1.3.2. 安装配置zsh

* 参考文献：[zsh安装和配置](https://www.bilibili.com/video/BV1sv41147FS/?spm_id_from=333.999.0.0&vd_source=a2b56472ff2d43bd075e1fbe889ebd9a)

* 安装zsh相关

    ~~~sh
    # 安装git
    apt install git
    # 安装zsh
    apt install zsh
    # 安装oh-my-zsh
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    # 安装zhs-autosuggestions
    cd ~/.oh-my-zsh/plugins
    git clone https://github.com/zsh-users/zsh-autosuggestions.git
    # 安装autojump
    apt install autojump
    ~~~

* 配置

    ~~~sh
    # 默认启动zsh
    vim ~/.bashrc
    export SHELL='which sh'
    zsh
    exit

    # zsh添加插件zhs-autosuggestions
    vim ~/.zshrc
    plugins=(
          git
          zsh-autosuggestions
          autojump
    )
    ~~~

### 1.3.3. python

> the advantage of installing python from source code is we can easily manage different version of python

#### 1.3.3.1. prepare

* we need install a lot of lib before build python

  ~~~sh
  # for _ctypes module
  apt-get install libffi-dev
  # for _uuid module
  apt-get install uuid-dev
  # for _bz2
  apt-get install libbz2-dev
  # for _dbm
  apt-get install libgdbm-dev
  # for _gdbm
  apt-get install libgdbm-compat-dev
  # for _lzma
  apt-get install liblzma-dev
  # for _tkinter
  apt-get install tk-dev
  # for nis
  apt-get install libnsl-dev
  # for readline
  apt-get install libreadline-dev

  # for download openssl and build openssl
  # curl -o openssl-3.2.0.tar.gz https://www.openssl.org/source/openssl-3.2.0.tar.gz
  # ./config
  # make -j100
  apt install libssl-dev

  ~~~

#### 1.3.3.2. Download Python Source Code

* Go to the Python downloads page (<https://www.python.org/downloads/source/>) and get the source code for the version you want to build.

#### 1.3.3.3. Extract the Source Code

* Use a tool like tar to extract the downloaded source code:

  ~~~sh
  tar -xzf Python-3.x.x.tgz
  cd Python-3.x.x
  ~~~

#### 1.3.3.4. Configure the Build

* Run the following commands to configure the build:

  ~~~sh
  ./configure
  ~~~

  * --enable-optimizations: all stable optimizations active (PGO, etc)
  > apt install libssl-dev, so no need --with-openssl=/root/app/openssl/openssl-3.2.0: install requests

* If you want to customize the build, you can use options such as --prefix to specify the installation directory.

#### 1.3.3.5. Build and Install

* Run the following commands to build and install Python:

  ~~~sh
  make -j100
  ~~~

#### 1.3.3.6. install lib

~~~sh
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
~~~

### 1.3.4. supervisor

* in supervisor.conf

  ~~~sh
  command=%(ENV_PYTHON)s main_frame/main.py flask_server 0.0.0.0 5000
  ~~~

  * use ENV_PYTHON, it means you should define PYTHON env，in superviosr，you need to add "ENV_" prefix to the env var.
  
### 1.3.5. mongo

* [mongo](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian-tarball/)
