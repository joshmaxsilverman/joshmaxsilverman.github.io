---
layout: post
published: true
title: Social Distance Swimming Pool
date: 2020/07/04
---

>Question: It's 8:59 at the $N$-lane town pool and the coronavirus is absolutely ripping. In an effort to mitigate the spread, swimmers must stay at least one lane apart. In one minute, the swimmers will hop into the pool, one lane at a time, until it becomes impossible to obey social distancing. If there are $N$ swimmers, how many do you expect to be left crying on the side of the pool?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-stay-in-your-lane/))

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

![](/img/2020-07-06-social-distance-pool-animation.gif){:width="500px" class="image-centered"}

{:caption}
Illustrating the pool recursion induced by the first swimmer hopping in the third lane.

Generalizing, this becomes the recursive equation

$$S(N) = 1 + 2\frac{S(1) + S(2) + \ldots + S(N-2)}{N}.$$

### So... how many swimmers?

Before moving on to finer points, let's use the formula to find the expected number of swimmers in a $5$ lane pool. First of all, we have the base cases of $1$ and $2$ lane pools, for which we can only fit a single swimmer so $S(1) = S(2) = 1.$ 

For $5$ lanes, we get

$$S(5) = 1 + 2\frac{S(1) + S(2) + S(3)}{5}$$

plugging in $S(3) = 1 + 2S(1)/3 = 5/3$ and the bases cases, we get

$$S(5) = 1 + 2\frac{1 + 1 + 5/3}{5} = 1 + 2\frac{11/3}{5} = \frac{37}{15}.$$

So, on average, $5 - 37/15 \approx 2.53$ swimmers willl be left crying on the side of the pool.

### Recursive evaluation

We can code this up (in Python) like

```python
from functools import lru_cache

@lru_cache(maxsize=10000)
def S(n):
    if n <= 2:
        return 1
    else:
        return 1 + 2 / n * sum( S(i) for i in range(1, n-1) )
```

<!-- This works but, since it's a recursive function, it's much faster if we remember earlier evaluations:

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
-->

Calculating `S(5)` we get $2.4\bar{6}$ in agreement with the calculation of $37/15$. Taking it to the next level, we find crushing linearity.

![](/img/2020-07-03-social-distancing-pool.png){:width="450px" class="image-centered"}

{:.caption}
After the initial values, this thing gets very linear.

For reference, here are the first few coefficients:

$$\begin{array}{|c|c|} \hline
n & S(n) \\ \hline
1 & 1 \\ \hline
2 & 1 \\ \hline
3 & 5/3 \\ \hline
4 & 2 \\ \hline
5 & 37/15 \\ \hline
6 & 26/9 \\ \hline 
7 & 349/105 \\ \hline
\end{array}$$

### What's that slope?

With the numbers from the script, we could divide the rise of the line by its run and get a slope. But what is its closed form?

The simple truth is that we don't deserve to know, not yet at least. We haven't put in the work.

To go about it, I will return to the generating function, last employed in a similar capacity to how we'll use it here: [providing rigorous justification for an answer that we basically already had](https://joshmaxsilverman.github.io/2020-04-11-spam-attack/).

The basic idea (and miracle) is that it is easier to solve for the object $G = \sum S(n)x^n$ than it is to solve for $S(n)$ directly. Once we have $G$ we can Taylor expand and the coefficient on $x^n$, noted $\left[x^n\right]G,$ will be equal to $S(n).$

