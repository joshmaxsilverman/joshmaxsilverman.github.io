---
layout: post
published: true
title: Consecutive Heads
date: 2019/12/07
---

>If you flip a fair coin 10 times (or n times for extra credit), how likely is it that the final two flips are the first and only time you see a consecutive pair of heads?

<!--more-->

## Solution

We will approach this combinatorially, counting how many sequences of length $n$ of $H$ and $T$ are as required -- ending in $HH$ with no previous occurences of $HH$. Let $C_n$ be the number of such sequences.

Let's look at the sequences for small $n$:

$C_1 = 0$: [none]

$C_2 = 1$: $HH$

$C_3 = 1$: $THH$

$C_4 = 2$: $HTHH$, $TTHH$

$C_5 = 3$: $THTHH$, $HTTHH$, $TTTHH$

$C_6 = 5$: $HTHTHH$, $TTHTHH$, $THTTHH$, $HTTTHH$, $TTTTHH$

A first observation is that it looks like we're seeing the Fibonacci numbers: starting with $0$ and $1$, each is the sum of the previous two. 

A second observation confirms this. We can generate the sequences of length $n$ from those of length $n-1$ and $n-2$ as follows. From each sequence of length $n-2$, generate one of length $n$ by inserting $HT$ before the final $HH$. From each sequence of length $n-1$, generate one of length $n$ by inserting $T$ in the same spot. All sequences of length $n$ are generable in exactly one of these two ways. They end either in $HTHH$, in which case the rest of the sequence must be one of the sequences of length $n-2$ minus the final $HH$, or in $TTHH$, in which case the rest of the sequence must be a sequence of length $n-1$ minus the terminal $THH$.

So $C_n = C_{n-2} + C_{n-1}$, and these are indeed the Fibonacci numbers $F_{n-1}$.

Having numbered the sequences of flips that are as required, we can get the desired probability simply by dividing by the total number of possible sequences $2^n$:

$$P_n = \frac{F_{n-1}}{2^n}$$


Let's play for even more extra credit. The smallest values of $P_n$ are:

$$\frac{0}{2}, \frac{1}{4}, \frac{1}{8}, \frac{2}{16}, \frac{3}{32}, \frac{5}{64}, \ldots$$

Now, if we flip a coin until we get $HH$ (and stop), we are virtually certain (probability $1$) to succeed. But of course succeeding means either succeeding at the first flip, or at the second, or at the third, and so on. So we have established an interesting fact:

$$\sum_{n=1}^\infty \frac{F_{n-1}}{n^2} = \frac{0}{2} + \frac{1}{4} + \frac{1}{8} + \frac{2}{16} + \frac{3}{32} + \frac{5}{64} + \ldots = 1$$

<br>