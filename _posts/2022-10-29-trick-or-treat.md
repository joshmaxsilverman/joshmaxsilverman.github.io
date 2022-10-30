---
layout: post
published: false
title: Neurotic Halloween
date: 2022/10/29
subtitle: How close can you get to perfect candy disbursement?
tags:
---

>**Question**:

<!--more-->

([FiveThirtyEight](URL))

## Solution

The approach is roughly

- illuminate the logic with the worst cases
- solve the problem, pretend the chocolate is continuous
- update the approach for discrete chocolates
- calculate the expectation
- make sure that physics chutzpah didn't mislead us by resolving with dynamic programming

### Worst case

If we want to incur the maximum average penalty, we can either always dispense $3$ chocolate or always dispense $1$ chocolate. 

In the first case, we'll run out of chocolate by the $50^\text{th}$ trick or treater (ToT) and so, $X$ (our penalty) will always be $50.$ In the second case, we'll have $100$ candies left by the $50^\text{th}$ ToT and, so, have an average of $50$ candies left over after the last ToT has come to the door. 

Evidently, the optimal approach is something between these two extremes.

### Chocolate continuum 

The penalty is symmetric with respect to leftover candy and unserved ToTs, so we should aim to run out of candies precisely at the average number of ToTs, dispensing $150/100 = 1.5$ chocolates each visit until we run out. 

If we aimed slightly beyond $100,$ we'd be 

any candy that's left after the $50^\text{th}$ ToT will contribute to our penalty. 

so we should aim to run out of candy by the $100^\text{th}$ ToT (the average number of ToTs).

On average, there will be $100$ ToTs. So, if we were free to divide the chocolate anyway we like, then we would want to 

### Discrete adjustment

### Expectation penalty

### Optimality check



<br>
