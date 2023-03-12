---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

we want to find the trajectory that makes the time from start to finish as small as possible.

the logic will be to express the total time $T$ in terms of the shape of the trajectory and the two endpoints, and then use functional calculus to find the minimal shape.

in the big picture, that problem is analytic without the constraint. the shortest path between two points is a cycloid.

given two points and the imperative to minimize time, the cycloid will do whatever it needs to minimize time. however, we aren't allowed to build the track below $\Delta h.$ still, the cycloid is the fastest trajectory between points. this means that the fastest path is to follow a cycloid down to the lowest allowable height, hit the bottom at $\Delta x,$ follow the floor for a while, then follow the same curve back up to the opposite side. 

this makes good physical sense -- energy is conserved, and dipping down the full $\Delta y$ means we achieve the maximum velocity for the majority of the trajectory.

### calculation

with the logic behind us, what remains is deriving the shape of the curve (a cycloid), use it to determine the value of $\Delta x,$ and then plug the trajectory back into the expression for $T.$

the total time $T$ is the sum of all the little time intervals that make up the trajectory:

$$ T = \int dt. $$

the tiny distance traveled by the marble along the trajectory in time $dt$ is equal to $ds$ divided by the instaneous velocity:

$$ dt = \frac{ds}{v(y)} $$

breaking the linear segment into its horizontal and vertical components, we get $ds = \sqrt{dx^2 + dy^2}$ and so

$$
  \begin{align}
T &= \int \dfrac{\sqrt{dx^2 + dy^2}}{v(y)} \\
  &= \int dx\,\dfrac{\sqrt{1 + \left(\frac{dy}{dx}\right)^2} }{v(y)}.
  \end{align}
$$

conserving energy, the marble's velocity at height $y$ below its starting point is $v(y) = \sqrt{2gy}.$ 

with this, we get

$$ T = \int dx\,\sqrt{\dfrac{1 + {y^\prime}^2}{2gy}}. $$

we want to find the curve $y(x)$ that minimizes $T.$ if we had that function (let's call it $y^*(x)$), and it really is a minimum, then any small change we make to it should keep $T$ very close to the minimum value. in a sense, taking the derivative of $T$ with respect to the function $y(x)$ should be $0.$

<!-- https://github.com/joshmaxsilverman/joshmaxsilverman.github.io/blob/master/_posts/2023-02-11-improbable-sky.md -->

<br>
