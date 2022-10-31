---
layout: post
published: false
title: Neurotic Halloween
date: 2022/10/29
subtitle: How close can you get to perfect candy disbursement?
tags:
---

>**Question**:

<!--more-->

([FiveThirtyEight](URL))

## Solution

The approach is roughly

- illuminate the logic with the worst cases
<!-- - solve the problem, pretend the chocolate is continuous -->
- update the approach for discrete chocolates
- calculate the expectation
- make sure that physics chutzpah didn't mislead us by resolving with dynamic programming

### Worst case

If we want to incur the maximum average penalty, we can either always dispense $3$ chocolate or always dispense $1$ chocolate. 

In the first case, we'll run out of chocolate by the $50^\text{th}$ trick or treater (ToT) and so, $X$ (our penalty) will always be $50.$ In the second case, we'll have $100$ candies left by the $50^\text{th}$ ToT and, so, have an average of $50$ candies left over after the last ToT has come to the door. 

Evidently, the optimal approach is something between these two extremes.

<!-- ### Chocolate continuum 

The penalty is symmetric with respect to leftover candy and unserved ToTs, so we should aim to run out of candies precisely at the average number of ToTs, dispensing $150/100 = 1.5$ chocolates each visit until we run out. 

If we plan for e.g. $99$ ToT, then we'll add an average penalty of $1/101$ 

If we aimed slightly beyond $100,$ we'd be 

any candy that's left after the $50^\text{th}$ ToT will contribute to our penalty. 

so we should aim to run out of candy by the $100^\text{th}$ ToT (the average number of ToTs).

On average, there will be $100$ ToTs. So, if we were free to divide the chocolate anyway we like, then we would want to  -->

### Chocoallotment

We can figure out the "shape" of the strategy by thinking about the penalties.

After the $50^\text{th}$ ToT, we're penalized for undisbursed chocolates. So, after that point, we'll only hand out single chocolates. This also means that, before ToT $50,$ it doesn't matter what order we hand out chocolates in, only the total number we dispense by that point.

So, we'll plan for some number $L$ of ToTs, handing out single chocolates to ToTs $50$ through $L,$ and a total of $\left(150-L\right)$ to ToTs $1$ through $49$:

$$
  \overbrace{\\{C_1, C_2, \ldots, C_{49}, 1, 1, 1, \ldots, 1\\}}^{L\text{ entries}}
$$

### Expectation penalty

If there are more than $L$ ToTs then we'll incur, on average, a penalty of $\frac12(150-L)$ for the unserved ToTs, which happens with probability $(150-L)/101.$ 

If there are less than $L$ ToTs, then we'll incur, on average, a penalty of $(L-50)/2$ which happens with probability $(L-50)/101.$

If there are $L$ ToTs, then we'll incur a penalty of $(150 - L)$ for the unserved ToTs with probability $1/101.$

Putting it together, the expected penalty is

$$
  \frac12\frac{\left(150-L\right)^2}{202} + \frac12\frac{\left(L-50\right)^2}{202} + \frac{150-L}{101}
$$

which is minimized at $L=201/2$ which can be seen by symmetry, or expanding it. Temporarily writing $150$ as $U$ and $50$ as $B,$ we get

$$
  (U-L)^2 + (L-B)^2  + 2(U-L) = U^2 + B^2 + 2U + 2L(L- (U + B + 1))
$$

which manifestly has roots at $L=0$ and $L = (U + B + 1)$ and opens upward. Parabolas bottom out at the average of their roots, so the strategy of minimum penalty is $L_\text{min} = (U+B+1)/2 = 100.5$

Since $L$ is an integer, we go with $L=100$ which gives an average penalty of $2550/101.$

### Optimality check

We should check that our physics chutzpah did not lead us astray. At each step, we have a choice between three decisions:

- hand out $1$ chocolate,
- hand out $2$ chocolates, or
- hand out $3$ chocolates.

We should always make the choice that minimies expectation, so the expected penalty starting from $C$ candies, after seeing $T$ trick or treaters, is

$$
  E(C,T) = \min\limits_c\\{\gamma(C-1, T+1), \gamma(C-2,T+1), \gamma(C-3,T+1)\\}.
$$

The value of the choice $\gamma(C, T)$ depends on where we find ourselves. 

- if we've seen less than $49$ ToTs so far, then we immediately make our next choice. 
- if we reach the end with no candies, we have no penalty. 
- if we run out of candies, and we've seen $49$ or more ToTs, then there's a $1$ in $(150-T)$ chance that we've just given candy to the final ToT. If that's not the case, then we incur an average penalty of half the potential remaining ToTs.
- if we have candies remaining and have seen $49$ or more ToTs, then we've either seen the last ToT, or we have another choice to make.

Finally, we can't have a negative amount of candies. Putting it all together, we have.

$$
  \displaystyle \gamma(C,T) = 
  \begin{cases}
    E(C,T) & T < 49 \\
    0 & C=0,T=150 \\
    \left(1-\dfrac{1}{150-T}\right)\dfrac{150-T}{2} & C=0, T\geq 49 \\
    \dfrac{1}{150-T}C + \left(1-\dfrac{1}{150-T}\right)E(C,T) & C > 0, T\geq 49 \\
    \infty & C<0
  \end{cases} 
$$

Running this in Python, we get $E(150,0) = 2550/101,$ as expected.

```python
from functools import lru_cache

impossible = 10_000

@lru_cache(maxsize=10_000_000)

def gamma(C, T):
  if C < 0:
    return impossible
  if T == 150:
    return C
  if T < 49:
    return E(C,T)
  if C == 0:
    return 1/(150-T) * 0 + (1 - 1/(150-T)) * (150-T)/2
  if C > 0:
    return 1/(150-T) * C + (1 - 1/(150-T)) * E(C, T)

def E(C, T):
  return min([gamma(C-1, T+1), gamma(C-2, T+1), gamma(C-3, T+1)])
```

<br>
