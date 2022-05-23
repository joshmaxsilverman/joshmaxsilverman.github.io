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

If Sag A*'s spin axis points toward Earth at random, then the probability is equal to the fraction of solid angles consistent with the alignment.

# Approximate

Because $10^\degree$ is small patch of surface, curvature won't mess things up too much and we can approximate the surface patch as a circle of radius $s = \theta.$

$$
  \begin{align}
    P(\text{Sag A}^*\text{ alignment}) &= \dfrac{\pi\theta^2}{4\pi} \\
    &= \frac14 \left(\frac{10}{180}\pi\right)^2 \\
    &\approx 0.007615
  \end{align}
$$

# Exact

For amusement, we can integrate the surface patch to find the exact solid angle:

$$
  \begin{align}
    \Delta S &= 2\pi\int\limits_{0}^{\dfrac{10\pi}{180}}\sin\theta\, d\theta \\
    &= 2\pi\left(1 - \cos\theta)\midd_{\theta = \dfrac{10 \pi}{180}} \\
    &\approx 0.007596
  \end{align}
$$

Indeed, if we expand this to second order and divide by $4\pi,$ it becomes $\frac12\left(1 - 1 + \frac12\theta^2\right) = \frac14\theta^2,$ which is exactly what we got with the circle approximation.



<br>
