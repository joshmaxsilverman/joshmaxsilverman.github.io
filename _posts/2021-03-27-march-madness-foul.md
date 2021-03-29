---
layout: post
published: true
title: "A Permutation Most Foul"
date: 2021/03/27
---

>**Question**: You're playing a game of three on three basketball in a weird league. The rule on foul shots on a three pointer is that all three players from the team get to take turns shooting three foul shots. However, to get the second foul shot the team must make the first, and to get the second foul shot the team must make the second. As soon as a player misses, the foul shooting is over. If the players on your team have foul shot percentages $a,$ $b,$ and $c$ (no two equal), then what is the maximum number of shooting orders that would produce the same expected number of points?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-solve-march-mathness/))

## Solution

The three shooters have probabilities $a,$ $b,$ and $c$ to make the foul shot. 

If they go in the order $(a,b,c)$ then 

- there is probability $(1-a)$ to get $0$ points, 
- probability $a(1-b)$ to get $1$ point (they have to make the first, 
- then miss the second), probability $ab(1-c)$ to get $2$ points, and 
- probability $abc$ to get $3$ points, 

making the expectation value

$$\begin{align}
  \langle S(a,b,c)\rangle &= 0(1-a) + a(1-b) + 2ab(1-c) + 3abc. \\
     &= a + ab + abc
\end{align}$$

### Permuting

Permuting the players, we have $6$ potentially distinct expectation values:

$$\begin{align}
  \langle S(a,b,c)\rangle &= a + ab + abc  \\
  \langle S(a,c,b)\rangle &= a + ac + abc  \\
  \langle S(b,a,c)\rangle &= b + ab + abc  \\
  \langle S(b,c,a)\rangle &= b + bc + abc  \\
  \langle S(c,b,a)\rangle &= c + cb + abc  \\
  \langle S(c,a,b)\rangle &= c + ca + abc 
\end{align}$$

All the expectations share the term $abc,$ which we can drop, which just leaves the terms of the form $x(1+y).$

$$\begin{align}
  \langle S^\prime(a,b,c)\rangle &= a(1+b) \\
  \langle S^\prime(a,c,b)\rangle &= a(1+c) \\
  \langle S^\prime(b,a,c)\rangle &= b(1+a) \\
  \langle S^\prime(b,c,a)\rangle &= b(1+c) \\
  \langle S^\prime(c,b,a)\rangle &= c(1+b) \\
  \langle S^\prime(c,a,b)\rangle &= c(1+a)
\end{align}$$

### Finding equal permutations

The permutations are symmetric with respect to the variables, so we can start building the set of equal expressions with any of the $6.$ Let's start with the first.

- The first and second share a factor of $a,$ so they can't be equal without forcing $b=c$ which is not allowed.
- The first and third can't be equal without forcing $a=b,$ which is not allowed.
- The first and fourth can be equal since it doesn't force any disallowed equalities.
- The first and fifth share a factor of $(1+b),$ and so can't be equal without forcing $a=c.$
- The first and sixth can't be equal because of the condition forced on $c$ by setting the first and fourth equal.

So, there can be at most $2$ of the expectations that are equal.

### Is this a good idea?

Suppose we pursued this expectation. We'd have free choice of $a$ and $b,$ and we'd be forced to take

$$\begin{align} 
  c &= \frac{a(1+b)}{b} - 1 \\
    &= \frac{ab + a - b}{b} \\
    &= a + \left(\frac{a}{b} - 1\right)
\end{align}$$

If $a > b$ then the second term is positive and $c > a$ so that

$$ c > a > b. $$

But if $a < b$ then the second term is negative and $c < a$ so that

$$ c < a < b. $$

However, to maximize the expectation $\langle S(a,b,c)\rangle,$ the probabilities need to be in decreasing order, which means that the equal shooting profiles are suboptimal.


<br>
