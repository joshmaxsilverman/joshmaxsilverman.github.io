---
layout: post
published: true
title: Here's lookin' at you, Sag A* 
tags: probability geometry
subtitle: Or here's lookin at us?
date: 2022/05/22
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

if Sag A*'s spin axis points toward Earth at random, then the probability is equal to the fraction of solid angles consistent with the alignment.

# Approximate

because $\SI{10}{\degree}$ is small patch of surface, curvature won't mess things up too much and we can approximate the surface patch as a circle of radius $s = \theta.$

$$
  \begin{align}
    P(\text{Sag A}^*\text{ alignment}}) &= \dfrac{\pi\theta^2}{4\pi} \\
    &= \frac14 \frac{10}{180}\pi \\
    &\approx 0.0076
  \end{align}
$$

# Exact

For amusement, we can integrate the surface patch to find the exact solid angle:

$$
  \frac{\Delta S}{4\pi} = 2\pi\int\limits_{0}^{\dfrac{10\pi}{180}}\sin\theta\, d\theta = 2\pi\left(1 - \cos\theta)\midd_{\theta = \dfrac{10 \pi}{180}}
$$



<br>
