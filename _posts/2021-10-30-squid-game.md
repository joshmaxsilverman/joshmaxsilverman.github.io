---
layout: post
published: true
title: Squid game
subtitle: How many will die crossing this entropic bridge?
source: fivethirtyeight
tags: probability counting recursion
date: 2021/10/30
theme: probability
---

>**Question**: Congratulations, you’ve made it to the fifth round of The Squiddler — a competition that takes place on a remote island. In this round, you are one of the 16 remaining competitors who must cross a bridge made up of 18 pairs of separated glass squares. 
>
>To cross the bridge, you must jump from one pair of squares to the next. However, you must choose one of the two squares in a pair to land on. Within each pair, one square is made of tempered glass, while the other is made of normal glass. If you jump onto tempered glass, all is well, and you can continue on to the next pair of squares. But if you jump onto normal glass, it will break, and you will be eliminated from the competition.
>
>You and your competitors have no knowledge of which square within each pair is made of tempered glass. The only way to figure it out is to take a leap of faith and jump onto a square. Once a pair is revealed — either when someone lands on a tempered square or a normal square — all remaining competitors take notice and will choose the tempered glass when they arrive at that pair.
>
>On average, how many of the 16 competitors will survive and make it to the next round of the competition?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-survive-squid-game-riddler/))

## Solution

In the standard problem, there are more tiles $t$ than contestants $c$.

To get a clear conceptual picture, it's better to think about the case where contestants outnumber tiles, $c > t$. 

### Conceptual argument

How many will die? contestants can die whenever a tile is reached for the first time. 

Since there are $t$ tiles, and each has $p=\frac12$ to kill, we expect $\langle d\rangle = \frac12 t$ deaths, and $\left(c-\frac12 t\right)$ survivors.

If we naively apply this to the standard case, where $t > c$, then we expect $\langle s\rangle = c - \frac12 t = 7$ survivors.

But, in the standard case, things are, in principle, a little more complicated.

### Broken symmetry

When $c > t,$ we are guaranteed at least $(c - t)$ survivors. With this floor in place, outcomes are symmetric: 

- each outcome has probability $2^{-t}$, and 
- each outcome with $(c - t + j)$ survivors is mirror to an outcome with $(c - j)$ survivors. 

For example, the case where all $t$ tiles result in a death ($c- t + 0$ survivors) is symmetric with the case where there no tiles result in a death ($c-0$ survivors).

When $t > c,$ this symmetry is broken. There are multiple ways for all $c$ contestants to die, while there is only one way for them all to live.

Despite the broken symmetry, it's not too hard to deal with, and we can do it in at least two ways: by counting and by recursion.

### Counting

When $d$ people die, it means that $d$ of $t$ tiles broke. We can distribute $d$ breaks over $t$ tiles in $\binom{t}{d}$ unique ways, and each way has probability $1/2^t.$ This means that the expected number of survivors is just

$$
\begin{align}
\langle s \rangle &= \frac{1}{2^t}\sum\limits_{d=0}^c \left(c - d\right)\binom{t}{d} \\
&= \frac{1,835,028}{2^{18}} \\
&= 7.0000762939453125
\end{align}
$$

So, even though in principle there is a broken symmetry, the spoiling cases are so unlikely (when $p=\frac12$) that we essentially get no boost over the naive prediction.

### Recursion

If we find the game at the $t^\text{th}$ tile with $d$ deaths, it means that we got to the $(t-1)^\text{th}$ tile with $d$ or $(d-1)$ deaths, so

$$
P(d,t) = \frac12 P(d-1,t-1) + \frac12 P(d, t-1)
$$

We can solve this with generating functions, or by implementing it. Doing that (and recognizing the base case $P(0,0) = 1$) gets the same result as the sum.

A third way (another recursion, based on runs of death-free tile hopping) also gets the same result. Both are [coded up here](https://colab.research.google.com/drive/1emNV-9L6_hC4Vs5ZDQtet6GqbmsT9Jmi#scrollTo=9lxqhre9biUz).


<br>
