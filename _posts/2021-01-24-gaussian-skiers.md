---
layout: post
published: true
title: Gaussian skiers
date: 2025/11/18
subtitle: How safe are you for winning the first heat?
tags: scaling approximation
---

>**Question**: You're in your town's head to head marble racing championship, the traditional way to determine who is the town's next mayor. The race is split into two heats and your time in either heat is a random, normally distributed variable. If you have the fastest time in the first run, what is the probability $P_\text{win it all}$ that you end up winning the event, as determined by the sum of your times on heat run?
>
>**Extra credit**: what if there are $29$ other candidates in the race?
>
>**Extra extra credit** What about $N$?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-skillfully-ski-the-slopes/))

## Solution (originally published 2021-01-24)

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

The formal solution I was trying to approximate (to no avail) almost five years ago was the following:

If the first and second heat times for racer $j$ are $f_j$ and $s_j$, and the winner goes first, then

- each $f_j$ can range from $f_1$ up to $\infty$ (all other racers are slower than the winner in heat one)
- each $s_j$ can range from $f_1 + s_1 - f_j$ up to $\infty$ (because anything faster would cause racer $j$ to win the race)
- $f_1$ and $s_1$ can range from $-\infty$ to $\infty$ (because the winner sets the constraints for the other racers)

The probability that racer $j$ meets these conditions is 

$$ J(f_1,s_j) = \int\limits_{f_1}^\infty \text{d}f_j\, \mathcal{N}(f_j) \int\limits_{f_1 + s_1 - f_j}^\infty \text{d}s_j\, \mathcal{N}(s_j). $$

The constraint on the losers is set by the times of the winner, Racer $1$, so they're independent of each other and the probability that all $(N-1)$ satisfy the constraint is just

$$ J(f_1,s_1)^{N-1}. $$

The probability that the racer who wins the first heat wins the whole race is then just

$$ N \int\limits_{-\infty}^\infty \text{d}f_1\mathcal{N}(f_1) \int\limits_{-\infty}^\infty\text{d}s_1 \mathcal{N}(s_1)J(f_1,s_1)^{N-1}. $$

We can evaluate this numerically for e.g. $N=30$ and we get $0.31471089\ldots$, which closely matches simulation.

However, it is not easy to get a formula for general $N$ because the integral $J$ depends strongly on the values of $f_1$ and $s_1$. Depending on how they're set it could be very likely, a tossup, or very unlikely for a given Racer $j$ to lose to Racer $1$. Without definite values, we can't evaluate the integral or systematically approximate it.

The crucial insight is that we actually don't have to...

Instead, we can calculate the expected value of the probability that the winner of the first heat wins the whole race. The strategy will be to find the probability that the winner of the first heat wins in terms of their first heat time, and then average this using the probability distribution of the winning first heat time.

$$ P(\text{heat 1 winner wins}) = \int\limits_{-\infty}^\infty \text{d}x\, P(\text{first heat winner wins}|x)P(\text{first heat time is }x). $$

We know two useful things about the winner
- they won the first heat
- their first heat time plus their second heat time is less than the expected minimum total time of the $(N-1)$ other racers.

To win the first heat, they need the probability of beating their first heat time $f_1$ to be less than $1/N.$

The probability that a normal variable is less than a target $v$ is 

$$ P(z < -v) = \int\limits_{-\infty}^{-v} \text{d}z\, \mathcal{N}(z), $$

which is approximated by 

$$ \mathcal{N}(v)/v. $$

The minimum should occur at the value $\gamma$ where the probability to fall short of $\gamma$ is less than $\frac1N.$ So, we can find the likely value of $f_1,$ $\gamma,$ by solving

$$ 
    \begin{align}
        \frac{\mathcal{N}(\gamma)}{\gamma} &= \frac1N \\
    \frac{e^{-\gamma^2/2}}{\sqrt{2\pi}\gamma} &= \frac1N \\
    \gamma^2/2 + \log \sqrt{2\pi}\gamma &= \log N.
    \end{align}
$$

We could solve this by iterated approximation, but to first order we can keep the dominant quadratic $\gamma$ term and find $\gamma \approx \sqrt{2\log N}.$ It isn't the most wonderful approximation, but improves as $N$ grows and is consistent with the other approximations we'll make. The plot shows the distribution of minima for samples of $N$ unit normal variables in blue and the approximation for the mean in gold for $N$ ranging from $10$ to $10^6.$

