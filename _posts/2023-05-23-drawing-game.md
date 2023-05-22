---
layout: post
published: false
title: 
date: 2023/05/23
subtitle:
tags:
---

>**Question**:
>

<!--more-->

([FiveThirtyEight](URL))

## Solution

each time we draw a number $k,$ we have to figure out if it's worth more to cash it in, or to hedge so that there are $(h+k)$ numbers in the bowl to start the next round, taking into account how many rounds we have left, $\ell.$

### approximate argument

crudely, if we decide to cash in for $n$ rounds in a row, the expected value of play is 

$$n\langle k \rangle = \frac12 nh.$$

if we decide to hedge for the first $(n-1)$ turns, and cash in on the last, the expected value of play is 

$$ \frac12 \left(\frac{h+\frac12h}{h}\right)^{n-1} h = \frac12 \left(\frac32\right)^{n-1}h, $$

since we expect to raise the highest number $h$ by $\frac12h$ on each draw, and the expected value of the cash in is half the highest number at the time of the draw.

the hedging strategy wins out at $n=4.$

<br>
