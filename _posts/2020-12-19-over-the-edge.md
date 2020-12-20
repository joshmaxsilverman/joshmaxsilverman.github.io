---
layout: post
published: false
title: Living on the Edge
date: 2020/12/19
---

>**Question**: Trapped in your apartment under Stage $4$ lockdown, with the Riddler about to take a $2$-week hiatus, you sit at your kitchen table avoiding the solve so that you'll still have something to look forward to. Sadly, there's nothing but a half full glass of water and a cardboard circle, upon which is written the GPS coordinates of your last stash of buried 

<!--more-->

([FiveThirtyEight](URL))

## Solution

The disc — as with all objects — will tip if its center of mass extends beyond the edge of what it's resting on. The first part is simple for the disc; due to its radial symmetry, its center of mass is at its center. The second part isn't as clear.

### The edge(s) of the glass

With a straight object over a straight edge — like a book off a desk — the edge is obvious. 

On the rim there are two answers: the disc can fall **off** the glass or **into** it. 

To fall off the glass, the center of the disc has to extend beyond the rim. Beyond the rim, gravity will pull the center of mass down with no force to tilt it back up.

### When do we fall in?

Falling in is another story. The center of the disc **can** extend over the inside of the glass — being pulled down by gravity — while the glass exerts a force to tilt the disc back up. This is because the glass exerts force on the disc at the points of contact. When the center of mass first breaches the inner rim, the points of contact are further in than the center of mass. But as we continue to push the disc, the angle between the points of contact and the center of mass grows until the three points are lined up. This is the furthest inward we can place the disc because the downward pull of gravity an the upward force of the glass are balanced, and there's no imbalance of tilting forces. If we were to push it any further then the points of contact wouldn't be able to provide a tilting force to oppose gravity and the disc would fall in.

So, if the center of mass is anywhere from the outer rim of the glass to the radius where the center of mass becomes colinear with the points of contact, the disc will stay up. As we've shown, this happens when the chord connecting the points of contact is equal to the diameter of the smaller disc.

Using the Pythagorean theorem, this radius is 

$$r^* = \sqrt{R^2 - r^2}.$$

### Will we fall in?

Assuming that we place the center of the disc at a random point inside the rim, the probability that the disc stays up is equal to the area of the annular region between $r^*$ and $R:$

$$\begin{align}
P_\text{stable} &= \dfrac{A_\text{stable}}{A_\text{total}} \\
&= \dfrac{\pi R^2 - \pi {r^*}^2}{\pi R^2} \\
&= \left(\dfrac{r}{R}\right)^2
\end{align}$$

For the disc in question, this probability is $1/2^2 = 1/4.$

<br>
