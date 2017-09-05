---
layout: post
published: true
title: Foul Shots
date: 2017/09/05
---

>You’re hanging out with some friends, shooting the breeze and talking sports. One of them brags to the group that he once made 17 free throws in a row after years of not having touched a basketball. You think the claim sounds unlikely, but plausible. Another friend scoffs, thinking it completely impossible. Let’s give your bragging friend the benefit of the doubt and say he’s a 70-percent free-throw shooter.
>
>So, who’s right? What is the number of free throws that a 70-percent shooter would be expected to take before having a streak of 17 makes in a row? And what if his accuracy was a bit worse?

<!--more-->

[(fivethirtyeight.com)](https://fivethirtyeight.com/features/is-your-friend-full-of-it/)

## Solution

Let $E_n$ denote the expected number of shots it will take to make $n$ in a row, and suppose you have a $p$ chance of making each shot.  

When you first make $n-1$ shots in a row (at expected shot $E_{n-1})$ you have a $p$ chance of first making $n$ in a row with one more shot and $(1-p)$ chance of missing that next shot and being back on square one, expecting to need $E_n$. So:

$$E_n = E_{n-1} + p(1) + (1-p)(E_n+1)$$

Solving,

$$E_n = \frac{1}{p} + \frac{1}{p}E_{n-1} $$

Since $E_0$ is zero, $E_1$ is $1/p$, $E_2$ is $1/p+1/p^2$, and in general:

$$E_n = \sum_{i=1}^n\frac{1}{p^i}$$

By a well-known formula for partial sums of [a geometric series](http://mathworld.wolfram.com/GeometricSeries.html),

$$E_n = \frac{1}{p}\left(\frac{1-\frac{1}{p^n}}{1-\frac{1}{p}}\right)$$

For $p=.7$ and $n=17$, this is about $1430$ shots.
