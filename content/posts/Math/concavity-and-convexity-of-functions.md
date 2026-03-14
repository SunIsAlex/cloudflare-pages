---
weight : 1000
date : '2026-03-09T20:51:00+08:00'
draft : false
title : '浅谈函数的凹凸性'
categories : ['高联一试']
tags : ['导数']
---
# 函数的凹凸性 (Convexity and Concavity of Functions)

## 1. 基于二阶导数的定义 (Second Derivative Test)

设函数 $f: I \subset \mathbb{R} \to \mathbb{R}$ 在区间 $I$ 上二阶可导：

- **上凸函数 (Convex Up / Concave)** 如果
  $$f''(x) \ge 0, \quad \forall x \in I,$$
  则称 $f$ 在 $I$ 上是 **上凸 (convex up)** 或 **凹的 (concave)**。

- **下凸函数 (Convex Down / Convex)** 如果
  $$f''(x) \le 0, \quad \forall x \in I,$$
  则称 $f$ 在 $I$ 上是 **下凸 (convex down)** 或 **凸的 (convex)**。

> 注：这里 $f''(x) = 0$ 时，函数可能是线性。

---

## 2. 基于琴生不等式 (Jensen's Inequality)

设 $f: I \subset \mathbb{R} \to \mathbb{R}$ 是定义在凸集 $I$ 上的函数：

- **上凸函数 (Convex Up / Concave)** 对任意 $x_1, x_2 \in I$ 和 $\lambda \in [0,1]$：
  $$f(\lambda x_1 + (1-\lambda) x_2) \ge \lambda f(x_1) + (1-\lambda) f(x_2)$$
  则 $f$ 是 **上凸 (convex up)** 或 **凹函数 (concave)**。

- **下凸函数 (Convex Down / Convex)** 对任意 $x_1, x_2 \in I$ 和 $\lambda \in [0,1]$：
  $$f(\lambda x_1 + (1-\lambda) x_2) \le \lambda f(x_1) + (1-\lambda) f(x_2)$$
  则 $f$ 是 **下凸 (convex down)** 或 **凸函数 (convex)**。

---

## 3. 基于切线位置的定义 (Tangential Property)
{{< notice info >}}
此方法可以加强琴生不等式(**拓宽变量范围**)
{{< /notice >}}
设函数 $f: I \subset \mathbb{R} \to \mathbb{R}$ 在区间 $I$ 上可导。通过比较曲线与其在任意点 $x_0 \in I$ 处的切线 $L(x) = f(x_0) + f'(x_0)(x - x_0)$ 的相对位置来定义：

- **上凸函数 (Convex Up / Concave)** 如果曲线始终位于切线的**上方**（或重合）：
  $$f(x) \ge f(x_0) + f'(x_0)(x - x_0), \quad \forall x, x_0 \in I$$
  则称 $f$ 是 **上凸 (convex up)** 或 **凹函数 (concave)**。

- **下凸函数 (Convex Down / Convex)** 如果曲线始终位于切线的**下方**（或重合）：
  $$f(x) \le f(x_0) + f'(x_0)(x - x_0), \quad \forall x, x_0 \in I$$
  则称 $f$ 是 **下凸 (convex down)** 或 **凸函数 (convex)**。

---

## 4. 对比总结 (Comparison)

| 方法 (Method) | 上凸函数条件 (Convex Up / Concave) | 下凸函数条件 (Convex Down / Convex) | 注释 (Notes) |
| :--- | :--- | :--- | :--- |
| **二阶导数** | $f''(x) \ge 0$ | $f''(x) \le 0$ | 局部微分条件 |
| **琴生不等式** | $f(\text{内分点}) \ge \text{函数值的内分}$ | $f(\text{内分点}) \le \text{函数值的内分}$ | 割线在曲线下方/上方 |
| **切线位置** | $f(x) \ge \text{切线函数}$ | $f(x) \le \text{切线函数}$ | 曲线在切线上方/下方 |

我们采取**定义一**,将定义二作为**导出结论**

# 利用二阶导数证明琴生不等式 (Jensen's Inequality)

### 1. 构造辅助函数
设定目标函数 $f(x)$ 为二阶可导函数，且满足 $f''(x) > 0$（即 $f(x)$ 为严格凸函数）。

为了证明对于 $\lambda \in [0, 1]$，有 $f(\lambda x_1 + (1-\lambda)x_2) \le \lambda f(x_1) + (1-\lambda)f(x_2)$，我们固定 $x_1$ 和 $\lambda$，构造关于 $x$ 的辅助函数 $F(x)$：

$$F(x) = f(\lambda x_1 + (1-\lambda)x) - \lambda f(x_1) - (1-\lambda)f(x)$$

