---
layout: post
published: true
title: Can you fling the fractal darts?
date: 2025/12/08
subtitle: How many points will you asymptotically approach?
tags: recursion fractals linearity-of-expectation
---

>**Question**: You are playing darts with your friend, Apollonius, who has brought his own dartboard. However, this dartboard is somewhat … different. Instead of being a circle divided into concentric rings and sectors, the dartboard is a unit circle (i.e., with radius $1$) that’s divided via an Apollonian gasket. In particular, this gasket is defined by two horizontally adjacent, congruent circles with radius $1/2.$ (Note: An Apollonian gasket also includes circles above, below, and around these two circles of radius $1/2.$ Put simply, you keep drawing circles that are tangent to three other circles wherever you can.)
>
>But that’s not all! Every circle on the dartboard, no matter how small, is also its own Apollonian sub-gasket. Like the larger circle, every gasket, sub-gasket, sub-sub-gasket, etc., are defined by two horizontally adjacent, congruent circles with radii that are half the radius of their outer circle.
>
>Having trouble imagining what this dartboard looks like? You’re not alone! Fortunately, Quowong created an image of the dartboard:
>
>![](https://substackcdn.com/image/fetch/$s_!VAWq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad54f80c-220c-4ccc-ad27-3f3a6d77f3e9_469x470.png)
>
>Now, when you throw a dart at this board, your score is the sum of the areas of every circle for which the dart lies inside or on the circumference. (Remember, the entire board is a unit circle.)
>
>What is the most a single dart can score?
>
>**Extra credit**: Suppose each point on the dartboard is equally likely to be hit by a dart. On average, what score would you expect a single dart to earn?


<!--more-->

([Fiddler on the Proof](URL))

## Solution

There are two big pieces to this problem. One is finding the radii of all the sub-gaskets inside the unit circle and the other is calculating expected points due to the sub-circles.

We'll do the second part first.

## Expected points

When we are throwing our first dart, we will get points for being inside the unit circle, plus whatever recursive points resulting from which level-$1$ subcircle we land inside, meaning the biggest circle we are inside that is not the unit circle itself. 

Since each circle is its own Apollonian gasket, and we land at random inside them, we are sampling the inside of each sub-gaskets uniformly. 

We can use this fact to calculate the expected multiplier. Let's call $\gamma A$ the expected points resulting from landing inside a circle of area $A.$ starting from the unit circle, we have

$$ \gamma \pi = \pi + \gamma \langle A_j\rangle_{j\in\text{set of level-1 circles}}. $$

The probability to land inside a circle of area $A = \pi r_j^2$ is that area relative to the overall area, e.g. $\pi r_j^2/\pi = r_j^2.$ so 

$$ \langle A_j\rangle_{j\in\text{set of level-1 circles}} = \frac{\sum\limits_{j\in\text{set of level-1 circles}} \pi r_j^4}{\sum\limits_{j\in\text{set of level-1 circles}} r_j^2}. $$

Solving for $\gamma$ we get

$$ \gamma = \frac{1}{1 - \frac{\sum\limits_{j\in\text{set of level-1 circles}} \pi r_j^4}{\sum\limits_{j\in\text{set of level-1 circles}} r_j^2}}. $$

To carry out this calculation, we just need the set of level-$1$ circles to sum over. Since this is infinite, we can't have it, but since the contribution of individual circles falls off as $r^4,$ we can get a very good approximation with a large set.

## Finding the level-$1$ circles

Each time we draw a new circle that's tangent to three existing ones, represented by the triple $(r_a,r_b,r_c)$, we get a new one of radius $r_d$ that's tangent to all three. That means we get three new opportunities to draw a new circle, given by the triple $(r_a, r_b, r_d)$, $(r_a,r_d,r_c),$ and $(r_d,r_b,r_c).$ Determining the radius of the new circle is a classic problem solved by Descarte's appropriately named ![circle theorem](https://en.wikipedia.org/wiki/Descartes%27_theorem#Statement) which relates the four radii like

$$ \left(1/r_a+1/r_b+1/r_c+1/r_d\right)^2 = 2\left(1/r_a^2 + 1/r_b^2+1/r_c^2+1/r_D^2\right). $$

If a circle encompasses the others, its sign is negative.

Starting from the top level, where we have two spaces both described by the triples $\left(-1,\frac12, \frac12\right).$ From there, we can just proceed one level at a time, consuming the current triples, computing the resulting radii, and accumulating the new triples for the next round. 

## Implementation

For ease of typing, the code is written in terms of the circles' inverse radii a.k.a. curvatures:

```python
import math
from collections import Counter, defaultdict

depth = 17
initial_triples = ((-1, 2, 2), (-1, 2, 2))

def descartes_theorem(triple):
    k1, k2, k3 = triple
    sum_of_prods = k1 * k2 + k2 * k3 + k3 * k1
    return (k1 + k2 + k3) + 2.0 * math.sqrt(sum_of_prods)


def generate_curvatures(initial_triples, depth):
    current_triples = [tuple((triple)) for triple in initial_triples]
    level_curvatures = defaultdict(list)

    for level in range(depth):
        next_triples = []

        for triple in current_triples:
            new_curvature = descartes_theorem(triple)
            level_curvatures[level + 1].append(new_curvature)
            a, b, c = triple

            for x, y in ((a, b), (a, c), (b, c)):
                next_triples.append(tuple(((x, y, new_curvature))))
        
        current_triples = next_triples

    return level_curvatures

level_curvatures = generate_curvatures(initial_triples, depth)

curvatures = []
for val in level_curvatures.values():
    curvatures.extend(val)

curv_freq = Counter(curvatures)
# remove artifact of starting with two triples
curv_freq[2] = 2
# remove the unit circle
curv_freq[-1] = 0

num = sum(freq / curv ** 4 for curv, freq in curv_freq.items())
denom = sum(freq / curv ** 2 for curv, freq in curv_freq.items())

Q = num / denom
gamma = 1 / (1 - Q)

exp_points = math.pi * gamma
```
which, for $17$ recursions, gets 

$$\langle \text{points}\rangle = \pi \gamma \approx 3.7108642714207782\ldots, $$

computed over 129,140,165 circles. This is an overestimate, since each recursion brings smaller and smaller circles into the expected value calculation.

You could also do this using the found data at OEIS sequences ![A042944](https://oeis.org/A042944) and ![A042946](https://oeis.org/A042946), as I did at first, but due to the low number of datums, you end up with $\gamma A \approx \sim3.825$

## Standard credit

The maximum possible score is found by landing inside the biggest possible circle at each level of recursion which means the unit circle, the half unit circle, the quarter unit circle and so on. This gives $\pi\left(1+\frac1{2^2} + \frac{1}{2^4} + \frac1{2^6} + \ldots\right) =  4\pi/3.$ 

But, if we hit at the exact point of contact between the two half unit circles, we can double our points, making the maximum possible score for an individual dart $8\pi/3.$ 

However, hitting two circles at once doesn't matter in expectation, since it is a probability zero event.

<br>
