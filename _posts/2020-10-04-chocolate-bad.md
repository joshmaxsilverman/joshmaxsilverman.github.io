---
layout: post
published: true
title: A Bag of Chocolates
date: 2020/10/04
---

>Question

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-eat-all-the-chocolates/))

## Solution

At the bottom of this bag hides a small amplitude pendulum. But first we'll work out the structue of the bag's states and the transitions that happen between them.

### Intuition

When we start the game, we pick a chocolate, any old chocolate. No matter what it is, we'll eat it. 

But the next time we draw a chocolate, we'll eat it only if it's the same kind as the last one we picked. If it's different, then we start the game over with the remaining chocolates. 

Without doing any analysis we can see that if we have a big imbalance, like $100$ dark chocolates and $1$ soymilk chocolate, then we are overwhelmingly likely to draw a dark chocolate. 

It is always possible that, amidst our dark chocolate eating spree, we pick a soymilk chocolate. However, we wouldn't immediately eat it. Since our most recently consumed chocolate would have been dark, we'd have start the game over and draw another. Unless we pick the soymilk chocolate on the second draw as well, then we'll keep on chugging with dark. 

This shows an important property of the system: once we start eating a certain kind of chocolate, it's easier for us to keep eating it. The reason being that we have to "fail" twice to switch to the other one.

### Modeling

When we start the game, we have $m$ soymilk chocolates, $d$ dark chocolates, and no most recently consumed chocolate, so anything can happen. We call this state blank slate, or $\mathbf{BS}$ and the state of the system is denoted by $\left(m, d\right).$ 

From here we can select a soymilk chocolate with probability $m/\left(m+d\right)$ or a dark chocolate with probability $d/\left(m+d\right).$

<br>