### 2. 求导分析
对 $F(x)$ 关于 $x$ 求一阶导数：
$$F'(x) = (1-\lambda) f'(\lambda x_1 + (1-\lambda)x) - (1-\lambda)f'(x)$$
提取公因子后得：
$$F'(x) = (1-\lambda) \left[ f'(\lambda x_1 + (1-\lambda)x) - f'(x) \right]$$

**已知条件：** 若 $f''(x) > 0$，则 $f'(x)$ 在定义域上单调递增。

---

### 3. 分情况讨论单调性

#### 情况一：当 $x < x_1$ 时
1. **变量位置：** 此时 $\lambda x_1 + (1-\lambda)x$ 是 $x_1$ 和 $x$ 的加权平均值，由于 $x < x_1$，则有：
   $$x < \lambda x_1 + (1-\lambda)x < x_1$$
2. **导数符号：** 因为 $f'(x)$ 单调递增，所以 $f'(\lambda x_1 + (1-\lambda)x) > f'(x)$。
3. **结论：** 此时 $F'(x) > 0$，函数 $F(x)$ 单调递增。

#### 情况二：当 $x > x_1$ 时
1. **变量位置：** 由于 $x > x_1$，加权平均值满足：
   $$x_1 < \lambda x_1 + (1-\lambda)x < x$$
2. **导数符号：** 因为 $f'(x)$ 单调递增，所以 $f'(\lambda x_1 + (1-\lambda)x) < f'(x)$。
3. **结论：** 此时 $F'(x) < 0$，函数 $F(x)$ 单调递减。

---

### 4. 最终结论
计算 $F(x)$ 在 $x = x_1$ 处的值：
$$F(x_1) = f(\lambda x_1 + (1-\lambda)x_1) - \lambda f(x_1) - (1-\lambda)f(x_1) = 0$$

由单调性可知，$F(x)$ 在 $x = x_1$ 处取得极大值（也是最大值）$0$。
因此，对于任意的 $x_2$，均有：
$$F(x_2) \le F(x_1) = 0$$

代入 $F(x)$ 的定义式并移项，得证：
$$f(\lambda x_1 + (1-\lambda)x_2) \le \lambda f(x_1) + (1-\lambda)f(x_2)$$
等号成立时当且仅当$x_1=x_2$
# 利用 $n=2$ 结论证明 $n$ 元琴生不等式

### 1. 前提结论（已证）
已知对于 $f''(x) > 0$ 的凸函数，二元琴生不等式成立：
$$f(\lambda x_1 + (1-\lambda)x_2) \le \lambda f(x_1) + (1-\lambda)f(x_2) \quad \text{其中 } \lambda \in [0, 1]$$

### 2. 核心思想：整体代换法
我们将 $n$ 个变量的加权平均拆分为：**第 $n$ 个变量** 与 **前 $n-1$ 个变量构成的整体**。

设 $\sum_{i=1}^n \lambda_i = 1$。令 $L = \sum_{i=1}^{n-1} \lambda_i$，则有 $L + \lambda_n = 1$。
$n$ 元组合式可以改写为：
$$\sum_{i=1}^n \lambda_i x_i = \left( \sum_{i=1}^{n-1} \lambda_i x_i \right) + \lambda_n x_n = L \cdot \left( \sum_{i=1}^{n-1} \frac{\lambda_i}{L} x_i \right) + \lambda_n x_n$$

### 3. 推导步骤

#### 第一步：应用二元结论（降维）
令 $X_{n-1} = \sum_{i=1}^{n-1} \frac{\lambda_i}{L} x_i$，这是一个新的自变量。此时原式变为二元加权：
$$f\left( L \cdot X_{n-1} + \lambda_n x_n \right)$$
由于 $L + \lambda_n = 1$，直接套用 **$n=2$** 的结论：
$$f(L \cdot X_{n-1} + \lambda_n x_n) \le L \cdot f(X_{n-1}) + \lambda_n f(x_n)$$

#### 第二步：迭代展开
现在我们需要处理 $f(X_{n-1})$，即：
$$f\left( \sum_{i=1}^{n-1} \frac{\lambda_i}{L} x_i \right)$$
注意到这里的系数和 $\sum_{i=1}^{n-1} \frac{\lambda_i}{L} = \frac{L}{L} = 1$，它依然符合琴生不等式的形式，但规模缩小到了 $n-1$。

通过重复上述“提取最后一个变量”的操作：
1. 将 $n-1$ 元拆解为 $(n-2)$ 的整体与第 $n-1$ 个变量，应用一次 $n=2$ 结论。
2. 将 $n-2$ 元进一步拆解...
3. 直到最后拆解为 $n=2$。

