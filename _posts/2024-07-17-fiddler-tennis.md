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

To do that, we're going to use partition functions to keep track of the probabilities of all possible outcomes for each class of event. 

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

From these we can form the partition functions, where we attach the probability for a score gap of $j$ to a term $s^j:$

$$ Z_\text{win} = 2\left(s^2 \frac{5}{16} + s^3 \frac{1}{8} + s^4 \frac{5}{16}\right) $$

Likewise, the possibilities for the score gap of a loser are $Z_\text{win}$ with $s$ mapped to $1/s:$

$$ Z_\text{lose} = 2\left(\frac{1}{s^2} \frac{5}{16} + \frac{1}{s^3} \frac{1}{8} + \frac{1}{s^4} \frac{5}{16}\right) $$

Playoff games are similar, except the range for the score gap goes from $7$ down to $2,$ with the same logic determining the counting:

$$
  \begin{align}
    P_g(7) &= \frac{1}{2^7} \\
    P_g(6) &= \binom{7}{1} \frac{1}{2^8} \\
    P_g(5) &= \binom{8}{2} \frac{1}{2^9} \\
    P_g(4) &= \binom{9}{3} \frac{1}{2^{10}} \\ 
    P_g(3) &= \binom{10}{4}\frac{1}{2^{11}} \\ 
    P_g(2) &= \frac12 - \sum_j P_g(j)
  \end{align}
$$

with similar partition functions formed from them given by $Z_\text{playoff win}.$

### Sets

A set is awarded to the first player to win $6$ games, winning by at least $2$ games. 

Keeping track of sets according to the number of games won and lost by the winner, $(w,\ell),$ this gives us sets $(6,0),(6,1),(6,2),(6,3)$ and $(6,4)$ for which there are $\binom{w+\ell-1}{\ell}$ ways to order the wins and losses.

The partition functions representing these outcomes is given by 

$$ Z_{w,\ell} = \binom{w+\ell-1}{\ell}Z_\text{win}^wZ_\text{loss}^\ell. $$

If a set gets to $(5,5)$ then it goes to a two game playoff. 

If the same player wins both games, then they win the set. This outcome has $\binom{10}{5}$ possible orders and the possible outcomes are given by

$$ \binom{10}{5} Z_\text{win}^7 Z_\text{loss}^5. $$

The other possibiltiy is that the players split the two playoff games, and the game goes into a one game playoff. The one game playoff has distinct outcomes from the regular games, so the possibilities are given by

$$ \binom{10}{5}\binom{2}{1}Z_\text{win}^6 Z_\text{loss}^6 Z_\text{playoff win}. $$

Putting this all together, the partition function for all possible winning sets is

$$ Z\text{set win} = 2\left(Z_\text{win}^6 + \binom{6}{1}Z_\text{win}^6Z_\text{loss} + \binom{7}{2}Z_\text{win}^6Z_\text{loss}^2 + \binom{8}{3}Z_\text{win}^6Z_\text{loss}^3 + \binom{9}{4}Z_\text{win}^6Z_\text{loss}^4 + \binom{10}{5} Z_\text{win}^7 Z_\text{loss}^5 + \binom{10}{5}\binom{2}{1}Z_\text{win}^6 Z_\text{loss}^6 Z_\text{playoff win}\right). $$

and $Z_\text{set loss}$ is found by replacing $s$ with $1/s$ in $Z_\text{set win}.$

### Match

With all the legwork out of the way, the match is straightforward. A match can be won by winning the first two games in a row, or by losing either of the first two sets, followed by winning the third set, so

$$ Z_\text{match win} = \frac{1}{2!}Z_\text{set win}^2 + \frac{1}{2!}Z_\text{set win}^2 Z_\text{set loss}. $$



<br>

