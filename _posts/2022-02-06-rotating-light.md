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

The polarization state of a photon is a vector we can look at from any perspective we like. For example, we can think of an arbitrary photon in the basis of horizontal and vertical polarization, e.g. 

$$ \lvert\gamma\rangle = \alpha\lvert\rightarrow\rangle + \beta\lvert\uparrow\rangle. $$ 

When the photon passes through a polarized filter, the component that's perpendicular to the polarizer is extinguished.  

So, at each filter, we need to rotate the photon into the basis of the filter and then extinguish the "horizontal" component in that basis. E.g. the state of the photon becomes

$$
\begin{align}
\lvert\gamma^\prime\rangle &= \left(\begin{array}\\cos\Delta\theta_i & \sin\Delta\theta_i \\ -\sin\Delta\theta_i & \cos\Delta\theta_i\end{array}\right) \cdot \left(\begin{array}\ 0 & 0 \\ 0 & 1\end{array}\right)\lvert\gamma\rangle \\
&= \left(\begin{array} 0 & 0 \\ 0 & \cos\Delta\theta_i\end{array}\right)\lvert\gamma\rangle
\end{align}
$$

In other words, 

$$ \lvert\gamma\rangle = \alpha\lvert\rightarrow\rangle + \beta\lvert\uparrow\rangle \longrightarrow \betacos\Delta\theta_i \lvert\gamma\rangle. $$


<br>
