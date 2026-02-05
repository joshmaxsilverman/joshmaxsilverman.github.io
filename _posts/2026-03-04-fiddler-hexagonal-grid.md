---
layout: post
published: true
title: Hexagonal walker
date: 2026/02/04
subtitle: disappearing food
source: fiddler
kind: puzzles
theme: probability
tags: fourier-transform random-walk
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

originally, i was not going to write anything up because i just had a recursion i evaluated on the computer. but a day after submission, i realized there ought to be a clean solution through fourier transform. moreover, it's a nice example to learn on, and perhaps generalize for the first time from the textbook example of 1d random walk.

first, a word about the intuition. different from transforming a signal that varies in time to a sum of frequency modes, we are not decomposing the probability distribution into signals. instead, we are transforming the spatial variation into a sum of static patterns. the component patterns are periodic and vary in their wavelengths all the way from infinity down to the unit spacing of the lattice.

### 1d random walk

to start, let's do the ordinary, balanced random walk.

each lattice point is connected to its two neighbors with equal chance to move left or right at each step. this means that the probability to be at position $x$ at time $t,$ $\omega(x,t)$ is equal to

$$ \omega(x,t) = \frac12\omega(x-1,t-1) + \frac12\omega(x+1,t-1). $$

using the fourier transform $\widetilde{\omega}(x,t) = \int_\text{all}\, \text{d}x\, e^{ikx} \omega(x,t)$ we get

$$
    \begin{align}
        \widetilde{\omega}(k,t) &= \frac12\int_\text{all}\text{d}x \left[e^{ikx}\omega(x-1,t-1) + e^{ikx}\omega(x+1, t-1)\right] \\
        &= \frac12\int_\text{all}\text{d}x \left[e^{ik}e^{ik(x-1)}\omega(x-1,t-1) + e^{-ik}e^{ik(x+1)}\omega(x+1, t-1)\right] \\
        &= \frac12\left(e^{ik} + e^{-ik}\right)\widetilde{\omega}(k, t-1) \\
        &= \cos k \times \widetilde{\omega}(k, t-1) \\
        &= \cos^t k \times \widetilde{\omega}(k, 0)
    \end{align}
$$

because the standing patterns are on the lattice, the smallest wavelength is the lattice spacing, so $k$ is always less than or equal to $1$ and we can approximate $\cos$ as $1-x^2/2:$

$$
    \begin{align}
        \widetilde{\omega}(k,t) &\approx \left(1-k^2/2\right)^t\widetilde{\omega}(k, 0) \\
        &= \left(1-k^2/2\right)^t \widetilde{\omega}(k,0) \\
        &\approx e^{-k^2t/2}\widetilde{\omega}(k,0) \\
        &= e^{-k^2t/2}
    \end{align}
$$

the second to last line comes from the fact that the initial condition for $\omega$ is $\omega(x,0) = \delta(x)$ so $\widetilde{\omega}(k,0) = \int\text{d}x e^{ikx}\delta(x) = 1.$

to put this back in terms of position, we add up all the standing patterns with the inverse transform:

$$
    \begin{align}
        \omega(x,t) &= \frac{1}{2\pi}\int\text{d}k\, e^{-ikx} \widetilde{\omega}(x,t) \\
        &= \frac{1}{2\pi}\int\text{d}k\, e^{-ikx - k^2t/2} 
    \end{align}
$$

we can turn this into a gaussian integral by shifting the quadratic in the exponent to kill the linear term

$$ \frac{k^2t}{2} + ikx = \left(k\sqrt{\frac{t}{2}} + \frac{ix}{\sqrt{2t}}\right)^2 + \frac{x^2}{2t}. $$

plugging this back in, we get

$$
    \begin{align}
        \omega(x,t) &= e^{-x^2/2t}\frac{1}{2\pi}\int\text{d}k\, e^{-\left(k\sqrt{t/2} + ix/\sqrt{2t}\right)^2} \\
        &= e^{-x^2/2t}\frac{1}{2\pi\sqrt{t}} \int\text{d}k^\prime e^{-{k^\prime}^2/2} \\
        &= e^{-x^2/2t}\frac{1}{\sqrt{2\pi t}}
    \end{align}
$$

setting $x$ to zero, we get the $1$d analogue of the disappearing food problem. and after $t$ steps, we expect to find the fraction $1/\sqrt{2\pi t}$ of the original food left at the origin. plugging in $1/100,$ it would take approximately $t \approx 10,000/2\pi \approx 1592$ steps.

### Hexagonal lattice

for the full problem, we have to accommodate a few details. there are two dimensions that the walkers can move in. they can move directly right or left, changing $x$ by $\pm 1,$ or they can move diagonally changing $(x,y)$ by $\left(\pm 1/2, \pm \sqrt{3}/2\right).$ 

