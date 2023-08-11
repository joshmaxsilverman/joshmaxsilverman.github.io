---
layout: post
published: false
title: 
date: 2023/08/08
subtitle: Buffon's lattice
tags: probability geometry
---

>**Question**: Consider 3-space (i.e. $\mathbb{R}^3$) partitioned into a grid of unit cubes with faces defined by the planes of all points with at least one integer coordinate. For a fixed positive real number $\ell$, a random line segment of length $\ell$ (chosen uniformly in location and orientation) is placed in this cubic lattice.
>
>What length $\ell$ maximizes the probability that the endpoints of the segment lie in orthogonally adjacent unit cubes (that is, the segment crosses exactly one integer-coordinate plane), and what is this maximal probability?

<!--more-->

([Jane Street](URL))

## Solution

the rod is an awkard object to picture geometrically. we can clean things up by using the prism whose diagonal is the rod. the prism crosses cell boundaries whenever the rod does.

the probability we are after is

$$\begin{align}
P(\text{crosses only one face}) &= P(\text{crosses only top face}) \\
 &+ P(\text{crosses only side face}) + P(\text{crosses only back face}).
\end{align}$$

however, the three sub-probabilities are the same by symmetry, so 
 
$$ P(\text{crosses only one face}) = 3 P(\text{crosses only top face}).$$
 
any given prism can be defined in terms of the rod length $\ell,$ the angle from the $x$-axis $\theta$ and the angle from the $z$-axis $\phi.$

in these variables, the prisms width, depth, and height are

$$
  \begin{align}
    w &= \ell\cos\phi\cos\theta \\
    d &= \ell\cos\phi\sin\theta \\
    h &= \ell\sin\theta
  \end{align}
$$

with those in hand, the prism has a limited volume of points that it can occupy without crossing two faces of the unit cube.

the prism will cross the top face of the unit cube whenever the $z$-coordinate is within $h$ of it. the probability of this occuring is equal to $P_\text{top} = h = \sin\theta.$ likewise, the probability that this doesn't happen is $1 - P_\text{top}.$

the situation is the same for the other sides, and we have $P_\text{side} = w$ and $P_\text{back} = d.$

with this, we can find the probability that any given prism crosses only the top face

$$ P(\text{crosses only top face})_{\theta,\phi} = P_\text{top}(\theta,\phi)(1-P_\text{side}(\theta,\phi))(1-P_\text{back}(\theta,\phi)). $$

taking the expectation over all directions $(\theta, \phi)$ we get

$$ P(\text{crosses only one face}) = 3\oint \text{d}\theta\text{d}\phi\sin\phi \left[P_\text{top}(\theta,\phi)(1-P_\text{side}(\theta,\phi))(1-P_\text{back}(\theta,\phi))\right].$$

the integral gets us ...

solving for the maximum, we find $\ell_* = ....$

plugging this into the expression for the probability of crossing a single side, we get $p_* = ...$

or approximately ... and ...

<br>
