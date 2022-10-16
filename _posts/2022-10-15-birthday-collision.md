---
layout: post
published: false
title: Birthday collisions
date: 2022/10/15
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

I found three ways to solve this problem: by approximation, counting through recursion, and counting through combinatorics.

The first way is the most insightful and helps reveal what the exact solutions add to the picture, so we'll start there.

## Approximate argument

An exact way to treat the birthday twin case is to multiply the probability that the second person doesn't collide with the first $(1-1/365),$ with the probability that the third person doesn't collide with the first two $(1-2/365)$ and so on up to the $n^\text{th}$ person. The resulting expression is exact and at some point falls below $50%$ giving us the answer for birthday twins.

Each term in the product $(1-j/365)$ is approximately equal to $e^{-j/365}$ and so we can add up all the exponents $\frac{1}{365}\left(1 + 2 + \ldots + n\right) = n(n-1)/2$ and we end up with $P(\text{no collisions in }n\text{ people}) \approx e^{-n^2/(2!\cdot 365)}.$ This is nice but, but the logic doesn't easily extend to triplets and above.

A more audacious way to get the same result is to think about pairs. As long as no pair of people in the room share the same birthday, we keep adding new people. Among $n$ people there are $\binom{n}{2}$ possible pairs and the chance that any given pair has a collision is $\frac{1}{365},$ so the probability of no collisions among $n$ people is approximately

$$\left(1-\frac{1}{365}\right)^\binom{n}{2} \approx e^{-\dbinom{n}{2}/365}$$

The probability of **having** a collision among $n$ (or fewer) people is then $\text{cdf}(n) = 1 - e^{-\dbinom{n}{2}/365}.$

To find the average amount of people at which the collision first appears $n^*$, we can get the $\text{pdf}$ by differentiating the $\text{cdf}$

$$\text{pdf}(n) = \text{cdf}^\prime(n) \approx \dfrac{n}{365}e^{-n^2/(2!\cdot365)}.$$

The expected value of $n^*$ is then $\int\limits_0^{365}dn\ n\ \text{pdf}(n),$ or

$$
    \int\limits_0^{365}dn\ n \dfrac{n}{365}e^{-n^2/(2!\cdot 365)}
$$

<br>
