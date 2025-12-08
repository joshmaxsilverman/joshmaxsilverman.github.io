---
layout: post
published: false
title: Apollonian dartboard
date: 2025/12/08
subtitle:
tags:
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

there are two big pieces to this problem. one is finding the radii of all the sub-gaskets inside the unit circle and the other is calculating expected points due to the sub-circles.

we'll do the second part first.

when we are throwing our first dart, we will get points for being inside the unit circle, plus whatever recursive points resulting from which level-$1$ subcircle we land inside, meaning the biggest circle we are inside that is not that unit circle itself. since each circle is its own Apollonian gasket, and we land at random inside it, we are sampling the are inside each sub-gaskets uniformly. we can use this to calculate the expected multiplier:

let's call $\gamma A$ the expected points resulting from landing inside a circle of area $A.$ starting from the unit circle, we have

$$ \gamma \pi = \pi + \gamma \langle A_j\rangle_{j\in\text{set of level-1 circles}}. $$

the probability to land inside a circle of area $A = \pi r_j^2$ is that area relative to the overall area, e.g. $\pi r_j^2/\pi = r_j^2.$ so 

$$ \langle A_j\rangle_{j\in\text{set of level-1 circles}} = \frac{\sum\limits_{j\in\text{set of level-1 circles}} \pi r_j^4}{\sum\limits_{j\in\text{set of level-1 circles}} r_j^2}. $$

solving for $\gamma$ we get

$$ \gamma = \frac{1}{1 - \frac{\sum\limits_{j\in\text{set of level-1 circles}} \pi r_j^4}{\sum\limits_{j\in\text{set of level-1 circles}} r_j^2}}. $$

each time we draw a new circle that's tangent to three existing ones, represented by the triple $(r_a,r_b,r_c)$, we get a new one of radius $r_d$ that's tangent to all three. that means we get three new opportunities to draw a new circle, given by the triple $(r_a, r_b, r_d)$, $(r_a,r_d,r_c),$ and $(r_d,r_b,r_c).$ determining the radius of the new circle is a classic problem solved by Descarte's appropriately named ![circle theorem](https://en.wikipedia.org/wiki/Descartes%27_theorem#Statement) which relates the four radii like

$$ \left(1/r_a+1/r_b+1/r_c+1/r_d\right)^2 = 2\left(1/r_a^2 + 1/r_b^2+1/r_c^2+1/r_D^2\right). $$

if a circle encompasses the others, its sign is negative.

starting from the top level, where we have two spaces both described by the triples $\left(-1,\frac12, \frac12\right).$ from there, we can just proceed one level at a time, consuming the current triples, computing the resulting radii, and accumulating the new triples for the next round. for ease of typing, the code is written in terms of the circles' inverse radii a.k.a. curvatures:

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

computed over XYZ circles. this is an overestimate, since each recursion brings smaller and smaller circles into the expected value calculation.


## Standard credit

the maximum possible score is found by landing inside the biggest possible circle at each level of recursion which means the unit circle, the half unit circle, the quarter unit circle and so on. this gives $\pi\left(1+\frac1{2^2} + \frac{1}{2^4} + \frac1{2^6} + \ldots\right) =  4\pi/3.$ 

but, if we hit at the exact point of contact between the two half unit circles, we can double our points, making the maximum possible score for an individual dart $8\pi/3.$ 

however, hitting two circles at once doesn't matter in expectation, since it is a probability zero event.

<br>
