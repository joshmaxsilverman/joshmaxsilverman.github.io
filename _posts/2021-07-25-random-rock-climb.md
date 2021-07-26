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

Suppose there are $3$ placed holds. 

It could be that there is a gap after $h_1$ or after $h_2$ or after $h_3.$ 

$$ P(h_1) + P(h_2) + P(h_3). $$

But $P(h_1)$ and $P(h_2)$ both encompass $P(h_1 & h_2),$ which means that we are double counting $P(h_1 & h_2)$ (and $P(h_2 & h_3)$ and $P(h_3 & h_1)$). So, we subtract them off:

$$ P(h_1) + P(h_2) + P(h_3) - P(h_1 & h_2) - P(h_2 & h_3) - P(h_3 & h_1). $$

Here we have the same problem again. Each of the $P(h_i)$ terms contain a copy of $P(h_1 & h_2 & h_3),$ as do each of the $P(h_i & h_j)$ terms, which means that we need to add it back in. Finally, we have

$$ P(\text{gap}) = P(h_1) + P(h_2) + P(h_3) - P(h_1 & h_2) - P(h_2 & h_3) - P(h_3 & h_1) + P(h_1 & h_2 & h_3). $$


<br>
