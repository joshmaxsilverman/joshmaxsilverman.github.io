---
layout: post
published: true
title: Hit the bullseye, kind of
date: 2021/01/10
---

>**Question**: each night, you like to wind down with a relaxing game of one-upsmanship against yourself, throwing darts at your bullseye one by one, trying to get each one closer than the last. When a dart lands further from the center than the one that came before, the streak is over. Over the course of your life, how many darts will you throw on the average night? Assume that inside the bullseye, the darts are equally likely to land at any point inside the outer ring of the dart board.

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-cut-the-square-into-more-squares/))

## Solution

We'll pretend we have an infinite set of infinite sequences of sampled circles, $\mathcal{C}_\infty.$ 

Draw a sample with circles of radius $\\{r_1, r_2, \ldots\\}.$ The probability that it corresponds to $j$ successful shots is the probability that the first $j$ elements are ordered times the probability that the $\left(j+1\right)^\text{st}$ circle is out of order:

$$P\left(j\,\text{shots}\right) = P(\text{first $j$ circles in order})\times P(r_{j+1} > r_j).$$

$P(\text{first $j$ circles in order})$ is straightforward: there are $j!$ orderings of $j$ elements, only $1$ of which is in the right order. So this is just $1/j!.$

The second bit requires us to know $r_j.$ In expectation, the smallest of $n$ uniformly random numbers is just $1/(n+1).$ The reason, briefly, is that the expected positions of the smallest, second smallest, ..., up to the largest are equally spaced. The probability of the $\left(j+1\right)^\text{st}$ number being greater than this is just 

$$P(r_{j+1} > r_j) = \left(1 - \frac{1}{j+1}\right) = \dfrac{j}{j+1}.$$

This gives

$$P\left(j\,\text{shots}\right) = \dfrac{1}{j!}\dfrac{j}{j+1}.$$

The number of points won through $j$ successful shots is $\left(j+1\right),$ so

$$\begin{align}
\langle S\rangle &= \sum_{j=1}^\infty \left(j+1\right) \dfrac{1}{j!}\dfrac{j}{j+1} \\
&= \sum_{j=1}^\infty \frac{1}{\left(j-1\right)!} \\
&= e.
\end{align}$$


<br>
