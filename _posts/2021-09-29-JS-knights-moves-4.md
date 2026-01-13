---
layout: post
published: false
title: Knights moves four
date: 2021/09/29
subtitle: How many knight moves cover the board?
source: fivethirtyeight
theme: algorithms
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

Before starting in on the search for the knight's path, we can figure out how many moves they made.

Because there are 17 regions, and each region sums to the same total, the sum of all numbers is divisible by 17:

$$ 
\frac12 N(N+1) \bmod 17 = 0.
$$

Also, the knight's $\mathbf{L}$ move alternate between two subgrids, so the smallest region contains an odd and an even. This means that the common sum is odd. 

<br>
