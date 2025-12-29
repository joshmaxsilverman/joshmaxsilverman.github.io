---
layout: post
published: false
title: Javelin toss
date: 2025/12/29
subtitle: 
tags:
---

>**Question**

<!--more-->

([Fiddler on the Proof](URL))

## Solution

before we embark on calculating, let's sketch out the big picture of the approach:

- in the first level of belief, the two players want to find the value of the first roll where their expected score is the same whether they reroll or stay put.
- at the second level, S is able to learn something about J's first roll, so S should be able to be less aggressive when J's first is low, and should be more aggressive when J's first roll is high. 
- at the third level of belief, J knows exactly what thresholds S is using to trigger their rerolls and so, in turn, should be able to be less aggressive managing their reroll.

given the three thresholds we gather from that analysis (J's new threshold, and S's low and high thresholds), we can add up the probabilities of all scenarios where J is victorious. 

### Level 1: the unmolested game

in the symmetric game, each of S and J only know their own first roll plus the fact that the other player is in the same situation. this means that their strategy has to be something of the form "if my first roll $R_1$ is greater than $t$, then keep it, else reroll." the value of that threshold will be at the point where their expected probability of winning is the same whether they reroll or stay put. intuitively, below this point they will be playing too conservatively, and above this point too aggressively. 

let's take the position of player J, whose first roll we suppose is at the threshold $c,$ the probability that they win without rerolling is the probability that the other player rerolls below them. this is the chance that the first player rerolls times the probability they are less than $c$, which is just $c\times c=c^2.$

in the case where $J$ rerolls, they have two ways to win. one is if $S$ stays put because they're over the threshold and lose to $J$'s reroll, and the second is if $S$ rerolls and loses to $J$'s reroll. the first has probability $(1-c)$ and the second has probability $c\times\tfrac12.$

setting these equal, we get

$$ \begin{align}
(1-c) + \frac12 c &= c^2\\
0 &= c^2 +\frac12c - 1 &= 0
\end{align} $$

which has physical root 

$$ c = \tfrac12\left(\sqrt{5} - 1\right) \approx 0.61803399\ldots $$

### Level 2: the molested game

in the second level, $S$ understands $J$ to be playing the standard game while $S$ has secret information from their fuzzy surveillance bit. they will find out if $J$'s first roll exceeds their chosen threshold $d.$ this allows $S$ to set their threshold to $t_+$ or $t_-$ based on the value of the bit. 

before we calculate, we can anticipate some aspects of the thresholds. first of all, $d$ should be at least $c$ since $S$ believes $J$ will reroll for anything less than $c.$ second since $d \geq c$, $t_+$ should be greater than $c$ since we know $J_1$ is on average $\tfrac12(1 + c).$ finally, if we can be sure $J$ is rerolling, the ideal threshold to use is $t_- = \tfrac12$ since a reroll is expected to be $\tfrac12.$ 

first, the scenario where $S$ learns that $J_1 \leq d.$ this has four scenarios where $S$ ends up winning:

- $S$ keeps their first roll, $J$ rerolls and still loses. This means $S_1 > t_-,$ $J_1 < c,$ and $J_2 < S_1.$
- $S$ and $J$ both reroll, and $S$ wins. This means $S_1 < t_-,$ $J_1 < c,$ and $J_2 < S_2.$
- $S$ and $J$ keep their first roll and $S$ wins. This means $\max\{c,t_-\} < S_1 < 1$ and $c < J_1 < \min\{S_1, d\}.$
- $S$ rerolls and $J$ doesn't, and $S$ wins. This means $S_1 < t_-$ and $c < J_1 < \min\{S_1,d\}.$

put to integrals, this becomes

$$ P(J\,\text{wins}|c<d, J_1 < d) = 
\frac1d\left(
c\int\limits_{t_-}^1\text{d}S_1 \right) \int\limits_{0}^{S_1}\text{d}J_1 
+ ct_-\int\limits_{0}^1\text{d}S_2 \right) \int\limits_{0}^{S_2}\text{d}J_2
+ \int\limits_{\max\{c,t_-\}}^1\text{d}S_1 \right) \int\limits_{c}^{\min\{S_1,d\}}\text{d}J_1
+ t_-\int\limits_{c}^1\text{d}S_1 \right) \int\limits_{c}^{\min\{S_1,d\}}\text{d}J_2 
\right)

<br>
