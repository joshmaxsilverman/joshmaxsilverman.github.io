---
layout: post
published: true
title: An End to War
date: 2020/08/28
---

>*Question*: your friend's no-good, duplicitous, self-promoting grandchild has made extraordinary claims regarding their performance in the well-known cabin and road trip cardgame known as War. According to them, they've triumphed in a round where they won every single matchup with no ties, ending the game in a mere $26$ hands. Never one to let the feats of grandchildren go unchallenged, you set out to compute the probability of this occurrence. About how many rounds of War would one need to play to bear witness to this flawless victory?

<!--more-->

([FiveThirtyEight](URL))

## Solution

This problem has two pieces, one is the probability that the shuffle is such that every pair of cards has an unambiguous outcome, and the second is that every one of these matchups has the same victor. So,

$$P(\text{rout}) = P(\text{rout}|\text{no ties})P(\text{no ties}).$$

The second part is easy, given that we have an outcome with no ties, the probability that Duane's friend's granddaughter wins every one is just $1/2^{26},$ or, in the general case where there are $4n$ cards ($4$ of each of $n$ kinds),

$$P(\text{rout}|\text{no ties}) = \dfrac{1}{2^{2n}}.$$

### No ties

Getting an exact answer for $P(\text{no ties})$ calls for detailed combinatorics and, as far as I can tell, there is no way to go straight for the probability of zero collisions, $P_\text{rout}.$ However, it may be possible to get the asymptotic result with a lot less effort. And the asymptotic result might be accurate surprisingly early on in the $n\rightarrow\infty$ path.

### Infinite ranks

We can build the shuffled War deck one pair at a time, working with $4n$ total cards in the limit where $n$ is large. For each pair, the first card is drawn uniformly and the second card needs to be one of the $4n - 3$ remaining cards that don't have the same rank. The probability of this happening is 

$$P(\text{no match in first pair}) = \frac{4n-3}{4n} = 1 - \frac{3}{4n}$$

If we were dealing with small $n$ then we'd have to consider the possibility that the second pair involves one of the cards that appeared in the first. However, the probability of this happening when $n$ is large is $0$, so

$$P(\text{no match in second pair}) = 1 - \frac{3}{4n}$$

as well. 

As there are $2n$ pairs, the overall probability of no ties is

$$\begin{align}
P(\text{no ties}) &= \lim\limits_{n\rightarrow\infty}\left(1-\frac{3}{4n}\right)^{2n} \\
&= \lim\limits_{n\rightarrow\infty}\left(1 - \frac{3/2}{2n}\right)^{2n}
\end{align}$$

which is the definitional form for $e^{-3/2}.$

Putting it all together, the probability of Duane's friend's granddaughter winning her War match in a $26$ hand route is approximately

$$P(\text{rout}) = P(\text{rout}|\text{no ties})\times P(\text{no ties}) = \frac{1}{2^{2n}}e^{-3/2}$$

which is approximately $3.32489848\times 10^{-9}.$ 

### Expected waiting time

Answering the original question, we should expect to wait $T = 1/P(\text{rout})$ games to bear witness to the rout, or roughly $300,000,000$ games.

<br>
