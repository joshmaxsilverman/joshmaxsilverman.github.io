---
layout: post
published: false
title: "A Permutation Most Foul"
date: 2021/03/27
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

The three shooters have probabilities $a,$ $b,$ and $c$ to make the foul shot. 

If they go in the order $(a,b,c)$ then there is probability $(1-a)$ to get $0$ points, probability $a(1-b)$ to get $1$ point (they have to make the first, then miss the second), probability $ab(1-c)$ to get $2$ points, and probability $abc$ to get $3$ points, making the expectation value

$$\begin{align}
  \langle S(a,b,c)\rangle &= 0(1-a) + a(1-b) + 2ab(1-c) + 3abc \\
     &= a + ab + abc
\end{align}$$



<br>
