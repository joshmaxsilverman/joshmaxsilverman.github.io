---
layout: post
published: True
title: First passage time
date: 2025/12/10
subtitle: How long until a particle diffuses to $x$?
tags: statistical-mechanics first-passage-time
---

>**Question** given a population of diffusing particles, what is the probability distribution of first passage times ($\text{FPT}(x,t)$) to position $x?$ 
>
>Typically this is found by solving the diffusion differential equation to find the probability distribution, integrating that to find the survival, and then differentiating that to find the $\text{FPT}$ distribution. In this post we'll show how to solve for the $\text{FPT}$ distribution directly.

<!--more-->

([Physics](https://en.wikipedia.org/wiki/First-hitting-time_model))

## Background

Suppose a particle makes first passage to the origin from position $x$ in time $t.$ This can happen by moving $\Delta x$ to the left or right and making first passage from either of those locations in time $t-\Delta t.$ This means the $\text{FPT}$ distribution satisfies

$$ \text{FPT}(x, t) = \frac12 \text{FPT}(x-\Delta x, t-\Delta t) + \frac12 \text{FPT}(x + \Delta x, t-\Delta t). $$

Expanding first in $\Delta x$ we get, to second order in $\Delta x$

$$ \text{FPT}(x, t) = \text{FPT}(x,t-\Delta t) + \frac12\Delta x^2 \partial_x^2 \text{FPT}(x, t-\Delta t). $$

Expanding in $\Delta t,$ we get 

$$ \text{FPT}(x, t) = \text{FPT}(x, t) - \Delta t\partial_t \text{FPT}(x, t) + \frac12\Delta x^2 \partial_x^2 \text{FPT}(x, t) + \frac12\Delta x^2\Delta t\partial_t \text{FPT}(x, t). $$

The term with $\Delta x^2\Delta t$ is higher order than the rest of the equation, so we are left with

$$ 
  \begin{align} 
    \partial_t \text{FPT}(x, t) &= \frac{\Delta x^2}{2\Delta t} \partial_x^2 \text{FPT}(x, t) \\
        &= D \partial_x^2 \text{FPT}(x, t)
  \end{align}
$$

which is just the diffusion equation. This means that the first passage distribution itself satisfies the diffusion equation.

However, its initial condition is distinct from the diffusing particles. Their initial condition is a spike at position $0$ at time $t=0,$ i.e. $\text{FPT}(x,0) = \delta (x).$ On the other hand, the first passage distribution is a spike at time $0$ for position $x=0,$ i.e. $\text{FPT}(0,t) = \delta(t).$

## Approach

To solve this, we can find the impulse response $h(t)$ and convolve it with the signal ($\text{FPT}(0,t) = \delta(t)$) at the origin. But as this shows, we can instead find the step response and take its time derivative:

$$
  \begin{align}
    FPT(x,t) 
    &=  \int\limits_{-\infty}^t \text{d}\tau\, f(\tau)h(x,t-\tau) \\ 
    &= \int\limits_{-\infty}^t \text{d}\tau\, f(\tau)\, \frac{\text{d}}{\text{d} t}w(x,t-\tau) \\
    &= \frac{\text{d}}{\text{d}t}w(x,t)
  \end{align}
$$

since $f(\tau) = \delta(\tau).$ 

The step response is the time integral of $FPT(x,t)$ which is the cumulative distribution of first passage times, the probability that a particle's first passage to $x$ is $t$ or earlier. It stays zero at the origin for all $t$ and decays to zero as $x$ goes to infinity.


## Solving the differential equation

The differential equation is

$$ \partial_t w(x,t) = \frac12 \partial_x^2 w(x,t) $$

So long as the ratio $\eta = x/\sqrt{2t}$ is kept constant, the equation doesn't change. So, $w$ is a function of $\eta$ alone, and we can rewrite it $\partial_t w(\eta) = \frac12 \partial_x^2 w(\eta).$ Working this out, we get $\partial_x \eta = \eta/x,$ $\partial_t \eta = -\eta/2t,$ and

$$\begin{align}
\frac{\partial \eta}{\partial t} \cdot\frac{\partial w(\eta)}{\partial\eta} &= \frac12\partial_x \left(\frac{\partial\eta}{\partial x}\cdot\frac{\partial w(\eta)}{\partial\eta}\right) \\
&= \frac12\left(\frac{\partial \eta}{\partial x}\right)^2 \frac{\partial^2 w(\eta)}{\partial\eta^2} \\
-\frac{\eta}{2t}\partial_\eta w(\eta)&= \frac12 \frac{\eta^2}{x^2}\partial_\eta^2 w(\eta) \\
-2\eta\partial_\eta w(\eta) &= \partial_\eta^2 w(\eta) 
\end{align}$$

This can be directly integrated to find $\log \partial_\eta w(\eta) = -\eta^2$ leading to $\partial_\eta w(\eta) = \exp-\eta^2$ and 

$$ w(\eta) = w(x,t) = A + B\int\limits_0^\eta \text{d}z\, \exp-z^2. $$

The step response is $1$ at the origin for all time, giving

$$ 1 = A $$

and should be zero for all $x\neq 0$ at time zero, giving

$$ 0=A+B\int\limits_0^\infty\text{d}z\exp-z^2,  $$ 

so $B = -2/\sqrt{\pi},$ making 

$$ 
  \begin{align} w(x,t) &= \frac{2}{\sqrt{\pi}}\int\limits_\eta^\infty \text{d}z\, \exp -z^2 \\ 
  &= \text{erfc}\frac{x}{2\sqrt{t}}. 
  \end{align}
$$

Taking the time derivative, this gives

$$ \text{FPT}(x,t) = \frac{d}{dt} w(x,t) = \frac{x}{\sqrt{2\pi t^3}} e^{-x^2/2t}. $$

<!-- The usual forward approach evolves the distribution from a specific starting point $p(x,0) = \delta(x-x_0).$ If the starting point changes, then the whole process needs to be recalculated. By contrast, the approach we take here solves on equation whose solution contains FPT statistics for every possible starting state. The boundary condition is the same ($\text{FPT)(0,t)=\delta(t), \text{FPT}(x,0) = 0) and the starting point is just an argument. Once $w$ is known, the FPT is just the time derivative. -->



<br>
