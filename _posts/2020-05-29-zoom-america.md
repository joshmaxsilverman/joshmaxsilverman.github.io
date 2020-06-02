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

### Realizations

Under the surface fact that the zoom start- and end-times are random between 8:00 and 9:00 is the fact that they impose an order. The spacing between consecutive points can be scaled however we like — but each ordering of the points has the same set of relative spacings so, only their order is relevant. Finally, if we swapped the labels at random we'd have another valid call, so all orders are equally likely.

### Wherefore art thou super zoomer?

If one interval overlaps with every other then it has one of the following relationships with all other intervals:
1. it starts before them and ends after them
2. it starts before it does and ends before it does
3. it starts after does and ends after it does

If a person is the Superzoomer, they'll have to get on the call before the first person gets off the call. We can find the first leaver by starting at $8:00$ and stepping forward until we find the first hangup. This is Caller A.

The Superzoomer either starts inside this interval (check understanding: why couldn't they finish _inside_ this interval?), or fully contain this interval. 

So, turn back and find the first pair of endpoints you traverse (when you hit 8:00, loop around to 9:00), this is Caller B. If  Caller B starts after 8:00, then Caller B overlaps with all other callers.

That's because Caller B starts before the first finisher, and there are no callers who start after Caller B gets off the call.

But if Caller B doesn't start by 8:00, it means that they start after Caller A (the first ender). Moreover, there is no Caller C who encompasses both of them, since they would have been identified as Caller B.

### How many times are we going to try this?

Since all orders are equally likely, the three circle diagrams each occur a third of the time. As there's a Superzoomer in two of them, the probability of a universal called is $p_\text{superzoomer} = 2/3.$


If a Superzoomer exists they have to call in before the first person hangs up and noone can call in after they hang up. 


<br>
