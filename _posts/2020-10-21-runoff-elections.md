---
layout: post
published: true
title: Simple Runoff Elections
date: 2020/10/21
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

I initially held off on this problem because I couldn't interpret the intended probability model for the vote totals.

According to @xaqwg's tweet, we are filtering the set of all sums for the cases where 

$$v_1 + v_2 + \ldots + v_n = 1$$

where $v_i$ is the vote percentage for candidate $i.$ When all the percentages satisfy $0\leq v_i \leq 1,$ the set of possible outcomes forms a plane. For two candidates, this is just a line in the plane; for three candidates this is an equilateral triangle in $\text{3D},$ and so on.

When we consider the shape formed by space between the axes and the plane, it's known as a simplex, and contains all points for which $v_1+v_2+\ldots+v_n\leq 1.$

In general, an $n$-dimensional simplex has [volume $1/n!.$](https://en.m.wikipedia.org/wiki/Simplex#Volume) If we adjust things so that $v_1+v_2+\ldots+v_n\leq a,$ this modified simplex has volume 

$$\text{Vol}(v_1+v_2+\ldots+v_n\leq a) = \dfrac{a^n}{n!}.$$

Now let's look at some elections. If an election has no runoff, it means that one of the candidates managed to get $v_i > 50\%.$ That means that they have a tuple like

$$\text{election} = \left(0.2, 0.15, 0.51, 0.14\right)$$

If we bring out the winner's coordinate, then this becomes 

$$\text{election} = 0.51 \times, \overbrace{\left(0.2, 0.15, 0.14\right)}^{v_1 + v_2 + v_3 \leq \frac12}$$

<br>
