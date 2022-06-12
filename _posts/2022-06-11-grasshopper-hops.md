---
layout: post
published: false
title: Grasshopper hops
subtitle: Where will you find this mysterious creature?
tags: equilibrium detailed-balance rates
date: 2022/06/11
---

>**Question:** You are trying to catch a grasshopper on a balance beam that is 1 meter long. Every time you try to catch it, it jumps to a random point along the interval between 20 centimeters left of its current position and 20 centimeters right of its current position.
>
>If the grasshopper is within 20 centimeters of one of the edges, it will not jump off the edge. For example, if it is 10 centimeters from the left edge of the beam, then it will randomly jump to anywhere within 30 centimeters of that edge with equal probability (meaning it will be twice as likely to jump right as it is to jump left).
>
>After many, many failed attempts to catch the grasshopper, where is it most likely to be on the beam? Where is it least likely? And what is the ratio between these respective probabilities?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-catch-the-grasshopper/))

## Solution

to make this more concrete, we can think about infinitely many grasshoppers jumping around. we let them out at random positions on the beam and then let them hop around. the relative fraction of grasshoppers at position $x$ in this situation is equal to $p(x)$ in the single grasshopper problem. 

after a long time has gone by, the grasshoppers will reach an equilibrium state where the probability distribution isn't changing anymore. 

now, take a video of the grasshoppers hopping in the equilibrium state for a long time. if we play this movie backward, we wouldn't be able to tell the difference, since the probability distribution is constant in time. this means that the probability of any transition is the same as the probability of the reverse transition: $P(x\rightarrow y) = P(y\rightarrow x).$ 

the probability of observing the transition $x\rightarrow y$ is the probability of being at $x$ times the probability of transitioning to $y$ given a start at $x$

$$
  P(x\rightarrow y) = P(x)\cdot P(x \rightarrow y\rvert x)
$$

the time reverse equality means that

$$
  P(x) P(x\rightarrow y\rvert x) = P(y) P(y\rightarrow x\rvert y).
$$

with this in hand, we can peel off the probability distribution.

if we compare two points that have the full freedom of jumping to the left or right, then $P(x\rightarrow y\rvert x)$ is a uniform probability distribution for $x-0.2\leq y \leq x + 0.2,$ and likewise for $P(y\rightarrow x\rvert y).$ this means that $P(x) = P(y),$ and so $P(x) = \text{const.}$ from $0.2 \leq x\leq 0.8.$





<br>
