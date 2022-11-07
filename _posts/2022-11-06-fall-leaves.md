---
layout: post
published: false
title: Fall colors
date: 2022/11/06
subtitle:
tags:
---

>Question

<!--more-->




([FiveThirtyEight](URL))

## Solution


<!-- We want to know the probability that a single tree will have its fall colors at time $t$, $P(\text{color at }t).$ -->

The leaves can start changing at any time up until $t,$ so the chance that a single tree will have its fall colors at time $t$, $P(\text{color at }t),$ is

$$ P(\text{color at }t) = \int\limits_0^t\text{d}t_\text{c}\ P(\text{color at }t\rvert t_\text{c})P(t_\text{c}). $$

Given $t_\text{c},$ the probability that the tree is colored at time $t$ is 

$$ P(\text{color at }t\rvert t_\text{c}) = 
\begin{cases}
\dfrac{T-t}{T-t_\text{c}} & t \geq t_\text{c} \\
0 & t < t_\text{c}
\end{cases}.
$$

So, 

$$ P(\text{color at }t) = \int\limits_0^t\text{d}t_\text{c}\dfrac{T-t}{T-t_\text{c}}\dfrac{1}{T} = \dfrac{T-t}{T}\log\dfrac{T}{T-t}. $$

Changing variables to $t^\prime = t/T,$ we have

$$-(1-t^\prime)\log (1-t^\prime),$$ which is maximized when $\log (1-t^\prime)=-1,$ e.g. when $t^\prime=1-1/e.$

<!-- For this to hold, the time of color change has to be less than $t,$ and the time of leaf fall has to be greater than $t:$ -->

<!-- $$t_\text{f} > t > t_\text{c}. $$ -->

<br>
