---
layout: post
published: false
title: Genetic Triangles
date: 2021/10/24
---

>**Question**: one point is selected at random from each side of an equilateral triangle. What is the probability that the resulting triangle contains the center of the original?


<!--more-->

([FiveThirtyEight](URL))

## Solution

we need to tally up the weight of all triplets of points $\{s_1, s_2, s_3\},$ (each $s_i$ drawn from side $i$ of the equilateral triangle) that contain the center point $\left(\frac12,\frac{\sqrt{3}}{6}\right).$

to pick an order, we'll do $s_1,$ then $s_2,$ and then $s_3$ (counterclockwise). 

if we pick $s_1$ in $\left(0,\frac12\right),$ then it will be on the same side of the middle as point $s_3,$ otherwise it will be on the same side as $s_2.$ these two cases are symmetric, so we can just do it once and double the result. if the triangle were isosceles or scalene, we'd need to handle this case separately (but similarly).

starting from point $s_1,$ we shoot at side 2, hitting at point $s_2,$ and from there bounce to $s_3.$ to contain the center, the shot has to pass under the center, the bounce has to pass over it, and the line of sight from $s_3$ to $s_1$ has to pass the center on the left.

### The shot

the shot can hit side 2 anywhere from the bottom right corner of the triangle up to the intersection of side two with the ray from $s_1$ through the center, which serves as an upper bound, $U(s_1).$

<br>
