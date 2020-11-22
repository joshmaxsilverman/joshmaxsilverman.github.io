---
layout: post
published: true
title: Pass the Cranberry Sauce
date: 2020/11/22
---

>**Question**: it's Thanksgiving and your family is gathered 'round the circular dinner table, Tofurkey in the middle, as is tradition. When the time comes, your Aunt Riddla brings out her famous cranberry sauce, handing it to you to place on the table. Wherever you place it, the person sitting there will take some sauce and then pass it randomly to one of their neighbors with probability $r$ to the right, and probability $\ell$ to the left. 

This placement is no small decision though. You want to punish your naughty Uncle Zach so that he gets the cranberry sauce last! Where should you start the sauce off on its journey if you want Uncle Zach to be the most likely to be the last person to get that famous cranberry sauce?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-pass-the-cranberry-sauce/))

## Solution

the cranberry sauce on the table sweeps out a widening arc of diners who've had it, dividing the table into two sections. if the sauce wanders inside the arc, then nobody new gets the sauce, and if it reaches the egde then the arc expands. 

by construction, the section of people who have not had the sauce is continous, and winnows from each side until there's only one person left. 

### Neighbor to neighbor

for someone to be the last person remaining, the arc of the visited has to broaden til it reaches their neighbors, one after the other. for instance, if the sauce meandered its way from position $1$ to position $11$ (without hitting position $9$ in the process) before turning around and meandering its way to position $9$ (without hitting position $10$ in the process), then the person at position $10$ would be the last to receive the sauce.

of course it could also have happened in the reverse order, meandering clockwise to visit position $9$ (without hitting position $11$) before meandering back to position $11$ (without hitting position $10$).

the probability for the person at position $i$ to be the last one visited is the sum of the probability of these two events

$$ P(i) = P(1\rightarrow (i-1)\setminus (i+1))\times P((i-1)\rightarrow (i+1)\setminus i) + P(1\rightarrow (i+1)\setminus (i-1))\times P((i+1)\rightarrow (i-1)\setminus i) $$

### Unrolling the table

### Evolutionary fixing

### Being last

### Cases and graphs

### A time to be alone

<br>
