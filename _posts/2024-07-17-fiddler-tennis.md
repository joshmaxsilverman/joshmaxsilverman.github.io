---
layout: post
published: false
title: 
date: 2024/07/17
subtitle:
tags:
---

>Question

<!--more-->

([Fiddler on the Proof](URL))

## Solution

To solve this, we're going to directly build the probability distribution for the winner's score gap.

To do that, we're going to use series to keep track of the probabilities of all possible outcomes for each class of event. 

Before we start, let's summarize the $\text{game}\rightarrow\text{set}\rightarrow\text{match}$ scheme of tennis. 

At the base level we have games, which are played to $4$ (or $7$ for a special kind of playoff game) and are one by getting the balance of the points. We then have sets which are won by getting a balance of the game. Finally, we have matches which are won by getting a balance of the games. 

Games can be modeled independently of sets, sets are modeled in terms of games, and matches in terms of sets.

To start, let's figure out the probabilities of outcome for games.

### Games

A normal game is first to $4,$ while winning by at least $2.$ This means that the winner can win by either $4$ (by winning the first four games), by $3$ (by winning three of the first four, followed by winning the fifth game), or by $2$ (any of the remaining possibilities).

This means that the probability distribution for games looks like

$$ 
  \begin{align}
    P_g(4) &= \frac{1}{2^4} = \frac{1}{16} \\
    P_g(3) &= \binom{4}{1}\frac{1}{2^5} = \frac18 \\
    P_g(2) &= \frac12 - \frac{1}{2^4} - \binom{4}{1}\frac{1}{2^5} = \frac{5}{16}.
  \end{align}
$$

Playoff games are similar, except the range for the score gap goes from $7$ down to $2,$ with the same logic determining the counting:

$$
  \begin{align}
    P^*_g(7) &= \frac{1}{2^7} \\
    P^*_g(8) &= \binom{7}{1} \frac{1}{2^8} \\
    P^*_g(9) &= \binom{8}{2} \frac{1}{2^9} \\
    P^*_g(10) &= \binom{9}{3} \frac{1}{2^{10}} \\ 
    P^*_g(12) &= \binom{10}{5}\binom{2}{1} \frac{1}{2^{12}} \\ 
    P^*_g(13) &= \binom{10}{5} \frac{1}{2^{13}} \\ 
  \end{align}
$$


<br>

