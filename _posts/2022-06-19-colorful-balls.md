---
layout: post
published: true
title: Colorful balls
subtitle: How many do they have?
tags: counting inference
date: 2022/06/19
---

>**Question:** You have an urn with an equal number of red balls and white balls, but you have no information about what that number might be. You draw 19 balls at random, without replacement, and you get eight red balls and 11 white balls. What is your best guess for the original number of balls (red and white) in the urn?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-switch-a-digit/))

## Solution

In this problem, we are urn detectives. We want to look at the probability that there are $2S$ balls in the urn given that we drew $8$ red balls, and $11$ blue balls, and eyeball the maximum.

Using Bayes' rule, we can write $P(2S\text{ and }{\color{red}8},{\color{blue}11})$ two different ways:

$$
  P(2S\rvert{\color{red}8},{\color{blue}11}) = \frac{P({\color{red}8},{\color{blue}11}\rvert 2S)}{P({\color{red}8},{\color{blue}11})}P(2S).
$$

The denominator is the same for all values of $S,$ so we can forget about it.

We don't have any evidence about the number of balls beyond the balls we've drawn. So, to ensure we're unbiased, we use a uniform prior distribution with Dirac spikes at each possible value

$$
  P(2T) = \lim_{M\rightarrow\infty}\frac1M\sum_{i=11}\delta(2T-i).
$$ 

By design, this is uniform in $T$ and we can ignore it as well.

This tells us that 

$$
  P(2S\rvert{\color{red}8},{\color{blue}11}) = P({\color{red}8},{\color{blue}11}\rvert 2S)
$$

The right side can be gotten by counting: there are $\binom{S}{8}\binom{S}{11}$ ways to draw $8$ red balls and $11$ blue balls, and there are $\binom{2S}{19}$ ways to draw any $19$ balls, so:

$$
  P(2S\rvert{\color{red}8},{\color{blue}11}) \sim \dfrac{\binom{S}{8}\binom{S}{11}}{\binom{2S}{19}}
$$

Plotting this as a function of $S,$ we see that it's maximized at $S=17,$ which corresponds to $2S = 34$ total balls in the urn.

![](/img/2022-06-19-colorful-balls.png){:width="400 px" class="image-centered"}

That's just great. 

<br>