# 1. ! <https://zhuanlan.zhihu.com/p/637853787>

# 2. 重裝系統后使用chocolate安裝软件

[TOC]
>【github项目】 <https://github.com/xiewendan/game-dev-doc/tree/master>
> 核心亮点，使用了chocolate快速批量安装软件

# 3. 备份

* 备份数据

# 4. 安装软件

* chocolate

* 安装
  * 修改执行策略

    ~~~sh
    管理员启动`windows powsershell`
    set-ExecutionPolicy RemoteSigned
    ~~~

  * 修改`applist.ps1`文件
  * 使用`windows powsershell`执行`applist.ps1`

* 软件配置
  * 浏览器下载路径配置
  * vscode配置同步
  * [cap->ctrl](https://github.com/xiewendan/game-dev-doc/blob/master/2022/windows%E4%B8%AD%E4%BA%92%E6%8D%A2CapLock%E5%92%8CCtrl%E9%94%AE%E4%BD%8D/windows%E4%B8%AD%E4%BA%92%E6%8D%A2CapLock%E5%92%8CCtrl%E9%94%AE%E4%BD%8D.md) 或 直接执行`cap-ctl.reg`

* 卸载
  * 修改applist_uninstall.ps1配置文件
  * 使用`windows powsershell`执行`applist_uninstall.ps1`

# 5. 办公

* 下载工程
