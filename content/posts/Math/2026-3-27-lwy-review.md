---
weight : 1000
date : '2026-03-27T22:17:31+08:00'
draft : false
title : '26年3月27日课堂复盘'
---

# 两个重要数列
$n\in N^*$,有以下两个数列:
-  $a_n=(1+\frac{1}{n})^n$
-  $b_n=(1+\frac{1}{n})^{n+1}$

我们有以下两个结论:
1.  $a_n\lt e\lt b_n$
2.  $\{a_n\}$为**递增**数列,$\{b_n\}$为**递减**数列
3.  $\{a_n\},\{b_n\}$**收敛**,$\lim_{n \to \infty} a_n=\lim_{n \to \infty} b_n=e$

我们可以观看**优美的desmos图像**感受性质.
{{<desmos funcs="a_{n}=\left(1+\frac{1}{n}\right)^{n}|b_{n}=\left(1+\frac{1}{n}\right)^{n+1}|y=e">}}

下面进行证明:

先证(1),其等价于:

$$
\begin{gather}
n\ln (1+\frac{1}{n})\lt 1 \lt (n+1)\ln (1+\frac{1}{n})\\
\frac{1}{n+1}\lt\ln (1+\frac{1}{n})\lt \frac{1}{n} \\
这其实就是对数不等式链的核心:\\
x^2-x\ge xlnx\\\ge x-1\ge lnx\ge 1-\cfrac{1}{x}\\\ge \cfrac{lnx}{x}(x=0,x\gt 0)
\end{gather}
$$

对于(2),其证明有两大类流派:

## 恒等变形(~~导就完了~~)

$\{a_n\}$为**递增**数列,等价于:

$$
\begin{gather}
n\ln (1+\frac{1}{n})\lt (n+1)\ln (1+\frac{1}{n+1})\\
\frac{\ln (1+\frac{1}{n})}{\frac{1}{n}}\lt \frac{\ln (1+\frac{1}{n+1})}{\frac{1}{n+1}}\\
[一解]\\
构造函数:f(x)=\frac{\ln(x+1)}{x}(0\lt x\le 1)\\
f'(x)=\frac{\frac{x}{x+1}-ln(x+1)}{x^2}\\
注意到:\ln (x+1)\gt \frac{x}{x+1}(x\gt 0),有:\\
f'(x)\lt 0,f(x)单调递减,又:\\
\frac{1}{n}\gt \frac{1}{n+1}\\
证明完毕.\\
[另解]\\
构造函数g(x)=x[\ln(x+1)-\ln x](x\ge 1)\\
g'(x)=\ln \frac{x+1}{x}+\frac{x}{x+1}-1\\\gt 1-\frac{x}{x+1}+\frac{x}{x+1}-1=0\\
于是g(x)单调递增,Q.E.D.
\end{gather}
$$

可以发现,对此题,需要进行换元的方法未必比更直接的方法简便.主要问题还是在于,学会对**对数+分式型函数**求导.

18．（13 分）（2015 • 北京）已知函数 \( f(x) = \ln \left( \frac{1 + x}{1 - x} \right) \)，\( x \in (-1, 1) \)。  
（Ⅰ）求曲线 \( y = f(x) \) 在点 \( (0, f(0)) \) 处的切线方程；  
（Ⅱ）求证：当 \( x \in (0, 1) \) 时，\( f(x) > 2x \)；  
（Ⅲ）设实数 \( k \) 使得 \( f(x) > kx \) 对 \( x \in (0, 1) \) 恒成立，求 \( k \) 的最大值。

# 不等放缩

$$
(1+\frac{1}{n})^n\lt (1+\frac{1}{n+1})^{n+1}\\
根据"项数不够就凑一"原则:\\
1(1+\frac{1}{n})^n\lt (\frac{1+n(1+\frac{1}{n})}{n+1})^{n+1}=RHS\\
(1+\frac{1}{n})^{n+1}\gt (1+\frac{1}{n+1})^{n+2}\\
与均值不等式的不等号方向相反,所以取倒数:\\
即证:(\frac{n}{n+1})^{n+1}\lt (\frac{n+1}{n+2})^{n+2}\\
1(\frac{n}{n+1})^{n+1}\lt (\frac{1+(n+1)\frac{n}{n+1}}{n+2})^{n+2}=RHS
$$

用这种方法,可以证明**伯努利不等式**:
$$
x\gt -1,n\in N^*,则:
(1+x)^n\ge 1+nx\\
(当且仅当x=0或n=1时等号成立)\\
\underbrace{1 \times 1 \times \cdots \times 1}_{n-1 \text{ 个}}(1+nx)\\\le (\frac{1\times (n-1)+1+nx}{n})^n=LHS
$$

---

有了(1)(2)两个结论,根据**单调有界定理**即证(3)


