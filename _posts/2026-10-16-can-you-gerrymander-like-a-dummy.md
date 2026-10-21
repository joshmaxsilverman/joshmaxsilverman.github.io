---
layout: post
published: true
title: Can you gerrymander like a dummy?
date: 2026/10/20
subtitle: What are the chances you gerrymander yourself to defeat?
tags: probability optimization game-theory
source: fiddler
kind: puzzle
theme: probability
hide_from_recent: true
---

> **Question**: Fiddler Nation has an upcoming election between its two major political parties: the Suns and the Moons. You are drawing a new electoral map, and you have been tasked with [gerrymandering](https://en.wikipedia.org/wiki/Gerrymandering) on behalf of your party, the Moons. Fortunately, you know exactly how every citizen will vote in the election.
>
> Fiddler Nation has seven districts, each with an equal population. For simplicity, assume that the Moons win any district in which they receive *at least half* of the vote.
>
> What is the *smallest* total fraction of Fiddler Nation’s population needed to vote Moon such that it’s possible for the Moons to win a majority of the seven districts?
>
> **Extra Credit**: In the next election cycle you’re back at it, gerrymandering on behalf of the Moon party once more. This time, you can draw a map that results in any set of probabilities $P_1$, $P_2$, $P_3$, $P_4$, $P_5$, $P_6$, and $P_7$ that you’ll win each of the corresponding districts—subject to the constraint that the average of the probabilities is 1/2. In other words, $P_1 + P_2 + P_3 + P_4 + P_5 + P_6 + P_7 = 7/2$.
>
> The bosses of the Moon party want to go big. More specifically, they want to maximize the party’s chances of winning *at least five* of the seven districts. However, you are concerned that such a greedy attempt at gerrymandering may backfire, a phenomenon that has become known as [dummymandering](https://sites.socsci.uci.edu/~bgrofman/140%20Grofman%20and%20Brunell.%20%202005%20%20The%20Art%20of%20the%20Dummymander....pdf). When you draw a map that maximizes your chances of winning at least five districts, the probability the Moon party blows it and winds up losing a majority of the seven districts is $L_A$.
>
> Your personal preference is to simply maximize the party’s chances of winning *at least four* of the seven districts—a simple majority of them. When you draw a map that maximizes these chances, the probability the Moon party loses a majority of the seven districts is $L_B$.
>
> How much greater than $L_B$ is $L_A$?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-gerrymander-like-a-dummy))

## Solution

When we make an electoral strategy, how should we allocate the Moon demographic across the districts?
We could give the same amount to every district, or we could give a lot to some and a little to others, or any number of schemes.

We can figure out what's best by assuming we're at the maximal policy and inspecting pairs of districts.
<!-- the answer is actually the simplest, that we should give the same amount to every participating district and we can prove this with the following argument. -->

### Optimal allocation policy

Suppose we are at the optimal allocation for at least $k$ wins and pick two districts, 1 and 2, to inspect.

With the other districts held fixed, the probability of victory will have some terms where districts 1 and 2 both need to win, some where at least one of them needs to win, and some where neither needs to win.
Since the other districts are held constant, this will have the form

$$ 
	\begin{align}
		P_\text{Moon} &= A\cdot p_1p_2 + B\cdot \left(p_1+ p_2 - p_1p_2\right) + C \\
		&= (A-B)\cdot p_1p_2 + B\cdot R + C
	\end{align}
$$

Where $A$ is the chance the fixed districts have $k-2$ wins, $P(W=k-2)$, $B=P(W=k-1)$, and $C=P(W\geq k)$. 
By constraint, $p_1 + p_2 = R$ where $R$ is $\tfrac72$ minus the sum of the probabilities for Moon to win the other districts. 
Making this substitution, we get 

$$ P_\text{Moon} = A\cdot p_1(R-p_1) + B\cdot \left(R - p_1(R-p_1)\right) + C. $$

Taking the derivative of this expression, we get 

$$ \frac{\text{d}}{\text{d}p_1} P_\text{Moon} = (A-B)(R-2p_1) $$

which is zero when $p_1 = \frac12R.$ 
- if $(A-B)>0$ then $P_\text{Moon}$ is maximized when $p_1 = p_2 = R/2$, i.e. when $p_1$ and $p_2$ are both reset to their average.
- if $(A-B) < 0$ then this is a minimum, and $P_\text{Moon}$ is maximized by extremizing $p_1$ toward zero or one (without making the larger one bigger than $R$ or $1$).

In fact, this suggests an algorithm to find the set of local optima in the space of district allocations, from which we can identify the global optima.
Starting from a random configuration, we fix 5 of the districts at random, compute $(A-B)$ and then either average or extremize based on its sign. 
If we start from a modest number of initial conditions, we can map out the space this way.

Suppose we tried a more elaborate swap by taking some small amount of demographic $\gamma$ from district 3 and giving $\alpha$ of it to district 1 and $\beta$ of it to district 2.
Then the rate of increase would be the dot product of the gradient of $P_\text{Moon}$ with the changes $\Delta = \left(\alpha,\beta, -\gamma\right)$.

$$
	\begin{align} 
		\nabla P_\text{Moon}\cdot \Delta &= \alpha\frac{\partial P_\text{Moon}}{\partial p_1} + \beta\frac{\partial P_\text{Moon}}{\partial p_2} - \gamma\frac{\partial P_\text{Moon}}{\partial p_3} \\
		&= \alpha\frac{\partial P_\text{Moon}}{\partial p_1} + \beta\frac{\partial P_\text{Moon}}{\partial p_2} - \left(\alpha+\beta\right)\frac{\partial P_\text{Moon}}{\partial p_3} \\
		&= \alpha\left(\frac{\partial P_\text{Moon}}{\partial p_1}-\frac{\partial P_\text{Moon}}{\partial p_3}\right) + \beta\left(\frac{\partial P_\text{Moon}}{\partial p_2}-\frac{\partial P_\text{Moon}}{\partial p_3}\right)
	\end{align}
