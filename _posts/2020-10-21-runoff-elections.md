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

where $v_i$ is the vote percentage for candidate $i.$ 

### Geometry of an election

When all the percentages satisfy $0\leq v_i \leq 1,$ the set of possible outcomes forms a plane. For two candidates, this is just a line in the plane; for three candidates this is an equilateral triangle in $\text{3D},$ and so on.

When we consider the shape formed by space between the axes and the plane, it's known as a simplex, and contains all points for which $v_1+v_2+\ldots+v_n\leq 1.$ This means that the plane contains the actual elections while the volume contains that define a valid election with $n+1$ participants, i.e. by adding another candidate with vote percentage $v_{n+1} = \left(1-\sum_{i=1}^N v_i\right).$

### Weight as volume

Now let's look at some elections. If an election has no runoff, it means that one of the candidates managed to get $v_i > 50\%.$ That means that they have a tuple like

$$\text{election} = \left(0.2, 0.15, 0.51, 0.14\right)$$

If we bring out the winner's coordinate, then this becomes 

$$\text{election} = 0.51 \times \overbrace{\left(0.2, 0.15, 0.14\right)}^{v_1 + v_2 + v_3 \leq \frac12}.$$

So, every possible election without runoff is in a $1:1$ correspondence with a tuple whose sum is less than $1/2.$ These are exactly the points that are in the interior of the $(n-1)$ dimensional simplex with side length $a=1/2.$ 

In every election with runoff, the winning candidate could have been in $1$ of $N$ locations in the tuple so the total weight of runoff elections is

$$w_\text{no runoff} = N\times\text{Vol}(v_1 + v_2 + \ldots + v_{n-1} \leq \frac12).$$

If we look at a general election (with or without runoff) we can do the same: 

$$\text{election} = \left(0.24, 0.15, 0.47, 0.14\right) \rightarrow 0.24\times\overbrace{\left(0.15, 0.47, 0.14\right)}^{v_1 + v_2 + v_3 \leq 1}$$

except that the sum is equal to $1$ and we always pull out the value of $v_1,$ so there's no need to multiply by $N.$ 

### The weight of runoff

As a result, the total weight of all elections with $N$ candidates is the volume of the standard $(N-1)$-dimensional simplex

$$\begin{align}
w_\text{total} &= \text{Vol}(v_1 + v_2 + \ldots + v_{N-1} \leq 1).$$

The probability of a runoff election is simply

$$P(\text{runoff}) = 1-P(\text{no runoff}) = 1-\dfrac{w_\text{no runoff}}{w_\text{total}}.$$

### Volume of the standard simplex

In general, an $n$-dimensional simplex has [volume $1/n!.$](https://en.m.wikipedia.org/wiki/Simplex#Volume) If we adjust things so that $v_1+v_2+\ldots+v_n\leq a,$ this modified simplex has volume 

$$\text{Vol}(v_1+v_2+\ldots+v_n\leq a) = \dfrac{a^n}{n!}.$$


<br>