#### 第三步：代回原式
经过层层拆解（或利用归纳法思想），最终所有项都会被展开为：
$$f\left( \sum_{i=1}^n \lambda_i x_i \right) \le L \cdot \left[ \sum_{i=1}^{n-1} \frac{\lambda_i}{L} f(x_i) \right] + \lambda_n f(x_n)$$
消去分母上的 $L$：
$$f\left( \sum_{i=1}^n \lambda_i x_i \right) \le \sum_{i=1}^{n-1} \lambda_i f(x_i) + \lambda_n f(x_n) = \sum_{i=1}^n \lambda_i f(x_i)$$

### 4. 结论
只要二元形式（$n=2$）成立，就可以通过**将前 $k$ 项看作整体**的方式，像**剥洋葱**一样把不等式推广到任意 $n$ 元情况。
等号成立时当且仅当$x_1=x_2=...=x_n$
# 实战应用

从感性的角度认识,函数的凹凸性(或者说琴生不等式)其实描绘的是,自变量集中时和自变量分散时的函数值大小:
1. 对于上凸函数,自变量**集中**时函数值会比较**大**,自变量**分散**时函数值会比较**小**
2. 下凸函数,Vice Versa

以下两种情况琴生不等式适用:
1.  化乘法为加法(取对数)
2.  变量分离(单元函数)

举些例子具体说明一下:

### 小试牛刀
1.设$A=\sqrt[3]{3-\sqrt[3]{3}}+\sqrt[3]{3+\sqrt[3]{3}},B=2\sqrt[3]{3}$,比较A,B大小.
$B\gt A$,证明从略

2.$A,B,C为三角形的内角,证明:sinA+sinB+sinC\ge \frac{3\sqrt{3}}{2}$

3.$A,B,C$为锐角三角形的内角,证明:

(1)$cosA+cosB+cosC\le \frac{3}{2}$
(2)$tanA+tanB+tanC\ge 3\sqrt{3}$

4.用**广义**琴生不等式证明**广义**均值不等式:

$\sum_{i=1}^n \lambda_i = 1,\lambda_i\ge 0,a_i\ge0,则\prod_{i=1}^n a_i^{\lambda_i}\le \sum_{i=1}^n a_i\lambda_i$

提示:$f(x)=\ln x$
### 渐入佳境

1.(2022北京)已知函数 $f(x) = e^x \ln(1 + x)$．

（Ⅰ）求曲线 $y = f(x)$ 在点 $(0, f(0))$ 处的切线方程；

（Ⅱ）设 $g(x) = f'(x)$，讨论函数 $g(x)$ 在 $[0, +\infty)$ 上的单调性；

（Ⅲ）证明：对任意的 $s, t \in (0, +\infty)$，有 $f(s + t) > f(s) + f(t)$．

解析:注意到$f(0)=0$,所以(II)等价于$f(0) + f(s + t) > f(s) + f(t)$
相当于自变量越分散,函数值越大,这是**下凸函数**的特征.

$f'(x)=e^x(\ln(x+1)+\cfrac{1}{x+1})$

$f''(x)=e^x(\ln(x+1)+\cfrac{2}{x+1}-\cfrac{1}{(x+1)^2})=e^x(\ln(x+1)+\cfrac{2x+1}{(x+1)^2})\gt 0(x\ge 0)$

剩下的仿照琴生不等式**主元法**证明,洒洒水的事:

令 $m(x) = f(x+t) - f(x) - f(t) \quad (x > 0)$,

则 $m'(x) = f'(x+t) - f'(x) = g(x+t) - g(x)$,

由 (Ⅱ) 中 $g(x)$ 在 $[0, +\infty)$ 上单调递增，则由 $t > 0$ 得 $s+t > s$, 则 $g(x+t) > g(x)$ 即 $m'(x) > 0$,

说明 $m(x)$ 在 $[0, +\infty)$ 上单调递增.

再由 $s > 0$ 得 $m(s) > m(0)$, 即 $f(s+t) - f(s) - f(t) > f(0+t) - f(0) - f(t) = -f(0)$,

由 (Ⅰ) 中 $f(0) = 0$ 得 $f(s+t) - f(s) - f(t) > 0$,

所以 $f(s+t) > f(s) + f(t)$ 成立.

事实上,根据二元均值不等式,有:

$f(s+t) > f(s) + f(t) \ge f(\frac{s+t}{2}) (当且仅当s=t时取等)$

2.已知正数$a_i(i=1,2,...,n)满足\sum^{n}_{i=1}{a_i}=1,求证\prod^{n}_{i=1}{a_i+\frac{1}{a_i}}\ge(n+\frac{1}{n})^n$


### 证法一：教科书解析版

