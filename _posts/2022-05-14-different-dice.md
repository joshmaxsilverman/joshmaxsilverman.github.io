---
layout: post
published: true
title: Different Dice
subtitle: How many times will you roll before this game absorbs you?
tags: coarse-graining counting
date: 2022/05/14
---

>**Question**: You have four fair four-sided dice whose sides are numbered 1 through 4.
>
>You play a game in which you roll them all and divide them into two groups: those whose values are unique, and those which are duplicates. For example, if you roll a 1, 2, 2 and 4, then the 1 and 4 will go into the “unique” group, while the 2s will go into the “duplicate” group.
>
>Next, you reroll all the dice in the duplicate pool and sort all the dice again. You continue rerolling the duplicate pool and sorting all the dice until all the dice are members of the same group. If all four dice are in the “unique” group, you win. If all four are in the “duplicate” group, you lose.
>
>What is the probability you win the game?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/its-elementary-my-dear-riddler/))

## Solution

On first glance, there seem to be many states to track. each die can be $1$ through $4,$ so there are $4^4 = 256$ nominal states. 

Really, there are just six relevant meta-states:
- the beginning $\textbf{S}$
- two die are the same $\boldsymbol{aabc}$ 
- three die are the same $\boldsymbol{aaab}$ 
- all die are different $\boldsymbol{abcd}$ (the win state)
- two pairs of die are the same $\boldsymbol{aabb}$ (a lose state)
- all four die are the same $\boldsymbol{aaaa}$ (a lose state)

Reaching one of the last three states ends the game, while $aabc$ and $aaab$ are transient. 

![](/img/2022-05-14-different-dice-dynamics.png){:width="300 px" class="image-centered"}

## Coarse grained dynamics

The game can end in a win if it goes directly to $abcd,$ or it goes to to $aabc$ or $aaab$, possibly bounces around between them, and then goes to $abcd.$ 

Calling $P(x)$ the probability to win the game from state $x$ and $T(x\rightarrow y)$ the probability of transition from state $x$ to state $y$, the probability of winning the starting state is

$$
  P(\textbf{S}) =  T(\textbf{S}\rightarrow \boldsymbol{aabc})P(\boldsymbol{aabc}) + T(\textbf{S}\rightarrow \boldsymbol{aaab})(\boldsymbol{aaab}) + T(\textbf{S}\rightarrow \boldsymbol{abcd})
$$

We also have equations for $P(aabc)$ and $P(aaab):$ 

$$
    \begin{align}
      P(\boldsymbol{aabc}) &= T(\boldsymbol{aabc}\rightarrow \boldsymbol{aaab})P(\boldsymbol{aaab}) + T(\boldsymbol{aabc}\rightarrow \boldsymbol{aabc})P(\boldsymbol{aabc}) + T(\boldsymbol{aabc}\rightarrow \boldsymbol{abcd}) \\
      P(\boldsymbol{aaab}) &= T(\boldsymbol{aaab}\rightarrow \boldsymbol{aabc})P(\boldsymbol{aabc}) + T(\boldsymbol{aaab}\rightarrow \boldsymbol{aaab})P(\boldsymbol{aaab})+  T(\boldsymbol{aaab}\rightarrow \boldsymbol{abcd})
    \end{align}
$$

Unlike the starting state, they can return to themselves, directly or indirectly. 

## Transition combinatorics

To find the transition probabilities from the starting state, $T(\textbf{S}\rightarrow \boldsymbol{x}),$ we need

1. the number of ways $\Omega(D)$ to pick numbers for the duplicate group $D$
2. the number of ways $\Omega(U)$ to pick numbers for the unique group, $U$
3. the number of ways to order those numbers.

For example, if the target state is $\boldsymbol{aabc}$ then it has $1$ unique member in $D,$ $2$ members of $U$ and the transition probability is

$$
  T(\textbf{S}\rightarrow \boldsymbol{aabc}) = \overset{\Omega(D)}{\dbinom{4}{1}}\overset{\Omega(U)}{\dbinom{3}{2}}\overset{\text{orders}}{\dfrac{4!}{2!1!1!}}\frac{1}{4^4} = \frac{144}{256}
$$

carrying this through gets

