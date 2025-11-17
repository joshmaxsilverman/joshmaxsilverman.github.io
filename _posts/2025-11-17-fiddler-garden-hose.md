---
layout: post
published: true
title: Garden hose
date: 2025/11/16
subtitle: How far is the thirsty random tree from the gushing random hose?
tags: symmetry 
---

>**Question**: You and your assistant are planning to irrigate a vast circular garden, which has a radius of $1$ furlong. However, your assistant is somewhat lackadaisical when it comes to gardening. Their plan is to pick two random points on the circumference of the garden and run a hose straight between them.
>
>You’re concerned that different parts of your garden—especially your prized peach tree at the very center—will be too far from the hose to be properly irrigated.
>
>On average, how far can you expect the center of the garden to be from the nearest part of the hose?
>
> ** Extra credit**
>As before, your assistant intends to pick two random points along the circumference of the garden and run a hose straight between them.
>
>This time, you’ve decided to contribute to the madness yourself by picking a random point inside the garden to plant a second peach tree. On average, how far can you expect this point to be from the nearest part of the hose?

<!--more-->

([Fiddler on the Proof](URL))

## Solution

because of the radial symmetry, we can ignore the exact orientation of the hose and focus on the angle between the two random points on the perimeter. if the smaller angle made by the two points is $\theta$ then the distance from the hose to the center will be $\cos\frac12\theta.$

now, the placement of the second point relative to the first is uniformly random, so the probability distribution on $\theta$ is uniform from $0$ to $\pi.$ 

averaging the distance over $\theta$ we get an average distance from hose to tree of 

$$ 
  \begin{align}
  \frac1{\pi}\int_0^\pi \cos\frac12\theta &= \frac{2}{\pi}\left[\sin\frac12\pi -\sin0\right] \\ 
  &= \frac{2}{\pi} \\
  &\approx 0.63661977.
\end{align}
$$

## Extra credit

now the tree can be anywhere. as before, we can ignore the orientation of the hose. whereever the point lands, its distance to the closest point on the hose is the vertical separation between the line of the hose and the perpendicular line through the point.

the probability that a point lands distance $y$ from the center is proportional to the width of the chord at that height. since all points on the circle satisfy $x^2 + y^2 = 1$, the width of the strip is $2\sqrt{1-y^2}.$ since the integral of this over $y$ is just the area of the circle, the distribution is $\frac{2}{\pi}\sqrt{1-y^2}.$

so, the average distance for a given $h$ is simply

$$ \langle d(h)\rangle = \frac{2}{\pi} \int_h^1 d\text{y}\, (y-h)  + \frac{2}{\pi^2}  \int_{-1}^h d\text{y}\, (y-h) $$

which comes to

<>

plugging in $h = \cos\frac12\theta,$ we can average over $\theta$ and get

$$ \langle d\rangle = \frac{64}{9\pi^2}. $$

<br>
