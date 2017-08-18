---
layout: post
published: true
title: Converging Ratios
date: 2017/08/18
---

>Take a look at this string of numbers:
>
>333 2 333 2 333 2 33 2 333 2 333 2 333 2 33 2 333 2 333 2 …
>
>At first it looks like someone fell asleep on a keyboard. But there’s an inner logic to the sequence:
>
>Each digit refers to the number of consecutive 3s before a certain 2 appears. Specifically, the first digit refers to the number of consecutive 3s that appear before the first 2, the second digit refers to the number of 3s that appear consecutively before the second 2, and so on toward infinity.
>
>The sequence never ends, but that won’t stop us from asking us questions about it. What is the ratio of 3s to 2s in the entire sequence?

<!--more-->

[(fivethirtyeight.com)](https://fivethirtyeight.com/features/can-you-unravel-these-number-strings/)

## Solution

By "the ratio of 3s to 2s in the entire sequence" we can only understand the _limit_ of the ratios of 3s to 2s for initial segments of the sequence as those segments get larger.  Let's call that limit $r$. Then, for a very large initial segment $S$ of length $n$, the ratio of 3s to 2s is essentially $r$.  The segment $S^\*$ of the sequence _contributed_ by this initial segment contains all the 3s and 2s referred to by numbers in $S$ (it's another, longer, initial segment). Each 3 in $S$ contributes three 3s and a 2, and each 2 contributes two 3s and a 2.  The ratio of 3s to 2s in $S^\*$, which must also be $r$, is a simple function of the ratio ($r$) of the 3s to the 2s in $S$ that contribute them. Since the proportion of 3s in $S$ is $r/(r+1)$ and the proportion of 2s is $1/(r+1)$, the ratio of 3s to 2s in $S^\*$ is:

$$3\frac{r}{r+1}+2\frac{1}{r+1} = \frac{3r+2}{r+1} = r $$

$$r^2 - 2r -2 = 0 $$

The quadratic formula tells us that $r = 1+\sqrt{3}$, or about 2.732.

## Not so fast!

What we have actually shown is that, on the assumption that there _is_ a ratio $r$ that the partial ratios (ratios of initial segments) converge to, it is $1+\sqrt{3}$. It's entirely plausible that there is such a limiting ratio, but to be rigorous we need to prove it.

To do that, consider the sequence $r_0,r_1,\ldots$ of ratios of 3s to 2s that starts with the ratio of the sequence 3,3,3,2 ($r_0$ is 3), and which is such that at each step, the sequence is expanded by following the instructions of the earlier sequence. As we saw above, this means that:

$$r_0 = 3$$

$$r_i+1 = f(r_i)$$

where:

$$f(r) = \frac{3r+2}{r +1}$$

We saw above that $1+\sqrt{3}$ is a fixed point of this function (a value that when fed to the function yields itself). For all $r$ greater than $1+\sqrt{3}$ (including 3), $f$ yields a value less than $r$ and greater than $1+\sqrt{3}$. This allows us to establish that there is no limit to the $r_i$ that is greater than $1+\sqrt{3}$. For suppose there is, and call it $x$. Since we know that $f(x)$ is less than $x$, we know that we can pick an $r_i$ sufficiently close to $x$ that $f(r_i)$ is close to $f(x)$ and less than $x$. 

So our sequence $r_0, r_1,\ldots$ is bounded (by $1+\sqrt{3}$ and 3) and monotonic (in this case, decreasing), and has no limit greater than $1+\sqrt{3}$. It follows that it does have a limit, which can only be $1+\sqrt{3}$.  QED!

It turns out that $r_i$ approaches the limit very quickly indeed. In fact, $r_10$ is identical to that value up to 12 significant digits:

```
1+sqrt(3) is  2.73205080757
i     r(i)
0 3
1 2.75
2 2.73333333333
3 2.73214285714
4 2.73205741627
5 2.73205128205
6 2.73205084164
7 2.73205081001
8 2.73205080774
9 2.73205080758
10 2.73205080757
'''
