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

- for a given choice of $\mathbf{x},$ the probability that $\mathbf{y}$ falls on the line from $\mathbf{x}$ to $\mathbf{p}$ is proportional to the length of that line $\ell(\theta).$ Next, the area of the polar strip at angle $\theta$ from which we can pick $\mathbf{x}$ is $\frac12 \ell^2(\theta)\,\text{d}\theta.$
- we can index the lines by their angle. The probability that two random points fall on a line through $\mathbf{p}$ at a given angle $\theta$ is proportional to the number of pairs of points that can define such a line which is the handshake between all points on the line, yielding a factor of $\frac12 \ell^2(\theta).$ Next, the probability that a random line through $\mathbf{p}$ would have angle $\theta$ is proportional to the number of ways to choose a point at an angle $\theta$ to $\mathbf{p},$ which is proportional to $\ell(\theta).$ 

The interpretive confusion comes from $\ell$ doing double duty in the probability and the measure of the physical space the points are chosen from.

![](/img/2025-06-08-fiddler-square-points-clean.png){:width="200-px" class="image-centered"}

Returning to the calculation, we need to find a concrete expression for $\ell(\theta).$ From the picture, it has a constant vertical component of $1$ while its horizontal component is $\ell(\theta)\sin\theta.$ This means its length is given by 

$$\ell^2(\theta) = 1 + \sin^2\theta \ell^2(\theta), $$

which leads to $\ell(\theta) = 1 / \cos\theta.$ So, the probability density for a corner of the square is just

$$ P_\text{corner} = 2\int\limits_0^{\pi/4}\text{d}\theta\, \frac{1}{\cos^3\theta}  = 2\left(\frac{1}{\sqrt{2}} + \tanh^{-1}\left(\tan\frac{\pi}{8}\right)\right) \approx 2.2956. $$

The case for the center is nearly the same, except that the green angle ranges from $-\pi/4$ to $pi/4$, doubling the result so that $P_\text{center} = 2P_\text{corner}.$

The middle edge is slightly more complicated, breaking into two unique integrals. 

The first, given by the salmon colored line in the diagram, has constant vertical component $\frac12$ and horizontal component $\ell_\theta \sin(\theta).$ This means that $\ell_\theta^2 = 1/2^2 + \sin^2\theta \ell_\theta^2$ which leads to $\ell_\theta = \frac1{2\cos\theta}.$ The salmon angle starts at zero and ranges up until $\tan\theta = 1/(1/2)$ or $\theta = \arctan 2.$

The second, given by the red line in the diagram, has constant horizontal component $1$ and vertical component $\ell_\theta \sin\theta$ which, like the corner and center cases, leads to $\ell_\theta = 1/\cos\theta.$ The red angle starts at zero and ranges up to $\tan\theta = 1/2$ or $\theta = \arctan \frac12.$

So, 

$$ P_\text{middle-edge} = 2\int\limits_0^{\arctan 2} \text{d}\theta \frac{1}{\left(2\cos\theta\right)^3} + 2\int\limits_0^{\arctan \frac12} \text{d}\theta \frac{1}{\left(\cos\theta\right)^3} = xxx. $$

We can estimate these quantities by generating random lines, discretizing the square, and testing if the line passes within a unit cell of $\mathbf{p}$

```python
import random
import math
import pandas as pd

eps=1e-3

def estimate_density(p, N=400_000_000):
    # MC estimate using small-band approximation.
    # pdf ~= P( distance(line(x, y), p) < eps ) / eps

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
    "center"      : (0.5, 0.5),
    "middle‑edge"   : (0.5, 0.001), # just off the boundary for robustness
    "near‑corner": (0.001, 0.001), # just off the boundary for robustness
}

results = []
for label, p in test_points.items():
    f_est = estimate_density(p)
    results.append({"Point": label, "Estimated pdf(p)": round(f_est, 3)})

df = pd.DataFrame(results)
```

which leads to 

$$
\begin{array}{c|c}
\text{Point} & \text{Estimated $pdf(\mathbf{p})$} \\ \hline
\text{center (0.5,0.5)}	& 3.062 \\
\text{mid‑edge (0.5,0.01)} & 1.273 \\
\text{near‑corner (0.001,0.001)} & 1.531
\end{array}
$$

<br>
