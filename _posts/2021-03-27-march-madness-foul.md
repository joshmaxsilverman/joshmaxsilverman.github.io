---
layout: post
published: true
title: "A Permutation Most Foul"
date: 2021/03/27
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

The three shootersd have probabilities $a,$ $b,$ and $c$ to make the foul shot. 

If they go in the order $(a,b,c)$ then there is probability $(1-a)$ to get $0$ points, probability $a(1-b)$ to get $1$ point (they have to make the first, then miss the second), probability $ab(1-c)$ to get $2$ points, and probability $abc$ to get $3$ points, making the expectation value

$$\begin{align}
  \langle S(a,b,c)\rangle &= 0(1-a) + a(1-b) + 2ab(1-c) + 3abc \\
     &= a + ab + abc
\end{align}$$

Permuting the players, we have $6$ potentially distinct expectation values:

$$\begin{align}
  \langle S(a,b,c)\rangle &= a + ab + abc = a(1+b) + abc \\
  \langle S(a,c,b)\rangle &= a + ac + abc = a(1+c) + abc \\
  \langle S(b,a,c)\rangle &= b + ab + abc = b(1+a) + abc \\
  \langle S(b,c,a)\rangle &= b + bc + abc = b(1+c) + abc \\
  \langle S(c,b,a)\rangle &= c + cb + abc = c(1+b) + abc \\
  \langle S(c,a,b)\rangle &= c + ca + abc = c(1+a) + abc
\end{align}$$

All the expectations share the term abc, which we can drop, which just leaves the terms of the form $x(1+y).$

<br>
