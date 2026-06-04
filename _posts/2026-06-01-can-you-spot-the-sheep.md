---
layout: post
published: true
title: Can you spot the sheep?
date: 2026/06/01
subtitle: What's the chance three randomly placed and oriented sheep can all see each other with their sheep eyes?
tags: probability geometry
source: fiddler
kind: puzzle
theme: probability
hide_from_recent : true
---

> **Question**: Two sheep are at two random points inside a square pen. They are munching grass and staring in two random directions. Each sheep has a field of view that’s 180 degrees.
>
> What is the probability that they both see each other?
>
> **Extra Credit**: Now, three sheep are at three random points inside a square pen. They are munching grass and staring in three random directions. As before, each sheep has a field of view that’s 180 degrees.
>
> What is the probability that all three sheep see each other?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-spot-the-sheep))

## Solution

Any three locations we pick will make a triangle of sheep. They'll be able to see each other so long as the visual field of each sheep encompasses the positions of the other two, so the probablility that the sheep all see each other is proportional to the product of the allowable range of orientation angles for each sheep.

![](/img/2026-06-03-fiddler-sheep-triangle.png){:width="500 px" class="image-centered"}

For example, sheep A's boundary of vision can range from being parallel to the $\left(\mathbf{r}_B - \mathbf{r}_A\right)$ line to being parallel with the $\left(\mathbf{r}_C - \mathbf{r}_A\right)$ line. This is equal to $\left(\pi - \theta\right)$

The probability that all three sheep have a correct orientation is therefore proportional to

$$ \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\pi-\gamma\right). $$

We have to average this over all possible positions for the three sheep. For small triangles, the geometry doesn't put much constaint on the permissible angles, but for large triangles, it's easier to be roughly equilateral than obtuse.

We can find this average at three levels of fidelity. 

### Order of magnitude

The first is to simply assume that each angle takes on the characteristic value of $\pi/3,$ an equilateral triangle. In this arrangement, the probability that any given sheep is validly oriented is $\left(2\pi/3\right)/2\pi = 2/3$ so that the probability all three are valid is $1/3^3 \approx 3.7\%.$ This is an overestimate because most triangles are not equilateral, and any departure from an equal split is less likely than this arrangement.

### Uniform distribution

The second thing we can do is average over all angular arrangements, making the radical assumption that all possible angle triples are uniformly distributed. This can be done analytically and, using the fact that $\theta+\beta+\gamma=\pi,$ we get

$$ P \approx \dfrac{\displaystyle\int_0^1\text{d}\theta \int_0^{\pi-\theta}\text{d}\beta\, \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\theta+\beta\right)}{\displaystyle\int_0^1\text{d}\theta \int_0^{\pi-\theta}\text{d}\beta}. $$

This comes out to $7/240 \approx 2.917\%$ which is only about $7\%$ too optimistic, again due to the overweighting of obtuse arrrangements.

### Exact treatment

The third way is to do the averaging exactly. Using the dot product, we can express the angle $\theta$ in terms of the sheep coordinates like

$$ \theta = \arccos\frac{\left(\mathbf{r}_B - \mathbf{r}_A\right)\cdot\left(\mathbf{r}_C - \mathbf{r}_A\right)}{\lvert \mathbf{r}_B - \mathbf{r}_A\rvert\lvert \mathbf{r}_C - \mathbf{r}_A\rvert}, $$

with similar formulas for $\beta$ and $\gamma.$ 

Averaging over all possible positions, and dividing by the total volume of $\left(\theta,\beta,\gamma\right)$-space, we get

$$ P = \dfrac{1}{\left(2\pi\right)^3}\int_0^1\text{d}x_A \int_0^1\text{d}y_A\int_0^1\text{d}x_B\int_0^1\text{d}y_B \int_0^1\text{d}x_C \int_0^1\text{d}y_C \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\theta+\beta\right). $$

If we evaluate this by numerical means we get $2.723\%$ which matches simulation.

```mathematica

rA = {xA, yA};
rB = {xB, yB};
rC = {xC, yC};

θ = ArcCos[(rC-rA).(rB-rA) / (Norm[rC-rA] Norm[rB-rA])];
γ = ArcCos[(rC-rB).(rA-rB) / (Norm[rC-rB] Norm[rA-rB])];
β = ArcCos[(rB-rC).(rA-rC) / (Norm[rB-rC] Norm[rA-rC])];

NIntegrate[
  (π - θ) (π - β) (π - γ)
 , {xA, 0, 1}, {yA, 0, 1}
 , {xB, 0, 1}, {yB, 0, 1}
 , {xC, 0, 1}, {yC, 0, 1}
 , Method -> "QuasiMonteCarlo"
 , PrecisionGoal -> 20
]
```

Looking at the distribution in $\theta,\beta$ space, and conditioning on the area of triangle, we see that smaller triangles have a more uniform distribution while large triangles overwhelmingly cluster around equilateral arrangements.

![](/img/2026-06-04-fiddler-sheep-heatmaps.png){:width="650 px" class="image-centered"}

<br>
