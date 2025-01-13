[TOC]

# 1. 问题

启动服务器，关闭服务等命令太多，不容易记住，用just，可以对命令进行封装，一边用简单的名字包含一系列命令，并且配置文件的所有子目录都可以执行，非常方便

# 2. 解决方案

## 2.1. 安装配置

* 安装参考 [just github](https://github.com/casey/just/blob/master/README.%E4%B8%AD%E6%96%87.md) 预制二进制文件

* 配置 .justfile

  ```sh
  default:
    just help
  
  start:
    start app

  help:
    @echo ""
    @echo "all the self define command"
    @echo "  save -- build save when you modify the save_desc"
    @echo "  build -- build all server"
    @echo "  start -- start the server"
    @echo "  stop -- stop the server"
    @echo "  dump -- print the traceback"
    @echo "  clear -- rm all log and run clear command"
    @echo ""
  ```

# 3. 结论

# 4. 展望

# 5. 文献
