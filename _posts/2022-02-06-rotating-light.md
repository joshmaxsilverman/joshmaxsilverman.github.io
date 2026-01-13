---
layout: post
published: True
title: Rotating light
tags: superposition physics concave
subtitle: How much light can you spin with a series of filters?
source: fivethirtyeight
date: 2022/02/06
theme: physics
---

>**Question:** I have a light source that’s polarized in the vertical direction, but I want it to be polarized in the horizontal direction. To make that happen I need … polarizers! When light passes through a polarizer, only the light whose polarization aligns with the polarizer passes through. When they aren’t perfectly aligned, only the component of the light that’s in the direction of the polarizer passes through.
>
>Unfortunately, that means I can’t turn vertically polarized light into horizontally polarized light with a single polarizer. But I can do it with two polarizers, as shown below.
>
>A vector is vertical. Its component along a 45 degree angle is shown. That second vector's component along another 45 degree angle is also shown. The final vector has half the length of the original.
If the first polarizer is positioned at an acute angle with respect to the light, and then the second polarizer is positioned at a complementary angle with respect to the first polarizer, some light will be horizontally polarized in the end.
>
>Now, I have tons of polarizers, and each one also reflects 1 percent of any light that hits it — no matter its polarization or orientation — while polarizing the remaining 99 percent of the light.
>
>I’m interested in horizontally polarizing as much of the incoming light as possible. How many polarizers should I use?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/a-riddle-that-will-make-you-scream/))

## Solution

The magic of the problem is this: one horizontal polarizer would block all the light, polarizers do nothing but block light, yet a stack of many polarizers in front of the horizontal one will let a ton of light through.

### One polarizer

The polarization of a photon is a vector we can look at from any perspective we like. For example, in the basis of horizontal and vertical polarization, the incoming vertically polarized beam looks like

$$ \lvert\gamma\rangle = 0\lvert\rightarrow\rangle + 1\lvert\uparrow\rangle. $$ 

So, at each filter, we need to rotate the polarization state into the basis of the filter and then extinguish the "horizontal" component in that basis. 

If the first filter makes an angle $\theta_1$ with the vertical then, putting this to transformations, the state becomes

$$
\begin{align}
\lvert\gamma^\prime\rangle &= \mathbf{R}(\theta_1) \lvert\gamma\rangle \\
&= \left(\begin{array}\ \cos\theta_1 & \sin\theta_1 \\ -\sin\theta_1 & \cos\theta_1\end{array}\right)\lvert\gamma\rangle,
\end{align}
$$

or, resolving to components in the new basis, 

$$ \lvert\gamma\rangle \longrightarrow \cos\theta_1\lvert\uparrow^\prime\rangle. $$

The physical probability of a photon in the beam interacting with the filter in either polarization state is the **magnitude** of the component in that direction. If the photon is interacts in the perpendicular state, then it's extinguished from the beam.

So, the probability of a photon passing the first filter is just the square of the veritcal component, $ \lvert\langle\uparrow^\prime\rvert\gamma^\prime\rangle\rvert^2 = \cos^2\theta_1.$

There is also a probability $f = 0.99$ for the photon to be physically reflected off the filter (and lost from the beam). This means that the overall probability of transmission through the first filter is 

$$ P(\text{transmit}) = f\cos^2\theta_1. $$

### A filter train

After a series of $n$ filters, the fraction of photons remaining in the beam will be

$$ P(\text{transmission}) = f^n \prod_{i=1}^n \cos^2\theta_i. $$

After the last filter, we need all of the light to be horizontally polarized. This means that the final polarization $\lvert\uparrow^n\rangle$ is the horizontal polarization state $\lvert\rightarrow\rangle,$ and we have

$$ \sum_i \theta_i = \frac{\pi}{2}. $$

### Best angles

Keeping $n$ fixed, we can think about the angular piece on its own. We want the product of the $\cos^2\theta_i$s to be as big as possible.

To get the intuition, think of two angles $\theta_1$ and $\theta_2$ that have to add up to some value $x.$ 

Because $\cos\theta$ always slopes downward on $\left[0,\frac{\pi}{2}\right),$ any decrease in $\cos\theta_1$ that we might avoid by keeping $\theta_1$ smaller than $\theta_2$ will be outweighed by the larger decrease that comes from increasing $\theta_2.$ 

The upshot of this is that we want to keep $\theta_1$ as small as possible without making $\theta_2$ bigger than it needs to be. In other words, we need to set them equal. For $n$ angles, this argument extends, and we should divide the overall rotation of $\pi/2$ into $n$ equal rotations of $\pi/(2n).$

### Maximize transmission

After all that, we know that maximal transmission through $n$ filters is achieved by making all the rotations equal, and so

$$ P(\text{transmission}) = f^n \cos^{2n}\frac{\pi}{2n}. $$

All that's left is to find the optimal number of filters, $n.$ Plotting this probability, we can see that it maxes out at $n=16$ where 

$$P(\text{transmission}) = 0.99^{16} \left(\cos\frac{\pi}{32}\right)^{32} \approx 0.72959455363.$$

![](/img/2022-02-06-rotating-light.JPG){:width="450 px" class="image-centered"}


<br>
