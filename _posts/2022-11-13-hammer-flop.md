---
layout: post
published: true
title: Fast Hammer
date: 2022/11/13
subtitle: 
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

Throughout the hammer's fall, energy is conserved. When the hammer makes angle $\phi$ with the ground, the energy is

$$ E = \frac12 MV^2 + Mg\ell\sin\phi. $$

Initially, the hammer is standing straight which lets us solve for $V(\phi):$

$$ V(\phi) = \sqrt{2g\ell\left(1-\sin\phi\right)}. $$

We care about the horizontal component of the hammer's velocity, $V_x(\phi) = V(\phi)\sin\phi.$ We want to maximize this, and it's easier to do that working with the square $V_x(\phi)^2:$

$$ V_x(\phi)^2 = \sin^2\phi\left(1-\sin\phi\right). $$

Taking the derivative and setting it to zero, we get 

$$ 2\sin\phi\cos\phi = 3\sin^2\phi\cos\phi, $$

so that $V_x(\phi)$ is maximized when $\sin\phi = \frac23.$

The hammer hits the door when $\ell\sin\phi = d_\text{init},$ so we should place the hammer $\boxed{d_\text{init} = \frac23\ell}$ away from the door. 

If we do that, then the hammer will hit the door with speed $V_x = \frac23\sqrt{\frac23 g\ell} \approx 9.41\text{ m/s}$

<br>
