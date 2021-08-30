---
layout: post
published: true
title: $t$ for tackle
date: 2021/08/30
---

>**Question**: Hames Jarrison has just intercepted a pass at one end zone of a football field, and begins running — at a constant speed of $15$ miles per hour — to the other end zone, $100$ yards away.
>
>At the moment he catches the ball, you are on the very same goal line, but on the other end of the field, $50$ yards away from Jarrison. Caught up in the moment, you decide you will always run directly toward Jarrison’s current position, rather than plan ahead to meet him downfield along a more strategic course.
>
>Assuming you run at a constant speed (i.e., don’t worry about any transient acceleration), how fast must you be in order to catch Jarrison before he scores a touchdown?

<!--more-->

([FiveThirtyEight](URL))

## Solution

First, we can work in the reference frame of the chaser and find the speed at which the chaser approaches the leader. 

The chaser moves directly at the leader so their motion only works to close the gap. The leader, however, moves away from the chaser, so long as their trajectories are not parallel. If the chaser makes an angle $\theta$ with the $x$-axis, then the leaders velocity in the frame of the chaser is $V_L = V_L \langle \cos(\theta-\frac{\pi}{2}), \sin(\theta-\frac{\pi}{2}\rangle = V_L\langle \sin\theta, \cos\theta\rangle.$ So, the chaser closes the gap with speed $V_\text{rel} = V_L\sin\theta - V_C.$

Over the course of the chase, this gap shrinks by $L,$ so

$$
\begin{align}
-L &= \int\limits_0^T dt \left(V_L\sin\theta - V_C\right) \\
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
-L &=  V_L S - V_C T \\
2L &= V_C S
\end{align}
$$

or

$$
\begin{align}
-L &= 2L\frac{V_L}{V_C} - V_C T \\
V_C T &= L\left(2\frac{V_L}{V_C} + 1\right) \\
T &= L\frac{2V_L + V_C}{V_C^2} \\
\dfrac{2L}{V_L} &= L\frac{2V_L + V_C}{V_C^2}
\end{align}
$$

We can solve this to find $V_C$ in terms of $T,$ $L,$ and $V_L$:

$$
V_C = \dfrac{1+\sqrt{17}}{4}V_L
$$

<br>
