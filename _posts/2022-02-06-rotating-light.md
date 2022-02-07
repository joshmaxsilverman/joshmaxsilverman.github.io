---
layout: post
published: True
title: Rotating Light
date: 2022/02/06
---

>**Question:** jjj

<!--more-->

([FiveThirtyEight](URL))

## Solution

The magic of the problem is this: one horizontal polarizer would block all the light, polarizers do nothing but block light, yet a stack of many polarizers in front of the horizontal one will let a ton of light through.

### One polarizer

The polarization of a beam photon is a vector we can look at from any perspective we like. 

For example, in the basis of horizontal and vertical polarization, the incoming vertically polarized beam looks like

$$ \lvert\gamma\rangle = 0\lvert\rightarrow\rangle + 1\lvert\uparrow\rangle. $$ 

When the beam passes through a polarized filter, the component that's perpendicular to the polarizer is extinguished.  

So, at each filter, we need to rotate the polarization state into the basis of the filter and then extinguish the "horizontal" component in that basis. 

If the first filter makes an angle $\theta_1$ with the vertical then, in the new basis, the state becomes

$$
\begin{align}
\lvert\gamma^\prime\rangle &= \left(\begin{array}\ \cos\theta_1 & \sin\theta_1 \\ -\sin\theta_1 & \cos\theta_1\end{array}\right)\lvert\gamma\rangle,
\end{align}
$$

or, resolving to components in the new basis, 

$$ \lvert\gamma\rangle \longrightarrow \sin\theta_1\lvert\rightarrow^\prime\rangle + \cos\theta_1\lvert\uparrow^\prime\rangle. $$

The physical probability of a photon in the beam being in either polarization state is the **magnitude** of the component in that direction. 

So, the probability of a photon passing the first filter is just the square of the veritcal component, $ \lvert\langle\uparrow^\prime\rvert\gamma^\prime\rangle\rvert^2 = \cos^2\theta_1.$

However, there is also a probability $f = 0.99$ for the photon to be physically reflected off the filter (and lost from the beam). This means that the overall probability of transmission through the first filter is 

$$ P(\text{transmit}) = f\cos^2\theta_1 $$

### A filter train

After a series of $n$ filters, the state of the beam will be

$$ P(\text{transmission}) = f^n \prod_{i=1}^n \cos^2\theta_i. $$

After the last filter, we want all of the light to be horizontally polarized. This means that the final polarization $\lvert\uparrow^n\rangle$ is the horizontal polarization state $\lvert\rightarrow\rangle,$ and we have

$$ \sum_i \theta_i = \frac{\pi}{2}. $$

### Best angles

Keeping $n$ fixed, we can think about the angular piece on its own. We want the product of the $\cos^2\theta_i$s to be as big as possible.

To get the intuition, think of two angles $\theta_1$ and $\theta_2$ that have to add up to some value $x.$ 

Because $\cos\theta$ always slopes downward on $\left[0,\frac{\pi}{2}\right],$ any decrease in $\cos\theta_1$ that we might avoid by keeping $\theta_1$ smaller than $\theta_2$ will be outweighed by the larger decrease from increasing $\theta_2.$ 

The upshot is that we want to keep $\theta_1$ as small as possible without making $\theta_2$ bigger than it needs to be. In other words, we should make them equal. All all $n$ angles, this argument extends, and it turns out we should divide the overall rotation of $\pi/2$ into $n$ equal rotations of $\pi/(2n).$

### Maximize transmission

After all that, we know that maximal transmission through $n$ filters is achieved by making all the rotations equal, and so

$$ P(\text{transmission}\rvert $n$\ \text{filters} = f^n \cos^{2n}\frac{\pi}{2n} $$.

Plotting this probability, we we see that it maxes out at $n=16$ where $P(\text{transmission}) = 0.99^{16} \left(\cos\frac{\pi}{32}\right)^{32} \approx 0.72959455363.$

![](/img/2022-02-06-rotating-light.jpg){:width="450 px" class="image-centered"}





<br>
