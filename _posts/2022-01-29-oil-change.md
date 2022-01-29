---
layout: post
published: True
title: Calendrical Oil Change
date: 2022/01/29
---

>Question

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-tune-up-the-truck/))

## Solution

Oil molecules age by one month, every month — anything 11 months old or younger is still "good", while everything 12 months and up is "bad". 

<!-- We can use thirteen variables $\{O_0, \ldots, O_{11}, O_\text{old}$ to track the composition of the tank, one for each viable month and a bucket for all the bad stuff.  -->

At the end of each month, each molecule has a birthday and a quart is drained from the tank, which affects all molecules equally.

From moment $t$ to $(t+1),$ the fractional composition of the tank changes like

$$O_m(t+1) = (1 - \frac{1}{12})O_{m-1}(t)$$ 

for all ages from $m=1$ to $11$ months, and the old molecules accumulate like 

$$ O_\text{old}(t+1) = \left(1-\frac{1}{12}\right)\left(O_{11}(t) + O_\text{old}(t)\right). $$

After the first step, $O_0(t) = \frac{1}{12}.$

As time goes by, 1 month olds emerge, then 2 months old, and so on until, finally, we see 11 month olds. Because all molecules age from the freshly injected molecules, once $m$ months have gone by, the fraction of $m$-month olds becomes a constant:

$$ O_m = \frac{11^m}{12^m}O_0 = \frac{11^m}{12^{m+1}} $$

After $m = 12$ months, we have an all ages event, and the population becomes fixed (no more $t$ dependence), and we can solve

$$ O_\text{old} = \frac{11}{12}\left(O_{11} + O_\text{old}\right) $$

to find $O_\text{old} = \frac{11^{12}}{12^{12}} \approx 0.35199562801.$





<!-- $$
O_0 \overbrace{\longrightarrow}^{(1-\frac{1}{12})} O_1 \overbrace{\longrightarrow}^{(1-\frac{1}{12})} O_2 \overbrace{\longrightarrow}^{(1-\frac{1}{12})} \ldots 
$$

Putting this together, we get 

$$
\begin{align}
O_1(t+1) &= \left(1-\frac{1}{12}\right) O_0(t) \\
O_2(t+1) &= \left(1-\frac{1}{12}\right) O_1(t) \\
&\vdots \\
O_{11}(t+1) &= \left(1-\frac{1}{12}\right) O_{10}(t) \\
O_\text{old}(t+1) &= \left(1-\frac{1}{12}\right) (O_{11}(t) + O_\text{old}(t)
$$ -->










<br>
