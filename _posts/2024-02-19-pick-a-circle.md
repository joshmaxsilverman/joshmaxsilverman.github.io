---
layout: post
published: false
title: Pick a circle
date: 2024/02/19
subtitle:
tags: d
---

>Question

<!--more-->

([Jane Street](URL))

## Solution

we want to calculate the volume of $(x_1,y_1,x_2,y_2)$-space that contributes to circles with diameters contained in the square. 

$$ \int dx_1 \int dy_1 \int dx_2 \int dy_2\ \mathbb{I}(\text{diameter forms circle contained in the unit square}). $$

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

$$ P(\text{interior circle}) \propto \int dr\, 2\pi r(1-2r)^2. $$

but we need to be careful about the unit area in either set of coordinates. in moving to the (center, separation) coordinate system, we stretch out each unit vector by a factor of $\sqrt{2}.$ we can see this by calculating the magnitude of e.g. $d\vec{x}_c$ or by calculating the area element $dA = dx_1\,dx_2$ in terms of $dx_c$ and $dx_r.$

taking the derivative, we get $d\vec{x}_c = \frac12\left(d\vec{x}_1 + d\vec{x}_2\right)$ which has magnitude $\frac12\sqrt{dx_1^2 + dx_2^2} = \frac{1}{\sqrt{2}}dx_1.$ 

taking cross products, we get $dA = \lvert d\vec{x}_c\times d\vec{x}_r\rvert = \lvert\frac14\left(d\vec{x}_1\times d\vec{x}_2 + d\vec{x}_2\times d\vec{x}_1\right)\rvert = \frac{dx_1dx_2}{2},$ which gives us 

$$ dx_c\,dx_r = \frac12dx_1\,dx_2. $$

with this, we can finish the expression for the volume of phase space contributed by circles of diameter $2r:$

$$ dr\,4\times 2\pi r(1-2r)^2. $$

integrating this over all valid radii, we get 

$$ \begin{align}
  P(\text{interior circle}) &= 8\pi\int\limits_0^\frac{1}{2}dr\, r(1-2r)^2 \\
                            &= 8\pi \int\limits_0^{\frac12}dr\, \frac12\left[(1-2r)^2 - (1-2r)(1-2r)^2\right] \\
                            &= 2\pi \int\limits_0^1 du\, \left[(1-u)^2 - (1-u)^3\right] \\
                            &= \frac{\pi}{6}
\end{align} $$

this approach is nice apart from the unit area changing under our feet. 

### systematic

another way to go is probability. the probability that a random pair of points makes an interior circle is the sum over all possible radii $r$ that a pair of points make a circle of radius $r$ that's an interior circle.

$$ P(\text{points forms an interior circle}) = \int dr\, P(\text{points forms an interior circle of radius $r$}). $$

we can break this up into two simpler distributions:

$$ P(\text{points form an interior circle}\rvert\text{diameter $r$}) \cdot P(\text{radius $r$}) $$

let's do the second piece first. since we pick the points randomly, we can treat the $x$ and $y$ coordinates independently. the probability of getting radius $r$ is the probability that the $x$ and $y$ components of the diameter form a vector of magnitude $2r.$ 

$$ P(\text{radius $r$}) = \int d\theta\, P(\text{$x_1-x_2 = 2r \cos\theta$})P(\text{$y_1-y_2 = 2r \sin\theta$}). $$

the probability that two random unit variables are separated by a distance $d$ is just $2(1-d).$ 

one way to see this is to place two points a distance $d$ apart with the left hand one at the origin. there is $(1-d)$ worth of open space to slide them through before the right hand point hits $1.$ lastly, we can swap the order of the points.

so the probability is

$$ \begin{align}
  P(\text{radius $r$}) &= 4\int\limits_0^{\frac12\pi} d\theta\, 4(1-2r\cos\theta)(1-2r\sin\theta) \\
  &= 8r(\pi -4(2-r)r). 
\end{align} $$

the next piece is straightforward in concept, but tricky to calculate. if we randomly place the center of the circle at coordinates $(x_c,y_c),$ what is the probability that it forms an interior circle.

first of all, the center can't be within a radius of the square's boundary. this means that the probability is $0$ inside the semi-circles of radius $r$ around each corner.

likewise, if the center is more than a radius away from the boundary, the circle will definitely be interior, so the probability is $1$ inside the central $(1-2r)$ by $(1-2r)$ square. 

drawing what we've figured out so far, we have:

[drawing]

the tricky regions are the area under the semi-circle boundary, and the rectangular protuberance. 

the idea is, in each region, to calculate the fraction of possible orientations that lead to the circle being interior: $\theta_\text{valid}/\theta_\text{possible}.$

**rectangular protuberance**

in the rectangular protuberance, we have an interior circle so long as $x_c$ is further from the wall than $r\sin\theta.$ this defines a range of angles $(-\theta,\theta)$, between which the circle won't cross the wall. solving $r\sin\theta = 1-x_c$ gives us $2\theta = 2\arcsin\left(\frac{1-x_c}{r}\right).$ since the angle is chosen at random, the probability that the circle is interior is just 

$$\begin{align} 
  P_\text{curve}(\text{interior circle})(x_c) &= 2\theta/\pi \\
  &= \frac{1}{\pi}\arcsin\left(\frac{1-x_c}{R}\right)
\end{align} $$

adding up over all possible values of $x_c,$ the probability of a circle whose center is under the curve being interior is

$$ P_\text{curve}(\text{interior circle}) = (1-2r)\int\limits_{1-r}^1 dx_c\, \frac{1}{\pi}\arcsin\left(\frac{1-x_c}{r}\right) = \frac{(\pi-2)r(1-2r)}{2\pi}. $$

**under the curve**

the region under the curve

<br>
