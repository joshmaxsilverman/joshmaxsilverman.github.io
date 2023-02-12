---
layout: post
published: false
title: The Chance in Our Stars
date: 2023/02/11
subtitle: A cool puzzle if planes could fly at $\approx 0\,\text{mph}.$
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

on first thought, there doesn't seem to be a puzzle — the planes are spherically symmetric and so are the stars. what makes the difference?

the stars are spherically symmetric, in actuality and with respect to our perspective. the planes however are on a nearby sphere which means that, for the same angular increment, there are more planes at the horizon then there are when we look straight up.

to see this, we can just draw a sphere representing the uniform plane distribution. a patch of view, perpendicular to our line of sight, sweeps out a larger patch of the plane sphere whereas at the North pole, they are one and the same.

## calculation

with this intuition, we can go about calculating the probability distributions. 

### stars

first of all, the stars are uniform with respect to our perspective. i.e. if we are just considering small patches of sky, we'd have a true uniform distribution $p(\theta,\phi) = 1/4\pi.$ 

however, we have to account for the fact that when we look up at an angle $\theta$ to the horizon, we can look at any angle $\phi.$ this gives small angles of $\theta$ a larger circle of sky to intercept. the radius if proportional to $\cos\theta$ so

$$ p_\text{star}(\theta) = \dfrac{\cos\theta}{\int\limits_0^{\frac12\pi}\cos\theta\,\text{d}\theta} = \cos\theta $$

### airplanes

the planes are not too much different, except that we have to account for the tilt of the airplane sphere relative to our line of sight, and the changing distance between where we stand to the airplane sphere.

we can analyze the tilt by drawing a triangle. our vision patch is perpendicular to us and, so, makes angle $\theta$ with the corresponding patch on the sphere. that means our patch is a projection of the airplane patch at angle $\theta,$ so that $\text{d}A = \text{d}A^\prime/\cos\theta.$

the length of the patch in the $\theta$-direction is just $\ell \Delta \theta,$ while the circumference of the strip is $2\pi\ell\cos\theta,$ making $dA = 2\pi\ell^2\cos\theta/cos\theta = 2\pi\ell^2.$

now $\ell$ itself is a function of $\theta,$ which we can find with the law of cosines, which for posterity, we'll derive.

taking the sides to be vectors of lengths $R,$ $R+h,$ and $\ell,$ we have 

$$
  \begin{align}
    \lvert(R+h)\rvert^2 &= \left(\vec{\ell} + \vec{R}\right)\cdot\left(\vec{\ell} + \vec{R}\right) \\
    &= \ell^2 + R^2 + 2\ell R\cos\left(\theta + \tfrac12\pi\right)
  \end{align}
$$

which, after solving the quadratic for $\ell,$ gets 

$$ \ell(\theta) = \sqrt{h (h + 2 R) + R^2 \sin^2\theta} + R \sin\theta. $$
    

<br>
