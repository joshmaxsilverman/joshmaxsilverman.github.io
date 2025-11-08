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

now, the probability to remain at door $2$ flip flops between $\frac{2}{10}$ and $\frac12.$ because the effective rate of staying at door $2$ is higher, we should expect the contestant to stay at doors $1$ and $3$ more often as well to compensate. so $\gamma^\prime > \gamma.$

the transition from an even turn to an odd turn has the same relationships we worked above, so

$$ \begin{align}
P_1^\text{odd} &= \gamma^\prime P_1^\text{even} + \frac{4}{10}P_2^\text{even} \\
P_2^\text{odd} &= \left(1-\gamma^\prime\right) \left[P_1^\text{even} + P_2^\text{even}\right] + \frac{2}{10}P_2^\text{even} \\
P_3^\text{odd} &= \gamma^\prime P_3^\text{even} + \frac{4}{10}P_2^\text{even}
\end{align} $$

the transition from odd to even has the same structure, with a new rate for staying at door $2$

$$ \begin{align}
P_1^\text{even} &= \gamma^\prime P_1^\text{odd} + \frac14 P_2^\text{odd} \\
P_2^\text{even} &= \left(1-\gamma^\prime\right) \left[P_1^\text{odd} + P_2^\text{odd}\right] + \frac12 P_2^\text{odd} \\
P_3^\text{even} &= \gamma^\prime P_3^\text{odd} + \frac14 P_2^\text{odd}
\end{align} $$

we can plug the first set of equations into the equation for door $1$ to get

$$ P_1^\text{even} = \gamma^\prime\left(\gamma^\prime P_1^\text{even} + \frac{4}{10}P_2^\text{even}\right) + \frac14\left(\left(1-\gamma^\prime\right) \left[P_1^\text{even} + P_2^\text{even}\right] + \frac{2}{10}\frac14P_2^\text{even}\right). $$

since the aim is for these probabilities to become equal, this equation becomes

$$ 1 = {\gamma^\prime}^2 + \gamma^\prime\frac{4}{10} + 2\frac14\left(1-\gamma^\prime\right) + \frac14\frac{2}{10} $$

or

$$ 0 = {\gamma^\prime}^2 -\frac{1}{10}\gamma^\prime -\frac{3}{10} $$

which has positive root 

<br>
