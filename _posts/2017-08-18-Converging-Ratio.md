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

By "the ratio of $3$s to $2$s in the entire sequence" we can only understand the _limit_ of the ratios of $3$s to $2$s for initial segments of the sequence as those segments get larger.  Let's call that limit $r$. Then, for a very large initial segment $S$ of length $n$, the ratio of $3$s to $2$s is essentially $r$.  The segment $S^\*$ of the sequence _described_ by this initial segment contains all the $3$s and $2$s referred to by numbers in $S$ (it's another, longer, initial segment). Each $3$ in $S$ describes three $3$s and a $2$, and each $2$ describes two $3$s and a $2$.  The ratio of $3$s to $2$s in $S^\*$, which must also turn out to be $r$, is also expressible as a simple function of the ratio ($r$) of the $3$s to the $2$s in $S$ that describe them. Since the proportion of $3$s in $S$ is $r/(r+1)$ and the proportion of $2$s is $1/(r+1)$, the ratio of $3$s to $2$s in $S^\*$ is:

$$3\frac{r}{r+1}+2\frac{1}{r+1} = \frac{3r+2}{r+1}$$

(If that doesn't seem very intuitive, think of it as the expected number of $3$s preceeding a $2$.)

Setting that equal to $r$ and multiplying out, we get:

$$r^2 - 2r -2 = 0 $$

The quadratic formula tells us that $r = 1+\sqrt{3}$, or about $2.732$. And so we're done! _Right?_

## Not so fast!

What we have actually shown is that, _on the assumption that there is_ a ratio $r$ that the partial ratios (ratios of initial segments) converge to, it can only be $1+\sqrt{3}$. It's certainly plausible that there is such a limiting ratio, and computing the ratio for initial subsequences encourages that thought, as the ratios are observed to tend quickly towards that value from above. But to be rigorous we need to prove it.

To do that, we will consider the sequence $r_0,r_1,\ldots$ of ratios of $3$s to $2$s that starts with the ratio of the sequence $3,3,3,2$, and which is such that at each step, the new sequence is the one described by the previous sequence. As we saw above, this means that:

$$r_0 = 3$$

$$r_{i+1} = f(r_i)$$

where:

$$f(r) = \frac{3r+2}{r +1}$$

![f(r) versus r](/img/convergingratios.png)

We saw above that $1+\sqrt{3}$ is a fixed point of this function (a value that when fed to the function yields itself); that's where the two curves intersect in the graph. For all $r$ greater than $1+\sqrt{3}$ (including $3$), $f(r)$ is less than $r$ and greater than $1+\sqrt{3}$. This allows us to establish that there is no limit to the $r_i$ that is greater than $1+\sqrt{3}$. For suppose there is, and call it $c$. Since we know that $f(c)$ is less than $c$, we know that we can pick an $r_i$ sufficiently close to $c$ that $f(r_i)$ is close enough to $f(c)$ to be less than $c$. 

So our sequence $r_0, r_1,\ldots$ is bounded (by $1+\sqrt{3}$ and $3$) and monotonicly decreasing, and has no limit greater than $1+\sqrt{3}$. It follows that it does have a limit, which can only be $1+\sqrt{3}$.  

It turns out that $r_i$ approaches the limit very quickly indeed. In fact, $r_{10}$ is identical to $1+\sqrt{3}$ to twelve significant digits (I found that surprising):

```
1+sqrt(3) is  2.73205080757

i r(i)
------
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
```

(Now, the $r_i$ sequence is not the entire sequence of ratios of $3$s to $2$s of initial subsequences of our main sequence $S$, so it is logically possible that while it converges, the entire ratio sequence does not. But the $r_i$ sequence illustrates a universal fact: described segments have ratios closer to $1+\sqrt{3}$ than their describing ones, and so any subsequence with a ratio departing from $1+\sqrt{3}$ is swamped in the long run by the sequence it describes, the sequence that second sequence describes, and so on, which all together will have a limiting ratio of $1+\sqrt{3}$.)

Interesting facts:
- If, instead of $3$ and $2$, we use $2$ and $1$ to form the sequence (so that it starts $2,2,1,2,2,1,2,1,\ldots$), the limiting ratio of $2$s to $1$s is the [golden ratio](http://mathworld.wolfram.com/GoldenRatio.html), $(1+\sqrt{5})/2$, or about $1.618$.
- The sequences $S_2$ and $S_3$ containing the positions of within our original sequence of $2$s and $3$s, respectively, are [Beatty Sequences](http://mathworld.wolfram.com/BeattySequence.html). Numbering positions from zero, whether we start with a $2$ or a $3$, the positions of subsequent $2$s and $3$s are, for positive integers $m$, $\lfloor{m(2+\sqrt{3})}\rfloor$ and $\lfloor{m((1+\sqrt{3})/2)}\rfloor$. (Those brackets indicate the _floor_ function, which gives the largest integer less than or equal to its argument.)

<br>
