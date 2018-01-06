---
layout: post
title: Strange Beds
date: 2018/01/06
published: true
---

>Each of seven dudes sleeps in his own bed in a shared dormitory. Every night, they retire to bed one at a time, always in the same sequential order, with the youngest dude retiring first and the oldest retiring last. On a particular evening, the youngest dude is in a jolly mood. He decides not to go to his own bed but rather to choose one at random from among the other six beds. As each of the other dudes retires, he chooses his own bed if it is not occupied, and otherwise chooses another unoccupied bed at random.
>
>1. What is the probability that the oldest dude sleeps in his own bed?
>2. What is the expected number of dudes who do not sleep in their own beds?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/where-will-the-seven-dwarfs-sleep-tonight/); I've switched to dudes from "dwarfs," in recognition that the latter term is not cared for by many people who are differently tall.)

### Solution

#### 1. What is the probability that the oldest dude sleeps in his own bed?

Let's work with $n$ dudes and beds.

The final open bed is that of either the youngest or the oldest dude, because every other dude will have taken their own bed if it was available.

The stipulation that the young dude chooses among the _other_ beds introduces a complication that kind of messes up what is otherwise a very pretty problem. Call the "pretty version" of the problem the one in which he can also end up in his own bed. In that version the oldest dude has probability $1/2$ of sleeping in his own bed, because whichever of the two possible final open beds is in fact open was the consequence of a random choice that did not privilege either over the other.

$$P^{pretty}_n = \frac{1}{2}$$

Asking for this probability in the problem as actually posed is equivalent to asking, in the pretty version, what the probability is that the oldest dude matches (sleeps in his own bed) _given_ that there is at least one mismatch. We find this as follows (where $M$ means that there is at least one mismatch, $O$ means that the oldest dude sleeps in his own bed, and $P(A\|B)$ is the conditional probability of $A$ given $B$):

$$P^{pretty}_n = P(M)P(O|M) + P(\neg M)P(O | \neg M) = \frac{n-1}{n}P^{as-posed}_n + \frac{1}{n}\cdot 1$$

$$P^{as-posed}_n = \frac{n-2}{n-1}\cdot\frac{1}{2}$$ 

For $7$ dudes and beds, that's $5/12$.

#### 2. What is the expected number of dudes who do not sleep in their own beds?

Label the $n$ dudes and beds $1$ through $n$.

Let's again start with the pretty version of the problem. When dude $k$ arrives, all $k-2$ beds from $2$ to $k-1$ are occupied (if dudes $2$ to $k-2$ had found them unoccupied, they'd have chosen them). One more bed is occupied among the other $n-k+2$ beds, namely beds $1,k,k+1,\ldots,n$, and it is occupied by a dude who chose it randomly. So bed $k$ is as likely as any of those to be the occupied one, and so the chance that it is occupied, which is the chance that dude $k$ ends up mismatched, is (for $k\geq2$):

$$P^{pretty}_k = \frac{1}{n-k+2}$$

So the probabilities for dudes $2,\ldots,n$ are $\frac{1}{n},\frac{1}{n-1},\ldots,\frac{1}{3},\frac{1}{2}$. And of course the probability for dude $1$ is $\frac{n-1}{n}$.

Asking for that same probability in the as-posed version of the puzzle is equivalent to asking, in the pretty version, what is the probability that dude $k$ is mismatched _given_ that at least one dude is mismatched? Using exactly similar reasoning as in part $1$, we determine that:

$$P^{as-posed}_k = \frac{n}{(n-1)}\cdot\frac{1}{n-k+2}$$

Now that we know, in both the simple and as-posed versions of the puzzle, how likely each dude is to be mismatched, we can compute the expected number of mismatched dudes by simply adding those probabilities for $k$ from $2$ to $n$, and adding also the probability that the first dude is mismatched.

Again we start with the pretty version:

$$E^{pretty}_n = \frac{n-1}{n}+\sum_{k=2}^n \frac{1}{n-k+2} 
= \sum_{i=1}^{n-1} \frac{1}{i} = H_{n-1}
$$

Here $H_n$ is the $n$th [harmonic number](http://mathworld.wolfram.com/HarmonicSeries.html) (which is defined as the sum it replaces here). The harmonic numbers are unbounded, so there is no limit to the expected mismatches for large $n$.

To get the expectation for the problem as posed, we can again redirect the question to the pretty version and ask, in that version,  what is the expected number of mismatches _given_ that there are any at all? The total expectation in the pretty version is the sum of two values. The first is the probability that there are no mismatches times the expected number of mismatches given that there are none; this value is of course $0$. The second is the expected number of mismatches given that there are any (and _this_ is the expectation we are looking for) times the probability that there is at least one mismatch (i.e., $\frac{n-1}{n}$). So:

$$E^{pretty}_n = \frac{n-1}{n}E^{as-posed}_n$$

$$E^{as-posed}_n = \frac{n}{n-1}H_{n-1}$$

Here are some values for small $n$ (the exact expectation for seven dudes, by the way, is $343/120$ in the problem as-posed, or $49/20$ in the pretty version):

n | Expected Mismatches 
--- |:---
2 | 2.0
3 | 2.25
4 | 2.44444444444
5 | 2.60416666667
6 | 2.74
7 | 2.85833333333
8 | 2.96326530612
9 | 3.05758928571
10 | 3.14329805996

The values are confirmed by this Monte Carlo simulation, which produced the plot below:

```python
from random import randint
Reps = 1000000
for N in range(3,101):
	Accum = 0
	for _ in range(Reps):
		State = list(range(N))
		MatchCount = 0
		del State[randint(1,N-1)]
		if not State[0] == 0:
			MatchCount += 1
		for i in range(1,N):
			if i in State:
				State.remove(i)
				MatchCount += 1
			else:
				del State[randint(0,N-i-1)]
		Accum += N-MatchCount
	print N, ",", 1.0*Accum/Reps
```

![Graph of expectation versus n.](/img/ExpectedMismatches.png)

<br>
