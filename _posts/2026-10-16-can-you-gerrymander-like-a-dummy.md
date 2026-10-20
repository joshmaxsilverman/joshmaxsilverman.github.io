---
layout: post
published: true
title: Can you gerrymander like a dummy?
date: 2026/10/20
subtitle: What are the chances you gerrymander yourself to defeat?
tags: probability optimization game-theory
source: fiddler
kind: puzzle
theme: probability
hide_from_recent: true
---

> **Question**: Fiddler Nation has an upcoming election between its two major political parties: the Suns and the Moons. You are drawing a new electoral map, and you have been tasked with [gerrymandering](https://en.wikipedia.org/wiki/Gerrymandering) on behalf of your party, the Moons. Fortunately, you know exactly how every citizen will vote in the election.
>
> Fiddler Nation has seven districts, each with an equal population. For simplicity, assume that the Moons win any district in which they receive *at least half* of the vote.
>
> What is the *smallest* total fraction of Fiddler Nation’s population needed to vote Moon such that it’s possible for the Moons to win a majority of the seven districts?
>
> **Extra Credit**: In the next election cycle you’re back at it, gerrymandering on behalf of the Moon party once more. This time, you can draw a map that results in any set of probabilities $P_1$, $P_2$, $P_3$, $P_4$, $P_5$, $P_6$, and $P_7$ that you’ll win each of the corresponding districts—subject to the constraint that the average of the probabilities is 1/2. In other words, $P_1 + P_2 + P_3 + P_4 + P_5 + P_6 + P_7 = 7/2$.
>
> The bosses of the Moon party want to go big. More specifically, they want to maximize the party’s chances of winning *at least five* of the seven districts. However, you are concerned that such a greedy attempt at gerrymandering may backfire, a phenomenon that has become known as [dummymandering](https://sites.socsci.uci.edu/~bgrofman/140%20Grofman%20and%20Brunell.%20%202005%20%20The%20Art%20of%20the%20Dummymander....pdf). When you draw a map that maximizes your chances of winning at least five districts, the probability the Moon party blows it and winds up losing a majority of the seven districts is $L_A$.
>
> Your personal preference is to simply maximize the party’s chances of winning *at least four* of the seven districts—a simple majority of them. When you draw a map that maximizes these chances, the probability the Moon party loses a majority of the seven districts is $L_B$.
>
> How much greater than $L_B$ is $L_A$?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-gerrymander-like-a-dummy))

## Solution

when we make an electoral strategy, we can choose to have a district get some Moon demographic, or to abstain. 
how should we allocate the Moon demographic across the districts that the boss decides should participate in the election?
we could give the same amount to every district, or we could give a lot to some and a little to others, or any number of schemes.

the answer is actually the simplest, that we should give the same amount to every participating district and we can prove this with the following argument.

### Equal allocation policy

suppose we are at the optimal allocation for participating districts and pick two districts, 1 and 2, to inspect. 

with the other districts held fixed, the probability of victory will have some terms where districts 1 and 2 both need to win, some where at least one of them needs to win, and some where neither needs to win.
since the other districts are constant, this will have the form

$$ P_\text{Moon} = A\cdot p_1p_2 + B\cdot \left(p_1+ p_2 - p_1p_2\right) + C $$

where $p_1 + p_2 = R$ and $R$ is 7/2 minus the sum of the probabilities for Moon to win the other districts. 
making this substitution, we get 

$$ P_\text{Moon} = A\cdot p_1(R-p_1) + B\cdot \left(R - p_1(R-p_1)\right) + C. $$

taking the derivative of this expression, we get 

$$ \frac{\text{d}}{\text{d}p_1} P_\text{Moon} = (A-B)(R-2p_1) $$

which is zero when $p_1 = \frac12R.$ 
so $P_\text{Moon}$ is maximized when $p_1$ and $p_2$ are both reset to their average.
because this is true of any two pairs of districts, the optimal arrangement is an equal division of Moon demographic among the participating districts. 

### Optimal gerrymandering strategy

if we want to maximize our chance of winning 4 or more districts, we can choose to have anywhere from 4 to 7 of the districts participating.
if we engage just 4 districts, then the probability to win at least 4 districts is simply 

$$ P_{\text{Moon},}4 = p^4 = \left(\frac{7}{2\cdot 4}\right)^4 \approx 0.5862 $$

if, instead, we engage 5 districts then the probability to win at least 4 would be $\left(\frac{7}{2\cdot 5}\right)^5 + 5\left(\frac{7}{2\cdot 5}\right)^4(1-\frac{7}{2\cdot 5}) \approx 0.5282$ which is lower than if we used 4 and it doesn't get better from there.
so, the optimal play for winning at least 4 districts is to evenly spread the Moon demographic over 4 districts and put zero in the other 3 districts.

if we're trying to win at least 5 districts, then we have to consider even distributions over $d = 5$, 6, or 7 engaged districts. 

using a maximum of $d$ engaged districts we have to compare the sums

$$ \sum_{j=5}^d \binom{d}{j}\left(\frac{7}{2d}\right)^j\left(1-\frac{7}{2d}\right)^{d-j} $$

for $d=5,6,7$ which yields $\approx 0.1681, \approx 0.2083, $ and $\approx 0.2266,$ respectively, which shows that the optimal choice to win at least 5 districts is to assign $\frac12$ demographic units to each of the 7 districts.

with half a population unit in every district, the probability of a Moon party loss is 

$$ L_A = 1 - \frac{1}{128}\left(\binom{7}{4} + \binom{7}{5} + \binom{7}{6} + \binom{7}{7}\right) = \frac12. $$

the probability that the Moon party loses with the 4 district plan is $L_B = 1-\left(7/8\right)^4 \approx 0.4138$ so the dummymander deficit is $L_A - L_B = \frac12-0.4138 \approx 0.0862$

<br>
