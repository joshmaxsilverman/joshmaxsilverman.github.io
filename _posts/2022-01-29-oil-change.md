---
layout: post
published: True
title: Calendrical oil change
subtitle: How fresh is the oil in your jalopy if you only change a quart per month?
source: fivethirtyeight
tags: probability steady-state 
date: 2022/01/29
theme: probability
---

>**Question:** You want to change the transmission fluid in your old van, which holds 12 quarts of fluid. At the moment, all 12 quarts are “old.” But changing all 12 quarts at once carries a risk of transmission failure.
>
>Instead, you decide to replace the fluid a little bit at a time. Each month, you remove one quart of old fluid, add one quart of fresh fluid and then drive the van to thoroughly mix up the fluid. (I have no idea if this is mechanically sound, but I’ll take Travis’s word on this!) Unfortunately, after precisely one year of use, what was once fresh transmission fluid officially turns “old.”
>
>You keep up this process for many, many years. One day, immediately after replacing a quart of fluid, you decide to check your transmission. What percent of the fluid is old?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-tune-up-the-truck/))

## Solution

Oil molecules age by one month, every month — anything 11 months old or younger is still "good", while everything 12 months and up is "old". 

### Population dynamics

At the end of each month, each molecule has a birthday and a quart is drained from the tank, which affects all molecules equally.

From time $t$ to $(t+1),$ the fractional composition of the tank changes like

$$O_m(t+1) = \left(1 - \frac{1}{12}\right)O_{m-1}(t)$$ 

for all ages from $m=1$ to $11$ months, and the old molecules accumulate like 

$$ O_\text{old}(t+1) = \left(1-\frac{1}{12}\right)\left(O_{11}(t) + O_\text{old}(t)\right). $$

Each month, a new quart is injected, so $O_0(t) = \dfrac{1}{12}.$

### Old and here to stay

As time goes by, $1$ month olds emerge, then $2$ month olds, and so on until, finally, we see $11$ month olds. Because all molecules age from the freshly injected molecules, once $m$ months have gone by, the fraction of $m$-month olds becomes a constant:

$$ 
\begin{align}
O_m &= \dfrac{11^m}{12^m}O_0 \\
&= \dfrac{11^m}{12^{m+1}} 
\end{align}
$$

After $m = 12$ months, we have an all ages event, and the population becomes fixed (no more $t$ dependence), and we can solve

$$ O_\text{old} = \dfrac{11}{12}\left(O_{11} + O_\text{old}\right) $$

to find $O_\text{old} = 11^{12}/12^{12} \approx 0.35199562801.$

![](/img/2022-01-29-oil-change.gif){:width="400px" class="image-centered"}

<br>
