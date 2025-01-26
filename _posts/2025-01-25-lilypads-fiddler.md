---
layout: post
published: false
title: Can you hop to the lily pad?
date: 2024/01/25
subtitle: The further you go, the harder it gets.
tags: master-equation recursion
---

>**Question**: You are a frog in a pond that has infinitely many lily pads, which are numbered “1,” “2,” “3,” etc in a row. You are currently on pad $2$, and your goal is to make it to pad $1$, which you would happily stay on forever.
>
>Whenever you are on pad $k$, you will hop to pad $(k−1)$ with probability $1/k$, and you will hop to pad $(k+1)$ with probability $(k−1)/k$.
>
>Now, what is the probability that you will ultimately make it to pad $1$?

<!--more-->

([Fiddler on the Proof](URL))

## Solution

on any given lilypad, we can step to the left or to the right. so, the probability that we reach pad $1$ is always equal to the probability we step to the left and go on to reach pad $1$ plus the probability we step to the right and go on to reach pad $1$. 

for example, from pad $2$, with equal probability, we can step directly to pad $1$, ending the quest, or we can step to pad $3$. we can write this as the equation

$$ P_2 = \frac12 + \frac12 P_3, $$

where $P_j$ is the probability that we reach pad $1$ from pad $j$. if we start on pad $1$, we're already there, so $P_1 = 1.$

on lilypad $3$, we can step left with probability $\frac13$ or right with probability $(1-\frac13)$, giving

$$ P_3 = \frac13 P_2 + \left(1-\frac13\right) P_4. $$

writing out the next few lilypads, we have the equations

$$
  \begin{align}
    P_4 &= \frac14 P_3 + \left(1-\frac14\right) P_5 \\
    P_5 &= \frac15 P_4 + \left(1-\frac15\right) P_6 \\
    P_6 &= \frac16 P_5 + \left(1-\frac16\right) P_7 \\
    P_7 &= \frac17 P_6 + \left(1-\frac17\right) P_8 \\
      &\vdots
  \end{align}
$$

and so on. every lilypad is like this, so we can write and analyze a general lilypad equation:

$$ P_j = \frac1j P_{j-1} + \left(1-\frac1j\right) P_{j+1}. $$

this connects three lilypads at a time, forward and backward, which is tough to solve directly for $P_j$. however, we might be able to massage it into an equation relating the two consecutive gaps (between $P_j$ and $P_{j-1}$, and between $P_{j+1} and $P_j$). if we rewrite the left hand side as $\frac1j P_j + (1-\frac1j)P_j,$ we get

$$ \frac1j P_j + (1-\frac1j)P_j = \frac1j P_{j-1} + \left(1-\frac1j\right) P_{j+1} $$ 

which simplifies to

$$ P_{j} - P_{j+1} = \frac1{j-1}\left(P_{j-1} - P_j\right). $$

this recurses down to the base case $j=2$:

$$ P_j - P_{j+1} = \frac{1}{(j-1)!}(P_1 - P_2). $$

this is convenient, because $P_1 = (P_1 - P_2) + (P_2 - P_3) + (P_3 - P_4) + \ldots $, and so

$$ 
  \begin{align}
    P_1 &= \sum_{j=2}^\infty \frac{1}{(j-1)!}(P_1 - P_2) \\
        &= (P_1 - P_2) \sum_{j=2}^\infty \frac1{(j-1)!} \\
        &= e(P_1 - P_2).
  \end{align}
$$

again, if we start on pad $1$, we're already there, so $P_1 = 1$ and we get 

$$ P_2 = \frac{e-1}{e}. $$

<br>
