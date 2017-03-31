---
layout: post
published: true
title: Picnic Chances
date: 2017/03/31
---


>On a lovely spring day, you and I agree to meet for a lunch picnic at the fountain in the center of our favorite park. We agree that we’ll each arrive sometime from noon and 1 p.m., and that whoever arrives first will wait up to 15 minutes for the other. If the other person doesn’t show by then, the first person will abandon the plans and spend the day with a more punctual friend. If we both arrive at the fountain at an independently random time between noon and 1, what are the chances our picnic actually happens?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/what-are-the-chances-well-meet-for-lunch/))

## Solution:

![Picnic Graph](/img/Picnic.PNG)

This diagram shows all the possibilities of our arrival times. The green region is where we arrive within fifteen minutes of one another.  For any time $t$ (in hours after noon) you might arrive, my arriving at the same time puts us at the point $(t,t)$ on the center diagonal, and we meet so long as I arrive within fifteen minutes of you, putting us somewhere on the horizontal line segment that extends up to fifteen minutes in both directions from that point, that is, from $(t-.25,t)$ (or $(0,t)$ if $t-.25\leq 0$) to $(t+.25,t)$ (or $(1,t)$ if $t+.25\geq 1$).  The probability that we meet, then, is the area of the green region, which is easiest to calculate by subtracting from 1 the area of the white triangles. Each has area 9/32, and so the probability that we meet is 1 - 9/16, or 7/16.

<br>
