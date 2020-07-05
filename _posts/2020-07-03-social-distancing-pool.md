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

Suppose the first swimmer jumps in and she goes into the $4^\text{th}$ lane. By the social distancing rule, this means that no other swimmer can go into the $3^\text{rd}$ lane or the $5^\text{th}$ lane. We effectively now have two copies of the original problem playing out in lanes $1$ through $2$ ($2$ lanes) and in lanes $6$ through $10$ ($5$ lanes).

In other words, the total number of swimmers we expect, given that the first swimmer hopped into lane $4$ is the swimmer in lane $4$ plus the expected number of swimmers in a $2$ lane pool plus the expected number of swimmers in a $5$ lane pool.

$$E(S_{10}\midd \text{swimmer in 4}) = 1 + E(S_2) + E(S_6)$$



<br>
