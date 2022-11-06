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


We want to know the probability that a single tree will have its fall colors at time $t$, $P(\text{color at }t).$

The leaves can start changing at any time up until $t,$ so

$$ P(\text{color at }t) = \int\limits_0^t\text{d}t_\text{c}\, P(\text{color at }t\rvert t_\text{c})P(t_\text{c}). $$

Given that $t > t_\text{c},$ the probability that $t_\text{f} > t$ is 

$$ P(\text{color at }t\rvert t_\text{c}) = \dfrac{T-t}{T-t_\text{c}}. $$

So, 

$$ P(\text{color at }t) = \int\limits_0^t\text{d}t_\text{c}\dfrac{T-t}{T-t_\text{c}}\dfrac{1}{T} = \dfrac{T-t}{T}\log\dfrac{T}{T-t}. $$

Changing variables to $t = t/T,$ 
<!-- For this to hold, the time of color change has to be less than $t,$ and the time of leaf fall has to be greater than $t:$ -->

<!-- $$t_\text{f} > t > t_\text{c}. $$ -->

<br>
