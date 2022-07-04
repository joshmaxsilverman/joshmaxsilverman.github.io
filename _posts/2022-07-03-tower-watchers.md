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

setting $h/R \approx 1/100$ as a cutoff for being spherical, we get $R \approx \sqrt[3]{100\sigma/G\rho^2} \approx \sqrt[3]{10^2\times 10^8\times 10^{11}/10^6}$ or $R\approx 10^5\text{ m}.$

## now you see me, now you don't

with $h/R \gtrapprox 10^{5}\text{ m}$ on the table, we can move on to the geometry. 

drawing the initial scenario, we get that $\cos\theta = R/(R + h_0)$ and $b^2 = (R + h_0)^2 - R^2.$

in the second situation, the guard in the high tower is going to continue moving up the tower. with respect to the center of the planet, we can describe their path by $y_\text{ht} = \frac{R}{b} x_\text{ht}.$

meanwhile, the guard on the ground will have a direct line of sight to the other guard. since they can just barely see each other, their line of sight will be parallel to the ground, and has the slope $b/R.$ as their initial position is given by $(R\sin\theta, R\cos\theta),$ their line of sight follows $y_\text{g} = R\cos\theta + \frac{b}{R}\left(x_\text{g} + R\sin\theta\right).$

setting this equal, we can find $x$ when the paths intersect:

$$
  x^\ast = \dfrac{R\cos\theta + b\sin\theta}{\dfrac{R}{b} - \dfrac{b}{R}}
$$

when the guard is at $\left(x^\ast, y^\ast\right)$ they are $R+h$ from the center of the planet:

$$
  \begin{align}
  \left(R + h\right)^2 &= {x^\ast}^2 + {y^\ast}^2 \\
  &= \left[1 + \left(\frac{R}{b}\right)^2\right]\left(\dfrac{R\cos\theta + b\sin\theta}{\dfrac{R}{b} - \frac{b}{R}}\right)^2 \\
    &= \left[1 + \left(\frac{R}{b}\right)^2\right] \dfrac{\left(\dfrac{R^2 + b^2}{R+h_0}\right)^2}{\left(\dfrac{R}{b}\right)^2\left[1-\left(\frac{b}{R}\right)^2\right]^2} \\
    &= \dfrac{b^2 + R^2}{R^{-2}\left(R^2 - b^2\right)^2}\left(R + h_0\right)^2 \\
    &= \dfrac{R^2\left(R+h_0\right)^4}{\left(R^2 - b^2\right)^2} \\
    &= \dfrac{R^2\left(R+h_0\right)^4}{\left[2R^2 - (R+h_0)^2\right]^2} \\
    &= \dfrac{R^2\left(R+h_0\right)^4}{(R-h_0)^4} \\
  \end{align}
$$

so, $ h = R\left(R+h_0)\right)^2/\left(R-h_0\right)^2 - R$

<br>
