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

after a long stretch of words, correlations with the beginning disappear and we should be equally likely to hit a space at any position. since half the words are three letters and half are four, this means that two out of every nine characters is a space, and $P(\text{space}) = 2/9.$

since a new word starts each line, we are asking, what is the probability that the 13th character on a new line is a space, and the 14th character on the next line is a space, and ... until the line $j$ at which it ends, where we multiply by the probability that the (12+j)th character on that line is a letter. in other words

$$ 
\begin{align}
  P(\text{river length}=\ell) &= P(12+1)\cdot P(12+2)\cdot \ldots \cdot P(12+\ell-1)\cdot\left(1-P(12+\ell)\right) \\
  &= \left(1-P(12+\ell)\right)\prod\limits_{j=1}^{\ell-1} P(12+j)
\end{align}
$$

because every word begins after a space, and ends on a space, the probability that position $j$ is a space is the probability that position $(j-4)$ ended on a space and the next word had three letters plus the probability $(j-5)$ ended on a space and the next word had four letters. since the probability of a three or four letter word after a space is $\frac12$, this becomes

$$ P(j) = \frac12 P(j-4) +\frac12 P(j-5) $$

at this point, we could code the recursion to find $P(j)$ and then take the weighted sum 

$$ \langle \ell\rangle = \dfrac{\sum\limits_{\ell=1}^\infty \ell P(\text{river length}=\ell)}{\sum\limits_{\ell=1}^\infty  P(\text{river length}=\ell)}. $$

<br>
