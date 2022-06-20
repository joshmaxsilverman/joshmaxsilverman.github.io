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

we want to look at the variation in the probability that there are $2S$ balls in the urn given that $8$ red balls, and $11$ blue balls were drawn.

using bayes rule, we can write $P(2S\text{ and }\color{red}{8}\color{black}{,}\color{blue}{11})$ two different ways:

$$
  P(2S\rvert\color{red}{8}\color{black}{,}\color{blue}{11}\color{black}) = \frac{P(\color{red}{8}\color{black}{,}\color{blue}{11}\color{black}\rvert 2S)}{P(\color{red}{8}\color{black}{,}\color{blue}{11}\color{black})}P(2S)
$$

the denominator is the same for all values of $S,$ so we can forget about it.

we don't have any evidence about the number of balls beyond the balls we've drawn. so, to ensure we're unbiased, we use a uniform prior distribution $P(T) = \limit_{M\rightarrow\infty}\sum_{i=11}\dfrac{\delta(T-i)}{M}.$ by design, this is uniform in $T$ and we can ignore it as well.

this tell us that 

$$
  P(2S\rvert\color{red}{8}\color{black}{,}\color{blue}{11}\color{black}) = P(\color{red}{8}\color{black}{,}\color{blue}{11}\color{black}\rvert 2S)
$$

the right side is easily computed. there are $\binom{S}{8}\binom{S}{11}$ ways to draw $8$ red balls and $11$ blue balls, and there are $\binom{2S}{19}$ ways to draw any $19$ balls, so:

$$
  P(2S\rvert\color{red}{8}\color{black}{,}\color{blue}{11}\color{black}) \sim \dfrac{\binom{S}{8}\binom{S}{11}}{\binom{2S}{19}}
$$

plotting this as a function of $S,$ we see that it's maximized at $S=17,$ which corresponds ton $34$ total balls in the urn.

great.

<br>
