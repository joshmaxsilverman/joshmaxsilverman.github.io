---
layout: post
published: true
title: Fair unfair coins
date: 2020/11/09
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

Von Neumann's probabilistic coin flip rests on the fact that the probability of $\mathbf{HT}$ and the probability of $\mathbf{TH}$ are both equal to $p(1-p).$ But it ignores two outcomes — $\mathbf{HH}$ and $\mathbf{TT}.$ 

We want to find an exhaustive set of outcomes that can be partitioned into two groups each with probability $1/2.$

Taking all the outcomes for $3$ coin flips, we get the probabilities

$$ \{\overbrace{\mathbf{HHH}}^{p^2}, \overbrace{\mathbf{HHT}}^{p^2(1-p)}, \overbrace{\mathbf{HTH}}^{p(1-p)}, \overbrace{\mathbf{HTT}}^{p(1-p)^2}, \overbrace{\mathbf{THH}}^{(1-p)p^2}, \overbrace{\mathbf{TTH}}^{(1-p)^2p}, \overbrace{\mathbf{THT}}^{(1-p)^2p, \overbrace{\mathbf{TTT}}^{(1-p)^3}}\} .$$

Of these, only $p^3$ and $(1-p)^3$ can eclipse $1/2$ on their own (at $1/\sqrt[3]{2}$ and $1-1/\sqrt[3]{2}$) — the maximum value of $p^2(1-p)$ (and of $p(1-p)^2$) is just $4/27.$ If we group some of the other terms with $p^3,$ it will still hit $1/2$ but it will do this at a $p > 1/\sqrt[3]{2}$

<br>
