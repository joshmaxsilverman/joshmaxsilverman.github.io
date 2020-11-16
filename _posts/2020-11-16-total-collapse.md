---
layout: post
published: true
title: Total Collapse
date: 2020/11/16
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

This problem is about devastation — games where our team gets to a point where they have a $99%$ chance to win only to completely blow the lead and lose the game. 

### Trajectory probabilities

By implication, there are points in the space of scores $(w,\ell)$ where there is a $99\%$ or greater chance for the player in the lead to go on to win. If we can find the set of those points, $\mathcal{S},$ then the probability of witnessing a collapse is just

$$P_\text{collapse} = \sum_{S_i\in\mathcal{S}} P(\text{start} \rightarrow S_i)\times P(S_i \rightarrow\text{collapse}).$$

Here, $P(S_i\rightarrow\text{collapse})$ is the probability that after reaching the point $S_i,$ the player in the lead goes on to lose the game. We don't care how the game makes it from $S_i$ to a loss, any path will do.

$P(\text{start}\rightarrow S_i)$ is the probability that a game makes it to the point $S_i.$ More specifically, it's the probability that the game makes it to $S_i$ before visiting any other point in $\mathcal{S}$ — if it's already been to $\mathcal{S}$ we ignore it since we don't want to double count. The fact that we need to classify trajectories according to which point in $\mathcal{S}$ they visit first makes this quantity tricky to calculate.

### From $\mathcal{S} to an $L$ — the likelihood of collapse

If we can calculate $P((w,\ell) \rightarrow\text{collapse})$ then we can find the points of $\mathcal{S}$ simply by scanning the grid for points where it is $ \leq 1\%.$

The Birds will lose if they get to $51$ losses. If we're at the point $(w, \ell)$ then we need to lose $51 - \ell$ more games to win. We can do that in a number of ways. We could lose $(51 - \ell)$ straight games, we could win $1$ game amidst losing $(51 - \ell)$, etc. In fact, we can win as many as $(51 - w - 1)$ more games so long as we lose $(51-\ell)$ of them in the process. 

The number of paths we can take that win $w^\prime$ games and lose $\ell^\prime$ games is just $\binom{w^\prime + \ell^\prime}{\ell^\prime}.$ When the game picks up from $(w, \ell),$ the total number of trajectories it can take is $2^{101 - w - \ell}.$ So, the total probability of a loss starting at the point $(w, \ell)$ is

$$ P_\text{loss}(w,\ell) = \frac{1}{2^{101 - w - \ell}} \sum_{w^prime = 0}^{w^\prime = 51 - \ell - 1} \binom{ w^\prime + \ell^\prime}{w^\prime}. $$

<br>
