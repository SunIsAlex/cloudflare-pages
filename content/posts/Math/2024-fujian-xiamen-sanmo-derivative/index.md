---
weight : 1000
date : '2026-04-03T20:48:40+08:00'
draft : false
title : '2024福建厦门三模导数'
categories : ["高考数学"]
tags : ["导数"]
---

![题干](zyb_1775220341946.jpg)

![alt text](zyb_1775221551076.jpg) ![alt text](zyb_1775221558477.jpg)
$$ 
\begin{cases}
\ln x\lt \frac{3(x^2-1)}{x^2+4x+1}, & 0 \lt x \lt 1 \\
\ln x\gt \frac{3(x^2-1)}{x^2+4x+1}, & x \gt 1
\end{cases}
$$

$$ 
\begin{cases}
\ln (x+1)\lt \frac{3x^2+6x}{x^2+6x+6}, & -1 \lt x \lt 0 \\
\ln (x+1)\gt \frac{3x^2+6x}{x^2+6x+6}, & x \gt 0
\end{cases}
$$

$$
\begin{cases}
\ln x\lt \frac{x^2+4x-5}{4x+2},\\
\ln (x+1)\lt \frac{x^2+6x}{4x+6}
\end{cases}
$$
关于$\ln x$和$\ln(x+1)$的不等式,可以由**平移**互相推出,所以**精度是一致**的.

{{<desmos funcs="y=\ln x|y=\frac{3(x^2-1)}{x^2+4x+1}|y=\frac{x^2+4x-5}{4x+2}" xmin="0" xmax="5" ymax="5" ymin="-5">}}

{{<desmos funcs="y=\ln (x+1)|y=\frac{3x^2+6x}{x^2+6x+6}|y=\frac{x^2+6x}{4x+6}" xmin="-1" xmax="4" ymax="5" ymin="-5">}}