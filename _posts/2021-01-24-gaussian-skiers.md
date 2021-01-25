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

If the first skier wins the first round by $\Delta T_1,$ they will prevail so long as they don't lose the second round by more than $\Delta T_1.$ 

The gap between the first round times $\left(\Delta T_1 = t^\text{A}_1 - t^\text{B}_1\right)$ which has some symmetric distribution $P(\Delta T_1).$ Since we know that person $\text{A}$ won the first round, we condition on the left side of $P$ and the expected value of $\Delta T_1$ is whatever the $25^\text{th}$ percentile of the distribution is. 

If person $\text{A}$ is to win overall, $\Delta T_1$ has to be less than or equal to $-\Delta T_2.$ The gap in the second round is a random variable from the same distribution, so the chance that $\Delta T_1 < -\Delta T_2$ is $1 - 0.25 = 0.75.$

So, the probability that person $\text{A}$ wins is $75\%.$


<br>
