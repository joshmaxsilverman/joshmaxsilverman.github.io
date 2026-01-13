---
layout: post
published: true
subtitle: How many times will you press the broken button?
source: fivethirtyeight
tags: expectation structure dynamics
title: Broken elevator
date: 2022/05/07
theme: probability
---

>**Question:** You are on the $10^\text{th}$ floor of a tower and want to exit on the first floor. You get into the elevator and hit $1.$ However, this elevator is malfunctioning in a specific way. When you hit $1,$ it correctly registers the request to descend, but it randomly selects some floor below your current floor (including the first floor). The car then stops at that floor. If it’s not the first floor, you again hit $1$ and the process repeats.
>
>Assuming you are the only passenger on the elevator, how many floors on average will it stop at (including your final stop, the first floor) until you exit?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-build-the-longest-ladder/))

## Solution

To avoid finicky bookkeeping, we can count the lobby as floor zero, instead of floor $1$. Also, it's equivalent to think in terms of how many times the passenger will press the button, and that's what we'll do.

When the passenger presses the button from floor $(k+1),$ they can either go to floor $k,$ or go to floors $0$ through $(k-1),$ which is the same as starting from floor $k$ but without the extra button press.

This means that the expected number of button presses from floor $(k+1)$ is 

$$
  \begin{align}
    \langle B_{k+1} \rangle &= \tfrac1k(1 + \langle B_k\rangle) + (1-\tfrac1k) \langle B_k\rangle \\
    &= \tfrac1k + \langle B_k\rangle,
  \end{align}
$$

<!-- When the passenger presses the button from floor $k,$ the elevator is equally likely to end up at any floor under it. 

So, they have uniform probability $\frac1k$ to arrive at any of the floors, which can be the lobby in one press or else any of the $(k-1)$ floors above the lobby from which they will make an average of $\langle B_{k-1}\rangle$ more presses.

So the expected value of the number of button presses from floor $k$ is equal to

$$
  \langle B_k\rangle = \dfrac1k + \dfrac1k\sum_{j=1}^{k-1}\left(1 + \langle B_j\rangle\right).
$$

The second term is just $\langle B_{k-1}\rangle,$

$$
\begin{align}
  \langle B_k\rangle &= \dfrac1k + \dfrac1k[\langle B_{k-1}\rangle + \overbrace{1 + \sum_{j=1}^{k-2}\left(1 + \langle B_j\rangle\right)}^{\left(k-1\right)\langle B_{k-1}\rangle}] \\
  &= \dfrac1k + \dfrac1k\left[\langle B_{k-1}\rangle + \left(k-1\right)\langle B_{k-1}\rangle\right] \\
  &= \dfrac1k + \langle B_{k-1}\rangle,
$$
\end{align} -->


so 

$$
  \langle B_k\rangle = 1 + \tfrac12 + \tfrac13 + \ldots + \tfrac1k,
$$ 

the $k^\text{th}$ harmonic number.

For the $9$ story building in question, this is $\frac{7129}{2520} \approx 
2.829$ button presses.
<br>
