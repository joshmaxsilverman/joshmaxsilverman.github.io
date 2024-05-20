---
layout: post
published: true
title: The radius of a rectangle
date: 2024/05/19
subtitle: What would the world look like if you could only see squares?
tags: scaling geometry
---

>**Question**: One of my favorite facts about circles is the relationship between their area and their circumference. For a circle with radius $r,$ its area is $\pi r^2$ and its circumference is $2\pi r.$ What’s neat here (or rather, one thing that’s neat here) is that if you take the derivative of the area formula with respect to $r,$ you get the circumference formula! In other words, $d(\pi r^2)/dr = 2\pi r.$ Amazing, right?
>
>(For those of you who are accustomed to using tau rather than pi, this still works. The area of a circle is $\tau r^2/2$ and its circumference is $\tau r.$ Once again, $d(\tau r^2/2)/dr = \tau r.$)
>
>Inspired by this fact, let’s define the term “differential radius.” The differential radius $r$ of a shape with area $A$ and perimeter $P$ (both functions of $r$) has the property that $dA/dr = P.$ (Note that $A$ always scales with $r^2$ and $P$ always scales with $r.$)
>
> What is the differential radius of a rectangle with sides of length $a$ and $b$? Your answer should be in terms of both $a$ and $b.$ Oh, and kudos if you can illustrate your solution geometrically!

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/when-is-a-triangle-like-a-circle))

## Solution

First, let's anticipate how it ought to scale

When the height or width goes to zero, then the area is zero and increasing the perimeter should not increase the area at all, so the differential radius is zero.

When the height or width dominates the other, but neither vanishes, then the increase in area should not depend on the length of the long side. So, when $a\gg b,$ the differential radius should be proportional to $b$ (and $a$ in the other limit).

When neither $a=b,$ the rectangle is a square and we should recover $r=\frac12 a.$ 

Already we could try to apply street-fighting mathematics. On the basis of our observations, the result must be proportional to $a$ and $b$ and thresholded by either one relative to the other. This basically narrows us down to

$$ \frac{ab}{a+b}. $$

But let's get there by regulation techniques.

### Analysis

One way to go is playing with the definition directly.

Call the aspect ratio $a/b$ of the rectangle $\gamma,$ then the area is $A = \gamma a^2$ and the perimeter is $P=2a(1+\gamma).$

So, $dA = 2\gamma a\, da$ and 

$$ \begin{align} dr &\equiv \frac{dA}{P} \\ &= \frac{\gamma}{1+\gamma} da. \end{align} $$

Since $\gamma$ is a constant, this means $r = a\frac{\gamma}{1+\gamma} + \text{const.}$ 

Multiplying through by $a$ we get 

$$ r = \frac{ab}{a+b} + \text{const.} $$

and the extreme cases show that $\text{const.}=0$

### Geometry 1

Area is created by exposed boundary stretching outward. 

We don't know what $r$ is, but let's extend it by $dr.$ If we do, then all linear dimensions will increase by the same ratio. The top makes new area $a\frac{dr}{r}b$ and the side makes new area $b\frac{dr}{r}a.$ 

The corner also makes new area but it is second order in $dr$ and goes to zero in the liit $dr \rightarrow 0.$

Altogether the new area makes $2ab\frac{dr}{r} + O(r^2)$ and we get

$$ 
  \begin{align}
    \frac{dA}{dr} &= P \\
    \frac{2ab}{dr}\frac{dr}{r} &= 2(a+b) \\
    \frac{ab}{a+b} &= r
  \end{align}
$$

Is that good enough?

### Geometry 2

No it is not.

Let's take a step back and find the real solution. What is a radius? 

One way to re-interpret it is the typical perpendicular distance from the center of expansion to the frontier of expansion.

In fact that's what our definition does — it asks for a "typical" radius relating new area to existing perimeter.

We can find the "typical" perpendicular distance by taking the average of perpendicular distance weighted by the length of its frontier.

For upward expansion, the perpendicular distance is $\frac12 a$ with frontier length $b,$ and for sideways expansion it is perpendicular distance $\frac12b$ with frontier length $a$:

$$ 
  \begin{align}
    r &= \frac{\frac12a b + \frac12 b a}{b+a} \\
    &= \frac{ab}{a+b}.
  \end{align}    
$$



<br>
