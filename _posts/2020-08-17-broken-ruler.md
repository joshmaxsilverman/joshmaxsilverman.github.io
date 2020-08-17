---
layout: post
published: true
title: Broken Ruler
date: 2020/08/17
---

>**Question**: Quality control at your ruler factory has taken a turn for the worst and your latest shipment of rulers are all broken into 4 pieces! What is the average length of the shard that contains the $\text{6 inch}$ mark?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/are-you-hip-enough-to-be-square/amp/?__twitter_impression=true))

## Solution

At first I solved the \(4\)-piece case with a cobbled-together multivariable integral, expecting the $N$-piece case to involve sums of compound integrals. However, following compelling empirical results from Goh Pi Han, I was inspired to look for a simple perspective.

The approach here will be to find the probability distribution for the length of the shard that includes the $\text{6 inch}$ mark ($x=1/2$ for the purpose of this solution). The the main insight is that for a length $\ell$ interval to cover the point $x = 1/2,$ all we need is that two points are a distance $\ell$ apart and that no other points interrupt that interval (or else it would become a covering interval of length $\ell^\prime < \ell$).

### Does it cover?

The first non-trivial issue here is the probability that a random interval of length $\ell$ will cover the point $1/2.$ 

First of all, if $\ell \geq 1/2,$ then this probability is $1$ — there's no way to place an interval of length $\ell > 1/2$ without encompassing the middle of the ruler. So, whatever expression we find, we expect it to equal $1$ when $\ell = 1/2.$

For a ruler of length $\ell,$ the total length of the region where we can place the shard's leftmost point is $1-\ell$ (we can't place it any further, or its right most point would include points not on the original ruler). And if the shard's leftmost point starts more than a distance $\ell$ away, it won't reach $1/2.$ 

So, the probability that a random shard of length $\ell$ covers the halfway point is $P_\text{cover} = \ell/(1-\ell),$ which equals $1$ when $\ell = 1/2,$ as we had hoped. To summarize,

$$P_\text{cover}=\begin{cases}
\dfrac{l}{1-l} & \text{when } \ell \lt 1/2 \\
\hfil 1 & \text{when } \ell \geq 1/2.
\end{cases}$$

### Cases

There are two fundamentally distinct cases. The first is where shard is formed from two points where the ruler has broken. When $\ell < 1/2$, this is the only way for the shard to form. 

<br>
