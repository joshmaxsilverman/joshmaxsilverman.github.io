---
layout: post
published: false
title: First passage time
date: 2018/04/21
subtitle: How long til a particle to diffuse to $x$?
tags:
---

>**Question** given a population of diffusing particles, what is the probability distribution of first passage times (FPT) to position $x?$ 
>
>Typically this is solved by solving for the diffusion differential equation to find the probability distribution, integrating that to find the survival, and then differentiating that to find the FPT distribution. In this post we'll show how to solve for the FPT distribution directly.

## Background

Suppose a particle makes first passage to the origin from position $x$ in time $t.$ This can happen by moving $\Delta x$ to the left or right and making first passage from either of those locations in time $t-\Delta t.$ This means the $FPT$ distribution satisfies

$$ FPT(x, t) = \frac12 FPT(x-\Delta x, t-\Delta t) + \frac12 FPT(x + \Delta x, t-\Delta t). $$

Expanding first in $\Delta x$ we get, to second order in $\Delta x$

$$ FPT(x, t) = FPT(x,t-\Delta t) + \frac12\Delta x^2 \partial_x^2 FPT(x, t-\Delta t). $$

Expanding in $\Delta t,$ we get 

$$ FPT(x, t) = FPT(x, t) - \Delta t\partial_t FPT(x, t) + \frac12\Delta x^2 \partial_x^2 FPT(x, t) + \frac12\Delta x^2\Delta t\partial_t FPT(x, t). $$

The term with $\Delta x^2\Delta t$ is higher order than the rest of the equation, so we are left with

$$ 
  \begin{align} 
    \partial_t FPT(x, t) &= \frac{\Delta x^2}{2\Delta t} \partial_x^2 FPT(x, t) \\
        &= D \partial_x^2 FPT(x, t). 
  \end{align}
$$

<!-- Typically this is approached by solving the diffusion equation, then integrating over positions up to but not beyond $x$ to get the survival probability, then differentiating that with respect to time to get the rate at which particles penetrate $x$ for the first time, with that rate proportional to the probability of passing the boundary for the first time at time $t.$ -->

<!--more-->

([Physics](URL))

## Solution

<br>