**题目：** 设 $f(x) = \ln(x + \frac{1}{x})$，证明对任意 $a, b \in (0, 1)$，有 $\frac{\ln(a + \frac{1}{a}) + \ln(b + \frac{1}{b})}{2} \geqslant \ln(\frac{a+b}{2} + \frac{2}{a+b})$。

**证明过程：**

即证：$(a + \frac{1}{a})(b + \frac{1}{b}) \geqslant (\frac{a+b}{2} + \frac{2}{a+b})^2$
即：$ab + \frac{1}{ab} + \frac{a}{b} + \frac{b}{a} \geqslant (\frac{a+b}{2})^2 + \frac{4}{(a+b)^2} + 2$  —— $(*)$

又 $\frac{a}{b} + \frac{b}{a} \geqslant 2$，$ab \leqslant (\frac{a+b}{2})^2$
并且 $y = x + \frac{1}{x}$ 在 $(0, 1]$ 为单调递减函数，
所以由 $ab \leqslant (\frac{a+b}{2})^2$ 可得 $ab + \frac{1}{ab} \geqslant (\frac{a+b}{2})^2 + \frac{1}{(\frac{a+b}{2})^2} = (\frac{a+b}{2})^2 + \frac{4}{(a+b)^2}$
从而 $(*)$ 式成立。所以 $f(x) = \ln(x + \frac{1}{x})$ 在 $(0, 1)$ 内为下凸函数。

由**琴生不等式**（Jensen's Inequality）：


$$\frac{1}{n} \sum_{i=1}^{n} \ln(a_i + \frac{1}{a_i}) \geqslant \ln\left(\frac{\sum_{i=1}^{n} a_i}{n} + \frac{n}{\sum_{i=1}^{n} a_i}\right) = \ln(n + \frac{1}{n})$$


（注：此处对应 $\sum a_i = 1$ 的特定情况）

---

### 证法二：手写推导版（利用导数验证凸性）

**已知：** $a_i > 0, \sum_{i=1}^{n} a_i = 1$
**求证：** $\prod_{i=1}^{n} (a_i + \frac{1}{a_i}) \geqslant (n + \frac{1}{n})^n$

**证明过程：**

令 $f(x) = \ln(x + \frac{1}{x})$，对其求导：


$$f'(x) = \frac{1}{x + \frac{1}{x}} \cdot (1 - \frac{1}{x^2}) = \frac{x}{x^2 + 1} \cdot \frac{x^2 - 1}{x^2} = \frac{x^2 - 1}{x(x^2 + 1)}$$

当 $x \in (0, 1)$ 时：
$x^2 - 1 < 0$ 且 $x(x^2 + 1) > 0$，故 $f'(x) < 0$，函数单调递减。

继续考察 $f'(x)$ 的单调性（即 $f(x)$ 的凸性）：
对于 $x_1 < x_2 < 1$，通过对比可知 $f'(x_1) < f'(x_2)$，即 $f'(x)$ 在 $(0, 1)$ 上单调递增。
因此 $f''(x) > 0$，说明 $f(x)$ 在 $(0, 1)$ 上是**下凸函数**。

根据**琴生不等式**：


$$\sum_{i=1}^{n} f(a_i) \geqslant n f\left(\frac{\sum a_i}{n}\right)$$

$$\ln \prod_{i=1}^{n} (a_i + \frac{1}{a_i}) \geqslant n \ln\left(\frac{1}{n} + \frac{1}{1/n}\right) = n \ln(n + \frac{1}{n}) = \ln(n + \frac{1}{n})^n$$

去对数得：


$$\prod_{i=1}^{n} (a_i + \frac{1}{a_i}) \geqslant (n + \frac{1}{n})^n$$


证毕。

一般来说,往往**取倒数**或**取相反数**可以改变不等号的方向:

3.(北大保送生考试)已知正实数$b_1,b_2,...,b_n$满足$\sum_{i=1}^n b_i=1$,证明:

$$ \frac{1}{n}\le \prod_{i=1}^n b_i^{b_i}\le \sum_{i=1}^n b_i^2$$

首先注意到取等条件是**变量全部相等**,显然需要**取自然对数**.

$$ -\ln n\le \sum_{i=1}^n(b_i\ln b_i)\le \ln(\sum_{i=1}^n b_i^2)$$

右边是好证的,使用**广义琴生不等式**即可.

左边可以用$f(x)=x\ln x$的**琴生不等式**证明,但实际上不必如此繁,**取相反数**后相当于:

$$\ln n\ge \sum_{i=1}^n(b_i\ln \frac{1}{b_i})$$

其实就是$f(x)=\ln x$的琴生不等式(但是不等号方向发生了改变)

