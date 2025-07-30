---
layout: post
published: false
title: Robot road trip
date: 2025/08/01
subtitle:
tags:
---

>**Question**

<!--more-->

([Jane Street](URL))

## Solution

### Setup

Because each car is spawned uniformly in time and space, we can condition on two speeds and find the relative fraction of spawn times and distances that lead to their intersection. 

### Relative probability of interaction

Let $t_B$ and $x_B$ be the time and position at which car $B$ was spawned, that travels at speed $v_B$. Considering the time and position of car A's spawn to be $(0,0)$, we have
$$v_At = x_B + v_B\left(t-t_B\right)$$
The latest spawn time that car $B$ can spawn is $T_A=N/v_A$, the time at which car $A$ comes off the highway. The earliest it can spawn is one lifetime before car $A$ despawns, $(N/v_A - N/v_B)$ so the range for $t_B$ is 

$$ N/v_A \geq t \geq N/v_A - N/v_B. $$

Because $t$ ranges from $0$ to $N/v_A$ the range for $x_B$ is 

$$ N \geq x_B \geq N - N(1 - v_B/v_A) $$

At the upper end, car $B$ spawns exactly where $A$ despawns and at the lower end, it is positioned so that $A$ can overtake it at the last minute.

Because we're told that each car has at most one interaction, the probability that any given car of speed $v_A$ overtakes a car of speed $v_B$ is proportional to the sub-volume coordinate space. Since $\Delta t$ and $\Delta v_B$ are both simple expressions in terms of velocity and $N$, they form a rectangle and the relative probability is just

$$ P(v_A\text{ overtakes }v_B) \propto \Delta t_B\Delta x_B = N^2\left(1/v_A - 1/v_B\right). $$
### Distance lost

With this in hand, we can find the relative expected lost distance, if only we had expressions for lost distance. 

First of all, it is awkward to frame the problem in terms of lost distance, since every trip lasts for $N$ miles. What's actually lost is time. But alas.

The distance lost accelerating and decelerating in the fast lane is the distance the slow car would have traveled in the time $v_B\Delta t = 2v_B(v_B-a)$ travels while decelerating $\langle v\rangle \Delta t = \left(v_B + a\right)\left(v_B-a\right)$ which is $2v_B^2-2v_Ba - v_B^2 + a^2 = v_B^2 + a^2 - 2v_Ba = (v_B-a)^2.$ 

In the slow lane, the car goes down to and up from zero ($a=0$) so it's just $v_B^2.$

### Expected loss

Now we can find the expected distance lost, with the help of computer algebra



<br>
