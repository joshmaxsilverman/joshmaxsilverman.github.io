---
layout: post
published: true
title: How lucky can a baseball team get?
date: 2026/08/09
subtitle: When every team is the same, how best is the best?
tags: approximation expectation variance
hide_from_recent: false
---

>**Question:** The Fiddler Baseball League consists of exactly two teams of equal skill: the Algebraists and the Geometers. Over the course of a season, these two teams play each other 162 times. Each team has an equal chance of winning each game, and the results of games are independent of one another.
>
>At the end of the season, on average, how many games would you expect the team with the better record to have won? (If the teams have the same record, then you should include one of them in your calculation.)
>
>**Extra credit:**
>After some expansion, the Fiddler Baseball League now boasts 30 teams. Over the course of a season, each team plays each other team five times. (Thus, each team plays a total of 145 games.) As before, each team has an equal chance of winning each game, and the results of games are independent of one another.
>
>At the end of the season, on average, how many games would you expect the team with the best record to have won? (If more than one team has the same best record, then you should include one of them in your calculation.)

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/how-lucky-can-a-baseball-team-get))

## Solution

Though the games are discrete events, each team plays enough that their distribution is pretty well approximated by the continuous counterpart. The plan is to 

- approximate the win total for each team by the normal distribution with matching mean and variance
- find the probability that all but one win total is less than $y$
- find the average of $y$

In doing this, we'll run into a nasty integrals of CDFs raised to high powers that we'll get around through approximation.

### Normalized teams

Each team plays $G = 145$ games and has probability $p = \tfrac12$ to win each one. This means that the expected numbers of wins is $\mu = \tfrac12\cdot G = 72.5$ and the variance is $\sigma^2 = Gp(1-p) = \tfrac14 \cdot 145 = 36.25.$ Since the number of games is large, we can approximate the distribution as a binomial with the same mean and variance $\phi(y) = \mathcal{N}(y\rvert \mu, \sigma).$

So, we can write the number of wins as the mean $\mu$ plus a random normal variable $y_i$ times the width of the distribution

$$ w_i = \mu + \sigma y_i, $$

and the expected maximum win count as

$$ \max_i w_i = \mu + \sigma \max_i y_i. $$

This means we'll be thinking about the maximum surplus relative to the mean, rather than the maximum win count itself, though they both correspond to the same thing.

### Expected maximum

The probability distribution of the maximum surplus $y$ is the probability that $(N-1)$ of the teams win less than the realized maximum surplus times the probability that the maximum surplus has value $y$ times $N$ since there are $N$ possible winners.

That is 

$$ P(\max_i y_i = y) = N\left[\int_{-\infty}^y \text{d}y^\prime \phi(y^\prime)\right]^{N-1} \phi(y) \, \text{d}y. $$

For ease of writing, we will call the bracketed integral $\Phi(y).$

So, the expected maximum surplus is

$$ y_\text{max} = N\int_{-\infty}^\infty \text{d}y\,  \Phi(y)^{N-1}\phi(y) y, $$

and the expected maximum win count is

$$ w_\text{max} = \mu + \sigma\cdot y_\text{max}. $$

We can evaluate the integral numerically but, before we do, we have to correct for the difference between the variance for the non-independent baseball league and our approximation by normal variables whose collective mean is free to vary. 

### Variance correction

The variance for the win total of a team is $\langle\left(w_i - \overline{w}\right)^2\rangle.$ In the real league, $\overline{w}$ is a constant because every game won by some team is lost by another. But in the normal variables, there is no such constraint. This means that there is correlation between the mean and the variables. Writing out the mean, we can see 

$$ \overline{y} = \frac{y_i + (N-1)y_j}{N}, $$

where $y_j$ is a shorthand for the $(N-1)$ variables for the other teams. The variance for the normal variables is 

$$
	\begin{align}
		\langle \left(y_i - \overline{y}\right)^2\rangle &= \langle y_i^2\rangle + \langle \overline{y}^2\rangle - 2\langle y_i\cdot \overline{y}\rangle
	\end{align}
