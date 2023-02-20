---
layout: post
published: false
title: Sicilian solitaire
date: 2023/02/19
subtitle: What do you do when you have no control and no chance? 
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

this puzzle has two question. the first is, what is the probability of winning? the second is, why would anyone want to play this game?

we'll approach the first question in two ways — by a simple approximation, and by exact recursion.

### approximation

in the deck, there are $12$ cards whose positions we care about: the four $1$s, the four $2$s, and the four $3$s. because the deck is scrambled, on average, each of those cards has probability $\frac23$ to not be placed into one of its own slots.

generalizing to $s$ suits and $r$ ranks, and $c$ counts, this gives

$$ P_\text{win} = \left(1-\frac{1}{c}\right)^{sc}. $$

this is a good approximation that gets better as $r$ increases.

### recursion

we can imagine placing numbers one at a time, starting from the first slot. 

suppose we've already placed $m$ cards, still have $n_1$ $1$s, $n_2$ $2$s, and $n_3$ $3$s, haven't lost yet, and are currently on a "$1$" slot. 

this means we can remain a winner so long as we place anything but a $1$ on the present turn. we can do this by placing a $2$ (probability $n_2/(40 - m)$), a $3$ (probability $n_3/(40-m)$), or any number from $4$ to $10$ (probability $(40 - m - n_1 - n_2 - n_3)/(40 - m)$).

this gives us 

$$ P(n_1, n_2, n_3, m) = \dfrac{n_2}{40-m}P(n_1, n_2-1, n_3, m+1) + \dfrac{n_3}{40-m}P(n_1, n_2, n_3-1, m+1) + \dfrac{40-m-n_1-n_2-n_3}{40-m}P(n_1, n_2, n_3, m+1) $$

when $m\bmod 3 = 0,$ with similar relationships for the $m\bmod 3 = 1$ and $m\bmod 3 = 2$ cases.

generalizing, we get

$$ P(\vec{n}, m) = \sum_{j\neq m\,\bmod\,c} \frac{n_j}{rs - m}P(\vec{n} - \hat{e}_j, m+1) + \dfrac{rs - m -\sum_j n_j}{rs -m}P(\vec{n}, m+1) $$

with $P(0,0,0,rs) = 0$ as the base case.

with $\vec{n} = \left(n_1 = 4, n_2 = 4, n_3 = 4\right),$ we get 

$$ P(\vec{n}, 0) = \dfrac{1124550557}{135373757400} \approx 0.008307 $$

### trends

we can use the recursive result to confirm different trends.

first, as $r$ increases, $P_\text{win}$ does indeed tend toward $(1-1/c)^{sc}.$

second, the naive prediction captures the variation in $P_\text{win}$ as we increase the count $c,$ tending toward $e^{-4}\approx 0.0183.$

finally, $P_\text{win}$ plummets to zero as the number of suits $s$ increases.


<br>
