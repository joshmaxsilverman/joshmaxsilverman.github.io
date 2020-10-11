---
layout: post
published: true
title: A Tale of Two U-turns
date: 2020/10/11
---

>Question

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-parallel-park-your-car/))

## Solution

### A few points

- each tire points tangential to its current path
- with wheels fixed, the truck travels in a circle

### situation 1

the body of the truck goes from one tire to the other. since the back tire is parallel to body, and each tire is tangent to the circle it's on, the front tire can't be on the same circle. because the wheels are locked during motion, the circles have the same center. project out a distance $\ell,$ wherever the front tire lands determines the outer circle which determines the turning radius. the small and large radii form right angles their respective tires.  $\ell$ is the projection of $R$ at the angle $\pi/2 - \theta$ so

$$\begin{align}
R\times \sin\left(\pi/2 - \theta\right) &= \ell \\
R\times\cos\theta &= \ell \\
R &= \dfrac{\ell}{\cos\theta}
\end{align}$$

### situation 2

this situation is simpler. first of all, the two tires have to tilt in opposite directions relative to the body of the truck. consider: if they tilted in the same direction, they'd be parallel and the truck would move on a straight line (circle of radius infinity). the tightest circle they can manage is by pointing the full 30 deg in opposing directions. because they have the same angle, they'll be on the same circle. drawing out the scenario, half the length of the truck is the projection of $R$ at the angle $\pi/2-\theta$, so

$$\begin{align}
R\times\sin\left(\pi/2 - \theta\right) &= \ell/2 \\
R\times\cos\theta &= \ell/2 \\
R &= \dfrac{\ell}{2\cos\theta}
\end{align}$$






<br>
