---
layout: post
published: false
title: 
date: 2018/04/21
subtitle: geometry distance intermediate-value-theorem
tags:
---

>**Question**: Two random points, one red and one blue, are chosen uniformly and independently from the interior of a square. What is the probability that there exists a point on the side of the square closest to the blue point that is equidistant to both the blue point and the red point?

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/beside-the-point-index/))

## Solution

First let's set some conventions:

- call the blue point $b$ and the red point $r$,
- take the side closest to $b$ to be the bottom of the square,
- take the blue point to fall inside the square's lower left octant.

To figure out the conditions for the point of equidistance to exist, let's do a thought experiment where we find it empirically. 

### Conditions for solution

Pick a random point $z$ on the bottom edge. If $z$ isn't equidistant from $b$ and $r$ then we need to shift it toward one of the corners. As long as one of the corners is closer to $b$ and the other is closer to $r$, this scheme will find the point. Why? The intermediate value theorem. If both corners are closer to $b$ or both are closer to $r$ then all points on the line are closer to one of the points than the other. In this case, moving the point $z$ is hopeless since the point of equidistance doesn't exist.

So the condition for such a point of equidistance to exist is 

$$ d(\text{left corner}, b) < d(\text{left corner},r)\, \mathbf{XOR}\,  d(\text{right corner},b) < d(\text{right corner},r). $$

<!-- Putting this to symbols, we get:

$$ x_r^2 + y_r^2 < x_b^2 + y_b^2 \,\,\mathbf{XOR}\,\, (x_r-1)^2 + y_r^2 < (x_b-1)^2 + y_b^2. $$ -->

This describes two quarter circles centered on either corner, with their mutual overlap removed. 
The radii are $r_\ell = x_b^2 + y_b^2$ and $r_r = (x_b-1)^2 + y_b^2$ so the total probability is equal to:

$$ P_\text{equidistance} = 8\left(\frac{\pi}{4}\left[x_b^2 + (1-x_b)^2 + 2y_b^2\right] - 2\times\text{area overlap}\right) $$

### Area of overlap

Reflecting the area of overlap across the $x$-axis, we can see it's a union of two circular segments. We can find each of their areas by taking the area of the circular wedge that envelops it and subtracting the area of the missing isosceles triangle.

The circles overlap at $x = x_b$

The area of the left segment is then 

$$ \frac12\left(\theta r_\ell^2 - x_b y_b\right). $$ 

Putting it together with the same analysis for the right segment, we get the area of the overlap

$$ \frac12\left(\theta r_\ell^2 - x_b y_b\right) + \frac12\left(\theta r_r^2 - (1-x_b) y_b\right) $$ 

and the total probability that a random red point has a line of equidistance with the blue point is 

$$ P_\text{equidistance} = 8\left(\frac{\pi}{4}\left[r_\ell^2 + r_r^2\right] - \left[\frac12\left(\theta r^2 - x_b y_b\right) + \frac12\left(\theta r_r^2 - (1-x_b) y_b\right)\right]\right). $$




<br>
