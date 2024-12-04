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
The radii are $x_b^2 + y_b^2$ and $(x_b-1)^2 + y_b^2$ so the total probability is equal to:

$$ P_\text{equidistance} = 8\times\frac{\pi}{4}\left[x_b^2 + (1-x_b)^2 + 2y_b^2\right] - 2\times\text{area overlap} $$

### Area of overlap

Reflecting the area of overlap across the $x$-axis, we can see it's a union of two circular segments. We can find each of their areas by taking the area of the circular wedge that envelops it and subtracting the area of the missing isosceles triangle.

The area of the left segment is then 

$$ 2\theta r^2 - \ell_\text{intersect}r\sin\theta, $$ 

where $r$ is the circle's radius, $\theta$ is the angle subtended by the segment, and $\ell_\text{intersect}$ is the $x$-position where the segment begin.

The circles overlap at $x = r_\ell + \frac12\left(r_r - r_\ell\right) = \frac12\left(r_\ell + r_r\right).$

what are the horizontal bounds of the circular segments?

(1-radius of right circle, intersection of the two circles, radius of left circle)

the radius of the left is $x_b^2+y_b^2$, the radius of the right is $(x_b - 1)^2 + y_b^2$.




<br>