![](/img/2025-11-28-fiddler-gaussian-skier-histcol.png){:width="250 px" class="image-centered"}

$f_1$ will be peaked near $\gamma$, but vary around it. We can rewrite $f_1 = -\gamma + x$ where $x$ is assumed small compared to $\gamma.$ The total time taken is $f_1 + s_1.$ Because $f_1$ and $s_1$ are both normal variables with variance $1$, if we divide the sum by $\sqrt{2}$ it will be a normal variable as too: $(f_1+s_1)/\sqrt{2}.$ 

Racer $1$ wins if $f_1+s_1$ is less than the smallest time of the $(N-1)$ other racers. The total time for other racers is also a normal variable $t_j = (f_j+s_j)/\sqrt{2}.$ The expected minimum for this variable is found the same way we found it for $f_1,$ except with $(N-1)$ in place of $N.$ In practice, $(N-1)\approx N$ for large $N$ so the expected minimum for the other racers is $-\gamma$ too.

So, Racer $1$ will win if $(f_1+s_1)/\sqrt{2} < -\gamma$ or

$$ \frac{-\gamma + x}{\sqrt{2}} + \frac{s_1}{\sqrt{2}} < -\gamma, $$

which is equivalent to 

$$ s_1 < -\overbrace{\left(\sqrt{2}-1\right)}^{\nu}\gamma + x. $$

So, for a given value of $x,$ the probability Racer $1$ wins is $\mathcal{N}(\nu \gamma + x)/(\nu\gamma + x).$ Working this out, we get

$$
    \begin{align}
        P(\text{Racer 1 wins}|x) 
        &= \frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma+x} e^{-(\nu\gamma+x)^2/2} \\
        &= \frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma+x} e^{-(\nu^2\gamma^2 + 2\nu \gamma x + x^2)/2} \\
        &\approx \frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma} e^{-(\nu^2\gamma^2 + 2\nu \gamma x)/2} \\
        &= \frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma} \left(e^{-\gamma^2/2}\right)^{\nu^2} e^{-\nu \gamma x} \\
        &= \frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma} \left(\frac{\sqrt{2\pi}\gamma}{N}\right)^{\nu^2} e^{-\nu\gamma x}
    \end{align}
$$

We dropped the $x^2$ term in the exponent on the assumption that the probability distribution of $x$ will crush the integrand before the $x^2$ term has a big impact. This will not be true for small values of $N$ so we should expect our approximation to overestimate, and converge asymptotically from above.

Now, the probability that a single racer's first heat time is over $-\gamma + x$ is one minus the probability that they're under: $1 - \frac{\mathcal{N}(-\gamma + x)}{-\gamma + x}.$ And the probability that none of the $(N-1)$ people's first heat time is faster is $\left[1 - \frac{\mathcal{N}(-\gamma + x)}{(-\gamma + x)}\right]^{N-1}.$ 

$$
    \begin{align}
        P(\text{first heat time < }-\gamma + x) &= \frac{1}{\sqrt{2\pi}}\frac{\mathcal{N}(-\gamma + x)}{(\gamma + x)} \\
        &= \frac{1}{\sqrt{2\pi}}\frac{e^{-(-\gamma + x)^2/2}}{(\gamma + x)} \\
        &= \frac{1}{\sqrt{2\pi}}\frac{e^{-(\gamma^2 -2x\gamma + x^2)/2}}{(\gamma + x)} \\ 
        &\approx \frac{1}{\sqrt{2\pi}}\frac{e^{-(\gamma^2 -2x\gamma)/2}}{\gamma} \\
        &= \frac{\mathcal{N}(\gamma)}{\gamma}e^{\gamma x} \\
        &= e^{\gamma x}/N
    \end{align}
$$

The probability that a racer's first heat time is greater than $(-\gamma + x)$ is then $(1-e^{\gamma x}/N)$ and the probability that the minimum first heat time is greater than $(-\gamma+x)$ is $\approx(1-e^{\gamma x}/N)^N = e^{-e^{\gamma x}}.$ So, the cumulative probability that the minimum is less than $(-\gamma+x)$ is $1 - e^{-e^{\gamma x}}$ and the probability distribution that the minimum first heat time is $x$ exactly is then just 

$$ P(\text{first heat min} = x) = \frac{\text{d}}{\text{d}x} 1 - e^{-e^{\gamma x}} = \gamma e^{\gamma x} e^{-e^{\gamma x}}. $$

