---
layout: post
published: true
title: Mike Trout Numerology
date: 2021/03/07
---

>Question

<!--more-->

([FiveThirtyEight](URL))

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

So, we have to march backward from $N=250$ and find the first place where the two sides do not span an integer.

$$
\begin{array}{|c|c|}\hline
250 & 249.5 & 250.5 \\
249 & 247.506 & 248.502 \\
248 & 245.52 & 246.512 \\
247 & 243.542 & 244.53 \\
246 & 241.572 & 242.556 \\
245 & 239.61 & 240.59 \\
244 & 237.656 & 238.632 \\
243 & 235.71 & 236.682 \\
242 & 233.772 & 234.74 \\
241 & 231.842 & 232.806 \\
240 & 229.92 & 230.88 \\
239 & 228.006 & 228.962 \\
\end{array}
$$



<br>
