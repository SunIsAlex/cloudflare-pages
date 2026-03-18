---
weight: 1000
date : '2026-02-10T17:31:25+08:00'
draft : false
title : '每日艺题 DAY001'
categories: ["每日艺题"]
tags: ["数学","数列"]
---
# \(S_{n},a_{n}\)联袂数列(无通项)
**题目：**  
>已知 \(\{a_n\}\) 是各项均为正数的无穷数列,其前 \(n\) 项和为 \(S_n\),且  
\[
a_n + S_n = a_n S_n \quad (n \in \mathbb{N}^*)
\]  
给出下列四个结论：
① \(a_2 = \sqrt{2}\)；  
② 存在一个正数 \(m_0\),使得对任意的 \(n \in \mathbb{N}^*\),都有 \(S_n < m_0\)；  
③ 数列 \(\{a_n\}\) 单调递减；  
④ 对任意的 \(n \in \mathbb{N}^*\),\(n \geq 2\),都有 \(a_{n-1} + a_{n+1} > 2a_n\)。  
其中所有正确结论的序号是___。
(SRC:北京101中2025-2026第一学期高三数学统练二)

先算几项,寻找规律：
| n | \(a_{n}\) |
| --- | --- |
| 1 | 2 |
| 2 | \(\sqrt{2}\) |
| 3 | \(\cfrac{-\sqrt{2}+\sqrt{10+4\sqrt{2}}}{2} \) |

根据计算,**①正确**.

到第三项,数列已经开始~~崩坏~~不好算了.

可以预见的是,通项应该是没戏的.

不过大概可以看出,\(a_{3}\lt \cfrac{-\sqrt{2}+\sqrt{18}}{2}=\sqrt{2}=a_{2}\lt a_{1} \),数列\(\{a_{n}\}\)是递减数列.

这也比较符合直觉,\(a_{n}=\cfrac{S_{n}}{S_{n}-1}=1+\cfrac{1}{S_{n}-1}\),而\(a_{n}\gt 0,S_{n}\)单调递增,那么\(a_{n}\)必然单调递减,并且始终大于1.

这样，便可以确定**③正确**.

由以上推理,有\(a_{n}\gt 1\),那么\(S_{n}\)显然没有上界，**②错误**.

④等价于
$$
a_{n-1}-a_{n}\gt a_{n}-a_{n+1}\gt 0
$$
即\(a_{n}\)递减的速度越来越慢,这也是合理的,毕竟\(a_{n}\)有下界1.

我们下面消去\(S_{n}\),证明这一点:
$$
\begin{gather}
S_{n}=1+\cfrac{1}{a_{n}-1}\\
S_{n+1}=1+\cfrac{1}{a_{n+1}-1}\\
(为什么写成这样的形式?\\分式相减可以让分母相减,\\分离常数可以让常数抵消)\\
a_{n+1}=-\cfrac{1}{a_{n}-1}+\cfrac{1}{a_{n+1}-1}\\
=\cfrac{a_{n}-a_{n+1}}{(a_{n}-1)(a_{n+1}-1)}\\
a_{n}-a_{n+1}=(a_{n}-1)(a_{n+1}-1)a_{n+1} ①\\
a_{n-1}-a_{n}=(a_{n-1}-1)(a_{n}-1)a_{n} ②\\
显然有②\gt ①\\
Q.E.D
\end{gather}
$$
不注意到分离常数的好处,证明④就比较困难:

贴一下AI(Grok)的证明:

To prove that \(a_{n-1} + a_{n+1} > 2a_n\) for all \(n \geq 2\), introduce the auxiliary sequence \(c_k = a_k - 1\) for \(k \in \mathbb{N}^*\). Since \(a_k > 1\) (as seen from the explicit terms and the form \(a_k = 1 + \frac{2}{\sqrt{S_{k-1}^2 + 4} + S_{k-1}} > 1\)), it follows that \(c_k > 0\).

The inequality \(a_{n-1} + a_{n+1} > 2a_n\) is equivalent to \(c_{n-1} + c_{n+1} > 2c_n\).

Define the function \(g(x) = \frac{\sqrt{x^2 + 4} - x}{2}\) for \(x > 1\) (noting \(S_k > 1\)). Then \(c_k = g(S_{k-1})\), so the inequality becomes \(g(S_{n-2}) + g(S_n) > 2g(S_{n-1})\).

