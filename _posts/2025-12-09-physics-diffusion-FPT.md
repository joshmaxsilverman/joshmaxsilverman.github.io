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

Diffusing particles perform a random walk where the probability is governed by

$$ P(x, t) = \frac{1+a}{2}P(x-\Delta x,t-\Delta t) + \frac{1-a}{2} P(x+\Delta x,t-\Delta t). $$

$a$ is an asymmetry to describe any drift that might be in the system. If we expand this equation to second order in $\Delta x$ we get

$$ \begin{align}
  P(x, t) &= \frac{1+a}{2}\left[P(x,t-\Delta t) - \Delta x \partial_x P(x,t-\Delta t) + \frac12 \Delta x^2 \partial_x^2 P(x,t-\Delta t)\right] + \frac{1-a}{2} \left[P(x,t-\Delta t) + \Delta x \partial_x P(x,t-\Delta t) + \frac12\Delta x^2\partial_x^2 P(x,t-\Delta t)\right] \\ 
&= P(x,t-\Delta t) - a\Delta x \partial_x P(x, t-\Delta t) + \frac12\Delta x^2\partial_x^2 P(x,t-\Delta t). 
  \end{align}
$$



Typically this is approached by solving the diffusion equation, then integrating over positions up to but not beyond $x$ to get the survival probability, then differentiating that with respect to time to get the rate at which particles penetrate $x$ for the first time, with that rate proportional to the probability of passing the boundary for the first time at time $t.$

<!--more-->

([Physics](URL))

## Solution

<br>
