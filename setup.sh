#!/bin/bash
set -e

# 1. 定义版本
HUGO_VERSION="0.157.0"

# 2. 安装 Hugo Extended
echo "Installing Hugo v${HUGO_VERSION}..."
curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" | tar -xz
mv hugo /usr/local/bin/

# 3. 安装 Golang (用于 Hugo Modules)
echo "Installing Golang..."
apt-get update && apt-get install -y golang

# 4. 验证版本
hugo version
go version

# 5. 执行构建
echo "Starting Hugo build..."
hugo --gc --minify
