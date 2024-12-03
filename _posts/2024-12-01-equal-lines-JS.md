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

Let's set some conventions

- call the blue point $b$ and the red point $r$.
- take the side closest to $b$ to be the bottom of the square.
- let $z$ be a trial point on that edge

if $z$ isn't equidistant from $b$ and $r$ then we need to move it toward one of the corners to find the point of equidistance. 

for this to be possible, one of the corners has to be closer to $b$ while the other is closer to $r$. if both are closer to $b$ or both are closer to $r$  then all points on the line are closer to one point than the other. then moving the point $z$ is hopeless.

so the condition for such a point of equidistance to exist is 

- $d(\text{left corner}, b) < d(\text{left corner},r)$ **AND**
- $d(\text{right corner},b) > d(\text{right corner},r)$ 

or vice versa. this is just:

$$ x_r^2 + y_r^2 < x_b^2 + y_b^2 \,\,\mathbf{XOR}\,\, (x_r-1)^2 + y_r^2 < (x_b-1)^2 + y_b^2 $$

this region makes two quarter circles centered on either corner, with their mutual overlap removed.

what are the horizontal bounds of the circular segments?

(1-radius of right circle, intersection of the two circles, radius of left circle)

the radius of the left is $x_b^2+y_b^2$, the radius of the right is $(x_b - 1)^2 + y_b^2$.




<br>
