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

### calculation

with this intuition, we can go about calculating the probability distributions. 

first of all, the stars are uniform with respect to our perspective. i.e. if we are just considering small patches of sky, we'd have a true uniform distribution $P(\theta,\phi) = 1/4\pi.$ 

however, we have to account for the fact that when we look up at an angle $\theta$ to the horizon, we can look at any angle $\phi.$ this gives small angles of $\theta$ a larger circle of sky to intercept. the radius if proportional to $\cos\theta$ so

$$ P_\text{star}(\theta) = \dfrac{\cos\theta \Delta\theta}{\int\limits_0^{\frac12\pi}\cos\theta\,\text{d}\theta}} = \cos\theta\Delta\theta $$

<br>
