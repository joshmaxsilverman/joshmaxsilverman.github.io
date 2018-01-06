---
layout: post
title: Strange Beds
date: 2018/01/06
published: true
---

>Each of the seven knights sleeps in his own bed in a shared dormitory. Every night, they retire to bed one at a time, always in the same sequential order, with the youngest knight retiring first and the oldest retiring last. On a particular evening, the youngest knight is in a jolly mood. He decides not to go to his own bed but rather to choose one at random from among the other six beds. As each of the other knights retires, he chooses his own bed if it is not occupied, and otherwise chooses another unoccupied bed at random.
>
>1. What is the probability that the oldest knight sleeps in his own bed?
>2. What is the expected number of knights who do not sleep in their own beds?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/where-will-the-seven-dwarfs-sleep-tonight/); I've switched to knights from "dwarfs," in recognition that the latter term is not cared for by many people who are differently tall.)

### Solution

<br>

#### 1.

Let's work with $n$ knights and beds.

The final open bed is that of either the youngest or the oldest knight, because every other knight will have taken their own bed if it was available.

The stipulation that the young knight chooses among the _other_ beds introduces a complication that kind of messes up what is otherwise a very pretty problem. Call the "pretty version" of the problem the one in which he can also end up in his own bed. In that version the oldest knight has probability $1/2$ of sleeping in his own bed, because whichever of the two possible final open beds is in fact open was the consequence of a random choice that did not privilege either over the other.

In the as-posed version, though, the symmetry is not perfect. There is probability $1/(n-1)$ that the youngest chooses the oldest's bed, in which case there is no chance that the latter will sleep in his own bed. The other $(n-2)/(n-1)$ of the time, because the bed-selection rules for all but the youngest and oldest knights are symmetrical as between those two beds, the chance that the oldest knight sleeps in his own bed is $1/2$. And so the overall probability is:

$$\frac{n-2}{2(n-1)}$$

For $7$ knights and beds, that's $5/12$.

#### 2.

Label the $n$ knights and beds $1$ through $n$. We want to find the expected number of mismatched knights, meaning ones who do not sleep in their own beds. 

Let's again start with the pretty version of the problem. When knight $k$ arrives, all $k-2$ beds from $2$ to $k-1$ are occupied (if knights $2$ to $k-2$ had found them unoccupied, they'd have chosen them). One more bed is occupied among the other $n-k+2$ beds, namely beds $1,k,k+1,\ldots,n$, and it is occupied by a knight who chose it randomly. So bed $k$ is as likely as any of those to be the occupied one, and so the chance that it is occupied, which is the chance that knight $k$ ends up mismatched, is:

$$P^{simple}_k = \frac{1}{n-k+2}$$

Asking for that same probability in the as-posed version of the puzzle is equivalent to asking, in the pretty version, in what fraction of cases in which there are any mismatches at all is knight $k$ mismatched? The overall fraction of cases in which there is at least one mismatch is $\frac{n-1}{n}$, and since the cases in which knight $k$ is mismatched is a subset of the cases in which there is at least one mismatch, the answer is:

$$P^{as-posed}_k = \frac{\frac{1}{n-k+2}}{\frac{n-1}{n}}
= \frac{n}{(n-1)(n-k+2)}$$

Now that we know, in both the simple and as-posed versions of the puzzle, how likely each knight is to be mismatched, we can compute the expected number of mismatched knights by simply adding those probabilities for $k$ from $2$ to $n$, and adding also the probability that the first knight is mismatched.

Again we start with the pretty version:

$$E^{pretty}_n = \frac{n-1}{n}+\sum_{k=2}^n \frac{1}{n-k+2} 
= \sum_{i=1}^{n-1} \frac{1}{i} = H_{n-1}
$$

Here $H_n$ is the $n$th [harmonic number](http://mathworld.wolfram.com/HarmonicSeries.html) (which is defined as the sum it replaces here). The harmonic numbers are unbounded, so there is no limit to the expected mismatches for large $n$.

Things are again a little less elegant in the problem as-posed:

$$E^{as-posed}_n = 1 + \sum_{k=2}^n \frac{n}{(n-1)(n-k+2)} 
= 1+\frac{n}{n-1}\sum_{k=2}^n \frac{1}{n-k+2}
$$

$$ = 1 + \frac{n}{n-1}\sum_{i=2}^n\frac{1}{i}
=1 + \frac{n}{n-1}\cdot (H_n-1)
= \frac{nH_n}{n-1}
$$

(We can again think of this as the expectation of mismatches in the subclass of cases in the pretty version where there are any mismatches at all.)

Here are some values for small $n$ (the exact expectation for seven knights, by the way, is $343/120$ in the problem as-posed, and $49/20$ in the pretty version):

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

