---
layout: post
published: false
title: 
date: 2024/06/01
subtitle:
tags:
---

>Question

<!--more-->

([Fiddler on the Proof](URL))

## Solution

we can learn a lot by thinking about the problem at different scales.

if we halve the length of our stick $\ell$ then both pieces are scaled by half as well. 

this scales the first product by $1/4$ and results in two games starting with lengths half as long as the unscaled game. this makes their product scale by $1/4$ too.

in general, if we scale the stick by $\gamma$ then we should find that $f(\gamma\ell) = \gamma^2 f(\ell).$

using this, the original recursion becomes

$$ f(1) = x(1-x) + \left[x^2 + (1-x)^2\right]f(1). $$

taking expectation with regard to $x,$ this becomes

$$ \begin{align}
  f(1)\int\limits_0^1 \text{d}x\, \left[1 - x^2 - (1-x)^2\right] &= \int\limits_0^1\text{d}x x(1-x) \\
  f(1) &= \frac{\frac12 - \frac13}{1 - \frac23} \\
  &= \frac12
\end{align} $$

the extra credit can be handled similarly. given the triple product, we get $f(\gamma \ell) = \gamma^3 f(\ell)$ instead of the quadratic.

working as before, we get

$$ \begin{align}
  f(1) &= f(a + b) + f(1 - a) + f(1 - b) - f(a) - f(b) - f(1 - a - b) 
  &= ab(1-a-b) + \left[(a+b)^2 + (1-a)^2 + (1-b)^2 - a^3 - b^3 - (1-a-b)^3\right]f(1)
\end{align} $$

taking expectations over $a$ (ranges from $0$ to $1$) and $b$ (ranges from $0$ to $1-a,$ we get 

$$ f(1) = \frac16. $$

<br>