$$

The expectation $\langle y_i^2\rangle$ is just $1$ since it is a normal variable. $\langle \overline{y}^2\rangle$ is $\langle \frac1{N^2}\left(\sum_k y_k\right)^2\rangle = \frac1{N^2}\cdot N = 1/N.$ The expectation $\langle y_i \overline{y}\rangle$ is just $1/N$ since $y_i$ is only correlated with itself and none of the other $y_j.$ This means that

$$ 
	\begin{align}
		\sigma^2 &= \langle \left(y_i - \overline{y}\right)^2\rangle \\
		&= 1 - 2/N + 1/N \\
		&= 1 - 1/N \\
		&= (N-1)/N. 
	\end{align}
$$

So, the variance of the simulated league $\sigma^2$ is not $1$ but instead the slightly supressed $(N-1)/N.$ To correct for this, we boost the variance used in $\Phi$ and $\phi$ from $1$ to $\sqrt{\tfrac{N}{N-1}}.$ In order to avoid carrying around a factor of $1/\sigma^2 = \tfrac{N-1}{N}$ around, we can make a change of variables to $z = \sqrt{\tfrac{N-1}{N}} y,$ which makes $\text{d}y = \sqrt{\tfrac{N}{N-1}}\text{d}z.$

This makes the expected maximum win count 

$$ w_\text{max} = \mu + \sqrt{\tfrac{N}{N-1}}\sigma \cdot y_\text{max}, $$

where the integral for $y_\text{max}$ is performed with standard issue normal variables (zero mean, and unit variance). We can now evaluate the integral numerically

```python
import numpy as np
import scipy as sp

N = 30

def integrand(z):
    return np.sqrt(N/(N-1)) * N * (0.5 * (1 + sp.special.erf(z / np.sqrt(2))))**(N-1) * sp.stats.norm.pdf(z) * z

y_max, _ = sp.integrate.quad(integrand, -np.inf, np.inf)
w_max = mu + sigma * expected_z_max

```

which comes out to $\langle w_\text{max} \rangle \approx 85.009.$ Running a $100,000$ game simulation, we get $\approx 84.96$

### Analytic approximation

Let's see if we can make an analytic approximation for the $y_\text{max}.$

$$ y_\text{max} = N\int_{-\infty}^\infty \text{d}y\,  \Phi(y)^{N-1}\phi(y) y. $$

First of all, $\phi(y)$ is the derivative of $\Phi(y)$ so we can rewrite this as

$$ y_\text{max} = \int_{-\infty}^\infty \text{d}y\,  \frac{\text{d}}{\text{d}y}\Phi(y)^N y. $$

The large power $(N-1)$ in the integral means that any values of $\Phi(y)$ that aren't close to $1$ are going to be squashed. So, only values of $y$ for which $\Phi(y)$ is close to $1$ will make significant contribution to the average. Because $\Phi(y)$ is close to $1,$ $1-\Phi(y) = \overline{\Phi}(y)$ will be close to zero. After making this substitution, we get

$$ 
	\begin{align}
		\Phi(y)^N &= \left(1- \overline{\Phi}(y)\right)^N \\
		&= \left(1- \frac{N\overline{\Phi}(y)}{N}\right)^N \\
		&\approx e^{-N\overline{\Phi}(y)}
	\end{align}
$$

Now the real issue is that $\overline{\Phi}(y)$ is hard to integrate, so we need a way to approximate it. A simple way would be to make a linear approximation. But if we did that $\overline{\Phi}$ would blow up to well outside of the natural range of $0$ to $1,$ making the approximation go haywire. A better option is to linearly approximate the log of $\overline{\Phi}(y).$ That way, the approximation continues to vary from $0$ to $N$ like the real $\overline{\Phi}(y).$

$$ 
	\begin{align}
		\log \overline{\Phi}(y) &\approx \overline{\Phi}(y_0) + (y-y_0)\frac{\text{d}}{\text{d}y}\log\overline{\Phi}(y)\bigg\rvert_{y=y_0} \\
		&\approx \overline{\Phi}(y_0) + (y-y_0)\frac{-\phi(y_0)}{\overline{\Phi}(y_0)}
	\end{align}
