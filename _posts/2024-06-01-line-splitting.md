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

replacing $a$ and $b$ with $x$ and $(1-x),$ the equation reads

$$ f(1) = \hat{x}(1-\hat{x}) + f(\hat{x}) + f(1-\hat{x}) $$

where the $\hat{x}$ indicates we're dealing with a random variable. really, this will give us one sample of $f(1),$ so we should write $f(1)$ as $f(1|\hat{x})$ and likewise introduce the random variables $\hat{y}$ and $\hat{z}$ on which the other evaluations of $f$ will depend: 

$$ f(1|\hat{x}) = \hat{x}(1-\hat{x}) + f(\hat{x}|\hat{y}) + f(1-\hat{x}|\hat{z}) $$

it's tempting to dive into cases, or recurse the equation, but we can learn a lot by thinking about the problem at different scales.

if we halve the length of the original stick $\ell,$ then we get the same problem scaled down by a factor of $2.$ this means the scale of all subsequent products of lengths drops by $1/2^2$

in general, if we scale the stick by $\gamma$ the sum of products will scale by $\gamma^2$ and so: 

$$ f(\gamma\ell) = \gamma^2 f(\ell). $$

plugging this in, the original recursion becomes

$$ f(1|\hat{x}) = \hat{x}(1-\hat{x}) + \hat{x}^2 f(1|\hat{y}) + (1-\hat{x})^2 f(1|\hat{z}). $$

averaging over $\hat{y}$ and $\hat{z}$ this becomes

$$ f(1|\hat{x}) = \hat{x}(1-\hat{x}) + \left[ \hat{x}^2 + (1-\hat{x})^2 \right]f(1), $$

and averaging over $x,$ it becomes

$$ \begin{align}
  f(1) &= \int\limits_0^1\text{d}\hat{x}\, \hat{x}(1-\hat{x}) + f(1) \int\limits_0^1\text{d}\hat{x}\, \left(\hat{x}^2 + (1-\hat{x})^2\right) \\
  &= \frac12 - \frac13 + f(1) \frac{2}{3} \\
&= \frac{\frac12 - \frac13}{1 - \frac23} \\
  &= \frac12
\end{align} $$

## Extra credit

the extra credit can be handled similarly. given the triple product, we get $f(\gamma \ell) = \gamma^3 f(\ell)$ instead of the quadratic.

working as before, we get

$$ \begin{align}
  f(1|\hat{a}\hat{b}) &= \hat{a}\hat{b}(1-\hat{a}-\hat{b}) + f(\hat{a} + \hat{b}) + f(1 - \hat{a}) + f(1 - \hat{b}) - f(\hat{a}) - f(\hat{b}) - f(1 - \hat{a} - \hat{b}) \\
  &= ab(1-a-b) + \left[(a+b)^2 + (1-a)^2 + (1-b)^2 - a^3 - b^3 - (1-a-b)^3\right] f(1)
\end{align} $$

taking expectations over $a$ (ranges from $0$ to $1$) and $b$ (ranges from $0$ to $1-a,$ we get 

$$ f(1) = \frac16. $$

<br>
