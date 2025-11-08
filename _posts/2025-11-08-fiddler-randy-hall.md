---
layout: post
published: false
title: 
date: 2025/11/08
subtitle:
tags:
---

>Question

<!--more-->

([Fiddler on the Proof](URL))

## Solution

### Standard credit

the contestant can be at door $1$ at time $(t+1)$ because they were there and stayed put or because they came from door $2$

$$ P_1(t+1) = \gamma P_1(t) + \frac{4}{10}P_2(t). $$

likewise, contestant can be at door $2$ at time $(t+1)$ because they came from doors $1$ or $3$ or because they were already there and stayed put

$$ P_2(t+1) = (1-\gamma)\left[P_1(t) + P_3(t)\right] + \frac{2}{10}P_2(t), $$

and the equation for door $3$ has the same form as for door $1.$

(we don't actually need all of these equations, but it's good setup for the extra credit where we will)

the point is to arrange so that the probability of being at any of the three doors is equal, so the first equation becomes

$$ 1 = \gamma + \frac{4}{10}$$

or $\gamma = \frac{6}{10}. $

### Extra credit

now, the probability to remain at door $2$ flip flops between $\frac{2}{10}$ and $\frac12.$

the transition from an even turn to an odd turn has the same relationships we worked above, so

$$ \begin{align}
P_1^\text{odd}(t+1) &= \gamma P_1^\text{even}(t) + \frac{4}{10}P_2^\text{even}(t) \\
P_2^\text{odd}(t+1) &= \left(1-\gamma\right) \left[P_1^\text{even}(t) + P_2^\text{even}(t)\right] + \frac{2}{10}P_2^\text{even}(t) \\
P_3^\text{odd}(t+1) &= \gamma P_3^\text{even}(t) + \frac{4}{10}P_2^\text{even}(t)
\end{align} $$

<br>
