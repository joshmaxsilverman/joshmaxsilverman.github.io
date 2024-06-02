---
layout: post
published: false
title: Interview line splitting
date: 2024/06/01
subtitle:
tags:
---

>Question

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-ace-the-technical-interview))

## Solution

it is tempting to dive into cases, or recurse the equation, but we can learn a lot by thinking about the problem at different scales.

if we halve the length of the original stick $\ell,$ then we end up with the same problem scaled down by a factor of $2.$ this means that the scale of all subsequent products of lengths drops by $1/2^2/$

in general, if we scale the stick by $\gamma$ the sum of products will scale by $\gamma^2:$ 

$$ f(\gamma\ell) = \gamma^2 f(\ell). $$

plugging this in, the original recursion becomes

$$ f(1|x) = x(1-x) + \left[x^2 + (1-x)^2\right]f(1|x). $$

giving the value of $f$ given the random value $x.$ 

averaging over $x,$ this becomes

$$ \begin{align}
  f(1)\int\limits_0^1 \text{d}x\, \left[1 - x^2 - (1-x)^2\right] &= \int\limits_0^1\text{d}x x(1-x) \\
  f(1) &= \frac{\frac12 - \frac13}{1 - \frac23} \\
  &= \frac12
\end{align} $$

the extra credit can be handled similarly. given the triple product, we get $f(\gamma \ell) = \gamma^3 f(\ell)$ instead of the quadratic.

working as before, we get

$$ \begin{align}
  f(1) &= f(a + b) + f(1 - a) + f(1 - b) - f(a) - f(b) - f(1 - a - b) \\
  &= ab(1-a-b) + \left[(a+b)^2 + (1-a)^2 + (1-b)^2 - a^3 - b^3 - (1-a-b)^3\right] f(1)
\end{align} $$

taking expectations over $a$ (ranges from $0$ to $1$) and $b$ (ranges from $0$ to $1-a,$ we get 

$$ f(1) = \frac16. $$

<br>
