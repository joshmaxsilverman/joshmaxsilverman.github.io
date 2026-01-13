---
layout: post
published: true
title: Simple runoff elections
date: 2020/10/21
subtitle: How often do random elections force a runoff?
source: fivethirtyeight
theme: probability
---

>**Question**: Like a banshee on a motorcycle, November approaches and brings with it everyone's favorite day: the election... But as we know, nobody can conduct a poll these days, what with phones and computers and all that. That means you have no idea what's going to happen. In fact, you might as well pull a random election result out of a hat. 
>
>The only way the nightmare can end is if one candidate manages $50\%$ of the vote or more, or else it goes to a runoff. If there are $N$ candidates running in your town, what is the probability that a runoff will be necessary?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/is-the-price-right/))

## Solution

I initially held off on this problem because I couldn't interpret the intended probability model for the vote totals. But according to [@xaqwg's clarifying tweet](https://mobile.twitter.com/xaqwg/status/1317117282213122052), we are filtering the set of all sums for the cases where 

$$v_1 + v_2 + \ldots + v_N = 1$$

where $v_i$ is the vote percentage for candidate $i.$ This is equivalent to weighting each possibility a single time, which corresponds to some nice geometry...

### Geometry of an election

The percentages satisfy $0\leq v_i \leq 1,$ so the set of possible outcomes forms a plane. For two candidates, this is just a line in the $2\text{D}$-plane; for three candidates, this is a tilted equilateral triangle in $\text{3D}$-space, and so on into higher dimensions for more and more candidates.  

When we consider the shape formed by space between the axes and the plane, it's known as a simplex, and contains all points for which $v_1+v_2+\ldots+v_N\leq 1.$ 

This means that the plane contains the actual elections while the volume contains points that could define a valid election with $N+1$ participants. We can realize that $(N+1)$-candidate election by adding another candidate whose vote percentage is $v_{N+1} = \left(1-\sum\limits_{i=1}^N v_i\right).$

### Weight as volume

Now let's look at some elections. If an election has no runoff, it means that one of the candidates managed to get $v_i > 50\%.$ That means that the percentages form a tuple like

$$\text{election} = \left(0.2, 0.15, 0.51, 0.14\right).$$

If we bring out the winner's coordinate, then this becomes 

$$\text{election} = 0.51 \times \overbrace{\left(0.2, 0.15, 0.14\right)}^{v_1 + v_2 + v_3 \leq \frac12}.$$

So, every possible election without runoff is in a $1:1$ correspondence with a tuple whose sum is less than $1/2.$ These tuples are exactly the points that are on the interior of the $(N-1)$ dimensional simplex with side length $a=1/2.$ 

Now the winning candidate could have actually been in any of the $N$ locations in the original tuple, so the total weight for runoff elections is

$$w_\text{no runoff} = N\times\text{Vol}(v_1 + v_2 + \ldots + v_{N-1} \leq \frac12).$$

If we look at a general election (with or without runoff) we can do the same: 

$$\text{election} = \left(0.24, 0.15, 0.47, 0.14\right) \rightarrow 0.24\times\overbrace{\left(0.15, 0.47, 0.14\right)}^{v_1 + v_2 + v_3 \leq 1}$$

except that the sum is equal to $1.$ Moreover, we always pull out the value of $v_1,$ so there's no need to multiply by $N.$ 

As a result, the total weight of all elections with $N$ candidates is the volume of the standard $(N-1)$-dimensional simplex

$$w_\text{total} = \text{Vol}(v_1 + v_2 + \ldots + v_{N-1} \leq 1).$$

### Volume of the standard simplex

An $N$-dimensional simplex has [volume $1/N!$](https://en.m.wikipedia.org/wiki/Simplex#Volume). If we generalize things so that $v_1+v_2+\ldots+v_N\leq a,$ this modified simplex has volume 

$$\text{Vol}(v_1+v_2+\ldots+v_N\leq a) = \dfrac{a^N}{N!}.$$

### Probability of runoff

The probability of a runoff election is simply

$$\begin{align}
P(\text{runoff}) &= 1-P(\text{no runoff}) \\
&= 1-\dfrac{w_\text{no runoff}}{w_\text{total}} \\
&= 1 - N\times\dfrac{\text{Vol}(v_1 + v_2 + \ldots + v_{N-1} \leq \frac12)}{\text{Vol}(v_1 + v_2 + \ldots + v_{N-1} \leq 1)} \\
&= 1 - N\times\dfrac{\frac{1}{2^{N-1}(N-1)!}}{\frac{1}{(N-1)!}} \\
&= \boxed{1 - \dfrac{N}{2^{N-1}}}.
\end{align}$$

which is $1/4$ for $3$ candidates, $1/2$ for $4$ candidates, $11/16$ for $5$ candidates, $13/16$ for $6$ candidates, etc.

<br>
