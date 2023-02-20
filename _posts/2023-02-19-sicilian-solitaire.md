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

$$ P_\text{win} = \left(\frac{c}{1+c}\right)^{sc}. $$

### recursion

sss


<br>
