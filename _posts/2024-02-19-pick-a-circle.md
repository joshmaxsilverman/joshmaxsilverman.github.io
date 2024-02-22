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

but we need to be careful about the unit area in either set of coordinates. in moving to the (center, separation) coordinate system, we stretch out each unit vector by a factor of $\sqrt{2}.$ we can see this by calculating the magnitude of e.g. $d\vec{x}_c$ or by calculating the area element $dA = dx_1\,dx_2$ in terms of $dx_c$ and $dx_r.$

taking the derivative, we get $d\vec{x}_c = \frac12\left(d\vec{x}_1 + d\vec{x}_2\right)$ which has magnitude $\frac12\sqrt{dx_1^2 + dx_2^2} = \frac{1}{\sqrt{2}}dx_1.$ 

taking cross products, we get $dA^\prime = \lvert d\vec{x}_c\times d_\vec{x}_r\rvert = \lvert\frac14\left(d\vec{x}_1\times d\vec{x}_2 + d\vec{x}_1\times d\vec{x}_2\right)\rvert = \frac{dx_1dx_2}{2},$ which gives us 

$$dx_c\,dx_r = \frac12dx_1\,dx_2. $$

with this, we can finish the expression for the amount of phase space contributed by circle of diameter $2r:$

$$ dr\,4\times 2\pi r(1-2r)^2. $$

integrating this over all valid radii, we get 

$$ 8\pi\int\limits_0^\frac{1}{2}\,dr r(1-2r)^2 $$

which by simple $u$-sub is 

$$ 4\pi \frac{(1-2r)^3}{3}\rvert_0^\frac{1}{2} = \frac{\pi}{6} $$

<br>
