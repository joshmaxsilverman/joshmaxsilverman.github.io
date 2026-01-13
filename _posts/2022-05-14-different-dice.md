---
layout: post
published: true
title: Different dice
subtitle: Get absorbed by these dice.
source: fivethirtyeight
tags: coarse-graining counting
date: 2022/05/14
theme: probability
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

On first glance, there seem to be many states to track. Each die has four sides, so there are $4^4 = 256$ nominal states. 

Really, there are just a few relevant meta-states:
- the beginning $\boldsymbol{S}$
- two die are the same $\boldsymbol{aabc}$ 
- three die are the same $\boldsymbol{aaab}$ 
- all die are different $\boldsymbol{abcd}$ (the win state)
- two pairs of die are the same $\boldsymbol{aabb}$ (a lose state)
- all four die are the same $\boldsymbol{aaaa}$ (a lose state)

Reaching one of the last three states ends the game, while $aabc$ and $aaab$ are transient. 

![](/img/2022-05-14-different-dice-graph.png){:width="300 px" class="image-centered"}

Also, $\boldsymbol{aaab}$ is equivalent to the starting state $\boldsymbol{S}.$ When the three $a$ get re-flipped, they are random with respect to $b,$ so it's as if $b$ gets flipped too.

With this insight, we can merge $\boldsymbol{S}$ and $\boldsymbol{aaab}$ and focus on the reduced three state game:

![](/img/2022-05-14-different-dice-reduced.png){:width="150 px" class="image-centered"}

## Coarse grained dynamics

The game ends in a win if it goes directly to $abcd,$ or if it bounces around between $aabc$ and $aaab,$ and then goes to $abcd.$ 

Calling $P(x)$ the probability to win the game from state $x$ and $T(x\rightarrow y)$ the probability of transition from state $x$ to state $y$, the probability of winning from the starting state is

$$
  P(\boldsymbol{S/aaab}) =  T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{aabc})P(\boldsymbol{aabc}) + T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{aaab})P(\boldsymbol{S/aaab}) + T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{abcd}).
$$

Likewise,

$$
  P(\boldsymbol{aabc}) = T(\boldsymbol{aabc}\rightarrow \boldsymbol{S/aaab})P(\boldsymbol{S/aaab}) + T(\boldsymbol{aabc}\rightarrow \boldsymbol{aabc})P(\boldsymbol{aabc}) + T(\boldsymbol{aabc}\rightarrow \boldsymbol{abcd}).
$$

## Transition combinatorics

To find the transition probabilities from the starting state, $T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{x}),$ we need

1. the number of ways $\Omega(D)$ to pick numbers for the duplicate group $D$
2. the number of ways $\Omega(U)$ to pick numbers for the unique group, $U$
3. the number of ways to order those numbers.

For example, if the target state is $\boldsymbol{aabc}$ then it has $1$ unique member in $D,$ $2$ members of $U$ and the transition probability is

$$
  T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{aabc}) = \overset{\Omega(D)}{\dbinom{4}{1}}\overset{\Omega(U)}{\dbinom{3}{2}}\overset{\text{orders}}{\dfrac{4!}{2!1!1!}}\frac{1}{4^4} = \frac{144}{256}.
$$

Carrying this through gets

$$
  \begin{array}{c|c|c}
    T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{abcd}) & \binom{0}{0}\binom{4}{4}\frac{4!}{1!1!1!1!}\frac{1}{4^4} & \frac{3}{32}\\ \hline
    T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{aabc}) & \binom{4}{1}\binom{3}{2}\frac{4!}{2!1!1!}\frac{1}{4^4} & \frac{9}{16} \\ \hline
    T(\boldsymbol{S/aaab}\rightarrow \boldsymbol{S/aaab}) & \binom{4}{1}\binom{3}{1}\frac{4!}{3!1!}\frac{1}{4^4} & \frac{3}{16}
  \end{array} 
$$

We also need the transition probabilities from $\boldsymbol{aabc}.$

To go from $\boldsymbol{aabc}$ to $\boldsymbol{S/aaab},$ the duplicates need to reroll as either both $\boldsymbol{b}$ or both $\boldsymbol{c},$ and we find: 

$$
  \begin{align}
    T(\boldsymbol{aabc} \rightarrow \boldsymbol{aaab}) &= \binom{2}{1}\frac{1}{4^2} \\
    &= \frac{1}{8}.
  \end{align}
$$

We can check our insight from above by doing the same calculation for the reverse transition. There are two possibilities: 
- $2$ of the rerolls are duplicates of each other and the third is another number different from $\boldsymbol{b},$ or 
- $1$ of the rerolls is a duplicate of $\boldsymbol{b}$ and the other two are distinct numbers each different from $\boldsymbol{b},$ so we get

$$
  \begin{align}
    T(\boldsymbol{aaab} \rightarrow \boldsymbol{aabc}) &= \left[\binom{3}{1}\binom{2}{1}\frac{3!}{2!} + \binom{3}{2}\frac{3!}{1!1!1!}\right]\frac{1}{4^3} \\
      &= \frac{9}{16},
  \end{align}
$$

as expected.

Carrying on like this, we can get the remaining transition probabilities:

$$
  \begin{array}{c|c|c}
    T(\boldsymbol{aabc}\rightarrow \boldsymbol{S/aaab}) & \binom{2}{1}\frac{1}{4^2} & \frac{1}{8} \\ \hline
    T(\boldsymbol{aabc} \rightarrow \boldsymbol{aabc}) & \left[4^2 - 3\binom{2}{1}\right]\frac{1}{4^2} & \frac{5}{8} \\ \hline
    T(\boldsymbol{aabc} \rightarrow \boldsymbol{abcd}) & \binom{2}{1}\frac{1}{4^2} & \frac{1}{8}
  \end{array} 
$$


<!--     T(\boldsymbol{aaab}\rightarrow \boldsymbol{aabc}) & \left[\binom{3}{1}\binom{2}{1}\frac{3!}{2!1!} + \binom{3}{2}\frac{3!}{1!1!1!}\right]\frac{1}{4^3} &  \frac{36}{64} \\ \hline
    T(\boldsymbol{aaab} \rightarrow \boldsymbol{aaab}) & \left[\binom{3}{1} + \binom{3}{1}\frac{3!}{2!1!}\right]\frac{1}{4^3} & \frac{12}{64} \\ \hline --         T(\boldsymbol{aaab} \rightarrow \boldsymbol{abcd}) & \frac{3!}{1!1!1!}\frac{1}{4^3} & \frac{6}{64} -->

## The probability to win, $P(\boldsymbol{S/aaab})$

With the transition probabilities in hand, the equations for $P(\boldsymbol{aabc})$ and $P(\boldsymbol{aaab})$ become 

$$
  \begin{align}
    P(\boldsymbol{aabc}) &= \frac18 P(\boldsymbol{S/aaab}) + \frac58 P(\boldsymbol{aabc}) + \frac18 \\
    P(\boldsymbol{S/aaab}) &= \frac{3}{16}P(\boldsymbol{S/aaab}) + \frac{9}{16}P(\boldsymbol{aabc}) + \frac{3}{32} \\
   \end{align}
 $$

which yields $P(\boldsymbol{aabc})= 29/60$ and
$$
  \boxed{P(\boldsymbol{S/aaab}) = \dfrac{9}{20} = 45\%}.
$$

<br>
