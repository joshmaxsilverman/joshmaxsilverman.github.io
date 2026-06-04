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

For example, sheep A's boundary of vision can range from being parallel to the $\mathbf{r}_A - \mathbf{r}_B$ line to being parallel with the $\mathbf{r}_A - \mathbf{r}_C$ line. This is equal to $\left(\pi - \theta\right)$

The probability that all three sheep have a correct orientation is therefore proportional to

$$ \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\pi-\gamma\right). $$

We have to average this over all possible positions for the three sheep. For small triangles, the geometry doesn't put much constaint on the permissible angles, but for large triangles, it's easier to be roughly equilateral than obtuse.

Using the dot product, the angle $\theta$ is given by

$$ \theta = \arccos\frac{\left(\mathbf{r}_B - \mathbf{r}_A\right)\cdot\left(\mathbf{r}_C - \mathbf{r}_A\right)}{\lvert \mathbf{r}_B - \mathbf{r}_A\rvert\lvert \mathbf{r}_C - \mathbf{r}_A\rvert}. $$

With similar formulas for $\beta$ and $\gamma.$ since $\theta+\beta+\gamma=\pi,$ we have

$$ P = \dfrac{1}{\left(2\pi\right)^3}\int_0^1\text{d}x_A \int_0^1\text{d}y_A\int_0^1\text{d}x_B\int_0^1\text{d}y_B \int_0^1\text{d}x_C \int_0^1\text{d}y_C \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\theta+\beta\right). $$

If we evaluate this by numerical means we get $2.719\%$ which matches simulation.

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
 , Method -> {"QuasiMonteCarlo", "Points" -> 100000000}
]
```

We can also go for an analytic approximation, making the radical assumption that all possible angle triples are uniformly distributed.

$$ P \approx \dfrac{\displaystyle\int_0^1\text{d}\theta \int_0^{\pi-\theta}\text{d}\beta\, \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\theta+\beta\right)}{\displaystyle\int_0^1\text{d}\theta \int_0^{\pi-\theta}\text{d}\beta}. $$

This comes out to $7/240 \approx 2.917\%$ which is only about $7\%$ too optimistic, likely due to the overweighting of obtuse arrrangements.

<br>
