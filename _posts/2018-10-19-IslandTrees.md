---
layout: post
published: true
title: Island Trees
date: 2018/10/19
---

>There is a single "tree" of $N$ islands, bridged together so that there is exactly one non-doubling-back path between any two islands.  Each island has a $p$ chance of being destroyed today, taking its bridges with it. How many separate island-trees are expected to result?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/so-your-archipelago-is-exploding-how-doomed-is-your-island/))

## Solution

We will derive $E(N)$, the expected number of remaining trees, inductively, and prove at the same time that it is indeed (as the problem statement presupposes) independent of the particular configuration of the bridges.  This is obvious for $N=1$, where there is only one configuration, and $E(1)$ is simply $1-p$.  

Suppose that configuration-independence holds for some arbitrary $N$ for which we know $E(N)$, and consider any tree of $N+1$ islands.  Take a particular "leaf" island (one with only one bridge), and call it $I$.  We know that the expected number of trees left if we ignore $I$ is $E(N)$. Whether the existence of island $I$ affects the number of remaining trees depends on whether the island $J$, to which it is bridged, is destroyed. If $J$ is not destroyed, the number of trees is no different than if $I$ were out of the mix, whether or not $I$ is destroyed. If $J$ is destroyed, and there's a $p$ chance of that, then there is a single additional tree ($I$ itself) if $I$ is not destroyed, and there's a $1-p$ chance of that.  So:

$$E(N+1) = E(N) + p(1-p)$$

Since we know that $E(1) = 1-p$, it follows that:

$$E(N) = (1-p) + (N-1)p(1-p)$$

This is maximized when its derivative is zero, namely, when:

$$p = \frac{N-2}{2(N-1)}$$

<br>
