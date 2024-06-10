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

the set of game states with $P_\text{win} \geq 90\%$ form a region in $(w,\ell)-$space where $w$ is the number of possessions the team has won and $\ell$ is the number they've lost. the boundary of this region forms a set of boundary points $\mathcal{S}.$

if we can find the probability of arriving at each point $S_i$ in $\mathcal{S},$ $P(\text{start} \rightarrow S_i)$ and the probability to lose after getting there $P(S_i\rightarrow\text{lose})$ then we can find the overall probability of seeing a team collapse:

$$ P_\text{collapse} = \sum_i P(\text{start} \rightarrow S_i) P(S_i\rightarrow\text{lose}). $$

<br>
