---
layout: post
published: false
title: Reasonable Sandwich
date: 2022/11/13
subtitle:
tags:
---

>**Question**: I have made a square peanut butter and jelly sandwich, and now it’s time to slice it. But rather than making a standard horizontal or diagonal cut, I instead pick two random points along the perimeter of the sandwich and make a straight cut from one point to the other. (These points can be on the same side.)

My slice is “reasonable” if I cut the square into two pieces and the smaller resulting piece has an area that is at least one-quarter of the whole area. What is the probability that my slice is reasonable?

<!--more-->

([FiveThirtyEight](URL))

## Solution

this problem is rooted in the geometry created by the slice, but to solve it we'll focus on the geometry of the parameter space — the plane defined by $a$ and $b,$ the positions along the sides where each cut is made.

if $a$ and $b$ are on adjacent sides, which happens $2/3$ of the time, then the smaller sandwich space is a simple triangle of area $\frac12ab.$ since we want the small piece to be reasonable, we have

$$ \frac14 \leq \frac12 ab \leq \frac12 $$

the upper bound is only reachable when $(a,b) = (1,1),$ so we can focus on the lower bound. multiplying through by $2,$ we get $\frac12 \leq ab,$ or

$$ b\geq \frac{1}{2b} $$

this is a curve from the point $(1,\frac12)$ to $(\frac12, 1).$ 

the area under this curve is $\frac12 + \int\limits_{\frac12}^1 \frac{\text{d}b}{2b} = \frac{\log 2}{2}.$

when $a$ and $b$ are on opposite sides, which happens the other $1/3$ of the time, the area is made up of a rectangle and a triangle. if e.g. $a > b,$ then the rectangle has area $1\times b$ and the triangle area is $\frac12 (a-b)\times 1,$ which makes $\dfrac12(a+b).$ when $b > a,$ the roles are reversed, but the expression is the same. 

again, we are considering the smaller piece, so $ \dfrac14 \leq \frac12(a+b) \leq \dfrac12,$ which gives us two inequalities: $a \geq \frac12 - b$ and $a \leq 1 - b.$

<br>
