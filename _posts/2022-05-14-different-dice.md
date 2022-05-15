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
- the beginning $\textbf{S}$
- two die are the same $aabc$ 
- three die are the same $aaab$ 
- all die are different $abcd$ (the win state)
- two pairs of die are the same $aabb$ (a lose state)
- all four die are the same $aaaa$ (a lose state)

reaching one of the last three states ends the game, while the first three are transient. 

a win can happen if the starting state goes directly to the win state $abcd,$ or it goes to to $aabc$ or $aaab$, possibly bounces around between them, and then goes to the win state $abcd.$ the probability of winning from the beginning

$$
  \boxed{
    P_\text{win}(\textbf{S}) = P(\textbf{S}\rightarrow abcd) + P(\textbf{S}\rightarrow aabc)P_\text{win}(aabc) + P(\textbf{S}\rightarrow aaab)P_\text{win}(aaab)
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

## transition probabilities

to find the transition probabilities from the starting state, $P(\textbf{S}\rightarrow x),$ we need

1. the number of ways $\Omega(D)$ to pick numbers for the duplicate group $D$
2. the number of ways $\Omega(U)$ to pick numbers for the unique group, $U$
3. the number of ways to order those numbers, $O(\{U,D}\)$

for example, if the target state is $aabc$ then it has $1$ unique member in $D$ and $2$ elements of $U$ and the transition probability is

$$
  P(\textbf{S}\rightarrow aabc) = \overset{\Omega(D)}{\dbinom{4}{1}}\overset{\Omega(U)}{\dbinom{3}{2}}\overset{O(\{U,D\}}{\dfrac{4!}{2!1!1!}}\frac{1}{4^4} = \frac{144}{256}
$$

carrying this through gets

$$
  \begin{array}{|c|c|} \hline
    P(\textbf{S}\rightarrow abcd) & \binom{4}{4}\frac{4!}{1!1!1!1!}\frac{1}{4^4} \\ \hline
    P(\textbf{S}\rightarrow aabc) & \binom{4}{1}\binom{3}{2}\frac{4!}{2!1!1!}\frac{1}{4^4} \\ \hline
    P(\textbf{S}\rightarrow aaab) & \binom{4}{1}\binom{3}{1}\frac{4!}{3!1!}\frac{1}{4^4} \\ \hline
  \end{array} 
$$
<br>
