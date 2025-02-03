---
layout: post
published: true
title: Can You Spin the Graph?
date: 2025/02/02
subtitle: If you tumble your function is it still a function?
tags: spherical-geometry vectors
---

>**Question**: In a more advanced course, you’ve been asked to draw a 3D sketch of the function ${z = \vert x\rvert + \lvert y\rvert}.$ As you’re about to do this, you are struck by another bout of dizziness, and your resulting graph is randomly rotated in $3\text{D}$ space.
>
>More specifically, your graph has the correct origin. But the true $z$-axis is equally likely to point from the origin to any point on the surface of the unit sphere. (Meanwhile, the $x$-axis is equally likely to point in any direction perpendicular to the $z$-axis. From there, the $y$-axis is uniquely determined.)
>
>What is the probability that the resulting graph you produce is in fact a function (i.e., $z$ is a function of $x$ and $y$)?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-spin-the-graph))

## Solution

if a function is a function, then it can't flip over. this means that the direction the surface faces needs to always point up or down. 

for example, this curve, which is not a function sees the arrow switch from pointing overall up, to overall down. more concretely, the $z$ component of the surface normal switches from positive to negative.

instead of tumbling the surface to find a random new orientation, we can equivalently pick a random new direction for the vertical. this is more convenient since it means we can keep constant coordinates for the $4$ faces of the surface $f(x,y) = \lvert x\rvert + \lvert y\rvert.$

the $4$ faces have the surface normals

$$
  \begin{align}
    \mathbf{n}_1 &= (+1, +1, +1) \\
    \mathbf{n}_2 &= (-1, +1, +1) \\
    \mathbf{n}_3 &= (+1, -1, +1) \\
    \mathbf{n}_4 &= (-1, -1, +1)
  \end{align}
$$

if we pick a random direction $\mathbf{v} = (v_x, v_y, v_z)$ for the new vertical, then the vertical component of a vector $\mathbf{n}$ is just $\mathbf{n}\cdot\mathbf{v}.$ taking the dot product of $\mathbf{v}$ with the normal of each face, we get four equations:

$$
  \begin{align}
    v_z &> v_x + v_y \\
    v_z &> -v_x + v_y \\
    v_z &> v_x - v_y \\
    v_z &> -v_x - v_y \\
  \end{align}
$$

since all of these equations have to hold, they reduce to 

$$ v_z > \lvert v_x\rvert + \lvert v_y\rvert. $$

if we draw $\mathbf{v}$ at random from the surface of the unit sphere, what is the chance this holds? we have to find the subset of $(\theta,\phi)$ that satisfy the equation.

writing $\mathbf{v}$ in spherical coordinates, we can see

$$ \mathbf{v} = (\cos\theta\cos\phi, \cos\theta\sin\phi, \sin\theta). $$

in this representation, the inequality is 

$$ \frac{\sin\theta}{\lvert \cos\theta\rvert} > \lvert\cos\phi\rvert + \lvert\sin\phi\rvert. $$

this identifies the set of $(\theta,\phi)$, and it consists of two four-leaf clover-esque patches:

[image of the clover]

exploiting the symmetry, we can use just one octant of the sphere and drop the absolute value signs. taking $\theta$ and $\phi$ to be between $0$ and $\frac12\pi$ the condition simplifies to

$$ \theta > \arctan\left(\cos\phi + \sin\phi\right). $$

to find the area of the clover patches relative to the sphere, we can add the points in this set. 

$$ 
  \begin{align}
    P(\text{tumble is a function}) &= \dfrac{\int\limits_0^{\frac12\pi}\text{d}\phi\, \int\limits_{\arctan\left(\cos\phi + \sin\phi\right)}^{\frac12\pi} d\Omega}{\int\limits_0^{\frac12\pi}\text{d}\phi\, \int\limits_0^{\frac12\pi} d\Omega} \\
    &= \dfrac2\pi\left(\frac\pi2 - 2\arcsin\frac1{\sqrt{3}}\right) \\
    &\approx 0.2163
  \end{align}
$$

<br>
