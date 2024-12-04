---
layout: post
published: true
title: Lines of equidistance
date: 2024/12/01
subtitle: What's the chance that two random points in the square are equidistant from some random point on the side that's closest to one of them?
tags: geometry distance intermediate-value-theorem
---

>**Question**: Two random points, one red and one blue, are chosen uniformly and independently from the interior of a square. What is the probability that there exists a point on the side of the square closest to the blue point that is equidistant to both the blue point and the red point?

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/beside-the-point-index/))

## Solution

First let's set some conventions:

- call the blue point $b$ and the red point $r$,
- take the side closest to $b$ to be the bottom of the square, and
- take the blue point to fall inside the square's lower left octant.

To figure out the conditions for the point of equidistance to exist, let's do a thought experiment where we find it empirically. 

### Conditions for solution

Pick a random point $z$ on the bottom edge. If $z$ isn't equidistant from $b$ and $r$ then we need to shift it toward one of the corners. As long as one of the corners is closer to $b$ and the other is closer to $r$, this scheme will find the point. Why? The intermediate value theorem. 

If both corners are closer to $b$ or both are closer to $r$ then all points on the line are closer to one of the points than the other. In this case, moving the point $z$ is hopeless since the point of equidistance doesn't exist.

So the condition for such a point of equidistance to exist is 

$$ d(\text{left corner}, b) < d(\text{left corner},r)\,\, \mathbf{XOR}\,\,  d(\text{right corner},b) < d(\text{right corner},r). $$

<!-- Putting this to symbols, we get:

$$ x_r^2 + y_r^2 < x_b^2 + y_b^2 \,\,\mathbf{XOR}\,\, (x_r-1)^2 + y_r^2 < (x_b-1)^2 + y_b^2. $$ -->

This describes two quarter circles centered on either corner, with their mutual overlap removed. 

![](/img/2024-12-01-region-plot.png){:width="450px" class="image-centered"}

The radii are $r_\ell^2 = x_b^2 + y_b^2$ and $r_r^2 = (1-x_b)^2 + y_b^2$ so the total probability is equal to:

$$ \frac{P_\text{equidistance}(x_b, y_b)}{8} = \frac{\pi}{4}\left(x_b^2 + (1-x_b)^2 + 2y_b^2\right) - 2\times\text{area of overlap} $$

### Area of overlap

Reflecting the area of overlap across the $x$-axis, we can see it's a union of two circular segments. We can find the area of each one by taking the area of the circular wedge that envelops it and subtracting the area of the missing isosceles triangle. 

The circles overlap at $x = x_b$ so the area of the left segment is $\frac12\left(\theta_\ell r_\ell^2 - x_b y_b\right).$ Putting it together with the same analysis for the right segment, we get the area of the overlap

$$ \text{area of overlap} = \frac12\left(\theta_\ell r_\ell^2 - x_b y_b\right) + \frac12\left(\theta_r r_r^2 - (1-x_b) y_b\right). $$ 

<!-- and the total probability that a random red point has a line of equidistance with the blue point is 

$$ P_\text{equidistance}(x_b, y_b) = 8\left(\frac{\pi}{4}\left[{r_\ell}^2 + r_r^2\right] - \left[\frac12\left(\theta_\ell {r_\ell}^2 - x_b y_b\right) + \frac12\left(\theta_r r_r^2 - (1-x_b) y_b\right)\right]\right). $$ -->

Now, we just have to average over all possible locations for the blue point in the lower left quadrant, which we can do by taking $y_b$ from zero to $x_b,$ and $x_b$ from zero to $\frac12$:

$$ 
  \begin{align}
    P_\text{equidistance} &= \int\limits_0^\frac{1}{2} \text{d}x_b \int\limits_0^{x_b}\text{d}y_b\, P_\text{equidistance}(x_b, y_b) \\
                          &= \frac{1+2\pi-\log 4}{12} \\
                          &\approx 0.491408 \ldots 
   \end{align} 
$$


<br>
