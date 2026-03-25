---
layout: post
published: true
title: Can you trace the locus?
date: 2026/03/23
subtitle: What are is mapped out by a string on some pegs?
tags: geometry 
source: fiddler
kind: puzzle
theme: geometry
---

> **Question**: I have a loop of string whose total length is $10.$ I place it around a unit disk (i.e., with radius 1) and pull a point on the string away from the disk until the string is taut, as shown below.
>
> I drag this point around the disk in all directions, always keeping the string taut, tracing out a loop. What is the area inside this resulting loop?
>
> **Extra credit**: Now I have a loop of string whose total length is $14,$ and I place it around two adjacent unit disks. As before, I pull a point on the string away from the disks until the string is taut, as shown below.
>
> I drag this point around the disks in all directions, always keeping the string taut, tracing out a loop. What is the area inside this resulting loop?




<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-trace-the-locus))

## Solution

With just one disk, the string meets the circle at two points of tangency and the total length of the string is $10.$ 

We can use these facts to find the radius of the point as it orbits the circle.

![](/img/2026-03-23-fiddler-locus-one-disk.png){:width="600 px" class="image-centered"}

Adding up the lengths around the string, we get

$$ 2\pi - 2\beta + 2\ell = 10, $$

and using the two right triangles with the tangents, it becomes

$$ 2\pi - 2\beta + 2\tan\beta = 10. $$

Solving this for $\beta$ we get $\beta\approx 1.2605292$ or $\ell = \tan\beta \approx 3.1189365.$ 

The radius is just $r = \ell/\sin\beta \approx 3.2753266.$ 

Plugging this in, the area swept out by the point is $A = \tfrac12\pi r^2 \approx 33.702266.$ 

## Extra credit

The extra credit is the same idea in principle, but operationally has bunch more geometric accounting to do.

As the point rotates around the disks, there are two qualitative regimes. 

In one of them, the string is tangent to both disks at once and in the other it has two points of tangency to one of them. 

We can reuse the work of the standard problem to find the radius of the point in the first regime, but we have to do a bit more work to find the radius in the second.

### Two tangents to two disks

Happily, if we draw the scenario, we have everything we need to divine the sought and sacred constraints.

![](/img/2026-03-23-fiddler-locus-two-tangents.png){:width="600 px" class="image-centered"}

First, we can use the law of cosines to relate the radius $r_\theta$ to lengths $\ell_1$ and $\ell_2.$ 

$$ 
    \begin{align}
        \ell_1^2 + 1 &= 1 + r_\theta^2 - 2r_\theta\cos(\pi-\theta) \\ 
        &= 1 + r_\theta^2 + 2r_\theta\cos\theta,
    \end{align}
$$
 
and, likewise

$$
    l_2^2 + 1 = 1 + r_\theta^2 - 2r_\theta\cos\theta.
$$

We can relate the angles $\beta_1$ and $\beta_2$ to $\theta$ and $r_\theta$ using right triangle trigonometry (involving the undrawn vertical of length $1$ from out point to the line connecting the circle centers), giving

$$ \cos\beta_1 = \frac{1+r_\theta\cos\theta}{\sqrt{1+\ell_1^2}} $$

and

$$ \cos\beta_2 = \frac{r_\theta\cos\theta - 1}{\sqrt{1+\ell_2^2}}. $$

Next, we need the angles $\gamma_1$ and $\gamma_2$ to find the length of the string's curved segments.

$\gamma_1$ is supplementary to $\beta_1$ plus its adjacent angle $z_1$

$$ 
    \begin{align}
        \gamma_1 &= \pi - \beta_1 - z_1 \\
        &= \pi - \beta_1 - \arcsin\frac{\ell_1}{\sqrt{\ell_1^2+1}}.
    \end{align} 
$$

Similarly, $\gamma_2$ is the complement of $z_2$ 

$$ \frac12\pi = \gamma_2 + z_2 $$

and

$$ \beta_2 + z_2 = \arcsin\frac{\ell_2}{\sqrt{\ell_2^2+1}}, $$

which leads to 

