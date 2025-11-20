---
layout: post
published: false
title: Gaussian Skiers
date: 2025/11/18
subtitle: How safe are you for winning the first heat?
tags: scaling approximation
---

>**Question**: You're in your town's heat to head marble racing championship, the traditional way to determine who is the town's next mayor. The race is split into two heats and your time in either heat is a random, normally distributed variable. If you have the fastest time in the first run, what is the probability $P_\text{win it all}$ that you end up winning the event, as determined by the sum of your times on heat run? Extra credit: what if there are $29$ other candidates in the race?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-skillfully-ski-the-slopes/))

## Solution

If the first skier wins the first round by $\Delta T_1,$ they will prevail so long as they don't lose the second round by more than $\Delta T_1.$ 

The gap between the first round times $\left(\Delta T_1 = t^\text{A}_1 - t^\text{B}_1\right)$ which has some symmetric distribution $P(\Delta T_1).$ Since we know that person $\text{A}$ won the first round, we condition on the left side of $P$ and the expected value of $\Delta T_1$ is whatever the $25^\text{th}$ percentile of the distribution is. 

If person $\text{A}$ is to win overall, $\Delta T_1$ has to be less than or equal to $-\Delta T_2.$ The gap in the second round is a random variable from the same distribution, so the chance that $\Delta T_1 < -\Delta T_2$ (and, therefore, that player $\text{A}$ wins) is $P_2 = 1 - 0.25 = 0.75.$

### Pushing on

There are several ways to manifest the result above through calculation but none of the them yielded to generalization. An approximate attempt yielded good results for low $N$ but broke down as $N$ grew, notably resisting the stable plateauing that persists near $30\%$ for a wide range of $N.$

A simulation suggests a roughly linear decrease on log-log axes, and yields $P_{30} \approx 0.314409.$ Its overall behavior is decently approximated by $P \approx x^{-1/3}$ over a wide range:

![](/img/FE48C7B9-2B85-4CF5-AD7E-BE6190F97836.png){:width="400 px" class="image-centered"}

{:.caption}
**Fig:** plot of $\log P(\text{first round winner wins})$ vs $\log N.$

```python
def round(N):
    data = [ np.random.normal() for _ in range(N) ]
    first_win = data.index(min(data))
    for i in range(N):
        data[i] += np.random.normal()
    overall_win = data.index(min(data))
    if first_win == overall_win:
        return 1
    else:
        return 0
  
domain = range(2, 50, 2)
datapoints = [np.mean([round(N) for _ in range(100000)])  for N in domain]
```

My attempts at an approximate solution for $N=30$ got the right shape, but took too long to "turn up". Updates forthcoming if I make progress.

## 2025-11-18 Update

If the first and second heat times for racer $j$ are $f_j$ and $s_j$, and the winner goes first, then

- each $f_j$ can range from $f_1$ up to $\infty$
- each $s_j$ can range from $f_1 + s_1 - f_j$ up to $\infty$
- $f_1$ and $s_1$ can range from $-\infty$ to $\infty$

The first condition ensures that Racer $1$ wins the first round and the second condition ensures they win the second. 

Call $J(f_1,s_1)$ the probability that a racer has a first heat time worse than $f_1$ and a total race time worse than $f_1 + s_1$. Then the probability the racer who wins the first heat wins the whole race is

$$ \int\limits_{-\infty}^\infty \text{d}f_1\int\limits_{-\infty}^\infty\text{d}s_1 \mathcal{N}(f_1)\mathcal{N}(s_1)J(f_1,s_1)^{N-1}. $$

In the large $N$ limit, the integral will only have significant mass where $J(f_1, s_1),$ otherwise the $(N-1)^\text{st}$ power would decay to zero. 

This implies that $J(f_1,s_1) \approx 1 - \varepsilon(f_1, s_1).$

$\varepsilon(f_1,s_1)$, being the complement of $J$ is the probability that one of $f_1 > f_j$ and $f_1+s_1 > f_j+s_j.$ 

This the probability of either event minus the probability of both events

$$ \varepsilon(f_1,s_1) = P(f_j < f_1) + P(f_j+s_j \leq f_1+s_1) - P(f_j < f_1\,\textbf{AND}\,f_j+s_j \leq f_1+s_1). $$

In large systems, the probability of both occuring is much smaller than the probability of either, so we can approximate

$$ \varepsilon(f_1,s_1) = P(f_j < f_1) + P(f_j+s_j \leq f_1+s_1) $$

We can approximate $(1-\varepsilon)^N \approx e^{-N\varepsilon}$, so $\varepsilon$ has to be on the order $1/N$ otherwise $J^N$ will shrink exponentially to zero instead of staying finite. This means that $N\varepsilon \approx 1.$

The winner's times are going to be negative (it's a normal distribution), and as more racers participate, they'll be driven to large negative values. 

The probability that $f_j$ is less than $f_1$ is 

$$ \int\limits_{-\infty}^{f_1} \text{d}f_j\, \mathcal{N}(f_j,1) $$ 

and the probability that $f_j+s_j\leq f_1+s_1$ is 

$$\int\limits_{-\infty}^{f_1+s_1} \text{d}(f_j+s_j)\, \mathcal{N}(f_j+s_j, 2) $$

Both of these are tails of the Gaussian distribution which is estimated by $\mathcal{N}(t)\left(1/t + 1/t^3\right).$ 

Setting both equal to $1/N$ and solving for $f_1^* $ and $(f_1^*+s_1^* ) $ we get (dropping the terms logarithmic in $f_1$ and $(f_1+s_1),$ we get $f_1^* \approx -\sqrt{2\log N} $ and $f_1^*+s_1^*\approx -2\sqrt{\log N}. $ Solving for $s_1^* $ we get $s_1^*\approx -(2-\sqrt{2})\sqrt{\log N}.$

So, the probability mass will be centered around $f_1 \approx f_1^* $ and $s_1 \approx s_1^* ,$ which are both roughly on the scale $\gamma = \sqrt{2\log N}.$ We can rescale them like $f_1 = f_1^* + x/\gamma$ and $s_1 = s_1^* + y/\gamma.$

Plugging them into the integrand, we get

$$ \begin{align}
    N \exp{-\left(f_1^2 + s_{1}^{2}\right)/2} &= N \exp{-\left(\gamma^2 + 2y + y^2/gamma^2 + {s_{1}^{*}}^2 + 2ys_{1}^{*}/\gamma + y^2/\gamma^2\right)/2} \\
    \end{align}
$$

Now we can go back to $J(f_1,s_1).$

<br>
