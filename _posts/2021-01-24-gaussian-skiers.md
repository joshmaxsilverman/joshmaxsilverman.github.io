---
layout: post
published: true
title: Gaussian Skiers
date: 2021/01/24
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

if the first skier wins the first round by $\Delta T,$ they will prevail so long as they don't lose the second round by more than $\Delta T.$ 

what's the probability that person A finishes $\Delta T$ ahead of person B?

$$ P(t_\text{A} - t_\text{B} = \Delta T) = \dfrac{1}{2\pi}\iint_\text{all} \delta(t_\text{A} - t_\text{B} = \Delta T) e^{-t_\text{A}^2/2} e^{-t_\text{B}^2/2} $$

<br>
