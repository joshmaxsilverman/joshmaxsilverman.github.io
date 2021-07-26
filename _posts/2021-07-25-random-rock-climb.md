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

For simplicity, I'm going to consider the bottom of the climb to be an obligatory hold, $h_0.$

Suppose there are two placed holds, $h_1$ and $h_2.$ 

It could be that there is a gap after $h_0$ or after $h_1$ or after $h_2:$ 

$$ P(h_0) + P(h_1) + P(h_2). $$

However, $P(h_0)$ and $P(h_1)$ both encompass $P(h_0 + h_1),$ which means that we are double counting $P(h_0 + h_1)$ (and $P(h_1 + h_2)$ and $P(h_2 + h_0)$). So, we subtract them off:

$$ P(h_0) + P(h_1) + P(h_1) - P(h_0 + h_1) - P(h_1 + h_2) - P(h_2 + h_0). $$

Here we fixed one problem, but caused another. Each of the $P(h_i)$ terms contain a copy of $P(h_0 + h_1 + h_2),$ as do each of the $P(h_i + h_j)$ terms, which means that it's fully gone and we need to add it back in. 

Finally, we have

$$\begin{align} 
P(\text{gap}) = &+(P(h_0) + P(h_1) + P(h_2))
\\ &- (P(h_0 + h_1) + P(h_1 + h_2) + P(h_2 + h_0)) 
\\ &+ P(h_0 + h_1 + h_2).
\end{align}$$

The single gap probabilities $P(h_i)$ are $(1 - g)^2$ (two holds were not placed in a window of size $g$), the double gap probabilities are $(1-2g)^2$ (two holds were not placed in a window of size $2g$), and the triple gap probabilities are given by $(1-3g)^2$ (two holds were not placed in a window of size $3g$), so

$$ P(\text{gap}) = \binom{3}{1}(1-g)^2 - \binom{3}{2} (1-2g)^2 + \binom{3}{3}(1-3g)^2. $$

In general, there can be as many as $\lfloor\ell / g\rfloor$ gaps. 



<br>
