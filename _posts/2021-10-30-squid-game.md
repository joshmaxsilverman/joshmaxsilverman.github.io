---
layout: post
published: false
title: Squid Game
date: 2021/10/30
---

>**Question**:

<!--more-->

([FiveThirtyEight](URL))

## Solution

in the standard problem, there are more tiles $t$ than contestants $c$.

to get a clear conceptual picture, it's better to think about the case where contestants outnumber tiles, $c > t$. 

### conceptual argument

how many will die? contestants can die whenever a tile is reached for the first time. 

since there are $t$ tiles, and each has $p=\frac12$ to kill, we expect $\langle d\rangle = \frac12 t$ deaths, and $\left(c-\frac12 t\right)$ survivors.

if we naively apply this to the standard case, where $t > c$, then we expect $\langle s\rangle = c - \frac12 t = 7$ survivors.

but, in the standard case, things are, in principle, a little more complicated.

### broken symmetry

when $c > t,$ we are guaranteed at least $(c - t)$ survivors. with this floor in place, outcomes are symmetric: 

a. each outcome has probability $2^{-t}$, and 
b. each outcome with $(c - t + j)$ survivors is mirror to an outcome with $(c - j)$ survivors. 

For example, the case where all $t$ tiles result in a death ($c- t + 0$ survivors) is symmetric with the case where there no tiles result in a death ($c-0$ survivors).

when $t > c,$ this symmetry is broken. there are multiple ways for all $c$ contestants to die, while there is only one way for them all to live.

despite the broken symmetry, it's not too hard to deal with, and we can do it in at least two ways: by counting and by recursion.

### counting

when $d$ people die, it means that $d$ of $t$ tiles broke. we can distribute $d$ breaks in $\binom{t}{d}$ unique ways, and each way has probability $1/2^t.$ this means that the expected number of survivors is just

$$
\begin{align}
\langle s \rangle &= \frac{1}{2^t}\sum\limits_{d=0}^c \left(c - d\right)\binom{t}{d} \\
&= \frac{458,757}{2^{18}} \\
&= 7.0000762939453125
\end{align}
$$

though in principle there is a broken symmetry, the spoling cases are so unlikely (when $p=\frac12$), we essentially get no boost over the naive prediction.

### recursion

if we find the game at the $t^\text{th}$ tile with $d$ deaths, then it means we were just at the $(t-1)^\text{th}$ tile with $d$ or $(d-1)$ deaths, so

$$
P(d,t) = \frac12 P(d-1,t-1) + \frac12 P(d, t-1)
$$

we can solve this with generating functions, or by implementing it. doing that (and recognizing the base case $P(0,0) = 1$) gets the same result as the sum.

a third way (another recursion, based on runs of death-free tile hopping) allows us to extend to the case where $p\neq\frac12$ (as does the above sum). both are [coded up here](https://colab.research.google.com/drive/1emNV-9L6_hC4Vs5ZDQtet6GqbmsT9Jmi#scrollTo=9lxqhre9biUz).


<br>
