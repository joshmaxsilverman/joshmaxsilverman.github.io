---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>Question

<!--more-->

([Fiddler on the Proof](URL))

## Solution

The rounded sum will equal the sum of the rounded numbers when the sum lands in a unit band around the number of rounded numbers.

### Setting up variables

Say we take a sum of fifty numbers and $35$ of them are in $\left(\frac12, 1\right).$ Then we can say that round has $U=35$ numbers that are rounded up, and $N-U = 15$ that are rounded down. the round of the sum would equal the sum of the rounded numbers if $\sum_j x_j$ falls between $35-\frac12$ and $35+\frac12.$

### Random walk

as we accumulate more numbers, the jaggedness of the individual unit variables dies off and the sum resembles a random walk.

if a number is rounded up then it has mean $\frac34$ and if a number is rounded down its mean is $\frac14.$ so, if we have $U$ roundups, the expected mean of the sum is 

$$ 
  \begin{align}
    \mu_U &= \frac14(N-U) + \frac34U \\
    &= \frac14N + \frac12U.
  \end{align}
$$

also, each random variable has an expected variance of 

$$
  \begin{align}
    \sigma^2_U &= \langle x - \langle x\rangle\rangle^2 \\
             &= 2\int\limits_0^{\frac12}\text{d}x\, \left(x - \frac14\right)^2 \\
             &= \frac{1}{48}
  \end{align}
$$

this means we can model the entire sum as a normal variable with mean $\mu_U$ and variance $\sigma^2_U.$

then, the probability that the roundings agree for a given $U$ is 

$$ P(\text{agree}\rvert U) = \int\limits_{U-\frac12}^{U+\frac12}\text{d}x\, \mathcal{N}_x(\mu_U, \sigma^2_U) $$

we could evaluate this, but it will bring error functions into our lives. since $\left(U-\frac12\right)$ and $\left(U+\frac12\right)$ are close, we can approximate this as simply the value of the integrand at $U$ times the interval's unit width, so:

$$ P(\text{agree}\rvert U) \approx \mathcal{N}_U(\mu, \sigma^2) $$

### Weighted average

the total probability of agreement is just the weighted average over all numbers of roundups $U$

$$ P(\text{agree}) = \int\text{d}U\, P(\text{agree}\rvert U) P(U). $$

the probability of $U$ roundups is the binomial distribution

$$ P(U) = \frac{1}{2^N}\binom{N}{U}. $$

happily, $P(U)$ is easily approximated with another normal distribution, $\mathcal{N}_U\left(\frac12 N, \frac14 N\right),$ so the probability of agreement is

$$ P(\text{agree}) = \int\limits_0^N\text{d}U\, \mathcal{N}_U\left(\mu_U, \sigma^2_U\right) \mathcal{N}_U\left(\frac12 N, \frac14 N\right), $$

which comes out to

$$ P(\text{agree}) = \sqrt{\frac{6}{\pi N}}. $$

plotting it against a simulation, we see good agreement as $N$ grows:

![](/img/2024-08-26-round-fiddler.png){:width="450 px" class="image-centered"}


<br>
