---
layout: post
published: true
title: Different Dice
date: 2022/05/14
---

>**Question**:

<!--more-->

([FiveThirtyEight](URL))

## Solution

on first glance, there seem to be many states to track. each die can be $1-4,$ so there are $4^4 = 256$ nominal states. 

really, there are just six relevant meta-states:
- the beginning $\textbf{start}$
- two die are the same $aabc$ 
- three die are the same $aaab$ 
- all die are different $abcd$ (the win state)
- two pairs of die are the same $aabb$ (a lose state)
- all four die are the same $aaaa$ (a lose state)

reaching one of the last three states ends the game, while the first three are transient. 

a win can happen if the starting state goes directly to the win state $abcd,$ or it goes to to $aabc$ or $aaab$, possibly bounces around between them, and then goes to the win state $abcd.$ the probability of winning from the beginning

$$
  \boxed{
    P_\text{win}(\textbf{start}) = P(\textbf{start}\rightarrow abcd) + P(\textbf{start}\rightarrow aabc)P_\text{win}(aabc) + P(\textbf{start}\rightarrow aaab)P_\text{win}(aaab)
   }
$$

from there we also have equations for $P_\text{win}(aabc)$ and $P_\text{win}(aaab):$ 

$$
  \boxed{
    \begin{align}
      P_\text{win}(aabc) &= P(aabc\rightarrow aaab)P_\text{win}(aaab) + P(aabc\rightarrow aabc)P_\text{win}(aabc) + P(aabc\rightarrow abcd) \\
      P_\text{win}(aaab) &= P(aaab\rightarrow aabc)P_\text{win}(aabc) + P(aaab\rightarrow aaab)P_\text{win}(aaab)+  P(aaab\rightarrow abcd)
    \end{align}
  }
$$

unlike the starting state, they can return to themselves, directly or indirectly. 

to find the transition probabilities from the starting state, $P(\textbf{start}\rightarrow x),$ we need to multiply

1. the number of ways to form the duplicated subgroup, $D$
2. the number of ways to form the unique subgroup, $U$
3. the number of ways to order those numbers

if the target state has $d$ elements of $D$ and $u$ elements of $U$ then the probability $P(\textbf{start}\rightarrow\textbf{target})$ is

$$
  P(\textbf{start}\rightarrow\textbf{target}) = \dbinom{4}{d}\dbinom{3}{u}\dfrac{4!}{u!d!}
$$

<br>
