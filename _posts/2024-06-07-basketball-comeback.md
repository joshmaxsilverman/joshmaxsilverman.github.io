---
layout: post
published: false
title: Can you make an incredible comeback?
date: 2024/06/09
subtitle: 
tags:
---

>Question

<!--more-->

([Fiddler on the Proof](URL))

## Solution

we are interested in collapses:

$$ \text{start tied} \rightarrow \text{get to 90\% chance to win} \rightarrow \text{lose} $$

the probability of winning a game is a function of the outcome of the possessions that already happened, and the number of possessions that remain. intuitively, to get a $90\%$ win probability early in the game requires a bigger lead than later in the game. 

the set of game states with $P_\text{win} \geq 90\%$ form a region in $(w,\ell)-$ space where $w$ is the number of possessions the team has won and $\ell$ is the number they've lost. the boundary of this region forms a set of boundary points $\mathcal{S}.$

<sketch of 90\% region>

if we can find the probability of arriving at each point $S_i$ in $\mathcal{S},$ $P(\text{start} \rightarrow S_i)$ and the probability to lose after getting there $P(S_i\rightarrow\text{lose})$ then we can find the overall probability of seeing a team collapse:

$$ P_\text{collapse} = \sum_i P(\text{start} \rightarrow S_i) P(S_i\rightarrow\text{lose}). $$

to avoid double counting, $$P(\text{start}\rightarrow S_i)$ should be first passage probabilities to the set $\mathcal{S}.$ in other words, it is the probability that the game reaches the state $S_i$ and that it hasn't been to another point in $\mathcal{S}$ before. were we to include second visitations, that would mean that a game could reach the $\geq 90\%$ region, then leave it, then come back, then collapse, and it would count twice toward being a collapse. 

so, we modify our equation 

$$ P_\text{collapse} = \sum_i P_\text{first passage}(\text{start} \rightarrow S_i) P(S_i\rightarrow\text{lose}). $$

we can find the first passage probability to a state $S_i \in \mathcal{S}$ by finding the unconditional probability to arrive there, and then subtract off the probability of going there by way of an earlier point $S_j \in \mathcal{S}.$ the probability of going to $S_i$ through $S_j$ is just $P_\text{first passage}(\text{start} \rightarrow S_j) P(S_j \rightarrow S_i,$ so we get the recursive relationship

$$ P_\text{first passage}(S_i) = P(\text{start}\rightarrow S_i) - \sum_{j\lt i} P_\text{first passage}(S_j)P(S_j \rightarrow S_i). $$

the base case is the number of ways to get to the first point of the boundary $S_1,$ for which the sum term is zero. 

now, to reach a state $(w,\ell)$ and end up losing, we need to finish the game with $\lfloor \frac12 N\rfloor + 1$ losses, which means that we need at least $\lfloor \frac12 N\rfloor + 1 - \ell$ losses from here on out. if we lose more, that's great, and we can lose up to $N - (w + \ell)$ additional possessions.

we can visualize the end game like so, finishing anywhere on the green segment is a win, and anything on the red a loss. 

<sketch of win condition>

if we are at point $(w,\ell)$ we need to count how many ways there are to end up on the red segment:

$$ P_\text{lose}(w,\ell) = \sum_{\ell^\prime = \lfloor \frac12 N\rfloor + 1 - \ell}^{N-(w+\ell)} P\left[(w,\ell)\rightarrow (N-(\ell+\ell^\prime), \ell+\ell^\prime)\right]. $$

now, the probability of moving from a point $(w_1,\ell_1)$ to point $(w_2,\ell_2)$ is just the number of ways to order $(w_2-w_1)$ wins and $(\ell_2-\ell_1)$ losses, times the probability of choosing any one of those orders:

$$ P((w_1,\ell_1)\rightarrow (w_2,\ell_2)) = \frac{1}{2^{w_2+\ell_2-w_1-\ell_1}}\binom{w_2+\ell_2-w_1-\ell_2}{w_2-w_1} $$



<br>