when we treat $x$ and $y$ as continuous variables, and integrate over them, we are undercounting. the discrete probability $\omega(x,y)$ sums to $1,$ but when we integrate, we are locating each lattice point in a unit of area, and the area of that unit is not $1,$ it is $\sqrt{3}/2.$ so, we will have to account for this when we invert the fourier transform. 

this makes $6$ directions that are picked uniformly, making the recursion equation (subscripting time for ease of reading)

$$ 
    \begin{align}
        \omega_t(x,y) &= \frac16\omega_{t-1}(x+1,y) + \frac16\omega_{t-1}(x-1,y) \\
        &+ \frac16\omega_{t-1}(x+\tfrac12,y+\tfrac{\sqrt{3}}{2}) +
        \frac16\omega_{t-1}(x+\tfrac12,y-\tfrac{\sqrt{3}}{2}) \\
        &+ \frac16\omega_{t-1}(x-\tfrac12,y+\tfrac{\sqrt{3}}{2}) + \frac16\omega_{t-1}(x-\tfrac12,y-\tfrac{\sqrt{3}}{2}). 
    \end{align}
$$

now, the static patterns are two dimensional so we need two wave numbers $k$ and $\ell.$ this means that each spatial dimension gets its own transform partner. taking the fourier transform, we get

$$ 
    \widetilde{\omega}_t(k, \ell) = \frac16\int\text{d}x\,\text{d}y\, e^{i{kx+\ell y}} \left[\begin{align}&\omega_{t-1}(x+1,y) + \omega_{t-1}(x-1,y) + \\
        &\omega_{t-1}(x+\tfrac12,y+\tfrac{\sqrt{3}}{2}) +
        \omega_{t-1}(x+\tfrac12,y-\tfrac{\sqrt{3}}{2}) + \\
        &\omega_{t-1}(x-\tfrac12,y+\tfrac{\sqrt{3}}{2}) + \omega_{t-1}(x-\tfrac12,y-\tfrac{\sqrt{3}}{2})\end{align}\right].
$$

doing the same kind of thing we did above 

$$ 
    \begin{align}
        \widetilde{\omega}_t(k, \ell) &= \frac16\left[e^{-ik} + e^{ik} + e^{-ik/2}e^{-i\sqrt{3}\ell/2} + e^{-ik/2}e^{i\sqrt{3}\ell/2} +  e^{ik/2}e^{-i\sqrt{3}\ell/2} + e^{ik/2}e^{i\sqrt{3}\ell/2}\right]\widetilde{\omega}_{t-1}(k, \ell) \\
        &= \frac13\left[\cos k + \cos\left(k/2 + \sqrt{3}\ell/2\right) + \cos\left(k/2-\sqrt{3}\ell/2\right)\right]\widetilde{\omega}_{t-1}(k,\ell)
    \end{align}. 
$$

repeating the expansion

$$ 
    \begin{align}
        \widetilde{\omega}_t(k, \ell) &= \frac13\left[1-\frac12k^2 + 1 - \frac18k^2 - \frac{3}{8}\ell^2 - \frac{\sqrt{3}}{4}k\ell + 1 - \frac18 k^2 - \frac{3}{8}\ell^2 + \frac{\sqrt{3}}{4}k\ell\right] \widetilde{\omega}_{t-1}(k,\ell) \\
        &= \frac13 \left[3 - \frac34 k^2 - \frac{3}{4}\ell^2\right] \widetilde{\omega}_{t-1}(k,\ell) \\
        &= \left[1-\frac{1}{4}k^2-\frac14\ell^2\right] \widetilde{\omega}_{t-1}(k,\ell) \\
        &= \left[1-\frac{1}{4}k^2-\frac14\ell^2\right]^t \widetilde{\omega}_0(k,\ell) \\
        &\approx e^{-\frac{1}{4}k^2t - \frac14\ell^2t} \widetilde{\omega}_0(k,\ell) \\
        &= e^{-\frac{1}{4}k^2t - \frac14 \ell^2t}
    \end{align}
$$

doing the inverse fourier transform we get

$$ \omega_t(x,y) \approx  \dfrac{e^{-(x^2+y^2)/t}}{\pi t}. $$

again, this undercounts due to $\text{d}x\text{d}y$ being a physical area, so we multiply by the unit area $\sqrt{3}/2$ and get

$$ \omega_t(x,y) \approx  \frac{\sqrt{3}}{2}\dfrac{e^{-(x^2+y^2)/t}}{\pi t}. $$

plugging in $(x,y) = (0,0)$ and solving for $t$ we get $t\approx 100\times \sqrt{3}/(2\pi)\approx 27.57$ which, after taking the ceiling, is dead on with the exact result of $28.$

<br>
