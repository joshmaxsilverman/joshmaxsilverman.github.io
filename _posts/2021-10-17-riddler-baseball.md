---
layout: post
published: true
title: Free Pete Rose
date: 2021/10/18
---

>**Question:** 

<!--more-->

([FiveThirtyEight](URL))

## Solution

The best thing to do is whatever we expect the best thing to do is.

After each game, we have the opportunity to play our best, so long as we're not in a hopeless position.

Hopeless positions are exactly those that we have no chance to win from. In other words, if we're in a position where A or B have won more than half the games but we still have less than 2 correct guesses logged.

 

$$
S(\text{less than 2 correct guesses}, \text{4 games won by a team}) = 0.
$$

If we're not in a hopeless position, then we have a choice to bet on A or B in the next game.

If we currently have $c$ correct guesses, and we bet on A, we could guess right or wrong, so our expected value is 

$$
\frac12 \overbrace{\langle S(c, \text{game : B})\rangle}^\text{we bet wrong} + \frac12 \overbrace{\langle S(c + 1, \text{game : A})\rangle}^\text{we bet right}
$$

On the other hand, we could bet B, which is worth

$$
\frac12 \overbrace{\langle S(c, \text{game : A})\rangle}^\text{we bet wrong} + \frac12 \overbrace{\langle S(c + 1, \text{game : B})\rangle}^\text{we bet right}
$$

We should choose the best of these two options.

So, the expectation that we make at least two successful predictions follows the recursion relation:

$$\begin{align}
\langle S(c,\text{game})\rangle = \max \{ &\frac12 \langle S(c, \text{game : A})\rangle + \frac12 \langle S(c + 1, \text{game : B})\rangle, \\
&\frac12 \langle S(c, \text{game : B})\rangle + \frac12 \langle S(c + 1, \text{game : A})\rangle
\}
\end{align}$$



<br>
