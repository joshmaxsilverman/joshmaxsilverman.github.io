---
layout: post
published: true
title: Pinball Lights
date: 2023/10/01
subtitle: How many shots does it take to turn the lights on?
tags: master-equation
---

>**Question**:

<!--more-->

([FiveThirtyEight](URL))

## Solution

let's think about the pinball machine as a series of states corresponding to the number of lit lights.

each time we shoot a ball, we move from state to state. if there are $j$ lights turned on, then we have probability $j/N$ to move down, and probability $(1-j/N)$ to move up.

bypassing the explicit probability distribution, we can relate the expected waiting time from state $j$ to the expected waiting time from states $(j-1)$ and state $(j+1)$:

$$ 
\begin{align}
  T_j &= \dfrac{j}{N}(1 + T_{j-1})  + (1-\dfrac{j}{N})(1+T_{j+1}) \\
      &= 1 + \dfrac{j}{N}T_{j-1}  + (1-\dfrac{j}{N})T_{j+1}
\end{align}
$$

by construction, this reflects the impossibility for state $j=0$ to move down (to $j=-1$) or for state $j=N$ to move up. also, by definition, $T_N = 0,$  since all the lights are lit.

we can solve the system of equations for each value of $N$ and plot the ratio of consecutive waiting times as a function of $j.$ evidently, the ratio is minimized at $j=6$ where 

$$ \dfrac{T_7}{T_6} = \frac{151}{78}, $$

which is about $2.5\%$ under the asymptotic value $2.$

![](/img/2023-10-01-pinball-plot.png){:width="450 px" class="image-centered"}



<br>
