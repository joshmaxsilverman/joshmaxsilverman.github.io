---
layout: post
published: true
title: Century Product
date: 2019/02/08
---

>Given any three random integers — X, Y and Z — what are the chances that their product is divisible by 100?


<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/525600-minutes-of-math/))


## Solution

Reading the question charitably (since "random integer" has no specific meaning), there will be an answer if there is a limit for a uniform distribution of positive integers up to some number $N$. But we can ignore that technicality, and make do with the idealization that since every second, fourth, fifth, and twenty-fifth integer are divisible by $2, 4, 5,$ and $25$, the chances of getting a random integer divisible by those numbers are $1/2$, $1/4$, $1/5$, and $1/25$.

The product $XYZ$ is divisible by $100$ if and only if it has at least two factors of $2$ and at least two factors of $5$.  The chance that it has at least two factors of $2$ is $1$ minus the chance that it has exactly zero factors of $2$ (which is $(1/2)^3$ or $1/8$) and minus the chance that it has exactly one factor of $2$.  It has exactly one factor of two if one of the three numbers itself has exactly one factor of $2$ and the other two are odd.  A number has exactly one factor of $2$ if it is one of the half of all even numbers that is not divisible by $4$; so $1/2$ times $1/2$, or $1/4$ of all numbers have this property.  So:

$$P(\text{XYZ divisible by 4}) = 1 - 1/8 - 3 \times 1/4 \times (1/2)^2 = 5/16$$

The calculation of the chance that $XYZ$ is divisible by $25$ is similar.  In this case, the chance that a number has exactly one factor of $5$ is the chance that it has at least one (which is $1/5$) minus the chance that it has at least two (which is $1/25$). So:

$$P(\text{XYZ divisible by 25}) = 1 - (4/5)^3 - 3 \times (1/5 - 1/25) \times (4/5)^2 = 512/625$$

These two probabilities are independent, because every twenty-fifth number divisible by $4$ is also divisible by $25$ (and vice versa).  Therefore the probability that $XYZ$ is divisible by both $4$ and $25$, that is, that it is divisible by $100$, is their product, which is exactly $.1243$.

<br>
