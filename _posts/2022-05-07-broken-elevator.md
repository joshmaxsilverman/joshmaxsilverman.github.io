---
layout: post
published: false
title: 
date: 2022/05/07
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

when the passenger presses the button from floor $k,$ the elevator is equally likely to end up at any floor under it. 

they have uniform probability $1/k$ to arrive at any of the floors, which can be the lobby in one press, or else any of the $(k-1)$ floors above the lobby from which they will make an average of $\langle B_{k-1}\rangle$ more presses.

so 

$$
  \langle B_k\rangle = \dfrac1k + \dfrac1k\sum_{j=1}^{k-1}\left(1 + \langle B_j\rangle\right)
$$

<br>
