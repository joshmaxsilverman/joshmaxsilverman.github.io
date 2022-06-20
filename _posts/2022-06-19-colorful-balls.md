---
layout: post
published: false
title: How many balls do they have?
date: 2022/06/19
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

in this problem, we are urn detectives. we want to look at the probability that there are $2S$ balls in the urn given that $8$ red balls, and $11$ blue balls were drawn, and find the maximum.

using bayes' rule, we can write $P(2S\text{ and }{\color{red}8},{\color{blue}11})$ two different ways:

$$
  P(2S\rvert{\color{red}8},{\color{blue}11}) = \frac{P({\color{red}8},{\color{blue}11}\rvert 2S)}{P({\color{red}8},{\color{blue}11})}P(2S)
$$

the denominator is the same for all values of $S,$ so we can forget about it.

we don't have any evidence about the number of balls beyond the balls we've drawn. so, to ensure we're unbiased, we use a uniform prior distribution 

$$
  P(T) = \lim_{M\rightarrow\infty}\sum_{i=11}\dfrac{\delta(T-i)}{M}.
$$ 

by design, this is uniform in $T$ and we can ignore it as well.

this tell us that 

$$
  P(2S\rvert{\color{red}8},{\color{blue}11}) = P({\color{red}8},{\color{blue}11}\rvert 2S)
$$

the right side can be gotten by counting: there are $\binom{S}{8}\cdot\binom{S}{11}$ ways to draw $8$ red balls and $11$ blue balls, and there are $\binom{2S}{19}$ ways to draw any $19$ balls, so:

$$
  P(2S\rvert{\color{red}8},{\color{blue}11}) \sim \dfrac{\binom{S}{8}\binom{S}{11}}{\binom{2S}{19}}
$$

plotting this as a function of $S,$ we see that it's maximized at $S=17,$ which corresponds to $34$ total balls in the urn.

that's just great. 

<br>
