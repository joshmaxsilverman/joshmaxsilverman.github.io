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

for example, from pad $2$, with equal probability, we can step directly to pad $1$, ending the quest, or we can step to pad $3$. if $P_j$ is the probability that we reach pad $1$ from pad $j$, we can write this as the equation

$$ P_2 = \frac12 + \frac12 P_3. $$

on lilypad $3$, we can step left with probability $\frac13$ or right with probability $(1-\frac13)$, giving

$$ P_3 = \frac13 P_2 + (1-\frac13\right) P_4. $$

writing out the next few lilypads, we have the equations

$$
  \begin{align}
    P_4 &= \frac14 P_3 + (1-\frac14\right) P_5 \\
    P_5 &= \frac15 P_4 + (1-\frac15\right) P_6 \\
    P_6 &= \frac16 P_5 + (1-\frac16\right) P_7 \\
    P_7 &= \frac17 P_6 + (1-\frac17\right) P_8 \\
      &\vdots
  \end{align}
$$

and so on.


when we're on lilypad $2$, we can either step to the left with probability $\frac12$, reaching lilypad $1$ and staying there happily ever after, or we can step to pad $3$ on the right. 

<br>
