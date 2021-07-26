---
layout: post
published: true
title: Random Rock Climb
date: 2021/07/25
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

### Standard credit ($1\text{D}$)

If there's a climbable path from the bottom to the top, it means that there is no gap bigger than $g$ between consecutive holds.

Likewise, if there is no climbable path, it means that one or more holds are followed by a gap bigger than $g.$ 

For bookkeeping purposes, I'm going to consider the bottom of the climb as an obligatory hold, $h_0.$

### Intuition with small $h$

Suppose there are two placed holds, $h_1$ and $h_2.$ As long as $1/g > 3,$ it could be that there is a gap after $h_0$ or after $h_1$ or after $h_2:$ 

$$ P(h_0) + P(h_1) + P(h_2). $$

However, $P(h_0)$ and $P(h_1)$ both encompass $P(h_0 + h_1),$ which means that we are double counting $P(h_0 + h_1)$ (and $P(h_1 + h_2)$ and $P(h_2 + h_0)$). So, we subtract them off:

$$ P(h_0) + P(h_1) + P(h_1) - P(h_0 + h_1) - P(h_1 + h_2) - P(h_2 + h_0). $$

Here we fixed one problem, but caused another. Each of the $P(h_i)$ terms contain a copy of $P(h_0 + h_1 + h_2),$ as do each of the $P(h_i + h_j)$ terms, which means that it's fully gone and we need to add it back in. 

Finally, we have

$$\begin{align} 
P_\text{gap} = &+\left[P(h_0) + P(h_1) + P(h_2)\right]
\\ &- \left[P(h_0 + h_1) + P(h_1 + h_2) + P(h_2 + h_0)\right]
\\ &+ P(h_0 + h_1 + h_2).
\end{align}$$

The single gap probabilities $P(h_i)$ are $(1 - g)^2$ (two holds were not placed in a window of size $g$), the double gap probabilities $P(h_i + h_j)$ are $(1-2g)^2$ (two holds were not placed in a window of size $2g$), and the triple gap probability $P(h_0 + h_1 + h_2)$ is $(1-3g)^2,$ so

$$ P_\text{gap} = \binom{3}{1}(1-g)^2 - \binom{3}{2} (1-2g)^2 + \binom{3}{3}(1-3g)^2. $$

In general, there can be as many as $\lfloor g^{-1}\rfloor$ gaps, and the probability of a gap with $h$ holds is

$$ P_\text{gap}(h, g) = \sum_{x=1}^{\lfloor g^{-1}\rfloor} (-1)^{x+1} \binom{h}{x}(1-xg)^{h-1}. $$

Likewise, the probability that the wall is climbable after $h$ holds is 

$$ P_\text{climb}(h, g) = 1 - P_\text{gap}(h, g). $$

The probability that the wall becomes climbable after placing the $h^\text{th}$ hold is then 

$$ P_\text{climb}(h, g) - P_\text{climb}(h-1, g) $$

And the expected number of holds that need to be placed to make the wall climbable is 

$$ \langle h \rangle = \sum_{h=0}^\infty (h-1) \times\left[P_\text{climb}(h, g) - P_\text{climb}(h-1, g)\right] $$



<br>
