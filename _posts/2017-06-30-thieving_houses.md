---
layout: post
published: true
title: Thieving Houses
date: 2017/06/30
---

>A town of 1,000 households has a strange law intended to prevent wealth-hoarding. On January 1 of every year, each household robs one other household, selected at random, moving all of that house’s money into their own house. The order in which the robberies take place is also random and is determined by a lottery. (Note that if House A robs House B first, and then C robs A, the houses of A and B would each be empty and C would have acquired the resources of both A and B.)
>
>Two questions about this fateful day:
>
>What is the probability that a house is not robbed over the course of the day?
Suppose that every house has the same amount of cash to begin with — say \$100. Which position in the lottery has the most expected cash at the end of the day, and what is that amount?
<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/who-steals-the-most-in-a-town-full-of-thieves/))

## Solution
Let there be $N$ houses initially with $D$ dollars each. 

The chance that a house never gets robbed is the product of the chances that each other house fails to rob it. Since each house has chance $(N-1)/(N-2)$ of failing to rob any given house, that probability is:

$$\left(\frac{N-2}{N-1}\right)^{N-1}$$

If $N$ is $1000$ and $D$ is $100$, that's about $.368$.

The chance that house $i$ does not get robbed before its own turn to rob is:

$$p_{nrb} = \left(\frac{N-2}{N-1}\right)^{i-1}$$

Thus, the expected amount of money in house $i$ right before its turn to rob is $Dp_{nrb}$, and the expected haul when house $i$ robs is the average of what's expected to be left in all the other houses:

$$E_{haul} = \frac{ND - Dp_{nrb}}{N-1}$$

The chance that house $i$ does not get robbed after its turn to rob is:

$$p_{nra} = \left(\frac{N-2}{N-1}\right)^{N-i}$$

House $i$'s expectation at the end of the day is the sum of the expected amount ($Dp_{nrb}$) in it just before it robs and its expected haul ($E_{haul}$), times its probability ($p_{nra}$) of retaining that money:

$$E_{end} = \left[D\left(\frac{N-2}{N-1}\right)^{i-1} + 
\frac{ND - D\left(\frac{N-2}{N-1}\right)^{i-1}}{N-1} \right] \cdot
\left(\frac{N-2}{N-1}\right)^{N-i}
$$

$$ = \left(D - \frac{D}{N-1}\right)\left(\frac{N-2}{N-1}\right)^{N-1}
 + \frac{ND}{N-1}\left(\frac{N-2}{N-1}\right)^{N-i}$$
 
It is easy to see that this expectation is maximized when $p_{nra}$ is maximized, which is of course when $i$ is $N$, that is, the last house to rob. If $N$ is $1000$ and $D$ is $100$, the expectation is approximately $136.8$.

The connection between the answers to the two parts of the puzzle ($.368$ chance of not being robbed all day and last-house expectation of $136.8$ is simple: the last house expects to retain $.368$ of its initial $100$, and expects to rob the average amount of money in all the other houses, which is either exactly $100$ (if it does not get robbed) or the very slightly higher $100/.999$ (if it does). That very slightly higher possibility adds to the overall expectation, but only a tiny amount.

The expectation of house $N$ simplifies further to:

$$ D \left[
\frac{1}{\left(1+\frac{1}{N}\right)^N} + \frac{N}{N-1} \right]$$

For large $N$, $(1+(1/N))^N$ approaches $e$ (thanks to John Snyder in the comments for pointing this out), and so the probability of any given house being robbed approaches $1/e$, and the expectation of the last house approaches $D(1 + 1/e)$, which you will not be shocked to learn is about $1.368$.

<br>
 
