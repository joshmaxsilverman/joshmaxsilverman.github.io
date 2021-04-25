---
layout: post
published: true
title: Election Comeback
date: 2021/04/24
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

The trick we're interested in is for the loser on election night to go on to be the winner when all is said and done. For the case at hand, this means that, on election night, a candidate has less than $\frac12 n_1$ (half of the votes), but gets enough in the mail-ins to end up with over half of the total votes (more than $\frac12 (n_1 + n_2)$). 

$$ P(\text{less than half on election night, but majority overall}) $$

Each person's vote is independent, so the probability that candidate $A$ gets $A_i$ votes total out of a bundle of $n_i$ votes is

$$ P(A_i, n_i) = \binom{n_i}{A_i} p^{A_i} (1-p)^{n_i - A_i}. $$

The overall probability of a comeback is the sum over all possible vote totals $A_1$ and $A_2$ that satisfy the conditions we laid out above:

$$ P(\text{comeback}) = \sum_{A_1, A_2} P(A_1, n_1) \times P(A_2, n_2) $$

### Respect your limits

The greatest number of votes the election night loser can get, yet still go on to win is one less than half the votes counted on election night, ($\frac12 n_1 - 1$). Similarly, the least number of votes that a comeback candidate can get on election night is $1$ more than half the total number of votes minus all the mail-in votes ($1 + \frac12 (n_1 + n_2) - n_2).$

Given $A_1$ votes on election night, the fewest votes the comeback candidate can get in the mail-ins is $A_1$ fewer than one more than half the total votes, $(1 + \frac12 (n_1 + n_2) - A_1).$ The greatest number of votes they can get is just all of the available mail-in votes, $n_2.$

### Add 'em up

Putting this together, we have an answer for a finite voting population

$$ P(\text{comeback}) = \sum_{A_1 = 1 + \frac12(n_1 + n_2) - n_2}^{\frac12 n_1 - 1}\,\sum_{A_2 = 1 + \frac12(n_1+n_2) - A_1}^{n_2} P(A_1, n_1)\times P(A_2 n_2) $$

If, say, our population had $100$ people, then $n_1 = 80,$ $n_2 = 20,$ and 

$$ \begin{align}
P(\text{comeback}) &= \frac{24161233910133742271486959445}{633825300114114700748351602688} \\
&\approx 0.0762394
\end{align}$$

However, our population has many, many people, so this simply will not do.

### Open the gates

For small populations, we can feel the discrete nature of the vote's binomial distribution, with substantial jumps at vote totals around the mean. But, when the population gets big, the binomial distribution smooths out and closely resembles a Gaussian of the same mean and variance. We get

$$ P(A, n) = \binom{n}{A}p^A(1-p)^(n-A) \rightarrow \frac{1}{\sqrt{2\pi n p(1-p)} e^{-(A-np)^2/2np(1-p)} $$

Turning the sums into integrals, we get

$$ \int\limits_{1 + \frac12(n_1 + n_2) - n_2}^{\frac12 n_1 - 1} dA_1 \int\limits_{1 + \frac12(n_1+n_2) - A_1}^{n_2} dA_2 P(A_1,n_1)\times P(A_2,n_2) $$

<br>
