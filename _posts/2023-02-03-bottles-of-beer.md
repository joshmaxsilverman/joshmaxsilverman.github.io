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

at each step, the song can either proceed to the next step (with probability $(1-f)$) or return to $99$ bottles (with probability $f$). so, the expectation number of verses to finish from "$j$ bottles" is

$$ T_j = 1 + (1-f)T_{j-1} + fT_{99}. $$

plugging this back into itself a few times, we get

$$
  \begin{align}
      T_j &= 1 + (1-f)T_{j-1} + fT_{99} \\
          &= 1 + \left[(1-f) + (1-f)^2T_{j-2}\right] + \left[(1-f)f + f\right]T_{99} \\
          &= 1 + \left[(1-f) + (1-f)^2 + (1-f)^3T_{j-3}\right] + \left[(1-f)^2f + (1-f)f + f\right]T_{99} \\
          &= \left[1 + (1-f) + (1-f)^2 + \ldots + (1-f)^{j-1}\right] + f\left[1 + (1-f) + (1-f)^2 + \ldots + (1-f)^j\right]T_{99} \\
          &= \dfrac{1 - (1-f)^j}{f} + \dfrac{1 - (1-f)^{j-1}}{f}T_{99}
  \end{align}
$$


<br>
