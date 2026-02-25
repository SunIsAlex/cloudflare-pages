# cloudflare-pages

一个基于 Hugo + PaperMod 构建的静态博客站点，部署于 Cloudflare Pages。  
集成自定义 Shortcodes（术语解释弹窗 + Desmos 计算器嵌入）以及扩展模块 hugo-notice-papermod。

---

## 特性

- 基于 Hugo（高性能静态生成）
- 使用 PaperMod 主题
- 适配 Cloudflare Pages 自动部署
- 自定义 Shortcodes：
  - desmos：嵌入 Desmos 计算器
  - term-modal：术语解释弹窗（支持独立 Markdown 文件）
- 依赖模块：
  - hugo-notice-papermod

---

## 环境要求

Hugo 版本必须 ≥ 0.146.0

在 hugo.toml 中：

```toml
[module]
  min_version = "0.146.0"
```

建议使用 Hugo Extended 版本。

检查版本：

```bash
hugo version
```

---

## 本地开发

### 克隆仓库

```bash
git clone https://github.com/SunIsAlex/cloudflare-pages.git
cd cloudflare-pages
```

### 初始化模块

```bash
git submodule update --init --recursive
hugo mod tidy
```

---

## 本地预览

```bash
hugo server -D
```

浏览器访问：

```
http://localhost:1313
```

---

## 构建生产版本

```bash
hugo --minify --gc
```

说明：

- --minify：压缩 HTML / CSS / JS
- --gc：清理未使用缓存资源

默认输出目录：

```
public/
```

---

## Cloudflare Pages 配置

| 项目 | 值 |
|------|------|
| 构建命令 | hugo --minify --gc |
| 输出目录 | public |
| 环境变量 | HUGO_VERSION=0.146.0 |

---

# Shortcodes 使用说明

## 1. Desmos 计算器

用法：

```
<desmos func="函数1|函数2|函数3">
```

示例：

```
<desmos func="y=x^2|y=2x+1|y=sin(x)">
```

说明：

- 使用 | 分隔多个函数
- 自动渲染为嵌入式 Desmos 计算器

---

## 2. term-modal 术语解释弹窗

用法：

```
<term-modal filename="example.mdtext">
```

文件存放位置：

```
assets/md/example.mdtext
```

说明：

- filename 对应 assets/md/ 目录
- 支持 Markdown 语法
- 点击术语后弹出解释框

---

## 项目结构（简化）

```
.
├── assets/
│   └── md/
├── content/
├── layouts/
├── static/
├── hugo.toml
```

---

## 依赖模块

- hugo-notice-papermod

同步模块：

```bash
hugo mod get
hugo mod tidy
```

---

## License

MIT License
