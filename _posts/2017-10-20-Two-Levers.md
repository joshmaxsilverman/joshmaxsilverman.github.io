---
layout: post
published: false
title: Two Levers
date: 2017/10/20
---

>One hundred prisoners are put into 100 completely isolated cells, numbered 1 to 100. Once they are in their cells, they cannot communicate with each other in any way. They are taken by the warden one at a time, but in no particular order, to a special room, Cell 0, in which there are two levers. As the prisoners enter the room, each lever is either up or down, but the levers’ starting positions are unknown. When in the room, a prisoner must flip exactly one of the levers. At any point, any prisoner may declare to the warden that all of the prisoners have been to the room. (The warden will take prisoners to the room indefinitely until someone makes a guess.) If the prisoner is correct, they are all released. If not, they are all executed.
>
>Knowing these rules, what strategy can the prisoners devise beforehand that will guarantee their release? How many trips to Cell 0 will it take on average before they are released?

<!--more-->

[(fivethirtyeight.com)](https://fivethirtyeight.com/features/can-you-please-the-oracle-can-you-escape-the-prison/)

## Solution

Designate one prisoner the Counter. Every time the Counter enters the room, if the left lever is down she adds $1$ to her tally, and flips it up; otherwise she toggles the right lever. Each other player, on their first two visits to the room in which the left lever is up, flips it down and otherwise toggles the right lever.

When the Counter has counted $198$, she knows that either the left lever started in the up position and all $99$ of the other prisoners have flipped it down twice, or it started in the down position and all but one of the other prisoners has flipped it down twice, that one prisoner having flipped it once. She tells the warden that all prisoners have been to the room.

To calculate the expected number of trips, we will assume that the levers' starting positions are not just unknown but up or down with probability $1/2$.

We'll first assume that the warden has flipped the left lever down at the start, so that the game ends when $98$ prisoners have flipped it down twice, the remaining prisoner once, and the Counter then arrives.  Now, suppose the left lever is newly flipped down, either by the warden or by one of the prisoners, and that $m$ prisoners have flipped the left lever just once and $n$ have flipped it twice. Let $E(m,n)$ be the expected number of remaining visits. We are looking for $E(0,0)$.  

If $98$ prisoners have flipped it down twice and the remaining prisoner once, then the game ends when the Counter next visits, which, given the $1/100$ probability of her visiting each time, is expected to be $100$ more visits. So we know that:

$$E(1,98) = 100$$

Suppose there are $m$ prisoners who have visited once and $n$ twice. Then we expect the Counter to visit and flip the lever back up in $100$ visits. After the next visit after that there is $m/100$ chance that one of those $m$ visitors will have now visited twice and so we'll expect $E(m-1,n+1)$ more visits. There is $(n+1)/100$ chance one of the $n$ prisoners or the Counter will have visited, so that we'd expect $E(m,n)-100$ more visits (the game is in state $(m,n)$ and the Counter has already arrived). And there is $(99-m-n)$ chance that a prisoner who hadn't yet flipped the left lever has now done so, so that we'd expect $E(m+1,n)$ more visits. Therefore:

$$E(m,n) = 101 + \frac{m}{100}E(m-1,n+1) +
\frac{n+1}{100}\left(E(m,n)-100\right) + 
\frac{99-m-n}{100}E(m+1,n)$$

$$E(m,n) = \frac{100}{99-n}\left(
100 - n + \frac{m}{100}E(m-1,n+1) +
\frac{99-m-n}{100}E(m+1,n)\
\right)$$

This lets us calculate that $E(0,0)$ is about $20,528$.

If the left lever starts in the up position, then the game will end when all $99$ prisoners have flipped it down twice, and then the Counter arrives. So we replace our initial condition in the recurrence with:

$$E(0,99) = 100$$

And because we expect the first non-Counter to visit in $100/99$ visits, we have:

$$E(0,0) = \frac{100}{99} + E(1,0)$$

This turns out to be a quicker $20,428$ visits, and so we average $20,478$ visits.

### Code (Python)

```python
# E(m,n) is the expected remaining number of visits when
# the game is newly in state (m,n) (meaning that m prisoners
# have flipped the lever just once and n twice) and the
# left lever is down.

# Lever starts down, in state (0,0)
E = {}
# Games ends at (1,98) plus 100 for Counter to arrive
E[(1,98)] = 100
for n in range(98,-1,-1):
	for m in range(99-n,-1,-1):
		if (m,n) == (1,98):
			continue
		Expect = 100 - n
		if m > 0:
			Expect += (m/100.0)*E[(m-1,n+1)]
		if m < 99-n:
			Expect += ((99-m-n)/100.0)*E[(m+1,n)]
		E[(m,n)] = Expect * (100.0/(99-n))
E_down = E[(0,0)]
print "Lever starts down:", E_down

#Lever starts up (the game is never in state (0,0))
E = {}
# Game ends at (0,99) plus 100 for Counter to arrive
E[(0,99)] = 100
for n in range(98,-1,-1):
	for m in range(99-n,-1,-1):
		Expect = 100 - n
		if m > 0:
			Expect += (m/100.0)*E[(m-1,n+1)]
		if m < 99-n:
			Expect += ((99-m-n)/100.0)*E[(m+1,n)]
		E[(m,n)] = Expect * (100.0/(99-n))
# The first flip down is at (1,0), which occurs at 
# expected visit 100/99
E_up = 100/99.0 + E[(1,0)]
print "Lever starts up:",E_up
print "Average: ",(E_down+E_up)/2
Output:
```
Lever starts down: 20427.6630505
Lever starts up: 20527.6630505
Average:  20477.6630505
[Finished in 0.1s]
```

<br>
