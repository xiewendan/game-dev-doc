#! https://zhuanlan.zhihu.com/p/595740932

# 1. windows上搞个linux系统
[TOC]
>【github项目】 https://github.com/xiewendan/game-dev-doc/tree/master

# 2. 问题

最近疫情，在家办公，家中没有linux系统，得部署一下开发环境，做如下记录

# 3. 解决方案

* linux选择
  * 常规的安装linux的方案有三：
    * wsl
    * 虚拟机
    * 双系统
    
    调研结果，最新的wsl2，其内部原理已经改成虚拟机，鉴于正常开发，需要在windows和linux经常切换，最终考虑采用wsl2

* 安装wsl2
  * 确保[bios虚拟化开启](https://zhuanlan.zhihu.com/p/394990397)
  * [安装wsl2](https://zhuanlan.zhihu.com/p/394990397)
    参考视频 https://space.bilibili.com/364122352/channel/seriesdetail?sid=1734445
  > 注：视频中提到`wsl --install`，只是用于preview，在最新的文档，已经支持wsl2正式版了

* [vscode环境配置](https://www.bilibili.com/video/BV1Zz4y167Vo/?spm_id_from=333.999.0.0&vd_source=a2b56472ff2d43bd075e1fbe889ebd9a)
  
* [zsh配置](https://www.bilibili.com/video/BV1sv41147FS/?spm_id_from=333.999.0.0&vd_source=a2b56472ff2d43bd075e1fbe889ebd9a)

* [docker环境搭建](https://www.bilibili.com/video/BV1nt4y1k7Fy/?spm_id_from=333.999.0.0&vd_source=a2b56472ff2d43bd075e1fbe889ebd9a)