The function \(g(x)\) is strictly decreasing (\(g'(x) < 0\)) and strictly convex (\(g''(x) > 0\)), as verified by computing the derivatives:

- \(g'(x) = - \frac{2(1 + \frac{x}{\sqrt{x^2 + 4}})}{(x + \sqrt{x^2 + 4})^2} < 0\),
- \(g''(x) > 0\) (detailed calculation shows the numerator \(2h^2 - h'd > 0\), where \(h(x) = 1 + \frac{x}{\sqrt{x^2 + 4}}\), \(h'(x) = \frac{4}{(x^2 + 4)^{3/2}}\), and \(d = x + \sqrt{x^2 + 4}\)).

Since \(\{a_k\}\) is strictly decreasing (\(a_k > a_{k+1} > 1\)), the partial sums satisfy \(S_n - S_{n-1} = a_n < a_{n-1} = S_{n-1} - S_{n-2}\), so \(\frac{S_{n-2} + S_n}{2} < S_{n-1}\).

By strict convexity of \(g\), \(g\left(\frac{S_{n-2} + S_n}{2}\right) < \frac{g(S_{n-2}) + g(S_n)}{2}\) (strict since \(S_{n-2} < S_n\)).

Since \(g\) is strictly decreasing and \(\frac{S_{n-2} + S_n}{2} < S_{n-1}\), it follows that \(g\left(\frac{S_{n-2} + S_n}{2}\right) > g(S_{n-1})\).

Combining these, \(\frac{g(S_{n-2}) + g(S_n)}{2} > g\left(\frac{S_{n-2} + S_n}{2}\right) > g(S_{n-1})\), so \(g(S_{n-2}) + g(S_n) > 2g(S_{n-1})\).

Thus, the inequality holds strictly for all \(n \geq 2\).
函数凹凸性都出来了,反正逆天程度是超出人类想象的*D:*

DeepSeek和Grok都不约而同的构造了\(a_{n}-1\)作为辅助数列,何意味.

## 拓展研究:
\(a_{n}\)是否能无限接近1?

这从直觉上讲是完全合乎理性的.

补充一个引理(Lemma):

>**单调有界定理**（Monotone Convergence Theorem）是实数系完备性的一个重要体现，包括两个部分：
>### 1. **单调递增有上界数列收敛**
>若数列 \(\{a_n\}\) 满足：
>- 单调递增：\(a_n \leq a_{n+1}\) 对所有 \(n \in \mathbb{N}^*\) 成立
>- 有上界：存在实数 \(M\)，使得 \(a_n \leq M\) 对所有 \(n\) 成立
则 \(\{a_n\}\) 收敛，且
\[
\lim_{n \to \infty} a_n = \sup\{a_n : n \in \mathbb{N}^*\}
\]
>### 2. **单调递减有下界数列收敛**
>若数列 \(\{a_n\}\) 满足：
>- 单调递减：\(a_n \geq a_{n+1}\) 对所有 \(n \in \mathbb{N}^*\) 成立
>- 有下界：存在实数 \(m\)，使得 \(a_n \geq m\) 对所有 \(n\) 成立
>则 \(\{a_n\}\) 收敛，且
\[
\lim_{n \to \infty} a_n = \inf\{a_n : n \in \mathbb{N}^*\}
\]
>PS:这里**sup,inf**分别是**上确界**和**下确界**的意思

在101中的这道题目中,\(a_{n}\)有下界1,且单调递减,那么肯定存在极限.

直接证明极限为1比较困难,我们不妨使用反证法:
$$
\begin{gather}
设\lim_{n \to \infty} a_{n}=L\\
假设L\gt 1\\
a_{N}=1+\cfrac{1}{S_{N}-1}\\
取N=1+\cfrac{1}{L-1},S_{N}\gt NL\gt N\\
a_{N}\lt 1+\cfrac{1}{N-1}=L
\\推出矛盾!\\
又L\ge 1,一定有L=1\\
Q.E.D
\end{gather}
$$

旁征博引
---

>**题目：**  
已知数列 \(\{a_n\}\) 的各项均为正数，其前 \(n\) 项和为 \(S_n\)，满足  
\[
a_n \cdot S_n = 9 \quad (n=1,2,\dots)
\]  
给出下列四个结论：
① \(\{a_n\}\) 的第 2 项小于 3；  
② \(\{a_n\}\) 为等比数列；  
③ \(\{a_n\}\) 为递减数列；  
④ \(\{a_n\}\) 中存在小于 \(\frac{1}{100}\) 的项。  
其中所有正确结论的序号是______。
(2022北京卷T15)

我们并不关心①②③,这是非常容易判断的,重点在于④:
$$
\begin{gather}
S_{n}=\cfrac{9}{a_{n}}\\
S_{n+1}=\cfrac{9}{a_{n+1}}\\
a_{n+1}=\cfrac{9(a_{n}-a_{n+1})}{a_{n}a_{n+1}}(♣)\\
由于数列 \{a_n\} 的各项均为正数,显然有a_{n}-a_{n+1}>0\\
则a_{n}是递减数列,且有下界1\\
应用单调有界定理,知a_{n}存在极限L\\
对♣等式左右两边求极限:\\
L=\cfrac{9(L-L)}{L^2}=0\\
那么对于足够大的n,a_n可以无限接近于0,④显然错误
\end{gather}
$$

>已知 \(\{a_n\}\) 是各项均为正数的无穷数列，其前 \(n\) 项和为\[ S_n, \text{且} \frac{1}{a_n} + \frac{1}{S_n} = 1 \ (n \in \mathbb{N}^*). \]  
给出下列四个结论：  
① \(a_1 + a_3 > 2a_2\);  
② \(\exists n_0 \in \mathbb{N}^*\)，使得 \(a_{n_0} < \dfrac{2025}{2024}\);  
③ 存在一个正数 \(m_0\)，使得对任意的 \(n \in \mathbb{N}^*\)，都有 \(S_n < m_0\);  
④ 对任意的 \(n \in \mathbb{N}^*\)，\(n \geq 2\)，都有 \(S_{n-1} + S_{n+1} < 2S_n\).  
其中所有正确结论的序号是 ___.
(出处不详,遇强则强)

由以上的分析,可以做出初步判断:

①②正确,③错误

④等价于\(a_{n+1}\lt a_{n}\),这就是第一题的③,所以④也正确.

综上,选\(\boxed{①②④}\)

# 小结
>莫让浮云遮望眼,撩开雾纱见真颜

即便面对*扑朔迷离,不可求通项*的数列,我们也有一套可行的解题方法(函数与极限).