---
layout: post
published: true
title: Can you hop to the lily pad?
date: 2025/01/25
subtitle: The further you go, the harder it gets.
tags: master-equation recursion
---

>**Question**: You are a frog in a pond that has infinitely many lily pads, which are numbered “1,” “2,” “3,” etc in a row. You are currently on pad $2$, and your goal is to make it to pad $1$, which you would happily stay on forever.
>
>Whenever you are on pad $k$, you will hop to pad $(k−1)$ with probability $1/k$, and you will hop to pad $(k+1)$ with probability $(k−1)/k$.
>
>What is the probability that you will ultimately make it to pad $1$?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-hop-to-the-lily-pad))

## Solution

On any given lilypad, we can step to the left or to the right. So, the probability we reach pad $1$ is always equal to the probability we step to the left and go on to reach pad $1$ plus the probability we step to the right and go on to reach pad $1$. 

Starting from pad $2$ we can step with equal probability directly to pad $1$, ending the quest, or to pad $3$. We can write this as the equation

$$ P_2 = \frac12 + \frac12 P_3, $$

where $P_j$ is the probability that we reach pad $1$ from pad $j$. If we start on pad $1$, we're already there, so $P_1 = 1.$ 

On lilypad $3$, we can step left with probability $\frac13$ or right with probability $(1-\frac13)$, giving

$$ P_3 = \frac13 P_2 + \left(1-\frac13\right) P_4. $$

Following the first two equations, if we hop from pad $2$ to pad $3$ then jump left twice to pad $1$, that happens with probability $\frac12\frac13\frac12 = \frac1{12},$ which shows that $P_2$ is at least $\frac12 + \frac1{12} = \frac{7}{12}.$

### Generalizing

Writing out the next few lilypads, we have the equations

$$
  \begin{align}
    P_4 &= \frac14 P_3 + \left(1-\frac14\right) P_5 \\
    P_5 &= \frac15 P_4 + \left(1-\frac15\right) P_6 \\
    P_6 &= \frac16 P_5 + \left(1-\frac16\right) P_7 \\
    P_7 &= \frac17 P_6 + \left(1-\frac17\right) P_8 \\
      \vdots
  \end{align}
$$

and so on. Every lilypad is like this, so we can write and analyze a general lilypad equation:

$$ P_j = \frac1j P_{j-1} + \left(1-\frac1j\right) P_{j+1}. $$

This connects three lilypads at a time, forward and backward, which is tough to solve directly for $P_j$. However, we might be able to massage it into an equation relating the two consecutive gaps (between $P_j$ and $P_{j-1}$, and between $P_{j+1}$ and $P_j$). 

### Solving the recursion

If we rewrite the left hand side as $\frac1j P_j + (1-\frac1j)P_j,$ we get

$$ \frac1j P_j + (1-\frac1j)P_j = \frac1j P_{j-1} + \left(1-\frac1j\right) P_{j+1} $$ 

which simplifies to

$$ P_{j} - P_{j+1} = \frac1{j-1}\left(P_{j-1} - P_j\right). $$

This recurses down to the base case $j=2$:

$$ P_j - P_{j+1} = \frac{1}{(j-1)!}(P_1 - P_2). $$

From this we can find $P_2$. Because the probabilities $P_j$ go to zero for large $j$, we can find $P_1$ by telescoping 

$$P_1 = (P_1 - P_2) + (P_2 - P_3) + (P_3 - P_4) + \ldots, $$ 

and so

$$ 
  \begin{align}
    P_1 &= \sum_{j=2}^\infty \frac{1}{(j-1)!}(P_1 - P_2) \\
        &= (P_1 - P_2) \sum_{j=2}^\infty \frac1{(j-1)!} \\
        &= e(P_1 - P_2).
  \end{align}
$$

Again, if we start on pad $1$, we're already there, so $P_1 = 1$ and we get 

$$ \boxed{P_2 = \frac{e-1}{e} \approx 0.63212056}. $$

While long trajectories are possibly in principle, $92%$ of the probability mass is contributed by the two shortest paths to pad $1$.

<br>
