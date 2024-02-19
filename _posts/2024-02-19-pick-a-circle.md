---
layout: post
published: false
title: 
date: 2024/02/19
subtitle:
tags:
---

>Question

<!--more-->

([Jane Street](URL))

## Solution

we want to calculate the volume of $(x_1,y_1,x_2,y_2)$-space that contributes to circles with diameters contained in the square. 

there are two ways to go, methodical, and symmetric.

### symmetric

instead of thinking in terms of the two points, we can describe the problem in terms of their center and separation. 

for a circle of radius $r,$ the center can occupy any position inside the $(1-2r)$ by $(1-2r)$ square inside the square. each of these centers then has an annulus of area $2\pi r\ \text{d}r$ around it. 

we are just counting phase space, so we can add up all such centers and radii and be done. 

the one thing we need to be careful about is the unit area in either set of coordinates. 

the length of the separation is twice the radius

<br>
