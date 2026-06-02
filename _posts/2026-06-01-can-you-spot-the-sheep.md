---
layout: post
published: true
title: Can you spot the sheep?
date: 2026/06/01
subtitle: What's the chance three random sheep can all see each other with their sheep eyes?
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

any three locations we pick will make a triangle of sheep. they'll be able to see each other so long as the visual field of each sheep encompasses the positions of the other two. the probablility that the sheep all see each other is proportional to the product of the allowable range of orientation angles for each sheep. 

for example, sheep A's boundary of vision can range from being parallel to the $AB$ line to being parallel with the $AC$ line. this is equal to $\pi - \theta$ with $\theta$ equal to

$$ \pi - \arccos\frac{\left(\mathbf{r}_B - \mathbf{r}_A\right)\cdot\left(\mathbf{r}_C - \mathbf{r}_A\right)}{\lvert \mathbf{r}_B - \mathbf{r}_A\rvert\lvert \mathbf{r}_C - \mathbf{r}_A\rvert}. $$

the probability that all three sheep have a correct orientation is therefore proportional to

$$ \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\pi-\gamma\right). $$

we have to average this over all possible positions for the three sheep. for small triangles, the geometry doesn't put much constaint on the permissible angles, but for large triangles, it's easier to be roughly equilateral than obtuse.

$$ P = \dfrac{1}{\left(2\pi\right)^3}\int_0^1\text{d}x_1 \int_0^1\text{d}y_1\int_0^1\text{d}x_2\int_0^1\text{d}y_2 \int_0^1\text{d}x_3 \int_0^1\text{d}y_3 \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\pi - \gamma\right). $$

if we evaluate this by numerical means we get $2.719\%$ which matches simulation.

```
mathematica

r1={x1,y1};
r2={x2,y2};
r3={x3,y3};

θ=ArcCos[(r3-r1).(r2-r1)/(Norm[r3-r1]Norm[r2-r1])];
γ=ArcCos[(r3-r2).(r1-r2)/(Norm[r3-r2]Norm[r1-r2])];
β=ArcCos[(r2-r3).(r1-r3)/(Norm[r2-r3]Norm[r1-r3])];

NIntegrate[
  (π - θ) (π - β) (π - γ)
 , {x1, 0, 1}, {y1, 0, 1}
 , {x2, 0, 1}, {y2, 0, 1}
 , {x3, 0, 1}, {y3, 0, 1}
 , Method -> "QuasiMonteCarlo"
 , MaxPoints -> 30000000
 , AccuracyGoal -> 20
 , PrecisionGoal -> 20
]
```

we can also go for an analytic approximation, making the radical assumption that all possible angle triples are uniformly distributed. since $\theta+\beta+\gamma=\pi,$ we have

$$ P \approx \dfrac{\displaystyle\int_0^1\text{d}\theta \int_0^{\pi-\theta}\text{d}\beta\, \left(\pi-\theta\right)\left(\pi-\beta\right)\left(\theta+\beta\right)}{\displaystyle\int_0^1\text{d}\theta \int_0^{\pi-\theta}\text{d}\beta}. $$

this comes out to $7/240 \approx 0.02916667$ which is only about $6\%$ too optimistic, likely due to the overweighting of obtuse arrrangements.

<br>
