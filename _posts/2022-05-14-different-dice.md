---
layout: post
published: true
title: Different Dice
date: 2022/05/14
---

>**Question**: You have four fair tetrahedral dice whose four sides are numbered 1 through 4.
>
>You play a game in which you roll them all and divide them into two groups: those whose values are unique, and those which are duplicates. For example, if you roll a 1, 2, 2 and 4, then the 1 and 4 will go into the “unique” group, while the 2s will go into the “duplicate” group.
>
>Next, you reroll all the dice in the duplicate pool and sort all the dice again. Continuing the previous example, that would mean you reroll the 2s. If the result happens to be 1 and 3, then the “unique” group will now consist of 3 and 4, while the “duplicate” group will have two 1s.
>
>You continue rerolling the duplicate pool and sorting all the dice until all the dice are members of the same group. If all four dice are in the “unique” group, you win. If all four are in the “duplicate” group, you lose.
>
>What is your probability of winning the game?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/its-elementary-my-dear-riddler/))

## Solution

on first glance, there seem to be many states to track. each die can be $1$ through $4,$ so there are $4^4 = 256$ nominal states. 

really, there are just six relevant meta-states:
- the beginning $\textbf{S}$
- two die are the same $aabc$ 
- three die are the same $aaab$ 
- all die are different $abcd$ (the win state)
- two pairs of die are the same $aabb$ (a lose state)
- all four die are the same $aaaa$ (a lose state)

reaching one of the last three states ends the game, while the first $aab$ and $aaab$ are transient. 

![](/img/2022-05-14-different-dice-dynamics.png){:width="300 px" class="image-centered"}

## Coarse grained dynamics

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

## Transition combinatorics

to find the transition probabilities from the starting state, $P(\textbf{S}\rightarrow x),$ we need

1. the number of ways $\Omega(D)$ to pick numbers for the duplicate group $D$
2. the number of ways $\Omega(U)$ to pick numbers for the unique group, $U$
3. the number of ways to order those numbers, $O(U,D)$

for example, if the target state is $aabc$ then it has $1$ unique member in $D$ and $2$ elements of $U$ and the transition probability is

$$
  P(\textbf{S}\rightarrow aabc) = \overset{\Omega(D)}{\dbinom{4}{1}}\overset{\Omega(U)}{\dbinom{3}{2}}\overset{O(U,D)}{\dfrac{4!}{2!1!1!}}\frac{1}{4^4} = \frac{144}{256}
$$

carrying this through gets

$$
  \begin{array}{c|c|c}
    P(\textbf{S}\rightarrow abcd) & \binom{4}{4}\frac{4!}{1!1!1!1!}\frac{1}{4^4} & \frac{24}{256}\\ \hline
    P(\textbf{S}\rightarrow aabc) & \binom{4}{1}\binom{3}{2}\frac{4!}{2!1!1!}\frac{1}{4^4} & \frac{144}{256} \\ \hline
    P(\textbf{S}\rightarrow aaab) & \binom{4}{1}\binom{3}{1}\frac{4!}{3!1!}\frac{1}{4^4} & \frac{48}{256}
  \end{array} 
$$

we also need the transition probabilities between the transient states, and from the transient states to $abcd$

to go from $aabc$ to $aaab,$ the duplicates need to reroll as either both $b$ or both $c$ 

$$
  \begin{align}
    P(aabc \rightarrow aaab) &= \binom{2}{1}\frac{1}{4^2} \\
    &= \frac{2}{4^2}
  \end{align}
$$

in the other direction, there are two possibilities: $2$ of the rerolls are duplicates of each other and the third is another number different from $b,$ or $1$ of the rerolls is a duplicate of $b$ and the other two are distinct numbers each different from $b.$ so we get

$$
  \begin{align}
    P(aaab \rightarrow aabc) &= \left[\binom{3}{1}\binom{2}{1}\frac{3!}{2!} + \binom{3}{2}\frac{3!}{1!1!1!}\right]\frac{1}{4^3} \\
      &= \frac{36}{64}
  \end{align}
$$

carrying on like this, we get all the remaining transition probabilities:

$$
  \begin{array}{c|c|c}
    P(aabc\rightarrow aaab) & \binom{2}{1}\frac{1}{4^2} & \frac{2}{16} \\ \hline
    P(aaab\rightarrow aabc) & \left[\binom{3}{1}\binom{2}{1}\frac{3!}{2!} + \binom{3}{2}\frac{3!}{1!1!1!}\right]\frac{1}{4^3} &  \frac{36}{64} \\ \hline
    P(aaab \rightarrow aaab) & \left[\binom{3}{1} + \binom{3}{1}\frac{3!}{2!}\right]\frac{1}{4^3} & \frac{12}{64} \\ \hline
    P(aabc \rightarrow aabc) & \left[4^2 - 3\binom{2}{1}\right]\frac{1}{4^2} & \frac{10}{16} \\ \hline
    P(aabc \rightarrow abcd) & \binom{2}{1}\frac{1}{4^2} & \frac{2}{16} \\ \hline
    P(aaab \rightarrow abcd) & \frac{3!}{4^3} & \frac{6}{64}
  \end{array} 
$$

## The probability to win, $P(\textbf{S})$

with the transition probabilities in hand, the equations for $P(aabc)$ and $P(aaab)$ become 

$$
  \begin{align}
    P(aabc) &= \frac18 P(aaab) + \frac58 P(aabc) + \frac18 \\
    P(aaab) &= \frac{3}{16}P(aaab) + \frac{9}{16}P(aabc) + \frac{3}{32} \\
   \end{align}
 $$

which yields $P(aabc)= 29/60$ and $P(aaab) = 9/20.$

Plugging these in to the original equation for $P(\textbf{S}),$ we get 

$$
  \boxed{P(\textbf{S}) = \dfrac{9}{20} = 45\%}.
$$

<br>
