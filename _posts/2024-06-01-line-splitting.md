---
layout: post
published: true
title: Interview line splitting
date: 2024/06/01
subtitle: What is the sum of the products of endless division?
tags: scaling recursion
---

>**Question**: Starting with a line segment of length 1, randomly split it somewhere along its length into two parts. Compute the product of these two lengths. Then take each of the two resulting segments and repeat the process. That is, for each one, randomly split it somewhere along its length into two parts and compute the product. Then do this for all four resulting segments, then the eight after that, and the 16 after that, and so on.
>
> After doing this (forever), you add up all the products you computed throughout. On average, what value would you expect this sum to approach?
>
>Another way to describe this week’s Fiddler is with a recursive function $f,$ defined by $f(L) = ab + f(a) + f(b).$ Here, $a$ and $b$ are random values between $0$ and $L,$ such that $a + b = L.$ The question asked above is this: On average, what value does $f(1)$ approach?
>
>For Extra Credit, we’ll be splitting segments into three parts rather than two. So let’s define a new function $g(L).$ But wait! We don’t have $g(L) = abc + g(a) + g(b) + g(c),$ like you might have expected.
>
>Instead, I’d like to introduce a slightly messier recursive definition: $g(L) = abc + g(a+b) + g(a+c) + g(b+c) − g(a) − g(b) − g(c).$ Here, $a, b,$ and $c$ are random values between $0$ and $L$ such that $a + b + c = L.$
>
>On average, what value does $g(1)$ approach?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-ace-the-technical-interview))

## Solution

Replacing $a$ and $b$ with $x$ and $(1-x),$ the equation reads

$$ f(1) = \hat{x}(1-\hat{x}) + f(\hat{x}) + f(1-\hat{x}) $$

where the $\hat{x}$ indicates we're dealing with a random variable. 

Really, this will give us one sample of $f(1),$ so we should write $f(1)$ as $f(1\rvert\hat{x})$ and likewise introduce the random variables $\hat{y}$ and $\hat{z}$ on which the other evaluations of $f$ will depend: 

$$ f(1\rvert\hat{x}) = \hat{x}(1-\hat{x}) + f(\hat{x}\rvert\hat{y}) + f(1-\hat{x}\rvert\hat{z}) $$

At this point it's tempting to dive into cases, or recurse the equation, but we can learn a lot by thinking about the problem at different scales.

If we halve the length of the original stick $\ell,$ then we get the same problem scaled down by a factor of $2.$ This means the scale of all subsequent products of lengths drops by $1/2^2$

In general, if we scale the stick by $\gamma$ the sum of products will scale by $\gamma^2$ and so: 

$$ f(\gamma\ell) = \gamma^2 f(\ell). $$

Plugging this in, the original relationship becomes

$$ f(1|\hat{x}) = \hat{x}(1-\hat{x}) + \hat{x}^2 f(1|\hat{y}) + (1-\hat{x})^2 f(1|\hat{z}). $$

Averaging over $\hat{y}$ and $\hat{z}$ this becomes

$$ f(1|\hat{x}) = \hat{x}(1-\hat{x}) + \left[ \hat{x}^2 + (1-\hat{x})^2 \right]f(1), $$

and averaging over $x,$ it becomes

$$ \begin{align}
  f(1) &= \int\limits_0^1\text{d}\hat{x}\, \hat{x}(1-\hat{x}) + f(1) \int\limits_0^1\text{d}\hat{x}\, \left(\hat{x}^2 + (1-\hat{x})^2\right) \\
  &= \frac12 - \frac13 + f(1) \frac{2}{3} \\
&= \frac{\frac12 - \frac13}{1 - \frac23} \\
  &= \frac12
\end{align} $$

## Extra credit

The extra credit can be handled similarly. given the triple product, we get $g(\gamma \ell) = \gamma^3 g(\ell)$ instead of the quadratic.

Working as before, we get

$$ \begin{align}
  g(1|\hat{a}\hat{b}) &= \hat{a}\hat{b}(1-\hat{a}-\hat{b}) + g(\hat{a} + \hat{b}) + g(1 - \hat{a}) + g(1 - \hat{b}) - g(\hat{a}) - g(\hat{b}) - g(1 - \hat{a} - \hat{b}) \\
  &= \hat{a}\hat{b}(1-\hat{a}-\hat{b}) + \left[(\hat{a}+\hat{b})^3 + (1-\hat{a})^3 + (1-\hat{b})^3 - \hat{a}^3 - \hat{b}^3 - (1-\hat{a}-\hat{b})^3\right] g(1)
\end{align} $$

Taking expectations over $a$ (ranges from $0$ to $1$) and $b$ (ranges from $0$ to $1-a$) 

$$ \begin{align}
g(1) &= \langle\hat{a}\hat{b}(1-\hat{a}-\hat{b})\rangle_{a,b} + g(1)\langle(\hat{a}+\hat{b})^3 + (1-\hat{a})^3 + (1-\hat{b})^3 - \hat{a}^3 - \hat{b}^3 - (1-\hat{a}-\hat{b})^3\rangle_{a,b} \\
g(1) &= \frac{1}{60} + \frac{9}{10}g(1)
\end{align} $$

where $\langle X \rangle_{a,b}$ means

$$ \displaystyle \dfrac{\int\limits_0^1\text{d}\hat{a}\int\limits_0^{1-a}\text{d}\hat{b}\, X}{\int\limits_0^1\text{d}\hat{a}\int\limits_0^{1-a}\text{d}\hat{b}}. $$

So, 
$$ g(1) = \frac16. $$

<br>