Putting it all together, the probability that the winner of the first heat wins the entire race is 

$$ \begin{align}
    P(\text{heat 1 winner wins}) &= \int\limits_{-\infty}^\infty \text{d}x\, P(\text{first heat winner wins}|x)P(\text{first heat time is }x) \\
    &\approx\frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma} \left(\frac{\sqrt{2\pi}\gamma}{N}\right)^{\nu^2} \int\limits_{-\infty}^{\infty} \text{d}x\,  e^{-\nu \gamma x} \gamma e^{\gamma x} e^{-e^{\gamma x}}.
\end{align}
$$

The integral has no actual $\gamma$ dependence which we can see by setting $z = e^{\gamma x}$ so that $\text{d}z = \gamma e^{\gamma x} \text{d}x = \gamma z \text{d}x$ so that the probability becomes 

$$ 
    \begin{align}
        P(\text{heat 1 winner wins}) &\approx \frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma} \left(\frac{\sqrt{2\pi}\gamma}{N}\right)^{\nu^2} \int\limits_{0}^{\infty} \text{d}z\, \frac{1}{\gamma z} \gamma z e^{-z} z^{-\nu} \\
        &\approx \frac{1}{\sqrt{2\pi}}\frac{1}{\nu\gamma} \left(\frac{\sqrt{2\pi}\gamma}{N}\right)^{\nu^2} \int\limits_{0}^{\infty} \text{d}z\, e^{-z} z^{-\nu}. 
    \end{align}
$$


The integral will get us an overall numerical factor, but already we can see how the problem will scale with $N.$ Pulling out the $N$ dependent terms from the prefactor, we have 

$$ 
    \begin{align}
        P(\text{heat 1 winner wins}) &\propto \gamma^{\nu^2-1}N^{-\nu^2} \\
        & \propto (\log N)^{1-\sqrt{2}} N^{-(3-2\sqrt{2})}. 
    \end{align}
$$

This integral is just the gamma function $\Gamma(1-\nu)$ making the final result 

$$ 
    \begin{align}
        P(\text{heat 1 winner wins}) &\approx \frac{1}{\nu}(4\pi)^\frac{\nu^1-1}{2}\Gamma(1-\nu)\left(\log N\right)^{\frac{\nu^2-1}{2}}N^{-\nu^2} \\
        &\approx (1+\sqrt{2})(4\pi)^{1-\sqrt{2}}\Gamma[2-\sqrt{2}]\left(\log N\right)^{1-\sqrt{2}} N^{-(3-2\sqrt{2})}.
    \end{align}
$$

![](/img/2025-11-28-fiddler-gaussian-skier-plot.png){:width="450 px" class="image-centered"}

As the number of racers increases the advantage of the first heat winner grows, far exceeding $1/N.$

To get more accurate predictions for small $N,$ we'd need to perturbatively develop the $e^{-x^2/2\gamma^2}$ that we dropped for the approximation, model the fluctuations in the second place racer, and use higher iteration estimates for $\gamma.$ The perturbative terms shrink with powers of $1/\log N$, so convergence is slow, but we can already see the asymptotic result (gold curve) and the simulation (blue points) converging.

## Update 2025-12-11

Let's make the improvements suggested above:
- modeling the fluctuations of the next best racer
- using the iterated approximation for the expected minimum

In our original approximation for $\gamma$

$$ 
    \begin{align}
        \frac{\mathcal{N}(\gamma)}{\gamma} &= \frac1N \\
    \frac{e^{-\gamma^2/2}}{\sqrt{2\pi}\gamma} &= \frac1N \\
    \gamma^2/2 + \log \sqrt{2\pi}\gamma &= \log N.
    \end{align}
$$

we dropped the $\log\sqrt{2\pi}\gamma$ term and solved for $\gamma$ to find $\gamma \approx \sqrt{2\log N}$ and called it a day. However, this is now a good approximation for the value of $\gamma$ which lets use replace the dropped term with a numerical approximation. 

Plugging back in in, we get the new equation

$$ \gamma^2/2 + \log \sqrt{2\pi}\sqrt{2 \log N} = \log N $$

which, solving for $\gamma$ gets us 

$$ \gamma \approx \sqrt{2} \sqrt{\log N - \log \left(2 \sqrt{\pi } \sqrt{\log N}\right)}. $$