$$

Which is just a linear combination of two pairwise exchanges. 
The only way for this to improve things is if one of the individual swaps does. 
The same kind of argument holds for more complex swaps.
So, a global optimum can't have any pairwise swaps that improve $P_\text{Moon}$ and so is a fixed point under the pairwise exchange rule laid out above. 


<!-- in fact, we can find these states by running the pairwise optimization strategy implied by the derivative condition above.
we start out from a random arrangement, then calculate $(A-B)$ for the arrangement using the five quantities held fixed.
if it's positive then we average the districts under inspections.
if it's negative then we set one of the variables to the remainder itself, and the other to zero. -->

When we run this out for the case of winning at least 4 districts, we get three fixed points 

- $(0,0,0,\frac78,\frac78,\frac78,\frac78),$ 
- $(0,0,\frac{7}{10},\frac{7}{10},\frac{7}{10},\frac{7}{10},\frac{7}{10}),$ and 
- $(0,\frac{7}{12},\frac{7}{12},\frac{7}{12},\frac{7}{12},\frac{7}{12},\frac{7}{12}),$ 

out of which the first arrangement has the highest probability to win.

For the case of optimizing at least 5 districts won, the sole fixed point is 

$$ \left(\frac12,\frac12,\frac12,\frac12,\frac12,\frac12,\frac12\right). $$

<!-- this means that all strategies will have some number of zero entries and some number of non-zero entries all equal to each other.  -->

```python
import itertools
import random
import numpy as np
from collections import defaultdict

def get_score(p, k):
	# probability of winning at least k districts
	d = np.array([1.0])
    # make probability distribution
	for x in p:
        d = np.convolve(d, [1 - x, x])
	return d[k:].sum()

def get_random_start():
    # generates random valid configuration
    while True:
        p = np.random.dirichlet(np.ones(7)) * 3.5
        if p.max() <= 1.0:
            return p

def find_local_optimum(p, k):
    p = np.array(p)
    while True:
        improved = False
        pairs = list(itertools.combinations(range(len(p)), 2))
        
        for i, j in pairs:
            s = p[i] + p[j]
            others = np.delete(p, [i, j])
            d = prob_wins(others)
            
            A = d[k - 2] if 0 <= k - 2 < len(d) else 0.0
            B = d[k - 1] if 0 <= k - 1 < len(d) else 0.0
            AminB = A - B

            # AminB > 0 -> average, AminB <= 0 -> extremize
            if AminB > 0:
                new_i, new_j = s / 2, s / 2
            else:
                new_i, new_j = min(1.0, s), max(0.0, s - 1.0)
            
            q = p.copy()
            q[i], q[j] = new_i, new_j
            
            if get_score(q, k) > get_score(p, k) + 1e-9:
                p = q
                improved = True
                
        if not improved:
            return np.sort(p)

for k in (4, 5):
    optima = defaultdict(lambda: 0)
    for _ in range(1000):
        p_start = get_random_start()
        p_end = find_local_optimum(p_start, k)
        optima[tuple(np.round(p_end, 3))] += 1

    print(f"local optima for k={k}:")
    for vec, count in optima.items():
        print(f"  {count:4d}x matches: {vec}")
```

### Optimal gerrymandering strategy

If we want to maximize our chance of winning 4 or more districts, we allocate Moon demographic equally across 4 districts, and set the rest to zero.

$$ P_{\text{Moon},4} = p^4 = \left(\frac{7}{2\cdot 4}\right)^4 \approx 0.5862 $$

By contrast, the optimal allocation for $k=5$ is to put a half unit of Moon demographic in each of the 7 districts.

<!-- if, instead, we engage 5 districts then the probability to win at least 4 would be $\left(\frac{7}{2\cdot 5}\right)^5 + 5\left(\frac{7}{2\cdot 5}\right)^4(1-\frac{7}{2\cdot 5}) \approx 0.5282$ which is lower than if we used 4 and it doesn't get better from there.
so, the optimal play for winning at least 4 districts is to evenly spread the Moon demographic over 4 districts and put zero in the other 3 districts.

if we're trying to maximize the chance to win at least 5 districts, then we have to consider even distributions over $d = 5$, 6, or 7 districts. 

using a maximum of $d$ engaged districts we have to compare the sums

$$ \sum_{j=5}^d \binom{d}{j}\left(\frac{7}{2d}\right)^j\left(1-\frac{7}{2d}\right)^{d-j} $$

for $d=5,6,7$ which yields $\approx 0.1681, \approx 0.2083, $ and $\approx 0.2266,$ respectively, which shows that the optimal choice to win at least 5 districts is to assign $\frac12$ demographic units to each of the 7 districts. -->

With this allocation, the probability of a Moon party loss is 

$$ L_A = 1 - \frac{1}{128}\left(\binom{7}{4} + \binom{7}{5} + \binom{7}{6} + \binom{7}{7}\right) = \frac12. $$

The probability that the Moon party loses with the $k=4$ district plan is $L_B = 1-\left(7/8\right)^4 \approx 0.4138$ so the dummymander deficit is $L_A - L_B = \frac12-0.4138 \approx 0.0862$



<br>
