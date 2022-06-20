---
layout: post
published: false
title: How many balls do I have?
date: 2022/06/19
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

we want to gauge the probability that there are $2S$ balls in the urn given that $8$ red balls, and $11$ blue balls were drawn.

using bayes rule, we can write $P(2S\text{ and }\color{red}{8}\color{black}{,}\color{blue}{11})$ two different ways:

$$
  P(2S\rvert\color{red}{8}\color{black}{,}\color{blue}{11}) = \frac{P(\color{red}{8}\color{black}{,}\color{blue}{11}\rvert 2S)}{P(\color{red}{8}\color{black}{,}\color{blue}{11})}P(2S)
$$

<br>
