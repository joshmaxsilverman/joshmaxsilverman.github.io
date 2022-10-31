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

Putting it together, the expected penalty is

$$
  \frac12\frac{\left(150-L\right)^2}{202} + \frac12\frac{\left(L-50\right)^2}{202}
$$

which is minimized at $L=100$ which can be seen by symmetry, or expanding it. Temporarily writing $150$ as $U$ and $50$ as $B,$ we get

$$
  (U-L)^2 + (L-B)^2 = U^2 + B^2 + 2L(L- (U + B))
$$

which manifestly has roots at $L=0$ and $L = U + B$ and opens upward. Parabolas bottom out at the average of their roots, so the strategy of minimum penalty is $L_\text{min} = (U+B)/2 = 100.$

### Optimality check

We can check that our physics chutzpah did not lead us astray. At each step, we have a choice between three decisions:

- hand out $1$ chocolate,
- hand out $2$ chocolates, or
- hand out $3$ chocolates.

We should always make the choice that minimies expectation, so the expected penalty starting from $C$ candies, after seeing $T$ trick or treaters, is

$$
  E(C,T) = \min\limits_c\\{\gamma(C-1, T+1), \gamma(C-2,T+1), \gamma(C-3,T+1)\\}.
$$

The value of the choice $\gamma(C, T)$ depends on where we find ourselves.

$$
  \displaystyle \gamma(C,T) = 
  \begin{cases}
    0 & T=150 \\
    \infty & C < 0 \\
    E(C,T) & C < 49 \\
    (1-\frac{1}{150-T})\frac{150-T}{2} & C =0 \\
    \frac{1}{150-T}C + (1-\frac{1}{150-T})E(C,T) & C > 0
  \end{cases} 
$$

<br>
