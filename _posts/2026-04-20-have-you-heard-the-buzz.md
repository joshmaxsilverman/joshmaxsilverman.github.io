---
layout: post
published: true
title: Have you heard the buzz?
date: 2026/04/20
subtitle: Taking the fizz out of Buzz and replacing it with limits
tags: recursion fractals
source: fiddler
kind: puzzle
theme: probability
hide_from_recent : true
---

> **Question**: I recently introduced my children to a game called “Buzz” (also known as “Fizz buzz”). In one particular variant of the game, anytime a number is a multiple of 7 or at least one of its digits is a 7, the player must say “buzz” instead of that number.
>
>For example, here is how the first 20 turns of the game should proceed: 1, 2, 3, 4, 5, 6, buzz, 8, 9, 10, 11, 12, 13, buzz, 15, 16, buzz, 18, 19, 20.
>
> How many times should “buzz” be said in the first 100 turns of the game?
>
> **Extra Credit**: There is a certain minimum number $N$ such that, for the $N^\text{th}$ turn in the game and for every turn thereafter, at least half the numbers up to that point have been buzzed. What is this value of $N$?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/have-you-heard-the-buzz))

## Solution

A number buzzes if it's a multiple of $7$ or contains a $7$ as one of its digits. 

Over an arbitrary sequence of consecutive numbers these two conditions can have an induced correlation, but because $7$ and $10$ are coprime, there is no actual connection. To get around these artifacts, we can look at all numbers up to a power of $10,$ which samples over all digits uniformly. 

On these subsets, $1/7$ of all numbers are divisible by $7.$ The chance that a random number contains a $7$ is the complement of the chance that there is no $7$ whatsoever, i.e. $P_\text{has 7} = 1-\left(9/10\right)^{N-1}.$

So, probability that a random number from that set buzzes is then

$$ \begin{align}
    P_\text{buzz}(N) &= P_\text{div by 7} + P_\text{has 7} - P_\text{div by 7} \times P_\text{has 7} \\
        &= \frac17 + \frac67\left[1-\left(\frac{9}{10}\right)^{N-1}\right]
    \end{align}
$$

Up to the $N^\text{th}$ order of magnitude $10^N$ we have included all possible $N$ digit numbers in our sample. Until we hit the next leading $7$ at $7\times 10^N,$ each additional $10^N$ numbers we consider will, asymptotically, have the same buzz statistics as the numbers up to $10^N$ since they don't have a leading $7.$ This means that the cumulative fraction of buzz numbers will be the same at $\\{10^N, 2\times 10^N, \ldots, 6\times 10^N\\}.$ 

Once we hit the leading $7,$ the statistic jumps up quite a bit before relaxing to the next anchor value at $10^{N+1}.$ This means that once we pass $7\times 10^N,$ the cumulative fraction of buzz numbers will never again go below that level. 

Each successive power of ten is related by 

$$ P_\text{buzz}\left(10^{N+1}\right) = \frac{9}{10} P_\text{buzz}\left(10^N\right) + \frac{1}{10}. $$


$P_\text{buzz}(7\times10^5) \approx 0.493866$ and $P_\text{buzz}(10^6)\approx 0.544479$ so the final dip below $0.5$ must occur between $700,000$ and $1,000,000.$ Using our result, exactly $7\times 10^5\times P_\text{buzz}(7\times10^5) \approx 345,706$ of the first $700,000$ numbers buzz. Since all numbers from $700,000$ up to $799,999$ start with a $7,$ they all buzz. 

So, the final dip will occur for the $N$ that saturates

$$ \frac{345,706 +\left(N - 700,000\right)}{N} \lt \frac12 $$

Simplifying, we get $N - 354,294 < \frac12N,$ or $N < 708,588.$ Therefore, the cumulative proportion of buzz numbers will be $\frac12$ or greater for once $N=708,588.$

![](/img/2026-04-20-fiddler-fizz-buzz.png){:width="700 px" class="image-centered"}

As $N$ gets very large, the expected cumulative proportion of buzz numbers approaches $1.$

