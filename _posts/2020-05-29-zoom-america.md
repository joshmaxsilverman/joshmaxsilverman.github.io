---
layout: post
published: false
title: Wherefore art thou superzoomer
date: 2018/04/21
---

>In one of the greatest disasters in collective planning all 330M residents of the U.S. join the same Zoom call by picking two random times between 8:00 and 9:00. They get on the call at the earlier time and get off at the later time. What is the probability that there is at least one person who is on for some portion of everyone else's call, the so-called Superzoomer? What is the chance of there being two Superzoomers on the same call?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/can-you-join-the-worlds-biggest-zoom-call/))

## Solution

### Insights

Under the surface fact that the zoom start- and end-times are random between 8:00 and 9:00 is the fact that they impose an order. The spacing between consecutive points can be scaled however we like — but each ordering of the points has the same set of possible spacings so. Finally, if we swapped the labels at random we'd have another valid call, so all orders are equally likely. So, spacings don't matter and all possible call schedules are equally probable.

If a Superzoomer exists they have to call in before the first person hangs up and they can't hang up until the last person starts. This means that they have one of the following relationships with every other person on the call:
1. it starts before them and ends after them
2. it starts before it does and ends before it does
3. it starts after does and ends after it does




<br>
