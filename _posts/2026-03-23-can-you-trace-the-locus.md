---
layout: post
published: true
title: Can you trace the locus?
date: 2026/03/23
subtitle: What are is mapped out by a string on some pegs?
tags: geometry 
source: fiddler
kind: puzzle
theme: geometry
---

> **Question**: I have a loop of string whose total length is $10.$ I place it around a unit disk (i.e., with radius 1) and pull a point on the string away from the disk until the string is taut, as shown below.
>
> I drag this point around the disk in all directions, always keeping the string taut, tracing out a loop. What is the area inside this resulting loop?
>
> **Extra credit**: Now I have a loop of string whose total length is $14,$ and I place it around two adjacent unit disks. As before, I pull a point on the string away from the disks until the string is taut, as shown below.
>
> I drag this point around the disks in all directions, always keeping the string taut, tracing out a loop. What is the area inside this resulting loop?




<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-trace-the-locus))

## Solution

the string meets the circle at two points of tangency and the total length of the string is $10.$ we can use these two facts to find the radius of the point as it orbits the circle.

drawing two right triangles with the tangents, we get

$$ 2\cdot\left(\pi - \theta\right) + 2\cdot\tan\left(\frac{\theta}{2}\right) = 10. $$

solving this for $\theta$ we get $\theta\approx 1.2605292$ or $\ell = \tan\theta \approx 3.1189365.$ 

the radius is just $r = \ell/\sin\theta$ or $r \approx 3.2753266.$ 

plugging this in, the area swept out by the point is $A = \tfrac12\pi r^2 \approx 33.702266.$ 

## Extra credit

conceptually, the extra credit is the same idea, but operationally it has a fair bit of geometric accounting to do.

as the point rotates around the disks, there are two qualitative regimes. in one of them, the string is tangent to both disks at once and in the other it has two points of tangency to one of them. we can reuse the work of the first part to find the radius of the point in the first regime, but we have to do a bit more work to find the radius in the second.

![](/img/2026-03-23-fiddler-locus-two-tangent.png){:width="450 px" class="image-centered"}

drawing the scenario, we have everything we need to divine the sought and sacred constraints.

first, we can use the law of cosines to relate the radius $r_\theta$ to lengths $\ell_1$ and $\ell_2.$ 

$$ 
    \begin{align}
        \ell_1^2 + 1 &= 1 + r_\theta^2 - 2r_\theta\cos(\pi-\theta) \\ 
        &= 1 + r_\theta^2 + 2r_\theta\cos\theta,
    \end{align}
$$
 
and, likewise

$$
    l_2^2 + 1 = 1 + r_\theta^2 - 2r_\theta\cos\theta.
$$

next we can relate the angles $\beta_1$ and $\beta_2$ to $\theta$ and $r_\theta$ using right triangle trigonometry giving us

$$ \cos\beta_1 = \frac{1+r_\theta\cos\theta}{\sqrt{1+\ell_1^2}} $$

and

$$ \cos\beta_2 = \frac{r_\theta\cos\theta - 1}{\sqrt{1+\ell_2^2}}. $$

next, we need the angles $\gamma_1$ and $\gamma_2$ to find the length of the curved segments of the string.

$\gamma_1$ is the complement of $\beta_1$ and its adjacent angle

$$ \gamma_1 = \pi - \beta_1 - \arcsin\frac{\ell_1}{\sqrt{\ell_1^2+1}}. $$

similarly, $\ell_2$ is the complement of the angle adjacent to $\beta_2$ 

$$ \frac12\pi - \gamma_2 = \arcsin\frac{\ell_2}{\sqrt{\ell_2^2+1}} - \beta_2. $$

finally, we have the total length of the string broken down into the straight segments, curved segments, and tangent segments.

$$ 14 = \frac12 \pi + 4 + \ell_1 + \ell_2 + \gamma_1 + \gamma_2. $$

this is a system of seven equations in eight variables that we can solve for $r_\theta$ with $\theta$ independent. 

i don't think it is resolvable analytically, but we can solve it numerically.

we just need to find the minimum value of $\theta$ where the disk maintains tangents on both disks.

![](/img/2026-03-23-fiddler-one-tangent.png){:width="450 px" class="image-centered"}

this occurs when $\ell_1$ is flat, which implies $\tan\theta = 1/(1+\ell_1)$ which gives $\theta_\text{min}=\arctan 1/(1+\ell_1) \approx 0.238173.$

below this value of theta, the string has two tangents to a single disk and the radius with respect to that disk is the same as in the first problem. now, the radius is about the center of the two disks, so we can use the law of cosines to relate the radius $r_\eta$ to $r_\theta.$ we get

$$ r_\eta^2 = 1 + r_\theta^2-2r_\theta\cos\theta $$

which simplifies to

$$ r_\theta = \cos\theta + \sqrt{r_\eta^2 - \sin^2\theta}. $$

with $r_\theta$ in hand in the two regimes, we can numerically integrate

$$ \text{area} = \frac12 \int_0^{\theta_\text{min}} \text{d}\theta\,\left[\cos\theta + \sqrt{r_\eta^2 - \sin^2\theta}\right]  + \frac12 \int_{\theta_\text{min}}^{\pi/2}\text{d}\theta\, r_\theta^2 . $$

this gets approximately $\text{area} \approx 52.367.$


