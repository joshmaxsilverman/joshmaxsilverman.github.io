---
layout: post
published: false
title: Birthday collisions
date: 2022/10/15
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

I found three ways to solve this problem: by approximation, counting through recursion, and counting through combinatorics.

The first way is the most insightful and helps reveal what the exact solutions add to the picture, so we'll start there.

## Approximate argument

An exact way to treat the birthday twin case is to multiply the probability that the second person doesn't collide with the first $(1-1/365),$ with the probability that the third person doesn't collide with the first two $(1-2/365)$ and so on up to the $n^\text{rm}$ person. The resulting expression is exact and at some point falls below $50%$ giving us the answer for birthday twins.

Each term in the product $(1-j/365)$ is approximately equal to $e^{-j/365}$ and so we can add up all the exponents $\frac{1}{365}\left(1 + 2 + \ldots + n\right) = n(n-1)/2$ and we end up with $P(\text{no collisions in }n\text{ people}) \approx e^{-n^2/(2!\cdot 365)}.$

A simpler, more audacious way to get here 

<br>
