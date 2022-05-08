---
layout: post
published: true
title: Broken Elevator
date: 2022/05/07
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

to avoid finicky bookkeeping, we're going to count the lobby as floor zero, instead of floor $1$. 

when the passenger presses the button from floor $k,$ the elevator is equally likely to end up at any floor under it. 

so, they have uniform probability $1/k$ to arrive at any of the floors, which can be the lobby in one press, or else any of the $(k-1)$ floors above the lobby from which they will make an average of $\langle B_{k-1}\rangle$ more presses.

so 

$$
  \langle B_k\rangle = \dfrac1k + \dfrac1k\sum_{j=1}^{k-1}\left(1 + \langle B_j\rangle\right)
$$

but the second term is just $\langle B_{k-1}\rangle:$

$$
  \begin{align}
    \langle B_k\rangle &= \frac1k + \frac1k\left(\langle B_{k-1}\rangle + \overbrace^{(k-1)\langle B_{k-1}\rangle}{1 + \sum_{j=1}^{k-2}\left(1 + \langle B_j\rangle}\right) \\
    &= \frac1k + \frac1k\left(\langle B_{k-1} + \left(k-1\right)\langle B_{k-1}\rangle\right) \\
    &= \frac1k + \langle B_{k-1}\rangle
  \end{align}
$$

so, the average number of presses on the way to the lobby from floor $k$ is just $1 + \frac12 + \frac13 + \ldots + \frac1k,$ which, for the $10$ story building in question, is $\frac{7129}{2520} \approx 
2.829.$
<br>
