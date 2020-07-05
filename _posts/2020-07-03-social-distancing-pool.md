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

$$S(6 | \text{first swimmer in lane 3}) = 1 + S(1) + S(2)$$

If the first swimmer had instead gone into the second lane, we'd get 

$$S(6 | \text{first swimmer in lane 2}) = 1 + S(3)$$

Since there's an equal chance of the first swimmer going in any lane, the expected number of swimmers in the pool is

$$\begin{align}
S(6) &= \frac{2\left(1 + S(4)\right) + 2\left(1 + S(3)\right) + 2\left(1 + S(1) + S(2)\right)}{6} \\
     &= 1 + 2\frac{S(1) + S(2) + S(3) + S(4)}{6}
\end{align}$$

Diagramatically, we can picture this recursion like

`<diagram of recursive pools>`

Generalizing, this becomes the recursive equation

$$S(N) = 1 + 2\frac{S(1) + S(2) + \ldots + S(N-2)}{N}.$$

### Recursive evaluation

We can code this up (in Python) like

```python
def S(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (1 + 1/n * (2 * sum(S(i) for i in range(n-1))))
```

This works but, since it's a recursive function, it's much faster if we remember earlier evaluations:

```python
from collections import defaultdict
memo = defaultdict(lambda: False)

def S(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (1 + 1/n * (2 * sum(memoized_S(i) for i in range(n-1))))
        
def memoized_S(n):
    if memo[n]:
        return memo[n]
    else:
        memo[n] = S(n)
    return S(n)
```

Calculating `S(5)` we get $2.4\bar{6}$ in agreement with the calculation of $37/15$. Taking it tot he next level, we find crushing linearity.

![](/img/2020-07-03-social-distancing-pool.png){:width="450px" class="image-centered"}

{:.caption}
After the initial values, this thing gets very linear.

### What's that slope?

With the numbers from the script, we could divide the rise of the line by its run and get a slope. But what is its closed form?

The simple truth is that we don't deserve to know, not yet at least. We haven't put in the work.

To go about it, I will return to the generating function, last employed in a similar capacity to how we'll use it here: [providing rigorous justification for an answer that we basically already had](https://joshmaxsilverman.github.io/2020-04-11-spam-attack/).

For a gentler introduction on how to use them, here's my guide:

Starting from

$$S(n) = 1 + 2\frac{S(1) + S(2) + \ldots + S(n-2)}{n}$$

we want to get $G(x) = \sum_n S(n)x^n.$ Going line by line,

$$\begin{align}
\sum_n S(n)x^n &= x\\
&= x^2 + \\
&= x^3 + \frac23 S(1)x^3 + \\
&= x^4 + \frac24 S(1)x^4 + \frac24 S(2) x^4 + \\
&= x^5 + \frac25 S(1)x^5 + \frac25 S(2) x^5 + \frac25 S(3) x^5 + \\
&= x^6 + \frac26 S(1)x^6 + \frac26 S(2) x^6 + \frac26 S(3) x^6 + \frac26 S(4) x^7 + 
&= x^7 + \ldots
\end{align}$$

which is enough to start working.

The column of bare $x$ powers becomes $x/(1-x).$ 

The terms with $S(1)$ are $2S(1)\left(x^3/3+x^4/4+x^5/5 + \ldots\right)$ and the terms with $S(2)$ are $2S(2)\left(x^4/4+x^5/5+x^6/6 + \ldots\right).$

Putting it together

$$G(x) = \frac{x}{1-x} + 2S(1)\left(\frac{x^3}{3}+\frac{x^4}{4}+\frac{x^5}{5} + \ldots\right) + 2S(2)\left(\frac{x^4}{4}+\frac{x^5}{5} + \frac{x^6}{6} \ldots\right) + \ldots$$

Recognizing the term by term integrals,

$$\begin{align}
G(x) &= \frac{x}{1-x} + 2S(1)\int dx\,\left(x^2 + x^3 + x^4\right) + 2S(2)\left(\int dx\, x^3 + x^4 + x^5\right) + \ldots \\
     &= \frac{x}{1-x} + 2S(1)\int dx\, \left(\frac{x^2}{1-x}\right) + 2S(2)\left(\int dx\, \frac{x^3}{1-x}\right) + \ldots \\
     &= \frac{x}{1-x} + 2\int dx\, \frac{1}{1-x}\left(S(1)x^2 + S(2)x^3 + S(3)x^4 + \ldots\right) \\
     &= \frac{x}{1-x} + 2\int dx\, \frac{x}{1-x}\left(S(1)x + S(2)x^2 + S(3)x^3 + \ldots\right)
\end{align}$$

The series inside the integral is just the generating function $G(x)$ so we get

$$G(x) = \frac{x}{1-x} + \int dx\, \frac{x}{1-x} 2G(x).$$

This can be solved with integrating factors.

$$\begin{align}
G(x) &= \frac{x}{1-x} + \int dx\, \frac{x}{1-x} 2G(x) \\
G'(x) &= \frac{1}{\left(1-x)^2} + 2\frac{x}{1-x}G(x)
\end{align}$$

<br>
