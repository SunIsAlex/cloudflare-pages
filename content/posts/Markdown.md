---
date : '2026-02-02T15:49:00+08:00'
draft : false
title : 'Markdown'
description: "by Alex"
categories : ['网站建设']
featured_image: "/images/hero.png"
---

>[Markdown](https://www.markdown.cn/docs/intro/)是一种轻量级标记语言，旨在让用户以易读易写的纯文本格式编写文档，并能够轻松转换为HTML等格式。

# 一、一级标题
用`#` 可以表示**一级标题**
## 二、级标题
用`##` 可以表示**二级标题**
### 三、级标题
用`###` 可以表示**三级标题**

分界线
---
用`---`表示**分界线**
**四、文本格式**  
用 `**粗体**` 或 `__粗体__` 表示**粗体**  
用 `*斜体*` 或 `_斜体_` 表示*斜体*  
用 `~~删除线~~` 表示~~删除线~~  

**五、列表**  
无序列表用 `*`,`+` 或 `-` 开头：  
* 项目一  
+ 项目二  
  - 子项目（缩进两个空格）  

有序列表用数字加英文句点：  
1. 第一项  
2. 第二项  
   1. 子项（缩进三个空格）  

**六、链接与图片**  
用 `[链接文本](网址)` 表示[链接](https://example.com)  
用 `![图片描述](图片地址)` 插入图片：  
![示例图片](https://picsum.photos/100/50)  

**七、引用**  
用 `>` 表示引用块：  
> 这是引用内容  
> 多行引用可连续使用 >  

**八、代码**  
行内代码用 \`反引号\` 包裹：例如 `print("Hello")`  
代码块用三个反引号 + 语言标识：  
````latex
```语言名称

代码内容
```
````
```python
def hello():
    print("Hello Markdown!")
```

```c
int main(){
    printf("Hello Markdown!")
    return 0;
}
```

**九、表格**  
用竖线 `|` 分隔列，连字符 `-` 分隔表头与内容：  
| 左对齐 | 居中对齐 | 右对齐 |  
| :--- | :---: | ---: |  
| 单元格 | 单元格 | 单元格 |  

**十、任务列表**  
用 `- [ ]` 或 `- [x]` 表示任务：  
- [ ]未完成  
- [x] 已完成  

**十一、脚注**  
用 `[^1]` 标注脚注位置，在文末用 `[^1]:` 定义内容[^1]。  

**十二、数学公式（部分平台支持）**  
行内公式：\( E=mc^2 \)

```latex
$E=mc^2$ 
```

块公式：

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}  
$$

```latex
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

*LaTex*公式同样可以用于化学（方程）式的书写

如果使用MathJax，应[安装mhchem拓展](https://bixuebihui.com/demo/chem/mhchem-demo.html)

```latex
$\ce{HNO3}$
```

$$ \ce{HNO3} $$

```latex
$$ \ce{2H2(g) + O2(g) ->[点燃] 2H2O(l)} $$
$$ \ce{CO2(g) + H2O(l) <=> H2CO3(aq)} $$
$$ K_{a}=\cfrac{[\ce{H2CO3}]}{[\ce{CO2}][\ce{H2O}]} $$
$$ \ce{Na2SO4} + \ce{BaCl2} = \ce{BaSO4 v} + 2\ce{NaCl} $$
$$ \ce{CaCO3} + 2\ce{HCl} = \ce{CO2 ^} + \ce{CaCl2} + \ce{H2O} $$
$$ \ce{^37SSO3^2-} + 2\ce{H+} = \ce{SO2 ^} + \ce{^37S v} + \ce{H2O} $$
% 注释："上吐下泻"
```

$$ \ce{2H2(g) + O2(g) ->[点燃] 2H2O(l)} $$
$$ \ce{CO2(g) + H2O(l) <=> H2CO3(aq)} $$
$$ K_{a}^{θ}=\cfrac{[\ce{H2CO3}]}{[\ce{CO2}][\ce{H2O}]} $$
$$ \ce{Na2SO4} + \ce{BaCl2} = \ce{BaSO4 v} + 2\ce{NaCl} $$
$$ \ce{CaCO3} + 2\ce{HCl} = \ce{CO2 ^} + \ce{CaCl2} + \ce{H2O} $$
$$ \ce{^37SSO3^2-} + 2\ce{H+} = \ce{SO2 ^} + \ce{^37S v} + \ce{H2O} $$

---

**十三、HTML标签**

有些MarkDown编辑器支持嵌入HTML标签（Hugo需单独设置允许HTML）
```HTML
<details>
    <summary>双击展开</summary>
    <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=80433022&bvid=BV1GJ411x7h7&cid=137649199&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</details>
```
<details>
    <summary>单击展开</summary>
    <p>你 被 骗 了</p>
    <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=80433022&bvid=BV1GJ411x7h7&cid=137649199&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</details>

---
```HTML
<button type='button'>一个按钮</button>
<!-- Hugo把Markdown渲染成HTML后，button的样式可能和默认不同 -->
```

<button type='button' onclick='alert("我被点了")' style="appearance: auto;
    font-style: ;
    font-variant-ligatures: ;
    font-variant-caps: ;
    font-variant-numeric: ;
    font-variant-east-asian: ;
    font-variant-alternates: ;
    font-variant-position: ;
    font-variant-emoji: ;
    font-weight: ;
    font-stretch: ;
    font-size: ;
    font-family: ;
    font-optical-sizing: ;
    font-size-adjust: ;
    font-kerning: ;
    font-feature-settings: ;
    font-variation-settings: ;
    font-language-override: ;
    text-rendering: auto;
    color: buttontext;
    letter-spacing: normal;
    word-spacing: normal;
    line-height: normal;
    text-transform: none;
    text-indent: 0px;
    text-shadow: none;
    display: inline-block;
    text-align: center;
    cursor: default;
    box-sizing: border-box;
    background-color: buttonface;
    margin: 0em 0em 0em 0em;
    padding-block: 1px;
    padding-inline: 6px;
    border-width: 2px;
    border-style: outset;
    border-color: buttonborder;
    border-image: initial;">一个按钮</button>

> 提示：不同平台（如GitHub、博客系统）对Markdown的扩展支持可能略有差异。

注：鄙人使用Hugo搭建了本网站。Hugo默认不支持LaTex数学公式，故鄙人参考了[此教程](https://gohugo.com.cn/content-management/mathematics/)

[^1]: 这是脚注的示例内容。
