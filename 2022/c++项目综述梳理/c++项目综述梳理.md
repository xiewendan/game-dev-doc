#! https://zhuanlan.zhihu.com/p/599058277
# 1. c++项目综述梳理

[TOC]

>【github项目】 https://github.com/xiewendan/game-dev-doc/tree/master

# 2. 问题

c++项目开发遇到比较多的问题，在此做一些综述性的梳理

# 3. 思路

*   基本规范
    *   如何写出高质量c++代码
    *   如何整理代码
*   编译调试
    *   如何编译c++项目
    *   如何调试c++项目
*   问题处理
    *   如何查闪退
    *   内存泄漏问题处理
    *   性能profile和优化

# 4. 解决方案

## 4.1. 基本规范

### 4.1.1. 如何写出高质量c++代码

*   c++语言，相比其它语言，具备较高的性能，但其内存管理上，比较容易出错，导致crash，因此需要深入学习c++，结合实践和工具，才能写出质量的c++代码

*   学习书籍推荐
    *   c++ primer书：系统介绍c++的语法
    *   effective c++：c++易错的写法，帮你总结出来

*   风格指南
    *   [google开源项目风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/)，包含了不同语言的风格指南
    *   保持统一的风格指南，更易阅读代码
    *   风格指南主要是编码的一些约定，涵盖范围很广
        *   排版：空格、空行、缩进等约定
        *   命名规范，是统一变量的命名。通常采用驼峰 szObjName或是下划线隔开 sz\_obj\_name
            *   这里推荐用\[变量范围限制]\[类型名前缀]\[变量名]\[类型名后缀]
                *   变量范围限制: m\_(成员变量), g\_(全局变量)，s\_(静态变量)
                *   类型名前缀：n(整数), d(double), f(float), sz(string)，b(bool)
                *   变量名：ObjName, Player等
                *   类型后缀：如果是对象类型，通常没有类型前缀，因此会加一个后缀，比如Obj，表明这是一个对象
        *   推荐写法
            *   可以减少比较多的错误，比如虚函数类，析构函数需要虚析构等等

*   工具
    *   windows上的ide，推荐用visual studio，vscode
    *   风格指南，如果没有检查工具的支持，是很难落地，并团队推广
        *   排版
            *   通常可以自动格式化
            *   格式化工具：vscode + C/C++ extension(Microsoft) + .clang\_format
                *   .clang\_format生成可以用`clang-format -style=google -dump-config > .clang-format` \[3]
                *   C/C++ extension(Microsoft)配置
                    "C\_Cpp.formatting": "clangFormat",
                    "C\_Cpp.clang\_format\_style": "file",
        *   命名规范：cppcheck里面有一个naming插件，在上面做一些修改，就可以进行前面命名检查
        *   推荐写法：用静态代码检查工具找出有问题的代码
            *   静态代码检查工具\[1]
            *   google的c++编码规范，配套工具是cpplint，原理是基于正则表达式匹配
            *   cppcheck侧重代码逻辑，可以和cpplint一起用，相互补充，原理是基于正则表达式匹配
                *   vscode + C/C++ Advanced Lint插件，可以整合cppcheck和clang
            *   clang-tidy采用基于语法分析书的静态代码检查，慢但检查更准确和全面
                *   clang-tidy基于compile\_commands.json，因此需要在cmake的编译选项添加-DCMAKE\_EXPORT\_COMPILE\_COMMANDS=ON
                *   到compile\_commands.json同目录下，执行`run-clang-tidy`，即可得到结果
                > 注 C/C++ Advanced Lint中的clang静态检查和clang-tidy的检查有什么区别?

### 4.1.2. 如何整理代码

*   整理代码的目标是什么？代码可读性
*   需要整理的内容：目录、文件、类、接口（是否可以删除，是否清晰，const引用）、实现
*   什么时候整理代码
    *   一般开发过程中会整理
    *   最后会从整体上进行一次整理（这会更全面）。
    *   后面回过头来看，不好看懂，还可以继续整理

> 推荐书籍: [《重构--改善既有代码的设计》](https://book.douban.com/subject/30468597/)

## 4.2. 编译调试

### 4.2.1. 如何编译c++项目

*   cmake可以方便做到跨平台编译，只需要写好cmake的配置文件即可。详细使用参看官方文档\[4]

### 4.2.2. 如何调试c++项目

*   使用gdb调试源码或coredump
    *   调试源码: `gdb exe`
    *   调试coredump: `gdb exe -c coredump`
    > gdb官方文档\[5]

## 4.3. 问题处理

### 4.3.1. 如何查闪退

*   一般闪退会有coredump，参看前面调试coredump的方式

### 4.3.2. 内存泄漏问题处理

*   valgrind查看内存泄漏
    valgrind --leak-check=full ./exe

### 4.3.3. 性能profile和优化

*   gperftools + graphviz \[6]
    *   gperftools采样的方式，得到profile结果
    *   graphviz可以将profile结果可视化的方式显示出来

# 5. 结论

本文将列举了常用的c++工具，可以帮助解决c++项目中遇到的问题

# 6. 文献

* [1] [C++静态代码检查工具？](https://www.zhihu.com/question/22178103?sort=created)
* [2] [c++静态代码工具总结](http://blog.guorongfei.com/2018/11/24/static-analizer/)
* [3] [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html)
* [4] [CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
* [5] [Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb/)
* [6] [使用 gperftools 进行 C++ 代码性能分析](https://zhuanlan.zhihu.com/p/539840046)

> 上述工具基本使用，参看官方网站，另外，可以在B站上面找找使用资料


