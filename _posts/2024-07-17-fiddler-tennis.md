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

From these we can form the polynomial, where we attach the probability for a score gap of $j$ to a term $s^j:$

$$ Z_\text{win} = \left(s^2 \frac{5}{16} + s^3 \frac{1}{8} + s^4 \frac{5}{16}\right) $$

Likewise, the possibilities for the score gap of a loser are $Z_\text{win}$ with $s$ mapped to $1/s:$

$$ Z_\text{lose} = \left(\frac{1}{s^2} \frac{5}{16} + \frac{1}{s^3} \frac{1}{8} + \frac{1}{s^4} \frac{5}{16}\right) $$

Playoff games are similar, except the range for the score gap goes from $7$ down to $2,$ with the same logic determining the counting:

$$
  \begin{align}
    P_g(7) &= \frac{1}{2^7} \\
    P_g(8) &= \binom{7}{1} \frac{1}{2^8} \\
    P_g(9) &= \binom{8}{2} \frac{1}{2^9} \\
    P_g(10) &= \binom{9}{3} \frac{1}{2^{10}} \\ 
    P_g(12) &= \binom{10}{5}\binom{2}{1} \frac{1}{2^{12}} \\ 
    P_g(13) &= \binom{10}{5} \frac{1}{2^{13}} \\ 
  \end{align}
$$

with similar polynomials formed from them.

### Sets




<br>

