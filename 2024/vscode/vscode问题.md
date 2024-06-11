## 1. 远程连接报错

在vscode中，使用remote ssh来连接远程服务器，连接失败报错如下：

~~~sh
Permissions for 'E:\\\346\235\250\346\262\233\351\234\226\\ssh_id\\id_rsa' are t
> oo open.
> It is required that your private key files are NOT accessible by others.
> This private key will be ignored.
> Load key "E:\\\346\235\250\346\262\233\351\234\226\\ssh_id\\id_rsa": bad permiss
> ions
> yangpeilin@10.215.249.220: Permission denied (publickey).
> 过程试图写入的管道不存在。
~~~

* 根据报错，发现是id_rsa的权限有问题，在windows下，对于权限理不清楚，直接把文件复制到用户目录下的.ssh文件夹即可
