---
layout: post
published: true
title: Can you weave the web?
date: 2025/06/08
subtitle: What is the probability that two random points form a line that goes through a particular point $\mathbf{p}$?
tags: indicators geometry pdfs
---

>**Question**: A spider weaves a web within a unit square (i.e., a square with side length $1$) in the following haphazard manner:
>
> First, the spider picks two points at random inside the square. In particular, it picks the points “uniformly,” meaning any point is equally likely to be picked as any other point.
> Next, the spider connects the two points with a strand of silk and extends the strand to two sides of the square.
>
>Within the unit square, which point (or points) is most likely to be on a new strand of silk, whose two defining points have not yet been picked?
>
>**Extra Credit**: as we just acknowledged, there exists a point (or points) in the unit square that is more likely than any others to be on the randomly selected silk strand.
>
>At the same time, there exists a point (or points) in the unit square that is less likely than any others to be on the random strand.
>
>How much more likely is a most likely point to be on the strand than a least likely point? More specifically, suppose the maximum of the probability density for being on the strand is $p_\text{max}$ and the minimum probability density is $p_\text{max}.$ What is the ratio $p_\text{max}/p_\text{max}$?



<!--more-->

([Fiddler on the Proof](URL))

## Solution

The probability that two random points $x$ and $y$ form a line through a given point $p$ is

$$ \int \text{d}\mathbf{x} \int \text{d}\mathbf{y} \mathbb{I}(\text{$\mathbf{x}$ and $\mathbf{y}$ form a line through $\mathbf{p}$}) $$

As literal as it seems, we can work this out to get the probability density for any $\mathbf{p}.$ Concretely, let's work out the case where $\mathbf{p}$ is the lower left corner.

Let's start by carrying out the integral over $\mathbf{y}:$

$$ \int \text{d}\mathbf{y} \mathbb{I}(\text{$\mathbf{x}$ and $\mathbf{y}$ form a line through $\mathbf{p}$}). $$

The indicator function is $1$ for all points $\mathbf{y}$ that fall on a line through the lower left corner and $\mathbf{x}.$ Drawing this out for an arbitrary $\mathbf{x}$, the support is the line labeled $\ell(\theta).$ 

Now we just have to integrate over $\mathbf{x}.$ To do this, let's represent $\mathbf{x}$ in polar coordinates $\mathbf{x} = (r, \theta).$ With this change, the integral becomes

$$ \int \text{d}\mathbf{x} \ell(\theta) = \int \text{d}\theta \int \text{d}r \, r\, \ell(\theta). $$

The range for $\theta$ is just zero to $\pi/4$ while $r$ ranges from zero to $\ell(\theta),$ so the integral further simplifies to

$$ \int\text{d}\theta\, \frac12 \ell^3(\theta), $$

This has two intuitive interpretations: 

- for a given choice of $\mathbf{x},$ the probability that $\mathbf{y}$ falls on the line from $\mathbf{x}$ to $\mathbf{p}$ is proportional to the length of that line $\ell(\theta).$ Meanwhile, area of the polar sector at angle $\theta$ from which we could pick $\mathbf{x}$ is just $\frac12 \ell^2(\theta)\,\text{d}\theta.$
- the probability that two random points fall on a line through $\mathbf{p}$ at a given angle $\theta$ is proportional to the number of pairs of points that form such a line which is the handshake between all points on the line $\ell(\theta),$ yielding a factor of $\frac12 \ell^2(\theta).$ Now, the probability that the angle $\theta$ would be chosen at random is proportional to the number of ways to choose a point at an angle $\theta$ to $\mathbf{p},$ which is proportional to $\ell(\theta).$ 

The interpretive confusion comes from $\ell$ doing double duty in the probability and the measure of the physical space the points are chosen from.

Returning to the calculation, we need to find a concrete expression for $\ell(\theta).$ From the picture, it has a constant vertical component of $1$ while its horizontal component is $\ell(\theta)\sin\theta.$ This means its length is given by 

$$\ell^2(\theta) = 1 + \sin^2\theta \ell^2(\theta), $$

which leads to $\ell(\theta) = 1 / \cos\theta.$ So, the probability density for a corner of the square is just

$$ 2\int\limits_0^{\pi/4}\text{d}\theta\, \frac{1}{\cos^3\theta}  = 2\left(\frac{1}{\sqrt{2}} + \tanh^{-1}\tan\frac{\pi}{8}\right) \approx 2.2956. $$

```python
import random, math, pandas as pd
# from ace_tools import display_dataframe_to_user

def estimate_density(p, N=400_000_000, eps=1e-3):
    # MC estimate using small-band approximation.
    # f ~= P( distance(line(x, y), p) < eps ) / eps

    px, py = p
    count = 0
    for _ in range(N):
        x1, y1 = random.random(), random.random()
        x2, y2 = random.random(), random.random()
        dx, dy = x2 - x1, y2 - y1
        len_sq = dx*dx + dy*dy
        dist = abs(dx * (y1 - py) - dy * (x1 - px)) / math.sqrt(len_sq)
        if dist < eps:
            count += 1
    return count / (N * eps)

test_points = {
    "center (0.5,0.5)"      : (0.5, 0.5),
    "mid‑edge (0.5,0.001)"   : (0.5, 0.001),  # just off the boundary for robustness
    "near‑corner (0.001,0.001)": (0.001, 0.001), # just off the boundary for robustness
}

results = []
for label, pt in test_points.items():
    f_est = estimate_density(pt)
    results.append({"Point": label, "Estimated f(x,y)": round(f_est, 3)})

df = pd.DataFrame(results)
```

<br>
