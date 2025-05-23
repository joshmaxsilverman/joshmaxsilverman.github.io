---
layout: post
published: true
title: How long is the river?
date: 2025/05/23
subtitle: 
tags:
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

after a long stretch of words, correlations with the beginning disappear and we should be equally likely to hit a space at any position. since half the words are three letters and half are four, this means that two out of every nine characters is a space, and $P(\text{space}) = 2/9.

since a new word starts each line, we are asking, what is the probability that the 13th character on a new line is a space, and the 14th character on the next line is a space, and ... until the line $j$ at which it ends, where we multiply by the probability that the (12+j)th character on that line is a letter. in other words

$$ 
\begin{align}
  P(\text{river of length }\, \ell) &= P(12+1)\cdot P(12+2)\cdot \ldots \cdot P(12+j-1)\cdot(1-P(12+j)\right) \\
  &= \left(1-P(12+j)\right)\prod\limits_{j=1}^\ell P(12+j)
\end{align}
$$

<br>
