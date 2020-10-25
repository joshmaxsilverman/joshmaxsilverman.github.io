---
layout: post
published: true
title: The Battle of Los Angeles
date: 2020/10/24
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

On first glance, Davis has a pretty nice advantage since he takes possession of the ball after every missed three point shot. However, Lebron has a chance to steal **every** time Davis takes possession. If Lebron was barred from stealing in the case where Davis starts the game with the ball, then the 1:1 would be perfectly symmetric if the probability $L_\text{steal}$ was $1/2.$ Since Lebron can steal in the first possession, we should expect the $L_\text{steal}$ required for a fair game to be something less than $1/2.$

### Half-court pinball

To start, it's good to get a handle on the kinds of games we can expect.

Lebron could start with the ball, shoot and miss, steal it from Davis, shoot and miss again, before Davis shoots and misses, before Lebron fails to steal the ball, before Davis shoots and scores. Just as easily, Davis could take the first possession, Lebron could fail to steal, and then Davis could score on his first shot attempt. There are $7$ steps in the first version and $3$ in the second, and there infinitely many other cases to consider, some of which are infinitely long.

Despite the variety, we can diagram the possibilities in three main steps. The first is from the beginning of the game $\mathbf{B],$ the second is Lebron possessing the ball $\mathbf{L}$ and the third is Lebron scoring $\mathbf{S}.$ 

From the top, Lebron can start with the ball (probability $1/2$), or it can go to Davis who shoots and misses $0$ or more times before Lebron steals it. If Davis shoots it and misses, it means that Lebron failed to steal it, so the probability for Davis to miss a shot is $\left(1-L_\text{steal}\right)D_\text{miss}.$

Since the steps

$$\text{Lebron fails to steal} \rightarrow \text{Davis misses}$$ 

return to the same state (Davis possessing the ball), they can form loops of arbitrary length, and the total probability that Lebron comes into possession of the ball is

$$\frac12 + \frac12L_\text{steal} + \frac12\left(1-L_\text{steal}\right)D_\text{miss}L_\text{steal} + \frac12\left(\left(1-L_\text{steal}\right)D_\text{miss}\right)^2 L_\text{steal} + \ldots $$

which is just

$$\frac12 + \dfrac{L_\text{steal}}{1 - \left(1-L_\text{steal}\right)D_\text{miss}}.$$

<br>
