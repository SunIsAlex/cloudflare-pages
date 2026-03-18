---
weight: 1000
date : '2026-02-12T16:54:26+08:00'
draft : false
title : '每日艺题 DAY002'
categories: ["每日艺题"]
tags: ["数学","数列"]
---

# \(a_n\)\(S_n\)联袂数列(有通项)
$$
\begin{gather}
a_nS_n=\cfrac{1}{4^n},a_1>0,求a_n.
\end{gather}
$$

## Attempt1:
$$
\begin{gather}
消去S_n:S_n=\cfrac{1}{a_n4^n}\\
S_{n+1}=\cfrac{1}{a_{n+1}4^{n+1}}\\
a_{n+1}=\cfrac{1}{4^{n+1}}({\cfrac{1}{a_{n+1}}-\cfrac{4}{a_n}})\\
=\cfrac{1}{4^{n+1}}({\cfrac{a_{n}-4a_{n+1}}{a_na_{n+1}}})
\end{gather}
$$

这样的形式还是太复杂了,遂放弃.

## Attempt2:
$$
\begin{gather}
消a_n:(S_{n}-S_{n-1})S_n=\cfrac{1}{4^n}\\
可以把\cfrac{1}{4^n}“雨露均沾”分给两个因式\\
令b_n=2^nS_n,有:\\
(b_{n}-2b_{n-1})b_n=1\\
即:{b_n}^2-2b_{n-1}b_n=1\\
从b_{n-1}到b_n比较困难,需要用求根公式,\\
何不反其道而行之?\\
b_{n-1}=\cfrac{{b_n}^2-1}{2b_n}\\
我们惊喜的发现,\\式子的形式类似于正切二倍角公式:\\
遂令c_n=\cfrac{1}{b_n}=tan(θ_n)>0(θ_n>0),\\
tan(θ_{n-1})=c_{n-1}=\cfrac{2b_n}{{b_n}^2-1}\\=\cfrac{2c_n}{1-{c_n}^2}=tan(2θ_n)\\
于是θ_n=\cfrac{θ_{n-1}}{2},我们便构建了从n-1到n的递推.\\
S_1=a_1=\cfrac{1}{2},b_1=1,c_1=1=tan(θ_1).\\
则θ_1=\cfrac{π}{4},θ_n=\cfrac{π}{2^{n+1}}.
S_n=\cfrac{b_n}{2^n}=\cfrac{1}{2^nc_n}\\=\cfrac{1}{2^ntan(\cfrac{π}{2^{n+1}})},\\
a_n=S_n-S_{n-1}\\=\cfrac{1}{2^ntan(\cfrac{π}{2^{n+1}})}-\cfrac{1}{2^{n-1}tan(\cfrac{π}{2^{n}})}(n\ge 2)\\
把tan写成cot就不会有定义域的问题:\\a_n=\cfrac{cot(\cfrac{π}{2^{n+1}})}{2^n}-\cfrac{cot(\cfrac{π}{2^{n}})}{2^{n-1}}(n\ge 1)
\end{gather}
$$
通项还可以继续化简:
$$
\begin{gather}
∵cot(x)-2cot(2x)=tan(x)\\
∴a_n=\cfrac{tan(\cfrac{π}{2^{n+1}})}{2^n}(n\ge 1)
\end{gather}
$$