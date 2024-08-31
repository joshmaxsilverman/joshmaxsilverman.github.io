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

Both can somehow inspect the entire tree, so there's no mystery about what they'll find in any sub-tree. Beren will win if at any level, they have a $B$ to choose. So, if Aaron is to win, there has to be a path from the beginning to infinity that alternates between $\{AA, AB, BA\}$ on Aaron turns and $AA$ on Beren turns.



<br>
