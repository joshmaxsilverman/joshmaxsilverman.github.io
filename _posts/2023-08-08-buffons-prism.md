---
layout: post
published: true
title: Buffon's prism
date: 2023/08/08
subtitle: If you throw a rod into a jelly lattice, how long should it be to maximize the chance to cross one wall?
tags: probability geometry
---

>**Question**: Consider 3-space (i.e. $\mathbb{R}^3$) partitioned into a grid of unit cubes with faces defined by the planes of all points with at least one integer coordinate. For a fixed positive real number $\ell$, a random line segment of length $\ell$ (chosen uniformly in location and orientation) is placed in this cubic lattice.
>
>What length $\ell$ maximizes the probability that the endpoints of the segment lie in orthogonally adjacent unit cubes (that is, the segment crosses exactly one integer-coordinate plane), and what is this maximal probability?

<!--more-->

([Jane Street](URL))

## Solution

the probability we are after is

$$\begin{align}
P(\text{one face only}) &= P(\text{top face only}) + P(\text{side face only}) \\ 
&\ + P(\text{back face only}).
\end{align}$$

but, by symmetry, these three sub-probabilities are the same, so 
 
$$ P(\text{one face only}) = 3 P(\text{top face only}).$$

### Prism geometry

the line segment is an awkard object to picture geometrically. we can clean things up by using a prism whose diagonal is the line segment. the prism crosses cell boundaries whenever the line segment does.
 
any given prism can be defined in terms of the line segment length $\ell,$ the angle $\theta$ from the $x$-axis and the angle $\phi$ from the $z$-axis.

in these variables, the prism's width, depth, and height are

$$
  \begin{align}
    w &= \ell\cos\phi\cos\theta \\
    d &= \ell\cos\phi\sin\theta \\
    h &= \ell\sin\theta
  \end{align}
$$

so, for example, if the corner of the cube closest to the origin is within $(1-h)$ of the plane $z=1,$ then the prism will cross it. so, the probability that a randomly placed prism crosses $(z=1)$ is $(1-h)$ and the probability that it does cross it is $h.$ 

with this observation in hand, we can quantify the limited volume of points the corner can occupy such that the prism crosses only one face.

### Forming the probability

the prism will cross the top face of the unit cube whenever the $z$-coordinate is within $h$ of it. with $\ell \leq 1,$ the probability of this occuring is $P_\text{top} = h.$ 

the situation is the same for the other sides, and we have $P_\text{side} = w$ and $P_\text{back} = d.$

<!-- likewise, the probability that this doesn't happen is $1 - P_\text{top}.$ -->

with this, we can find the probability that any given prism crosses only the top face

$$ 
P(\text{top face only})_{\theta,\phi,\ell} = P_\text{top}(\theta,\phi,\ell) (1-P_\text{side}(\theta,\phi,\ell))(1-P_\text{back}(\theta,\phi,\ell)).
$$

averaging over all possible directions $(\theta, \phi)$ we get

$$ \begin{align}
P(\text{one face only})(\ell) &= \langle P(\text{one face only}) \rangle_{\theta,\phi} \\
&= 3\int \text{d}\Omega, P(\text{top face only})_{\theta,\phi} \\
&= 3\int\limits_0^{\frac12\pi} \text{d}\theta\,\int\limits_0^{\frac12\pi}\text{d}\phi\,\sin\phi\, P(\text{top face only})_{\theta,\phi} \\
&= \frac{\ell\left(3\ell^2 -16\ell + 6\pi\right)}{4\pi}.
\end{align}$$

### Maximimzing $P(\text{one face only})$

solving for the maximum, we find 

$$\ell_* = \frac29 \left(8 - \sqrt{\frac12\left(128-27\pi\right)}\right) \approx 0.7452572091\ldots$$

plugging this into the expression for the probability of crossing a single side, we get 

$$
\begin{align}
 P(\text{one face only})^* &= \frac{\left(16-\sqrt{256-54\pi}\right)\left(27\pi + \sqrt{256-54\pi} - 64\right)}{243\pi} \\
 &\approx 0.5095346021\ldots
\end{align}
$$

plotting $P(\text{one face only})(\ell)$ against simulation, we see good agreement:

![](/img/2023-08-31-buffons-prism.png) {:width="450px" class="image-centered"}

the simulation is straightforward, we pick a random orientation for the line segment, we pick a random endpoint, and then we test if the cubes containing its endpoints are nearest neighbors in the lattice:

```mathematica
areAdjacent[end1_, end2_] := (
  (* check whether two end points are in orthogonally adjacent cubes *)
  
  {cube1, cube2} = Floor[{end1, end2}];
  gap = Norm[cube1 - cube2];
  adjacent = Boole[gap == 1];
  
  Return[adjacent];
  )

randomDir[] := (
  (* pick a random direction from the surface of the unit sphere *)

  randPt = Table[RandomReal[{-1, 1}], 3];
  length = Norm[randPt];

  Return@If[length <= 1
    , randPt / length
    , randomDir[]
    ];
  )

trial[length_] := (
  (* pick two random endpoints and test if they're adjacent *)

  randDir = length randomDir[];
  randPt1 = Table[RandomReal[], 3];
  randPt2 = randPt1 + randDir;
  adjacent = areAdjacent[randPt1, randPt2];

  Return[adjacent];
  )

measure[n_, l_] := Mean[Table[trial[l], n]];

dats = ParallelTable[{l, measure[1000000, l]}, {l, 0, 1, 0.05}];
```

<br>