$$
  \begin{array}{c|c|c}
    T(\textbf{S}\rightarrow \boldsymbol{abcd}) & \binom{0}{0}\binom{4}{4}\frac{4!}{1!1!1!1!}\frac{1}{4^4} & \frac{24}{256}\\ \hline
    T(\textbf{S}\rightarrow \boldsymbol{aabc}) & \binom{4}{1}\binom{3}{2}\frac{4!}{2!1!1!}\frac{1}{4^4} & \frac{144}{256} \\ \hline
    T(\textbf{S}\rightarrow \boldsymbol{aaab}) & \binom{4}{1}\binom{3}{1}\frac{4!}{3!1!}\frac{1}{4^4} & \frac{48}{256}.
  \end{array} 
$$

We also need the transition probabilities between the transient states, and from the transient states to $\boldsymbol{abcd}.$

To go from $\boldsymbol{aabc}$ to $\boldsymbol{aaab},$ the duplicates need to reroll as either both $\boldsymbol{b}$ or both $\boldsymbol{c}$ 

$$
  \begin{align}
    T(\boldsymbol{aabc} \rightarrow \boldsymbol{aaab}) &= \binom{2}{1}\frac{1}{4^2} \\
    &= \frac{2}{4^2}.
  \end{align}
$$

In the other direction, there are two possibilities: 
- $2$ of the rerolls are duplicates of each other and the third is another number different from $\boldsymbol{b},$ or 
- $1$ of the rerolls is a duplicate of $\boldsymbol{b}$ and the other two are distinct numbers each different from $\boldsymbol{b},$ so we get

$$
  \begin{align}
    T(\boldsymbol{aaab} \rightarrow \boldsymbol{aabc}) &= \left[\binom{3}{1}\binom{2}{1}\frac{3!}{2!} + \binom{3}{2}\frac{3!}{1!1!1!}\right]\frac{1}{4^3} \\
      &= \frac{36}{64}
  \end{align}
$$

Carrying on like this, we can get the remaining transition probabilities:

$$
  \begin{array}{c|c|c}
    T(\boldsymbol{aabc}\rightarrow \boldsymbol{aaab}) & \binom{2}{1}\frac{1}{4^2} & \frac{2}{16} \\ \hline
    T(\boldsymbol{aaab}\rightarrow \boldsymbol{aabc}) & \left[\binom{3}{1}\binom{2}{1}\frac{3!}{2!1!} + \binom{3}{2}\frac{3!}{1!1!1!}\right]\frac{1}{4^3} &  \frac{36}{64} \\ \hline
    T(\boldsymbol{aaab} \rightarrow \boldsymbol{aaab}) & \left[\binom{3}{1} + \binom{3}{1}\frac{3!}{2!1!}\right]\frac{1}{4^3} & \frac{12}{64} \\ \hline
    T(\boldsymbol{aabc} \rightarrow \boldsymbol{aabc}) & \left[4^2 - 3\binom{2}{1}\right]\frac{1}{4^2} & \frac{10}{16} \\ \hline
    T(\boldsymbol{aabc} \rightarrow \boldsymbol{abcd}) & \binom{2}{1}\frac{1}{4^2} & \frac{2}{16} \\ \hline
    T(\boldsymbol{aaab} \rightarrow \boldsymbol{abcd}) & \frac{3!}{1!1!1!}\frac{1}{4^3} & \frac{6}{64}
  \end{array} 
$$

## The probability to win, $P(\textbf{S})$

with the transition probabilities in hand, the equations for $P(\boldsymbol{aabc})$ and $P(\boldsymbol{aaab})$ become 

$$
  \begin{align}
    P(\boldsymbol{aabc}) &= \frac18 P(\boldsymbol{aaab}) + \frac58 P(\boldsymbol{aabc}) + \frac18 \\
    P(\boldsymbol{aaab}) &= \frac{3}{16}P(\boldsymbol{aaab}) + \frac{9}{16}P(\boldsymbol{aabc}) + \frac{3}{32} \\
   \end{align}
 $$

which yields $P(\boldsymbol{aabc})= 29/60$ and $P(\boldsymbol{aaab}) = 9/20.$

Plugging these in to the original equation for $P(\textbf{S}),$ we get 

$$
  \boxed{P(\textbf{S}) = \dfrac{9}{20} = 45\%}.
$$

<br>
