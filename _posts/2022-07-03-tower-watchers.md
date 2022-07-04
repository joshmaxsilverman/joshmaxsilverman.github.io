---
layout: post
published: true
title: Hide and go seek tower guards
subtitle: Now you see me, now you don't
tags: geometry approximation physics materials
date: 2022/07/03
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

the problem doesn't mention a radius for the planet, but mentions that it's spherical. 

however, the answer will strongly depend on the ratio of the initial height to the radius of the planet. if the planet is say, 1 m in radius, then there may be no height where the second guard can still see the first guard on the ground. 

## minimal radius for the planet

without a radius, we can estimate a lower bound. spheres in space don't happen by accident, they happen because the gravitation of the body is strong enough to collapse any irregularities that are significant with respect to the length scale of the planet. 

taking granite as our material, its compressive strenght is $\sigma = 10^8 \text{ N/m}^2$ and its density if about $\rho = 3000 \text{ kg/m}^3.$ assuming the protuberance has uniform area $A$ and height $h$, the total mass of the protuberance is $\rho A h.$ we can estimate the gravitational field of the planet by newton's constant times the mass divided by the length scale of the planet: $GM/R.$ 

equating the force at the base of the protuberance to the gravitational pull on the protuberance, we get the critical height $h$ at which the protuberance will crack:

$$
  \sigma A = \rho A h \dfrac{GM}{R}
$$

this gets us $h/R = \frac{\sigma}{\rho} \frac{1}{GM}.$

the mass of the planet is about $\rho R^3$ so we get $h/R = \frac{\sigma}{\rho^2 G R^3}.$

setting $h/R \approx 1/100$ as a cutoff for being spherical, we get $\rho R^3 \approx 100\sigma/\rho \approx \frac{100 \cdot 10^8 \cdot 10^{11}}{10^3} = 10^{18}\text{ kg}$ or $R\approx 10^5\text{ m}.$

## now you see me, now you don't

with $h/R \approx 10^{-5}$ on the table, we can move on to the geometry. 

<br>