<!-- Note that previously, the approximation $\gamma \approx \sqrt{2\log N}$ allowed us to replace $e^{-\gamma^2/2}$ with $N.$ The refined approximation means we'll have to preserve the integration. -->

Our original condition for Racer $1$ to win pegged the second best racer at constant $-\gamma,$ so we had

$$ \frac{f_1+s_1}{\sqrt{2}} < -\gamma $$

However, the minimum of the competition will fluctuate around $-\gamma$ just like Racer $1$ does. Accounting for this, we get the new condition

$$ \frac{-\gamma + x+s_1}{\sqrt{2}} < -\gamma + y $$

or

$$ s_1 \lt -\nu\gamma + \sqrt{2}y - x. $$

This makes the probability that the first heat winner wins it all, conditioned on their first heat time $-\gamma + x$ and the competitions time $-\gamma + y$ equal to

$$ P(\text{heat 1 winner wins}\rvert x, y) = f(-\nu\gamma + \sqrt{2}y - x) = \int\limits_{-\infty}^{-\nu\gamma +\sqrt{2}y - x} \text{d}z\, \mathcal{N}(z). $$

In our original calculation, we approximated this step using $f(z) \approx \mathcal{N}(z)/z,$ which was in part motivated by the fact that we could take advantage of $e^{-\gamma^2/2} \approx N.$ However, we then dropped terms in the denominator, introducing new error. And in any case, with our refined estimate for $\gamma,$ we can't make that substitution. 

We're assuming that the fluctuations around $-\gamma$ are small compared to $\gamma,$ so $\left(x - \sqrt{2}y\right)$ is small compared to $\nu\gamma.$ This means we can approximate $f(-\nu\gamma + \sqrt{2}y-x)$ in terms of $f(-\nu\gamma).$ Using the same $\mathcal{N}(z)/z$ approximation, we get

$$ f(-\nu\gamma+\sqrt{2}y -x) \approx f(-\nu\gamma) \frac{\mathcal{N}(-\nu\gamma + \sqrt{2}y - x)}{\mathcal{N}(-\nu\gamma} \frac{-\nu\gamma}{-\nu\gamma + \sqrt{2}y - x}. $$

<!-- -->
<!-- -->
<!-- -->
<!-- -->
<!-- -->




<!--
As the number of racers gets big, the exponent on $J$ will crush the product toward zero except where $J$ is close to $1.$ Any deviations from that region will be punished with increasing severity as $N$ grows.

This means that we can approximate it as one minus a small quantity that depends on $f_1$ and $s_1$ like so 

$$ J(f_1,s_1) \approx 1 - \varepsilon(f_1, s_1). $$

$J$ is the probability that a racer who is did not win heat $1$ loses so $\varepsilon(f_1,s_1)$, being the complement of $J,$ is the probability that at least one of the losing conditions is broken, i.e. $f_1 > f_j$ or $f_1+s_1 > f_j+s_j.$ 

This the probability of either event happening minus the probability of both events happening

$$ \varepsilon(f_1,s_1) = P(f_j < f_1) + P(f_j+s_j \leq f_1+s_1) - P(f_j < f_1\,\textbf{AND}\,f_j+s_j \leq f_1+s_1). $$

With many racers, the probability of both occuring is much smaller than the probability of either, so we can make the approximation

$$ \varepsilon(f_1,s_1) \approx P(f_j < f_1) + P(f_j+s_j \leq f_1+s_1). $$

Now, since $\varepsilon$ is small, $J^{N-1} = (1-\varepsilon)^{N-1} \approx e^{-N\varepsilon}.$ For $J^{N-1}$ to be close to $1,$ $\varepsilon$ has to be on the order $1/N$ otherwise $J^{N-1} \approx e^{-N\varepsilon}$ will shrink exponentially to zero instead of staying finite. This means 

$$ N\varepsilon \approx 1. $$

The probability that $f_j$ is less than $f_1$ is 

$$ P(f_j < f_1) = \int\limits_{-\infty}^{f_1} \text{d}f_j\, \mathcal{N}(f_j,1). $$ 

The probability that $f_j+s_j\leq f_1+s_1$ is 

$$ P(f_j+s_j \leq f_1+s_1) = \int\limits_{-\infty}^{f_1+s_1} \text{d}(f_j+s_j)\, \mathcal{N}(f_j+s_j, 2). $$

Here the normal distribution has variance $2$ instead of $1$ because the random variable is $(f_j + s_j)$, adding the unit variances!

With many racers, the winner's first heat time and total time are very likely going to be negative (it's a normal distribution), and as more racers participate, they'll be driven to large negative values. So, both of these probabilities are the lefthand tails of a Gaussian distribution which is estimated by 

