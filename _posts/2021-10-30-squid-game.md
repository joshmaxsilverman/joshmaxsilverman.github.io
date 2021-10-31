---
layout: post
published: false
title: Squid Game
date: 2021/10/30
---

>**Question**:

<!--more-->

in the standard problem, there are more tiles $t$ than contestants $c$.

to get a clear conceptual picture, it's better to think about the case where contestants outnumber tiles, $c > t$. 

how many will die? contestants can die whenever a tile is reached for the first time. 

since there are $t$ tiles, and each has $p=1/2$ to kill, we expect $\langle d\rangle = \frac12\times t$ deaths, and $\left(c-\frac12 t\right)$ survivors.

if we naively apply this to the standard case, where $t > c$, then we expect $\langle s\rangle = c - \frac12 t = 7$ survivors.

but, in the standard case, things are a little more complicated.

when $c > t,$ we are guaranteed to have at least $(c - t)$ survivors. with this floor in place, the outcomes are symmetric: a. each outcome has probability $1/2^t$, and b. each outcome with $n$ survivors is mirror to the set of outcomes with $n - (c - \frac12 t)$ survivors.



([FiveThirtyEight](URL))

## Solution

<br>
