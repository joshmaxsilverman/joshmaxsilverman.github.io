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

#### 1.

Let's work with $n$ knights and beds.

The final open bed is that of either the youngest or the oldest knight, because every other knight will have taken their own bed if it was available. There is probability $1/(n-1)$ that the youngest chooses the oldest's bed, in which case there is no chance the latter will sleep in his own bed. The other $(n-2)/(n-1)$ of the time, because the bed-selection rules for all but the youngest and oldest knights are symmetrical as between those two beds, the chance that the oldest knight sleeps in his own bed is $1/2$. And so the overall probability is:

$$\frac{n-2}{2(n-1)}$$

For $7$ knights and beds, that's $5/12$.

#### 2.

Label the $n$ knights and beds $1$ through $n$. Call $E_n$ the expected number of mismatched knights, meaning ones who do not sleep in their own beds. 

When a knight $k$ arrives to find his bed taken, the open beds are exactly bed $1$ and all beds greater than $k$. (If you don't find that obvious, it's easy to prove inductively.)

Suppose knight $k$ arrives to find his bed already taken. Then he is in _nearly_ the position of knight $1$ in a scenario with fewer ($n-k+1$, or for short, $m$) beds: he will randomly choose one of the $m$ open beds, but if he chooses bed $1$, he will be mismatched. Let's calculate the expected number $F_m$ of mismatches in such a situation.  Obviously $F_1$ is $1$. And in general $F_m$ is a function of $F_j$ for $j<m$. There is a $1/m$ chance that knight $k$ chooses bed $1$, for one mismatch, a $1/m$ chance he chooses the numerically second bed for an expectation of $1+F_{m-1}$ mismatches, a $1/m$ chance he chooses the third for an expectation of $1 + F_{m-2}$ mismatches, $\ldots$, and a $1/m$ chance he chooses the $m$th for an expected $F_1$ mismatches. So we have the recurrence:

$$F_1 = 1$$

$$F_m = \frac{1}{m}\cdot 1 + \sum_{j=1}^{m-1}\frac{1}{m}\left(1+F_j\right)
= 1 + \frac{1}{m}\sum_{j=1}^{m-1} F_j
$$

Now let's return to the start. Knight $1$ has, for $2\leq m \leq n$, a $1/(n-1)$ chance of landing (as a mismatch) in bed $m$ after which we expect $F_{n-m+1}$ additional mismatches. The overall expectation, then, is:

$$ E_n = 1 + \frac{1}{n-1} \sum_{j=1}^{n-1} F_j
$$

Here are some values for small $n$ (the exact value for seven knights, by the way, is $343/120$):

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

### Another approach

Let's ask how likely it is for a given knight, say knight $k$, to find his bed occupied. Each possible way for that to happen corresponds to an increasing sequence of numbers between $2$ and $k-1$, which number the earlier mismatches. Let one such sequence, $\sigma$, be $k_1,k_2,...k_i$. The chance for that sequence to arise and to be followed by a mismatch for $k$ is found by multiplying the chances of each step. Knight $k_1$ has $1/(n-1)$ chance of being the first mismatch. Then, knight $k_2$ has $1/(n-k_1+1)$ chance of being the second, $\ldots$, and finally $k$ has $1/(n-k_i+1)$ chance of being the $i+1$st mismatch. So where $f(x)$ is $1/(n-x+1)$:

$$ P(\sigma) = \frac{1}{n-1}\prod_{j \in \sigma}f(j) $$

Using $f[\sigma]$ to mean the image of $f$ over $\sigma$ --- that is, the set of its values at arguments that are members of the sequence --- since $f$ is a bijective (one-to-one) function, we can write this as:

$$ P(\sigma) = \frac{1}{n-1}\prod_{i \in f[\sigma]} i $$

There is one such increasing sequence, for knight $k$, for each subset of the set $S_{2,k-1}$ of numbers between $2$ and $k-1$. So the overall probability that knight $k$ will mismatch is:

$$P_k =  \frac{1}{n-1}\sum_{S \subseteq f[S_{2,k-1}]}\prod_{j \in S}i$$

In general, the sum of the products of every subset of a set is the same as the single product of the successors of every element in the set (each element increased by one). To see why, consider the set $\{2,3,4,5\}$ and the product:

$$(2+1)(3+1)(4+1)(5+1) = 2\cdot 1\cdot 1 \cdot 1 +2\cdot 3 \cdot 1 \cdot 1 +2\cdot 3 \cdot 4 \cdot 1 + \cdots$$

There is an element in the expansion of this product for each way of deciding, for every element of the set, whether to multiply with  it or rather the number $1$. That corresponds exactly to an arbitrary choice of subset.

So we know:

$$P_k = \frac{1}{n-1} \prod_{j=2}^{k-1}(f(j)+1) = \frac{1}{n-1} \prod_{j=2}^{k-1} \frac{n+2-j}{n+1-j}
$$

If you write out the first few terms, you'll see that the product cancels nicely, leaving us with the initial numerator and final denominator:

$$ P_k = \frac{1}{n-1}\cdot \frac{n+2-2}{n+1-(k-1)} = 
\frac{n}{(n-1)(n-k+2)}$$

Now that we know how likely each knight is to be mismatched, we can compute the expected number of mismatched knights by simply adding those probabilities for $k$ from $2$ to $n$ and adding $1$ for the first, always mismatched knight:

$$E_n = 1 + \sum_{k=2}^n \frac{n}{(n-1)(n-k+2)} 
= 1+\frac{n}{n-1}\sum_{k=2}^n \frac{1}{n-k+2}
$$

The addends in the sum on the right go from $1/n$ down to $1/2$, and so they form all but the initial element $1$ of [the Harmonic Series](http://mathworld.wolfram.com/HarmonicSeries.html). This tells us that the expectation is unbounded for large $n$, and also that we can write the expectation in a slightly tidier fashion:

$$E_n = 1 + \frac{n}{n-1}\cdot (H_n-1)$$

The "$n-1$" in there traces back to the stipulation that the first knight cannot randomly land on his own bed. If we erase that stipulation, then that term becomes $n$, the initial $1$ becomes $\frac{n-1}{n}$, and the expectation becomes $H_n - \frac{1}{n}$.

These approaches agree with one another and with this Monte Carlo simulation:

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

