---
layout: post
published: true
title: Drone delivery
date: 2023/01/21
subtitle: How much shorter as the crow flies?
source: fivethirtyeight
tags: expectation geometry integration 
theme: geometry
---

>**Question**: A  restaurant at the center of Riddler City is testing an airborne drone delivery service against their existing fleet of scooters. The restaurant is at the center of a large Manhattan-like array of square city blocks, which the scooter must follow.
>
>Both vehicles travel at the same speed, which means drones can make more deliveries per unit time. Assume that (1) Riddler City is circular in shape, as you may recall (2) deliveries are made to random locations throughout the city and (3) the city is much, much larger than its individual blocks.
>
>In a given amount of time, what is the expected ratio between the number of deliveries a drone can make to the number of deliveries a scooter can make?
>
>Extra credit: In addition to traveling parallel to the city blocks, suppose scooters can also move diagonally from one corner of a block to the opposite corner of the block. Now, what is the new expected ratio between the number of deliveries a drone can make and the number of deliveries a scooter can make?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-make-a-speedy-delivery/))

## Solution

Set some total amount of time $T,$ and give each delivery person an arbitrarily long list of addresses $\\{a_1,a_2,\ldots,a_m,\ldots\\}$ which they'll deliver to until time runs out. 

If $t_i$ is the time that the $i^\text{th}$ delivery ends up taking, then the total time for the deliveries is

$$ t_1 + t_2 + \ldots + t_m + \ldots $$

and the expected duration of the first $m$ deliveries is simply $m\langle t\rangle.$ 

The expected number of deliveries that will be made is then $n = T/\langle t\rangle.$

Because the speed of each vehicle is constant, time is directly proportional to distance $\left(d = vt\right)$. So, we can find $\langle t\rangle$ for each mode of transportation by averaging $d$ over all possible addresses in the city, i.e., $n = vT/\langle d\rangle.$ 

### The road to el $\langle d\rangle$-rado

Because the drone can fly straight to the target, if a delivery has coordinates $(x,y)$ on the city grid, the drone has to cover distance $\sqrt{x^2 + y^2}$ whereas the scooter, confined to the blocks of the grid, has to cover distance $\left(\lvert x\rvert + \lvert y\rvert\right).$

Summing over the points of the lattice could be an excursion, but the city is big in comparison to the lengths of its blocks. That means that we can approximate the grid with a fine mesh where the lengths of blocks become infinitesimally small relative to the city's expanse. 

### Estimating the advantage

Switching to polar coordinates, we get $\left(\lvert x\rvert + \lvert y\rvert\right) \rightarrow r\left(\lvert\cos\theta\rvert+ \lvert\sin\theta\rvert\right)$ and $\sqrt{x^2+y^2}\rightarrow r.$ The scooter distance for any given delivery target $(x,y)$ becomes

$$
  d_\text{scoot} = r\left(\lvert\cos\theta\rvert + \lvert\sin\theta\rvert\right)
$$

In this approximation (where the city is much bigger than its blocks), the distance dependence factors out, so the discrepancy will depend solely on the direction $\theta.$ From here on we will drop the factor of $r.$

The problem is the same whatever quadrant of the grid the delivery is in, so we can work with $\theta$ between $0$ and $\frac12\pi,$ where $\cos\theta$ and $\sin\theta$ remain positive, allowing us to drop the absolute values.

The expected advantage for drone deliveries is then just the ratio of the averages:

$$
  \begin{align}
    \dfrac{\langle d_\text{scoot}\rangle}{\langle d_\text{drone}\rangle} &= \dfrac{2}{\pi}\int\limits_0^{\frac12\pi}d\theta \left(\cos\theta + \sin\theta\right) \\
    &= \dfrac{4}{\pi} \\
    &\approx 1.273
  \end{align}
$$

### Extra credit

In the second scenario, the scootist can also travel along diagonals that cut through each block, if it can shorten their delivery. As long as they have to travel horizontally **and** vertically, it does.

To take advantage of this, they should travel diagonally until they are directly below or directly to the side of the delivery, and thereafter move in a straight line directly to the address.

Drawing a picture, this means traveling diagonally across $\min\\{x,y\\}$ blocks (which contributes distance $\sqrt{2}\min\\{x,y\\}$) followed by $\left(\max\\{x,y\\}-\min\\{x,y\\}\right)$ blocks straight to the target, making the distance to the target

$$
  \left(\sqrt{2}-1\right)\min\{x,y\} + \max\{x,y\}.
$$

![](/img/2023-01-23-min-max-delivery.png){:width="450 px" class="image-centered"}

The problem is symmetric across the line $x = y,$ so we can evaluate the problem when $x > y.$ With this restriction, the distance becomes

$$
  \left(\sqrt{2}-1\right) y + x.
$$

Again, forming the drone-to-scooter advantage, we get

$$
  \dfrac{\langle d_\text{scoot}\rangle}{\langle d_\text{drone}\rangle} = \frac{4}{\pi} \int\limits_0^{\frac14\pi} d\theta \left[\left(\sqrt{2}-1\right) \sin\theta + \cos\theta\right]
$$

which comes to 

$$ 
  \begin{align}
    \dfrac{\langle d_\text{scoot}\rangle}{\langle d_\text{drone}\rangle} &= \frac{4}{\pi}\left[\left(\sqrt{2}-1\right)\left(1-\dfrac{1}{\sqrt{2}}\right) + \frac{1}{\sqrt{2}}\right] \\
    &= \dfrac{8}{\pi}\left(\sqrt{2}-1\right) \\
    &\approx 1.055
  \end{align}
$$


<br>
