---
layout: post
published: true
title: Social Distance Swimming Pool
date: 2020/07/04
---

>Question: It's 8:59 at the 10-lane town pool and the coronavirus is absolutely ripping. In an effort to mitigate the spread, swimmers must stay at least one lane apart. In one minute, the swimmers will hop into the pool, one lane at a time, until it becomes impossible to obey social distancing. If there are 10 swimmers, how many do you expect to be left crying on the side of the pool?

<!--more-->

([FiveThirtyEight](URL))

## Solution

The easiest way to get started on this problem is to get started on this problem. 

Suppose the first swimmer jumps in and she goes into the fourth lane. By the social distancing rule, this means that no other swimmer can go into the third lane or the fifth lane. We effectively now have two copies of the original problem playing out in lanes $1$ through $2$ ($2$ lanes) and in lanes $6$ through $10$ ($5$ lanes).

In other words, the total number of swimmers we expect, given that the first swimmer hopped into lane $4$ is the swimmer in lane $4$ plus the expected number of swimmers in a $2$ lane pool plus the expected number of swimmers in a $5$ lane pool.

$$E(10 | \text{first swimmer in lane 4}) = 1 + E(2) + E(5)$$

If the first swimmer had instead gone into the second lane, we'd get 

$$E(10 | \text{first swimmer in lane 2}) = 1 + E(7)$$

Since there's an equal chance of the first swimmer going in any lane, the expected number of swimmers in the pool is

$$E(10) = \frac{2\left(1 + E(8)\right) + 2(1 + E(7)) + 2(1 + E(1) + E(6)) + 2(1 + E(2) + E(5)) + 2(1 + E(3) + E(4)}{N}$$

<br>
