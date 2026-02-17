---
date : '2026-02-03T10:35:29+08:00'
draft : false
title : 'Linux常用命令'
categories : ["Linux命令"]
---

# 文件管理
1. cat\(concatenate\)
    ```shell
    cat [options] [file]
    ```
    | options | description |
    | :---: | --- |
    | -n | 显示行号，会在输出的每一行前加上行号 |
    | -b | 显示行号，但只对非空行进行编号 |
    | -s | 压缩连续的空行，只显示一个空行 |
    | -E | 在每一行的末尾显示 $ 符号 |
    | -T | 将 Tab 字符显示为 ^I |
    | -v | 显示一些非打印字符 |

    PS:
    * 以上的options是大小写不敏感的\(capital insensitive\)
    * 可以有多个file
    
    ## Example
    ```
        root@datacon-winterc:~/quickstart# touch filename #创建filename文件
        root@datacon-winterc:~/quickstart# cat > filename #把标准输入重定向到filename文件
        test_message
        ^C
        root@datacon-winterc:~/quickstart# cat filename #查看filename文件
        test_message
        root@datacon-winterc:~/quickstart# cat /dev/null > filename
        #清空filename文件
    ```

    cat也可以用来制作/烧录镜像文件
    ```shell
    cat /dev/fd0 > OUT.img
    cat OUT.img > /dev/fd0
    ```

2. tar
```shell
root@datacon-winterc:~/quickstart# tar --help
Usage: tar [OPTION...] [FILE]...
```
```shell
touch a.c       
tar -czvf test.tar.gz a.c
//压缩 a.c文件为test.tar.gz
//-z for gzip
```
```shell
tar -tzvf test.tar.gz //列出压缩文件内容
tar -xzvf test.tar.gz a.c //解压文件
//-f for list, -x for extract
```