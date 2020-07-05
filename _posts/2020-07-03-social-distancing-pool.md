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

Generalizing, this becomes the recursive equation

$$E(N) = 1 + 2\frac{E(1) + E(2) + \ldots + E(N-2)}{N}.$$

We can code this up (in Python) like

```python
def gf(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (1 + 1/n * (2 * sum(gf(i) for i in range(n-1))))
```

This works but, since it's a recursive function, it's much faster if we remember earlier evaluations:

```python
from collections import defaultdict
memo = defaultdict(lambda: False)

def gf(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (1 + 1/n * (2 * sum(memoized_gf(i) for i in range(n-1))))
        
def memoized_gf(n):
    if memo[n]:
        return memo[n]
    else:
        memo[n] = gf(n)
    return gf(n)
```

Calculating `gf(5)` we get $2.4\bar{6}$ in agreement with the calculation of $37/15$.

![](/img/2020-07-03-social-distancing-pool.png){:width="450px" class="image-centered"}

{:.caption}
After the initial values, this thing gets very linear.

## What's that slope?

ddd

<br>
