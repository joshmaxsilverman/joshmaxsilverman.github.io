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

If the first filter makes an angle $\Delta\theta_1$ with the vertical, then

$$
\begin{align}
\lvert\gamma^\prime\rangle &= \left(\begin{array}\\cos\Delta\theta_1 & \sin\Delta\theta_1 \\ -\sin\Delta\theta_1 & \cos\Delta\theta_1\end{array}\right)\lvert\gamma\rangle,
\end{align}
$$

or, resolving to components, 

$$ \lvert\gamma\rangle = \lvert\uparrow\rangle \longrightarrow \sin\Delta\theta_1\lvert\rightarrow^\prime\rangle + \cos\Delta\theta_1\lvert\uparrow^\prime\rangle. $$

The physical probability of a photon in the beam being in either polarization state is the **magnitude** of the component in that direction. 

So, the probability of a photon passing the first filter is just $ \lvert\langle\uparrow^\prime\rvert\gamma^\prime\rangle\rvert^2 = \cos^2\Delta\theta_1.$

After a series of $n$ filters, the state of the beam will be

$$ \lvert\gamma\rangle_\text{final} = \product_{i=1}^n \cos\Delta\theta_i \lvert\uparrow^n\rangle. $$

After the last filter, we want all of the light to be horizontally polarized, so $\lvert\uparrow^n\rangle$ is just the horizontal polarization state $\lvert\rightarrow\rangle.$

<br>