For a gentler introduction on how to use them, [here's my guide](/img/generating-dice.pdf).

Starting from

$$S(n) = 1 + 2\frac{S(1) + S(2) + \ldots + S(n-2)}{n}$$

we want to get $G(x) = \sum_n S(n)x^n.$ Going line by line,

$$\begin{align}
\sum_n S(n)x^n &= x\\
&+ x^2 + \\
&+ x^3 + \frac23 S(1)x^3  \\
&+ x^4 + \frac24 S(1)x^4 + \frac24 S(2) x^4  \\
&+ x^5 + \frac25 S(1)x^5 + \frac25 S(2) x^5 + \frac25 S(3) x^5  \\
&+ x^6 + \frac26 S(1)x^6 + \frac26 S(2) x^6 + \frac26 S(3) x^6 + \frac26 S(4) x^6  \\
&+ x^7 + \ldots
\end{align}$$

which is enough to start working.

The column of bare powers of $x$ becomes $x/(1-x).$ 

Grouping terms,

$$G(x) = \frac{x}{1-x} + 2S(1)\left(\frac{x^3}{3}+\frac{x^4}{4}+\frac{x^5}{5} + \ldots\right) + 2S(2)\left(\frac{x^4}{4}+\frac{x^5}{5} + \frac{x^6}{6} \ldots\right) + \ldots$$

Recognizing the term by term integrals,

$$\begin{align}
G(x) &= \frac{x}{1-x} + 2S(1)\int dx\,\left(x^2 + x^3 + x^4\right) + 2S(2)\int dx\, \left(x^3 + x^4 + x^5\right) + \ldots \\
     &= \frac{x}{1-x} + 2S(1)\int dx\, \left(\frac{x^2}{1-x}\right) + 2S(2)\int dx\, \left(\frac{x^3}{1-x}\right) + \ldots \\
     &= \frac{x}{1-x} + 2\int dx\, \frac{1}{1-x}\left(S(1)x^2 + S(2)x^3 + S(3)x^4 + \ldots\right) \\
     &= \frac{x}{1-x} + 2\int dx\, \frac{x}{1-x}\left(S(1)x + S(2)x^2 + S(3)x^3 + \ldots\right)
\end{align}$$

The series inside the integral is just the generating function $G(x)$ so we get

$$G(x) = \frac{x}{1-x} + 2\int dx\, \frac{x}{1-x} G(x).$$

This can be solved with integrating factors.

$$\begin{align}
G(x) &= \frac{x}{1-x} + 2\int dx\, \frac{x}{1-x} G(x) \\
G^\prime(x) &= \frac{1}{\left(1-x\right)^2} + 2\frac{x}{1-x}G(x) \\
G^\prime(x) - \frac{2x}{1-x}G(x) &= \frac{1}{\left(1-x\right)^2} 
\end{align}$$

The left side looks like the derivative of $G(x)\times e^\text{(some function of $x$)}$ where the derivative of $\text{(some function of $x$)}$ is $-2x/(1-x)$:

$$\frac{d}{dx}\left(G(x)\times e^\text{(some function of $x$)}\right) = \frac{e^\text{(some function of $x$)}}{\left(1-x\right)^2}$$

So $\text{(some function of $x$)} = -\int dx\ 2x/(1-x) = 2x + 2\log(x-1)$ and $e^\text{(some function of $x$)} = e^{2x}\left(1-x\right)^2$.

$$\begin{align}
G(x)e^{2x}\left(1-x\right)^2 &= C + \int dx\ e^{2x} \\
G(x)e^{2x}\left(1-x\right)^2 &= C + \frac12 e^{2x} \\
G(x) &= \frac{Ce^{-2x} + \frac12}{\left(1-x\right)^2}
\end{align}$$

By the series definition, $G(0)$ should be zero, so $C = -\frac12$ and

$$G(x) = \frac12 \frac{1-e^{-2x}}{\left(1-x\right)^2}$$

Remember, the whole idea is that the series expansion of $G(x)$ will have the $S(n)$ as its coefficients. Doing this, we get

$$x+x^2+\frac{5}{3}x^3+2 x^4+\frac{37}{15}x^5+\frac{26}{9}x^6+\frac{349}{105}x^7+\ldots$$

which matches what we got with the script.

At last, we can go for the coefficient on $x^n$, $S(n).$ The numerator and denominator expand to 

$$G = \frac12 \left(1 - \sum_j \frac{\left(-2\right)^j}{j!}\right) \left(\sum_k (k+1) x^k\right)$$

So the terms in the expansion have the form 

$$\frac{\left(-2\right)^{j-1}}{j!}(k+1)x^k$$

Since we're looking for the coefficient on $x^n,$ we can set $j + k = n$ so that becomes $\left(-2\right)^{k-1}(n-k+1)/k!$ and we sum over all possible $k$, so

$$\left[x^n\right]G(x) = \sum\limits_{k=1}^n \frac{\left(-2\right)^{k-1}(n-k+1)}{k!} $$

working in the limit where $n$ is large, we can pull the $(n-k+1)$ out in front

$$\left[x^n\right]G(x) \approx n \sum\limits_{k=1}^n \frac{\left(-2\right)^{k-1}}{k!} = \frac12 n \sum\limits_{k=1}^n \frac{\left(-2\right)^{k}}{k!} = n\left(\frac12 - \frac{e^{-2}}{2}\right)$$

which shows, at last, that the slope of the graph is $\left(1-e^{-2}\right)/2 \approx 0.43233235838169365$ As a check, we calculate `S(100) - S(99) = 0.4323323583816858...`, not bad.
