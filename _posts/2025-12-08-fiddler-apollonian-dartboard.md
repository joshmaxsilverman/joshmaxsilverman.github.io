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

whenever we hit a circle, we get points for its area plus whatever additional points come from the sub-circles we are also inside. since each circle is its own Apollonian gasket, and we land at random inside it, we are sampling each gasket uniformly. we can use this to calculate the expected multiplier.

let $\gamma A$ be the expected points from landing inside a circle of area $A.$ starting from the unit circle, we have

$$ \gamma \pi = \pi + \gamma \langle A_j\rangle_{j\in\text{set of level-1 circles}}. $$

the probability to land inside a circle of area $A = \pi r_j^2$ is that area relative to the overall area, e.g. $\pi r_j^2/\pi = r_j^2.$ so 

$$ \langle A_j\rangle_{j\in\text{set of level-1 circles}} = \frac{\sum\limits_{j\in\text{set of level-1 circles}} \pi r_j^4}{\sum\limits_{j\in\text{set of level-1 circles}} r_j^2}. $$

solving for $\gamma$ we get

$$ \gamma = \frac{1}{1 - \frac{\sum\limits_{j\in\text{set of level-1 circles}} \pi r_j^4}{\sum\limits_{j\in\text{set of level-1 circles}} r_j^2}}. $$

each time we draw a new circle that's tangent to three existing ones, represented by the triple $(r_a,r_b,r_c)$, we get a new one of radius $r_d$ that's tangent to all three. that means we get three new opportunities to draw a new circle, given by the triple $(r_a, r_b, r_d)$, $(r_a,r_d,r_c),$ and $(r_d,r_b,r_c).$ determining the radius of the new circle is a classic problem solved by Descarte's appropriately named ![circle theorem](https://en.wikipedia.org/wiki/Descartes%27_theorem#Statement) which relates the four radii like

$$ \left(1/r_a+1/r_b+1/r_c+1/r_d\right)^2 = 2\left(1/r_a^2 + 1/r_b^2+1/r_c^2+1/r_D^2\right). $$

if a circle encompasses the others, its sign is negative.

starting from the top level, where we have two spaces both described by the triples $(-1,\frac12, \frac12\right).$ from there, we can just proceed one level at a time, consuming the current triples, computing the resulting radii, and accumulating the new triples for the next round. 





3.7108642714207782


<br>
