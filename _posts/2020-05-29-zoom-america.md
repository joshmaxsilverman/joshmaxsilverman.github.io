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
1. Superzoomer calls in before them and hangs up after them
2. Superzoomer calls in before them and hangs up before them
3. Superzoomer calls in after them and hangs up after them

Some Superzoomers look like this:

[stack of three superzoomer examples, superzoomer arc in blue]

Thinking about the forward problem got us very little — we couldn't see a recursion and we couldn't organize the combinatorics. This got us thinking, what would it take to dismantle a Superzoomer, e.g., what is the minimal surgery we'd have to do to erase the Superzoomer? 

Necessarily, we have to snip the edge of the Superzoomer. But if that's all we do, we can only reconnect that edge. So we have to cut another edge. If you do this enough times you start to see that it's always possible to pick the two edges to cut. Moreover, when you reconnect those edges, there are $3$ possible pairings, and $2$ of them make a Superzoomer.

Similarly, if you start with a call schedule that has no Superzoomer, you can trivially create one. Pick two slots such that if they were connected, they'd make a Superzoomer, connect them (making the Superzoomer), and then connect their former connected slots to form a new pair. 

Keeping on with this game, you can do the same with $2$ Superzoomers by cutting $3$ edges, with $3$ Superzoomers by cutting $4$ edges, and so on.

This is an exhilarating realization, but is it a mirage? Aren't we 


<br>