$$ \int\limits_{-\infty}^t \text{d}t^\prime \mathcal{N}(t^\prime) \approx \mathcal{N}(t)\left(1/t + 1/t^3\right). $$ 

$J$ is appoximately the product of the complements of these probabilities, which means the complements should both be close $1$ and therefore comparable to each other. This means that these probabilities should be comparable as well. 

Setting both equal to $1/N$, we can solve for the values $f_1^{\*} $ and $(f_1^{\*} + s_1^{\*} )$ that give $J^N$ sizable mass. After dropping terms logarithmic in $f_1$ and $(f_1+s_1)),$ we get $f_1^{\*} \approx -\sqrt{2\log N} $ and $f_1^{\*} + s_1^{\*} \approx -2\sqrt{\log N}. $ Solving for $s_1^{\*}$ we get $s_1^{\*} \approx -(2-\sqrt{2})\sqrt{\log N}.$

So, the probability mass will be centered around $f_1 \approx f_1^{\*} $ and $s_1 \approx s_1^\* ,$ with small deviations on either side. Both are roughly on the scale $\gamma = \sqrt{2\log N},$ so we can rescale the deviations like $f_1 = f_1^\* + x/\gamma$ and $s_1 = s_1^\* + y/\gamma.$


Now we can plug in to the exponent $\varepsilon(f_1,s_1).$

$$
\begin{align}
        \varepsilon(f_1,s_1) &\approx -\frac{1}{\sqrt{2\pi}}e^{-\left(f_1^\ast + x/\gamma\right)^2/2}\left[\frac{1}{f_1} + \frac{1}{f_1^3}\right] + \frac{1}{\sqrt{2\pi}}e^{-(f_1^\ast+s_1^\ast + x/\gamma + y/\gamma)^2/4}\left[\frac{\sqrt{2}}{f_1+s_1} + \frac{2\sqrt{2}}{(f_1+s_1)^3}\right] \\
        &\approx -\frac{1}{\sqrt{2\pi}}e^{-(\gamma^2 - 2x)/2}\left[\frac{1}{f_1} + \frac{1}{f_1^3}\right] + \frac{1}{\sqrt{2\pi}}e^{-(4\log N -2\sqrt{2} (x+y))/4}\left[\frac{\sqrt{2}}{f_1+s_1} + \frac{2\sqrt{2}}{(f_1+s_1)^3}\right] \\
        &= -\frac{1}{N\sqrt{2\pi}}e^{x}\left[\frac{1}{f_1} + \frac{1}{f_1^3}\right] + \frac{1}{N\sqrt{2\pi}}e^{(x+y)/\sqrt{2}}\left[\frac{\sqrt{2}}{f_1+s_1} + \frac{2\sqrt{2}}{(f_1+s_1)^3}\right] \\
        &\approx -\frac{1}{N\sqrt{2\pi}}e^{x}\left[\frac{1}{-\gamma} + \frac{1}{-\gamma^3}\right] + \frac{1}{N\sqrt{2\pi}}e^{(x+y)/\sqrt{2}}\left[\frac{1}{-\gamma} + \frac{1}{-\gamma^3}\right] \\
        &= \frac{1}{N\sqrt{2\pi}}\left(e^{x} + e^{(x+y)/\sqrt{2}}\right)\left(\frac{1}{\gamma} + \frac{1}{\gamma^3}\right)
\end{align}
$$


Plugging these into the $N\mathcal{N}(f_1)\mathcal{N}(s_1)$ part of the integrand, we get

$$
    \begin{align}
    \frac{1}{2\pi}N \exp{-\left(f_1^2 + s_{1}^{2}\right)/2} &= N \exp{-\left(\gamma^2 + 2x + x^2/\gamma^2 + {s_{1}^{\*}}^2 + 2ys_{1}^{\*}/\gamma + y^2/\gamma^2\right)/2} \\
    &\approx \frac{1}{2\pi}N \exp{-\left(2\log N - 2x + (6-2\sqrt{2})\log N - 2y (2-2\sqrt{2})\sqrt{\log N}/\sqrt{2\log N} + O(1/\gamma^2)\right)/2} \\
    &= \frac{1}{2\pi}N N^{-(4-2\sqrt{2})} \exp\left(x + y(\sqrt{2}-1)\right) \\
    &= \frac{1}{2\pi}N^{-(3-2\sqrt{2})} e^{x + y(\sqrt{2}-1)}
    \end{align}
