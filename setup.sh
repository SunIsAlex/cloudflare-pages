#!/bin/bash
set -e

# 1. 环境变量设置（确保命令能被找到）
export PATH=$PATH:/usr/local/go/bin:$(pwd)

# 2. 安装 Hugo (直接解压到当前目录，避免 /usr/local/bin 权限问题)
echo "Downloading Hugo v0.157.0..."
curl -L "https://github.com/gohugoio/hugo/releases/download/v0.157.0/hugo_extended_0.157.0_linux-amd64.tar.gz" | tar -xz

# 3. 安装 Golang (使用官方二进制包，比 apt-get 快且稳定)
echo "Downloading Golang..."
curl -L "https://golang.google.cn/dl/go1.22.0.linux-amd64.tar.gz" | tar -xz
# 解压后会有个 go 目录

# 4. 设置临时路径并验证
export PATH=$PATH:$(pwd)/go/bin
./hugo version
go version

# 5. 执行构建 (调用当前目录下的 hugo)
echo "Starting Hugo build..."
./hugo --gc --minify
