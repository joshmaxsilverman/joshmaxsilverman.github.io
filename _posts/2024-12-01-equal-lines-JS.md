---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>**Question**: Two random points, one red and one blue, are chosen uniformly and independently from the interior of a square. What is the probability that there exists a point on the side of the square closest to the blue point that is equidistant to both the blue point and the red point?

<!--more-->

([Fiddler on the Proof](URL))

## Solution

First let's set some conventions:

- call the blue point $b$ and the red point $r$.
- take the side closest to $b$ to be the bottom of the square.

To figure out the conditions for the point of equidistance to exist, let's do a thought experiment where we find it empirically. 

Pick a random point $z$ on the bottom edge. If $z$ isn't equidistant from $b$ and $r$ then we need to shift it toward one of the corners.

As long as one of the corners is closer to $b$ and the other is closer to $r$, this will find the point. If both corners are closer to $b$ or both are closer to $r$  then all points on the line are closer to one of the points than the other. In this case, moving the point $z$ is hopeless since the point of equidistance doesn't exist.

So the condition for such a point of equidistance to exist is 

- $d(\text{left corner}, b) < d(\text{left corner},r)$ **AND**
- $d(\text{right corner},b) > d(\text{right corner},r)$ 

(or vice versa). This is just:

$$ x_r^2 + y_r^2 < x_b^2 + y_b^2 \,\,\mathbf{XOR}\,\, (x_r-1)^2 + y_r^2 < (x_b-1)^2 + y_b^2 $$

This describes two quarter circles centered on either corner, with their mutual overlap removed, so the probability is equal to:

$$ \frac14\pi\left(x_b^2 + y_b^2\right) + \frac14\pi\left((1-x_b)^2 + y_b^2\right) - 2\times\text{area overlap} $$

The circles overlap at $x = r_\ell + \frac12\left(r_r - r_\ell\right) = \frac12\left(r_\ell + r_r\right).$

what are the horizontal bounds of the circular segments?

(1-radius of right circle, intersection of the two circles, radius of left circle)

the radius of the left is $x_b^2+y_b^2$, the radius of the right is $(x_b - 1)^2 + y_b^2$.




<br>