$$

Now we have to choose where to anchor $y_0$ for the approximation. The distribution $\Phi(y)^{N-1}\phi(y)$ should peak near $\Phi(y) \approx 1 - 1/N$ since, with $N$ variables, there should be less than a $1/N$ chance for a variable $y$ to exceed $y_\text{max}.$ So, we can anchor the expansion at the point $y_0$ where $\overline{\Phi}(y_0) = 1/N$ and

$$ \log\overline{\Phi}(y) \approx \log\frac1N - N\phi(y_0)\cdot(y-y_0), $$

or

$$ \overline{\Phi}(y) \approx \frac1N e^{- N\phi(y_0)\cdot(y-y_0)}. $$

Plugging this back in to the integral, we get

$$ y_\text{max} = \int_{-\infty}^\infty \text{d}y\,  \frac{\text{d}}{\text{d}y} e^{-e^{- N\phi(y_0)\cdot(y-y_0)}} y. $$

Changing variables to $z = N\phi(y_0)\cdot(y-y_0)$ so that $\text{d}z = N\phi(y_0)\text{d}y$ and $y = \frac{z}{N\phi(y_0)} + y_0,$ we get

$$ 
	\begin{align} 
		y_\text{max} &= \int_{-\infty}^\infty \text{d}y\,  \left(\frac{z}{N\phi(y_0)} + y_0\right) \frac{\text{d}z}{\text{d}y}\frac{\text{d}}{\text{d}z} e^{-e^{-z}} \\ 
		&= \int_{-\infty}^\infty \text{d}z\,  \left(\frac{z}{N\phi(y_0)} + y_0\right) \frac{\text{d}}{\text{d}z} e^{-e^{-z}} \\
		&= \frac{z}{N\phi(y_0)}\int_{-\infty}^\infty \text{d}z\,  z \frac{\text{d}}{\text{d}z} e^{-e^{-z}} + y_0\int_{-\infty}^\infty \text{d}z\, \frac{\text{d}}{\text{d}z} e^{-e^{-z}}
	\end{align} 
$$

The second term just becomes $y_0$ and the first becomes 

$$ \frac{1}{N\phi(y_0)} \int_{-\infty}^\infty \text{d}z\, z e^{-z}e^{-e^{-z}}. $$

which is $\gamma/(N\phi(y_0)) $ where $\gamma$ is the Euler-Mascheroni constant, so

$$ y_\text{max} = y_0 + \frac{\gamma}{N\phi(y_0)}. $$

We picked $y_0$ to that $\Phi(y_0) = 1-1/N$ so $y_0 = \Phi^{-1}(1-1/N).$ For the case of $N = 30$ this gets $\langle w_\text{max}\rangle \approx 85.32,$ which is within $0.4\%$ of the simulated answer. 

To see how the winner stands out from the crowd as the number of teams grows, holding to the pattern that each team plays $5$ games against each other team, so that $G=5(N-1),$ we can plot the result as a winning percentage along with a $500,000$ trial simulation and the numerical integral. We see excellent agreement as the number of teams grows.

We also see that, somewhat counterintuitively, the best team gets worse and worse as the competition intensifies. Even though there are more oponents to overcome, the crushing regularity of a large number of coin flips means that all teams are stuck close to the mean. As the number of teams grows toward infinity, the expected maximum decays toward $50\%.$

![](/img/2026-08-09-fiddler-baseball-theory-sim.png){:width="450 px" class="image-centered"}

If, instead, we scale the number of teams, but hold the number of games played constant at $145$ we do indeed see the winning teams win total grow with $N$ though rather slowly. Also, the fidelity of the normal approximation no longer increases with scale since that is tied to the number of games.

![](/img/2026-08-09-fiddler-baseball-theory-sim-constant-games.png){:width="728 px" class="image-centered"}

<br>
