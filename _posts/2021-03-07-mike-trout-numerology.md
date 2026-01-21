---
layout: post
published: true
title: Mike trout numerology
date: 2021/03/07
subtitle: Can a batting average’s first digits match games played?
source: fivethirtyeight
theme: number-theory
---

>**Question**: in one of the great numerological miracles of our time, baseball players are obtaining batting averages with the same first three significant digits as the number of games in the stretch that the batting statistics are taken over. Is this an effect of rare planetary alignment? Suppose that a baseball player gets $4$ at bats in every of the $N$ games they play. What is the greatest value of $N$ for which it is impossible for the digits of their batting average (rounded to the nearest thousandth) to equal the number of games they've played in.

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-bat-299-in-299-games/))

## Solution

Batting average is the probability that a batter gets a hit in any given at bat, i.e.

$$ \text{B.A.} = \dfrac{\text{hits}}{\text{at bats}} $$

If the player has $h$ hits on the $N$ game season, and therefore $4N$ at bats, then their batting average is

$$ \text{B.A.} = \dfrac{h}{4N} $$ 

The numerological phenomena we're interested in is the case when their batting average, rounded to the nearest thousandth, has the same digits as the number of games played. In other words, if the batting average is $x$ then we want to know if

$$ \text{round}(1000\times\dfrac{h}{4N}) = N $$

If a number rounds to $N,$ it means that it's either up to $1/2$ less than it or up to just less than $1/2$ greater than it:

$$ N - 1/2 \leq 1000\dfrac{h}{4N} \lt N + 1/2 $$

Multiplying through to isolate $h,$ this becomes

$$ \frac{(N-1/2)N}{250} \leq h \lt \frac{(N+1/2)N}{250} $$

This is the condition on $h$ that must be satisfied for the numerological miracle to occur. However, $h$ also has to be an integer, which means that the left and right hand sides of the inequality have to be on opposite sides of an integer. The gap between these two sides is $N/250,$ which is greater than $1$ so long as $N$ is greater than $250.$ 

The phenomena can fail to obtain when $N \lt 250$, so long as the two sides span an integer. So, we just have to march backward from $N=250$ and find the first place where the two sides do not span an integer.

We can see that the first (and greatest) failure occurs at $\boxed{N = 239}.$

$$
\begin{array}{|c|c|}\hline
N & (N-1/2)N/250 & (N+1/2)N/250 \\ \hline
250 & 249.5 & 250.5 \\ \hline
249 & 247.506 & 248.502 \\ \hline
248 & 245.52 & 246.512 \\ \hline
247 & 243.542 & 244.53 \\ \hline
246 & 241.572 & 242.556 \\ \hline
245 & 239.61 & 240.59 \\ \hline
244 & 237.656 & 238.632 \\ \hline
243 & 235.71 & 236.682 \\ \hline
242 & 233.772 & 234.74 \\ \hline
241 & 231.842 & 232.806 \\ \hline
240 & 229.92 & 230.88 \\ \hline
\bf{239} & \bf{228.006} & \bf{228.962} \\ \hline
238 & 226.1 & 227.052 \\ \hline
237 & 224.202 & 225.15 \\ \hline
236 & 222.312 & 223.256 \\ \hline
235 & 220.43 & 221.37 \\ \hline
234 & 218.556 & 219.492 \\ \hline
233 & 216.69 & 217.622 \\ \hline
232 & 214.832 & 215.76 \\ \hline
231 & 212.982 & 213.906 \\ \hline
230 & 211.14 & 212.06 \\ \hline
\end{array} 
$$



<br>
