---
weight : 1000
date : '2026-02-23T17:10:57+08:00'
draft : false
title : '泰勒展开'
cover :
   image: 'https://alexsun-imgbed.pages.dev/file/AgACAgEAAyEGAATlvtEQAAMEaZ7DPsesCdz-WKPDRVt395X2u5sAAp0LaxtpMvlEXE1vShVv74oBAAMCAAN5AAM6BA.jpeg'
---

# 泰勒公式

## 高数知识

泰勒 (Taylor) 公式的主要作用是用多项式逼近函数和近似计算，对应的分别是带有皮亚诺余项的泰勒公式和带有拉格朗日余项的泰勒公式。

### 1. 带有皮亚诺余项的泰勒公式

若函数 \( f(x) \) 在点 \( x_0 \) 处存在直至 \( n \) 阶导数，则有
\[f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \cdots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n + o((x - x_0)^n).\]

用得较多的是泰勒公式在 \( x_0 = 0 \) 时的特殊形式：
\[f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n + o(x^n).\]

它也称为 (带有皮亚诺余项的) {{<term-modal file="taylor-expansion.mdtext" id="taylor expansion">}}麦克劳林 (Maclaurin) 公式。{{</term-modal>}}

### 2. 带有拉格朗日余项的泰勒公式

若函数 \( f(x) \) 在 \([a, b]\) 上存在直至 \( n \) 阶的连续导函数，在 \((a, b)\) 内存在 \( n+1 \) 阶导函数，则对任意给定的 \( x, x_0 \in [a, b] \)，至少存在一点 \(\xi \in (a, b)\)，使得
\[f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \cdots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}.\]

当 \( x_0 = 0 \) 时，得到
\[f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n + \frac{f^{(n+1)}(\theta x)}{(n+1)!}x^{n+1} \quad (0 < \theta < 1).\]

它也称为 (带有拉格朗日余项的) 麦克劳林公式。

---

考虑**含拉格朗日余项**的麦克劳林公式,可以判断泰勒展开式与被展开函数的大小关系:

特别地,对于\(e^x\),它的n+1阶展开求导后就是n阶展开的导数(可以从积分的角度理解),并且存在"穿回穿回"的规律性:

\(e^x\ge 1(x\ge 0)\)

\(e^x\ge x+1\)

\(e^x\ge \cfrac{1}{2}x^2+x+1(x\ge 0)\)

{{< desmos funcs="y=e^x|y=1|y=x+1|y=(1/2)x^2+x+1" >}}
...

同理,对于\(sinx,cosx\)的泰勒展开,也可以类似的理解推导,并且判断展开式与函数的大小关系.

积分操作往往可以达到强化不等式的效果:

## 0线不等式
1.  \(e^x+e^{-x}\ge 2\)
2.  \(e^x-e^{-x}\ge 2x(x\ge 0)\)
   (Source:2007年全国I卷理科)
3.  \(e^x+e^{-x}\ge x^2+2\)  
4.  \(e^x-e^{-x}\ge 2(x+\cfrac{x^3}{6})(x\ge 0)\)

另一组实例:
1. \(xe^x\ge x\)
2. \((x-1)e^x\ge \cfrac{1}{2}x^2-1(x\ge 0)\)

## 1线不等式
-  \(e^x\)
   1. \(e^{x-1}\ge x\)
   2. \(e^{x}\ge ex\)
   3. \(e^x\ge \cfrac{e}{2}x^2+\cfrac{e}{2}\)
-  \(lnx\)
     1.  \(x^2-x\ge xlnx\ge x-1\ge lnx\ge 1-\cfrac{1}{x}\ge \cfrac{lnx}{x}(x=0,x\gt 0)\)
     2.  飘带函数
         - \(\cfrac{1}{2}(x-\cfrac{1}{x})\lt lnx\lt \cfrac{2(x-1)}{x+1},x\lt 1\)
         - \(\cfrac{1}{2}(x-\cfrac{1}{x})\gt lnx\gt \cfrac{2(x-1)}{x+1},x\gt 1\)

泰勒展开式的**堆砌组合**:

1. \(x\in[0,+\infty),e^x-x-2+cosx\ge0\)
2. \(e^x\gt lnx+2\)

**变量代换**也可以进一步强化不等式:

{{< notice info >}}
注意**自变量**的取值范围
{{< /notice >}}

在\(lnx\lt \cfrac{1}{2}(x-\cfrac{1}{x}),x\gt 0中,带入\sqrt{x},有lnx\lt \sqrt{x}-\cfrac{1}{\sqrt{x}},x\gt 0\)

(1)函数\(f(x)=xe^x-x-ln(x)\)的最小值

(2)函数\(f(x)=\cfrac{e^x}{x}-x+ln(x)\)的最小值

{{< collapse summary=查看答案 >}}
(1)1 (2)e-1
{{< /collapse >}}
二者的**外层函数**都是\(g(t)=e^t-t\),但是t的取值范围不同.

(1)\(x\ge 0,e^x-ax^2-x-1\ge 0\)恒成立,求\(a\)的取值范围
(2)\(x\in R,e^x-ax^2-x-1\ge 0\)恒成立,求\(a\)的取值范围

{{< collapse summary=查看答案 >}}
(1)\((-\infty,\cfrac{1}{2}]\)  (2)\((-\infty,0]\)

(1)是泰勒展开式

(2)涉及到极点效应(\(x=0\)为零点)
{{< /collapse >}}

