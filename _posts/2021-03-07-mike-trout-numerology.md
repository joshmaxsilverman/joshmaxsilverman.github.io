---
layout: post
published: true
title: Mike Trout Numerology
date: 2021/03/07
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

Batting average is the probability that a batter gets a hit in any given at bat, i.e.

$$ \text{B.A.} = \dfrac{\text{hits}}{\text{at bats}} $$

If the player has $h$ hits on the $N$ game season, and therefore $4N$ at bats, then their batting average is

$$ \text{B.A.} = \dfrac{h}{4N} $$ 

The numerological phenomena we're interested in is the case when their batting average, rounded to the nearest thousandth, has the same digits as the number of games played. In other words, if the batting average is $x$ then we want to know if

$$ \text{round}(1000\times\dfrac{h}{4N}) = N $$

If a number rounds to $N,$ it means that it's either up to $1/2$ less than it or up to just less than $1/2$ greater than it:

$$ N - 1/2 \lt \dfrac{h}{4N} \l N + 1/2 $$

<br>
