---
layout: post
published: true
title: Social Distance Swimming Pool
date: 2020/07/04
---

>Question: It's 8:59 at the 10-lane town pool and the coronavirus is absolutely ripping. In an effort to mitigate the spread, swimmers must stay at least one lane apart. In one minute, the swimmers will hop into the pool, one lane at a time, until it becomes impossible to obey social distancing. If there are 10 swimmers, how many do you expect to be left crying on the side of the pool?

<!--more-->

([FiveThirtyEight](URL))

## Solution

The easiest way to get started on this problem is to get started on this problem. But let's start simple, with $6$ lanes.

Suppose the first swimmer jumps in and she goes into the third lane. By the social distancing rule, this means that no other swimmer can go into the second lane or the fourth lane. We effectively now have two copies of the original problem playing out in lane $1$ and in lanes $5$ through $6$.

In other words, the total number of swimmers we expect, given that the first swimmer hopped into lane $3$ is the swimmer in lane $3$ plus the expected number of swimmers in a $1$ lane pool plus the expected number of swimmers in a $2$ lane pool.

$$E(6 | \text{first swimmer in lane 3}) = 1 + E(1) + E(2)$$

If the first swimmer had instead gone into the second lane, we'd get 

$$E(6 | \text{first swimmer in lane 2}) = 1 + E(3)$$

Since there's an equal chance of the first swimmer going in any lane, the expected number of swimmers in the pool is

$$\begin{align}
E(6) &= \frac{2\left(1 + E(4)\right) + 2\left(1 + E(3)\right) + 2\left(1 + E(1) + E(2)\right)}{6} \\
     &= 1 + 2\frac{E(1) + E(2) + E(3) + E(4)}{6}
\end{align}$$

Diagramatically, we can picture this recursion like

`<diagram of recursive pools>`

<br>
