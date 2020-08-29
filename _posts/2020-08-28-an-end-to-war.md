---
layout: post
published: false
title: 
date: 2020/08/28
---

>*Question*: your friend's no-good, duplicitous, self-promoting grandchild has made extraordinary claims regarding their performance in the well-known cabin and road trip cardgame known as War. According to them, they've triumphed in a round where they won every single matchup with no ties, ending the game in a mere $26$ hands. Never one to let the feats of grandchildren go unchallenged, you set out to compute the probability of this occurrence. About how many rounds of War would one need to play to bear witness to this flawless victory?

<!--more-->

([FiveThirtyEight](URL))

## Solution

This problem has two pieces, one is the probability that the shuffle is such that every pair of cards has an unambiguous outcome, and the second is that every one of these matchups has the same victor. So,

$$P(\text{rout}) = P(\text{rout}|\text{no ties})P(\text{no tides}).$$

The second part is easy, given that we have an outcome with no ties, the probability that Duane's friend's granddaughter wins every one is just $1/2^{26},$ or, in the general case where there are $4n$ cards ($4$ of each of $n$ kinds),

$$P(\text{rout}|\text{no ties}) = \dfrac{1}{2^{2n}}.$$

Getting an exact answer for $P(\text{no tides})$ calls for detailed combinatorics and, as far as I can tell, there is no way to go straight for the probability of zero collisions, $P_\text{rout}.$

<br>
