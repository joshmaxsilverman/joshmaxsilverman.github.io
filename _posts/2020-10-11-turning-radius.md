---
layout: post
published: false
title: A Tale of Two U-turns
date: 2020/10/11
---

>Question

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-parallel-park-your-car/))

## Solution

### A few principles

The motion of the truck abides two basic rules:

- each tire points tangential to its current path
- with wheels fixed, the situation is not chnaged by how we look at it, so the truck travels in a circle

### Situation 1

The body of the truck points from one tire to the other. Since the back tire is parallel to the truck's body, and each tire is tangent to the circle it's on, the front tire can't be on the same circle as the back one. Because the wheels are locked during motion, the circles have the same center. 

To find the larger circle, we can project out a truck length away from the back tire $\ell,$ and wherever the front tire lands determines the outer circle which determines the turning radius. 


The small and large radii form right angles their respective tires, so $\ell$ is the projection of $R$ at the angle $\left(\pi/2 - \theta\right)$ and

$$\begin{align}
R\times \sin\left(\pi/2 - \theta\right) &= \ell \\
R\times\cos\theta &= \ell \\
R &= \dfrac{\ell}{\cos\theta}
\end{align}$$

### Situation 2

This situation is simpler. 

First of all, the two tires have to tilt in opposite directions relative to the body of the truck. Consider: if they tilted in the same direction, they'd be parallel and the truck would move on a straight line (circle of radius infinity). 

The tightest circle they can manage is by pointing the full $30^\circ$ in opposing directions. And because they have the same angle, they'll be on the same circle. 

Drawing out the scenario, half the length of the truck $\ell/2$ is the projection of $R$ at the angle $\left(\pi/2-\theta\right),$ so

$$\begin{align}
R\times\sin\left(\pi/2 - \theta\right) &= \ell/2 \\
R\times\cos\theta &= \ell/2 \\
R &= \dfrac{\ell}{2\cos\theta}
\end{align}$$




<br>
