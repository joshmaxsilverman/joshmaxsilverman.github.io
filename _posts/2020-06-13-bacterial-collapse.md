---
layout: post
published: true
title: Bacterial Collapse
date: 2020/06/13
---

>A bacterial colony starts from a single cell that has a probability $\gamma$ of splitting into $2$ and a probability $1-\gamma$ of dying, as do all of its descendants. What's the probability that the colony is blessed with everlasting propagation? (e.g. the population never crashes to zero)

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/how-long-will-the-bacterial-colony-last/))

## Solution

The strain in question is _Riddlerium classicum_, about which not much is known apart from its cataclysmic reproductive viability (real bacteria are far more sucessful, Fig 4 in [Robust Growth of _Escherichia coli_](https://jun.ucsd.edu/files/publications/RobustGrowth_complete_CurrBiol2010.pdf)). Each cell that's born has a $20\%$ chance of dying, and an $80\%$ chance of forking into two new cells, each of which then have the same odds. 

### Colony viability

Before answering the main question, there's the issue of when the colony will be viable in the first place ($P_\infty > 0$ to be everlasting). 

The basic insight is that we need the expected number of cells in the next generation to be greater than $1$. In that case, the average outcome after one generation is that we have a solitary cell with the same existential crisis on its hands. 

So, if $\gamma < 1/2,$ we should expect $P_\infty = 0.$

### Colony flourishing

What if we want to go beyond the prayer of survival — how big does $\gamma$ need to be to push $P_\infty$ to whatever level we like? On first glance it seems like this could turn into a nested labyrinth of tracking the outcome for each branch of the lineage. 

However, each cell has the same prospects so the probability that the first cell leads to an everlasting colony is equal to the probability that either of its children leads to an everlasting colony. 

Symmetrically, the probability that the first cell leads to a finite colony is equal to the probability that it dies plus the probability that it reproduces, but both of its children's colonies spawn finite colonies.

Writing down the second of these,

$$P_\text{die} = (1-\gamma) + \gamma P_\text{die}^2.$$

This can be solved with the quadratic equation but if we divide by $P_\text{die}$ 

$$1 = \frac{(1-\gamma)}{P_\text{die}} + \gamma P_\text{die}$$

it's a little easier to see that $P_\text{die} = \left(1-\gamma\right)/\gamma.$

A colony either collapses or it doesn't, so $P_\text{die} + P_\infty = 1$ and 

$$P_\infty = 1 - \dfrac{1-\gamma}{\gamma} = \dfrac{2-\gamma}{\gamma}$.$






<br>
