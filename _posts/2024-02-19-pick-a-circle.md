---
layout: post
published: false
title: 
date: 2024/02/19
subtitle:
tags: d
---

>Question

<!--more-->

([Jane Street](URL))

## Solution

we want to calculate the volume of $(x_1,y_1,x_2,y_2)$-space that contributes to circles with diameters contained in the square. 

$$ \int dx_1 \int dy_1 \int dx_2 \int dy_2\ \mathbb{I}(\text{diameter forms circle contained in the unit square}. $$

there are two ways to go, methodical, and symmetric. 

### symmetric

instead of thinking in terms of the two points in $4-$space, we can describe the problem in terms of their center and separation in the plane:

$$ \begin{align}
  x_c &= \frac12\left(x_1 + x_2\right) \\
  y_c &= \frac12\left(y_1 + y_2\right) \\
  x_r &= \frac12\left(x_1 - x_2\right) \\
  y_r &= \frac12\left(y_1 - y_2\right)
\end{align} $$

how many positions can the center take? for a circle of radius $r,$ the center can occupy any position inside the $(1-2r)$ by $(1-2r)$ square inside the square. 

each point on the circle represents a pair (the point, and the point across from it on the circle). the number of such pairs is the annulus of area $(2\pi r)\text{d}r$ around the center. 

since we are just counting phase space, we can add over all such centers and radii. 

but we need to be careful about the unit area in either set of coordinates. 

the length of the separation is twice the radius 

<br>