$$
    \begin{align} 
        \gamma_2 &= \frac12\pi - \arcsin\frac{\ell_2}{\sqrt{\ell_2^2+1}} + \beta_2. 
    \end{align}
$$

Finally, we have the total length of the string broken down into the straight segments, curved segments, and tangent segments

$$ 14 = \frac12 \pi + 2 + \ell_1 + \ell_2 + \gamma_1 + \gamma_2. $$

We can turn the length constraint into am equation in $r_\theta$ and $\theta$ and numerically solve for $r_\theta$ at each $\theta.$

### Two tangents to one disk

Since we already have most of the work done for this part from the standard problem, we just need to find the minimum value of $\theta$ where the disk maintains tangents on both disks.

![](/img/2026-03-23-fiddler-one-tangent.png){:width="600 px" class="image-centered"}

This occurs when the top $\ell$ is flat, which implies $\tan\theta = 1/(1+\ell)$ or $\theta_\text{min}=\arctan 1/(1+\ell) \approx 0.238173.$

Below this value of theta, the string has two tangents to a single disk. The radius with respect to that disk is the same as in the first problem but, now, the radius is about the center of the two disks. We can use the law of cosines to relate the radius $r_\eta = \ell/\sin\beta$ (the radius from the standard problem) to $r_\theta.$ We get

$$ r_\eta^2 = 1 + r_\theta^2-2r_\theta\cos\theta $$

which simplifies to

$$ r_\theta = \cos\theta + \sqrt{r_\eta^2 - \sin^2\theta}. $$

With $r_\theta$ in hand for the two regimes, we can numerically integrate $r_\theta^2\text{d}\theta$ to find the area.

$$ \frac14 \text{area} = \overbrace{\frac12 \int_0^{\theta_\text{min}} \text{d}\theta\,\left[\cos\theta + \sqrt{r_\eta^2 - \sin^2\theta}\right]}^{\text{two tangents to one disk}}  + \overbrace{\frac12 \int_{\theta_\text{min}}^{\pi/2}\text{d}\theta\, r_\theta^2}^{\text{two tangents to two disks}} $$

which gets $\text{area} \approx 52.36472541.$

Plotting the resulting locus, we see a beautiful ellipsoid like creation

![](/img/2026-03-24-fiddler-locus-circles.png){:width="600 px" class="image-centered"}

```mathematica
sol = First @ NSolve[
   {
    2 (π - θ) + 2 s == 10
    , s == Tan[θ]
    , 0 <= θ <= 2 π
    }
   , {s, θ}
   , WorkingPrecision -> 20
   ]

ll = s /. sol
rr = s / Sin[θ] /. sol

l1[r_, θ_] := Sqrt[r^2 + 2 r Cos[θ]];
l2[r_, θ_] := Sqrt[r^2 - 2 r Cos[θ]];

β1[r_, θ_] := ArcCos[(1 + r Cos[θ])/Sqrt[1 + l1[r, θ]^2]];
β2[r_, θ_] := ArcCos[(-1 + r Cos[θ])/Sqrt[1 + l2[r, θ]^2]];

γ1[r_, θ_] := 
  Pi - ArcSin[l1[r, θ]/Sqrt[1 + l1[r, θ]^2]] - β1[r, θ];
γ2[r_, θ_] := 
  Pi/2 + β2[r, θ] - ArcSin[l2[r, θ]/Sqrt[1 + l2[r, θ]^2]];

eqn[r_, θ_] := 
  14 == Pi/2 + 2 + γ1[r, θ] + γ2[r, θ] + l1[r, θ] + 
    l2[r, θ];

rVal[θ_] := r /. FindRoot[eqn[r, θ], {r, 4}, WorkingPrecision -> 20]

θMin = ArcTan[1/(1 + ll)];

doubleTangentArea = 
  1/2 * NIntegrate[rVal[θ]^2, {θ, thetaMin, π/2}, 
    WorkingPrecision -> 10]

singleTangentArea = 
  NIntegrate[
   1/2 * (Cos[θ] + Sqrt[rr^2 - Sin[θ]^2])^2, {θ, 0,
     thetaMin}, WorkingPrecision -> 10];

totalArea = 4 * (doubleTangentArea + singleTangentArea)
```
