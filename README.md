
📄 cloudflare-pages

一个基于 Hugo + PaperMod 构建的静态博客站点，部署于 Cloudflare Pages。
集成自定义 Shortcodes（术语解释弹窗 + Desmos 计算器嵌入）以及扩展模块 hugo-notice-papermod。


---

✨ 特性

⚡ 基于 Hugo（高性能静态生成）

🎨 使用 PaperMod 主题

☁️ 原生适配 Cloudflare Pages 部署

🧩 自定义 Shortcodes：

desmos：嵌入 Desmos 计算器

term-modal：术语解释弹窗（支持独立 Markdown 文件）


📦 依赖模块：

hugo-notice-papermod




---

📦 环境要求

Hugo 版本必须 ≥ 0.146.0

[module]
  min_version = "0.146.0"

建议安装 Hugo Extended 版本。

检查版本：

hugo version


---

🚀 本地开发

1️⃣ 克隆仓库

git clone https://github.com/SunIsAlex/cloudflare-pages.git
cd cloudflare-pages

2️⃣ 初始化模块 / 子模块

如果使用 Git 子模块：

git submodule update --init --recursive

同步 Hugo 模块：

hugo mod tidy


---

🧪 本地预览

hugo server -D

访问：

http://localhost:1313


---

🏗 构建生产版本

项目使用如下构建命令：

hugo --minify --gc

说明：

--minify：压缩 HTML / CSS / JS

--gc：清理未使用缓存资源（garbage collect）


默认输出目录为：

public/


---

☁️ Cloudflare Pages 部署

在 Cloudflare Pages 中配置：

项目	值

构建命令	hugo --minify --gc
输出目录	public
环境变量	HUGO_VERSION = 0.146.0



---

🧩 Shortcodes 使用说明


---

📌 1️⃣ Desmos 计算器

用法

<desmos func="函数1|函数2|函数3">

示例

<desmos func="y=x^2|y=2x+1|y=sin(x)">

说明：

使用 | 分隔多个函数

会自动渲染为嵌入式 Desmos 计算器



---

📌 2️⃣ 术语解释弹窗（term-modal）

用于在文章中插入可点击术语解释弹窗。

用法

<term-modal filename="example.mdtext">

文件存放位置

assets/md/example.mdtext

说明：

filename 对应 assets/md/ 目录下的文件

.mdtext 文件支持 Markdown 语法

内容会在点击术语时以弹窗形式显示



---

📁 项目结构（简化）

.
├── assets/
│   └── md/              # term-modal 内容文件
├── content/             # 博客内容
├── layouts/             # 自定义模板 & shortcodes
├── static/              # 静态资源
├── hugo.toml            # 站点配置


---

📚 依赖模块

hugo-notice-papermod
提供 PaperMod 风格的提示框 / Notice 扩展功能


同步模块：

hugo mod get
hugo mod tidy


---

🛠 常见问题

Q: Cloudflare Pages 构建失败？

确认：

Hugo 版本 ≥ 0.146.0

构建命令为：


hugo --minify --gc


---

📄 License

MIT License


---

