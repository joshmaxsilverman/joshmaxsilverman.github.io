---
layout: post
published: true
title: $t$ for tackle
date: 2021/08/30
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

First, we can work in the reference frame of the chaser and find the speed at which the chaser approaches the leader. 

The chaser moves directly at the leader so their motion only works to close the gap. The leader, however, moves away from the chaser, so long as their trajectories are not parallel. If the chaser makes an angle $\theta$ with the $x$-axis, then the leaders velocity in the frame of the chaser is $V_L = V_L \langle \cos(\theta-\frac{\pi}{2}), \sin(\theta-\frac{\pi}{2}\rangle = V_L\langle \sin\theta, \cos\theta\rangle.$ So, the chaser closes the gap with speed $V_\text{rel} = V_L\sin\theta - V_C.$

Over the course of the chase, this gap shrinks from $L$ to $0,$ so

$$
\begin{align}
L &= \int\limits_0^T dt \left(V_L\sin\theta - V_C\right) \\
&= V_L\left(\int\limits_0^T dt\, \sin\theta\right) - V_C\cdot T.
\end{align}
$$

In principle, this integral requires us to know the behavior of $\theta(t).$ In practice, the same integral pops up in a simpler problem: the total distance that the chaser moves upfield, $2L.$ In the coordinate system of the field, their velocity is $V_C\langle \cos\theta, \sin\theta\rangle,$ so their total displacement upfield is just

$$
2L = V_C\int\limits_0^T dt\, \sin\theta.
$$

This leaves us with an algebra problem for $T$. Calling the integral $S,$ we get:

$$
\begin{align}
L &=  V_L S - V_C T \\
2L = V_C S
\end{align}
$$

or

$$
\begin{align}
L &= 2L\frac{V_L}{V_C} - V_C T \\
V_C T &= L\left(2\frac{V_L}{V_C} - 1\right) \\
T &= L\frac{2V_L - V_C}{V_C^2}
\end{align}
$$

We can solve this to find $V_C$ in terms of $T,$ $L,$ and $V_L$:


<br>
