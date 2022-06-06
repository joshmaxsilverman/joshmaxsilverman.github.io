---
layout: post
published: false
title: Oasis Exodus
date: 2022/06/05
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

the basic idea is that two travelers will not intersect so long as the one on the right makes a clockwise angle with the one on the left.

first, we can go quick and dirty to get an idea of how the solution should scale. 

# approximate argument

as $N$ gets big about half of the travelers should be on the top or bottom. if we divide the angular real estate into equal sized chunks, then we need the travelers on the top each to pick an angle from $1/(\frac12 N)$ of the available choices. the same goes for the travelers on the bottom.

putting it all together, the probability of no intersection is roughly $P(N) = 2^N/N^N,$ so $P(N) \sim N^{-N}.$

# counting argument



<br>
