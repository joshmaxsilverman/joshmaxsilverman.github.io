---
layout: post
published: false
title: 
date: 2023/02/03
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

at each step, the song can either proceed to the next step (with probability $(1-f)$) or return to $N = 99$ bottles (with probability $f$). so, the expectation number of verses to finish from "$j$ bottles" is

$$ T_j = 1 + (1-f)T_{j-1} + fT_{N}. $$

plugging this back into itself a few times, and using the fact that $T_0 = 0$, we get

$$
  \begin{align}
      T_j &= 1 + (1-f)T_{j-1} + fT_{N} \\
          &= 1 + \left[(1-f) + (1-f)^2T_{j-2}\right] + \left[(1-f)f + f\right]T_{N} \\
          &= 1 + \left[(1-f) + (1-f)^2 + (1-f)^3T_{j-3}\right] + \left[(1-f)^2f + (1-f)f + f\right]T_{N} \\
          &= \left[1 + (1-f) + (1-f)^2 + \ldots + (1-f)^{j-1}\right] + f\left[1 + (1-f) + (1-f)^2 + \ldots + (1-f)^{j-1}\right]T_{N} \\
          &= \dfrac{1 - (1-f)^j}{f} + \left(1 - (1-f)^{j}\right)T_{N}
  \end{align}
$$

so, $T_{N-1} = \left[f^{-1}\left(1 - (1-f)^{N-1}\right) + \left(1 - (1-f)^{N-1}\right)T_{N}\right]$

plugging this into the equation for $T_{N},$ we get

$$
  \begin{align}
    T_{N} &= \frac{1}{1-f} + \dfrac{1-(1-f)^{N-1}}{f} + \left[1-(1-f)^{N-1}\right]T_{N} \\
    &= \dfrac{f+1-f-(1-f)^N}{(1-f)f}\dfrac{1}{(1-f)^{N-1}} \\
    &= \frac{1}{f}\left[\dfrac{1}{(1-f)^{N}}-1\right]
  \end{align}
$$

since the probability of forgetting is staked to $f=1/N,$ $T_N$ becomes

$$ T_N = N\left[\dfrac{1}{(1-1/N)^{N}}-1\right], $$

so $T_N/N$ approaches $(e-1)$ as $N$ gets big.


<br>
