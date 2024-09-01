---
layout: post
published: false
title: Tree edge triage
date: 2018/04/21
subtitle:
tags:
---

>**Question**: Aaron and Beren are playing a game on an infinite complete binary tree. At the beginning of the game, every edge of the tree is independently labeled $A$ with probability $p$ and $B$ otherwise. Both players are able to inspect all of these labels. Then, starting with Aaron at the root of the tree, the players alternate turns moving a shared token down the tree (each turn the active player selects from the two descendants of the current node and moves the token along the edge to that node). If the token ever traverses an edge labeled $B,$ Beren wins the game. Otherwise2, Aaron wins.
>
>An example game is in the picture above: after the labeling, Aaron chooses to go left to avoid immediate defeat, but after Beren goes right Aaron is doomed to choose one of two $B$ paths and Beren wins.
>
>What is the infimum of the set of all probabilities p for which Aaron has a nonzero probability of winning the game? Give your answer in exact terms.

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/current-puzzle/))

## Solution

To get started, let's analyze Aaron and Beren's positions. 

Both can somehow inspect the entire tree, so there's no mystery about what they'll find in any sub-tree. Beren will win if at any level, she has a $B$-edge to choose. So, if Aaron is to win, there has to be at least one path from the beginning to infinity that alternates between $\{AA, AB, BA\}$ on the Aaron turns and $AA$ on the Beren turns.

Whenever we finish a Beren turn, we have an exact copy of the original situation. This means we can count ahead by two steps, and coarse grain over the rest of the turns.

Aaron can keep the game going forever if at least one of the branches he sees is infinite. So, the probability of an infinite game is the probability that one or the other leads to an infinite branch minus the probability that both do:

$$ P_\infty = 2p^3 P_\infty^2 - p^6 P_\infty^4. $$

We can divide through by $P_\infty$ (eliminating the trivial $P_\infty = 0$ solution) to get

$$ 1 = 2p^3 P_\infty - p^6 P_\infty^3. $$

<!-- So, the chance Aaron can keep the game going forever is the sum of the probabilities that

- Aaron sees $AA$, and at least one of them has two $A$ children with infinite branches,
- Aaron sees $AB$ or $BA$, and both of $A$'s children are $A$ with infinite branches.

The probability of the first case is $(2p^4 P_\infty2 - p^6 P_\infty^4)$ and the second is $2p^3(1-p)P_\infty^2.÷$ -->



<br>
