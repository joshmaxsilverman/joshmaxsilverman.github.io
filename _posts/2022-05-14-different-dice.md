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
- the beginning $\emptyset$
- two die are the same $aabc$ 
- three die are the same $aaab$ 
- all die are different $abcd$ (the win state)
- two pairs of die are the same $aabb$ (a lose state)
- all four die are the same $aaaa$ (a lose state)

reaching one of the last three states ends the game, while the first three are transient. 

a win can happen if the starting state goes directly to the win state $abcd,$ or it goes to to $aabc$ or $aaab$, possibly bounces around between them, and then goes to the win state $abcd.$ the probability of winning from the beginning

$$
  \boxed{
    P_\text{win}(\emptyset) = P(\emptyset\rightarrow abcd) + P(\emptyset\rightarrow aabc)P_\text{win}(aabc) + P(\emptyset\rightarrow aaab)P_\text{win}(aaab)
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

<br>
