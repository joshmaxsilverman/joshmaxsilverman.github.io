---
layout: post
published: false
title: An End to War
date: 2020/08/28
---

>**Question**: your friend's no-good, duplicitous, self-promoting grandchild has made extraordinary claims regarding their performance in the well-known cabin and road trip cardgame known as War. According to them, they've triumphed in a round where they won every single matchup with no ties, ending the game in a mere $26$ hands. Never one to let the feats of grandchildren go unchallenged, you set out to compute the probability of this occurrence. About how many rounds of War would one need to play to bear witness to their flawless victory?

<!--more-->

([FiveThirtyEight](URL))

## Solution

This problem has two pieces, one is the probability that the shuffle is such that every pair of cards has an unambiguous outcome, and the second is that every one of these matchups has the same victor. So,

$$P(\text{rout}) = P(\text{rout}|\text{no ties})P(\text{no ties}).$$

The second part is easy, given that we have an outcome with no ties, the probability that Duane's friend's grandchild wins every one is just $1/2^{26},$ or, in the general case where there are $4r$ cards ($4$ of each of $r$ kinds, where $r=13$ for the standard deck),

$$P(\text{rout}|\text{no ties}) = \dfrac{1}{2^{2r}}.$$

### No ties

Getting an exact answer for $P(\text{no ties})$ calls for detailed combinatorics and, as far as I can tell, there is no way to go straight for the probability of zero collisions, $P_\text{rout}.$ However, it may be possible to get the asymptotic result with a lot less effort. And the asymptotic result might be accurate surprisingly early on in the $r\rightarrow\infty$ path.

### Infinite ranks

We can build the shuffled War deck one pair at a time, working with $4r$ total cards in the limit where $r$ is large. For each pair, the first card is drawn uniformly and the second card needs to be one of the $4r - 3$ remaining cards that don't have the same rank. The probability of this happening is 

$$P(\text{no tie in first pair}) = \frac{4r-3}{4r} = 1 - \frac{3}{4r}$$

If we were dealing with small $r$ then we'd have to consider the possibility that subsequent pairs involve a rank that has already paired. However, the probability of this happening when $r$ is large is **very small$^\dagger$** compared to the probability of forming a tie with an unused rank. So, the probability for a tie in the second pair is

$$P(\text{no tie in second pair}) = 1 - \frac{3}{4r}$$

as well. 

As there are $2r$ pairs, the overall probability of no ties is

$$\begin{align}
P(\text{no ties}) &= \left(1-\frac{3}{4r}\right)^{2r} \\
&= \left(1 - \frac{3/2}{2r}\right)^{2r}
\end{align}$$

which, when we take $\lim\limits_{r\rightarrow\infty},$ is the definitional form for $e^{-3/2}.$

Putting it all together, the probability of Duane's friend's grandchild winning their War match in a $2r=26$ hand route is approximately

$$P(\text{rout}) = P(\text{rout}|\text{no ties})\times P(\text{no ties}) = \frac{1}{2^{2r}}e^{-3/2}$$

which is approximately $3.32489848\times 10^{-9}.$ 

### Expected waiting time

Answering the original question, we should expect to wait $T = 1/P(\text{rout})$ games to bear witness to the rout, or roughly $300,000,000$ games.

### Generalizing

In general, we can have $r$ ranks and $s$ suits. In that case, the number of hands is $s\times r/2$ and we have

$$\boxed{P(\text{rout}) = \dfrac{1}{2^{sr/2}}e^{-(s-1)/2}}$$

We can compare the asymptotic prediction for $P(\text{no tie})$ to a computer simulation for different values of $s$ and $r$. 

When there are many different suits $s,$ we should expect to need many different ranks $r$ for a good prediction. This is because the probability of ranks with multiple pairs rises with the number of suits, and our calculation explicitly ignores that possibility. As the green dot shows, the asymptotic result is already quite good for the standard deck, accurate to within $\approx6\%.$

![](/img/2020-08-28-P-no-tie-1000000-black.png
){: width="400px" class="image-centered"}

{:.caption}

Comparison of theoretical (solid lines) and empirical (dotted lines) results for $P(\text{no tie})$ for different values of $s$ and $r.$ The black dot indicates the result for a standard deck of cards.

---

### $^\dagger$Underwriting the ignorance of ranks with multiple pairs

...

<br>