$$

Putting these results together, and writing $\eta = 3-2\sqrt{2},$ the integrand becomes

$$ 
    \begin{align}
        \text{int} &= \frac{1}{\left(2\pi\right)^{3/2}} N^{-\eta} e^{x + \left(\sqrt{2}-1\right)y} \exp{- N \varepsilon(x,y)} \frac{\text{d}x\,\text{d}y}{\gamma^2} \\
        &= \frac{1}{\left(2\pi\right)^{3/2}} N^{-\eta} e^{x + \left(\sqrt{2}-1\right)y} \exp\left[{-\frac{1}{\sqrt{2\pi}}\left(e^{x} + e^{(x+y)/\sqrt{2}}\right)\left(\frac{1}{\gamma} + \frac{1}{\gamma^3}\right)}\right] \frac{\text{d}x\,\text{d}y}{\gamma^2}
    \end{align}
$$

The integral is over $x$ and $y$ which we can perform however is easiest. One nice way is to tilt $y$ so that the exponents $x$ and $(x+y)/\sqrt{2}$ become equal apart from a perturbation $h.$ In other words pick $y$ so that $(x+(y-h))/\sqrt{2} = x$ or $y = (\sqrt{2}-1)x + h.$ 

Plugging this in, and expanding in $h,$ the exponent in the second exponential becomes

$$ -\frac{1}{\sqrt{2\pi}}\left(e^{x} + e^{x + h/\sqrt{2}}\right)\left(\frac{1}{\gamma} + \frac{1}{\gamma^3}\right) \approx -\frac{e^x}{\sqrt{2\pi}}\left(2 + \frac{h}{\sqrt{2}} + \frac{h^2}{4}\right)\left(\frac{1}{\gamma} + \frac{1}{\gamma^3}\right). $$

Likewise, the first exponential becomes

$$ e^{x + \left(\sqrt{2}-1\right)y} = e^{x(1+(\sqrt{2}-1)^2) + (\sqrt{2}-1)h} = e^{Ax + Bh}. $$

Putting these altogether, the integrand is now

$$ \begin{align}
    &= \exp\left[Ax + Bh -\frac{e^x}{\sqrt{2\pi}}\left(2 + \frac{h}{\sqrt{2}} + \frac{h^2}{4}\right)\overbrace{\left(\frac{1}{\gamma} + \frac{1}{\gamma^3}\right)}^\Delta\right] \\
    &= \exp\left[\overbrace{\left(Ax - 2\frac{\Delta e^x}{\sqrt{2\pi}}\right)}^\theta + \overbrace{\left(B -\frac{\Delta e^x}{2\sqrt{\pi}}\right)}^\beta h -\overbrace{\frac{\Delta e^x}{\sqrt{2\pi}}}^\alpha h^2  \right]. \\
    &= \exp\theta \exp\left[-\alpha h^2 + \beta h\right] \\
    &= \exp\theta \exp\left[-\alpha \left(h^2 - \frac{\beta}{\alpha} h\right)\right] \\
    &= \exp\theta \exp\left[-\alpha \left(h - \frac12\frac{\beta}{\alpha}\right)^2 + \frac{\beta^2}{4\alpha}\right] \\
    &= e^{\theta + \beta^2/4\alpha} e^{-\alpha\left(h-\beta/2\alpha\right)^2}
\end{align}$$

The exponential in $h$ is now a simple Gaussian, so integrating over all $h$, we just get

$$ e^{\theta + \beta^2/4\alpha} \sqrt{\frac{\pi}{\alpha}}. $$

Now we have to do the integral over $x.$ Putting together all our pieces, we have 

$$ P = \frac{1}{\gamma^2}\frac{N^{-\eta}}{\left(2\pi\right)^{3/2}} \int \text{d}x\, e^{\theta + \beta^2/4\alpha} \sqrt{\frac{\pi}{\alpha}}. $$

What we ultimately want to know is how this integral scales in terms of the number of racers $N.$ If we keep all the terms in $\alpha$ and $\beta$ when we perform the integral, we would get not just this scaling form, but the numerical value of the coefficients on the terms. -->
 
<br>
