---
layout: post
published: true
title: Card collisions
date: 2024/04/21
subtitle: What's the chance no card sees its own reflection?
tags: approximation recursion mean-field
---

>**Question:** You and your friend both have standard decks of $52$ cards. First, you combine them into a single deck with $104$ cards, and you thoroughly shuffle it. Then, you randomly split this back into two decks with $52$ cards each—one for you, and one for your friend.
>
>Each of you draw one card at a time. If the two of you can make it through your entire decks without ever drawing the same card at the same time, you both win. Otherwise, you both lose.
>
>What is the probability that you and your friend will win this collaborative game?


<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-win-the-collaborative-card))

## Solution

First, we'll find the large deck limit with a mean-field approach, and then we'll calculate the exact probability for two $52$ card decks by recursion.

### Large deck limit

As the decks gets large the probability $P(\text{no collisions})$ tends to $1/\sqrt{e}\approx 0.60653\ldots$

To see this, let's build a game one pair of draws at a time. To start, we have two $N$-card decks shuffled to form one $2N$-card deck and each card has a twin. 

With finite decks, the rounds have correlations. An early collisionless round raises the chance that a later round will be too (since the early round leaves twinless cards in the deck). Likewise, early collisions beget later ones.

So, to properly treat finite games, we need to track the evolution of chains of draws (as we'll do in the next section).

With infinite decks, things are different. Each round leaves the abundance of twinless cards unchanged — the probability that a newly drawn card has appeared in a previous round is always $0\%.$ This means that rounds are independent in the infinite game. So, we can build a model for the finite game where rounds are independent and scale it to big $N.$

The probability that any given round has a collision is $1/(2N-1)$ so the expected number of collisions in a game is $N\times1/(2N-1)$ which tends to $1/2$ for big $N$. 

That means that the chance of a collision in any given round is $1/2N$ and the chance of no collision is $(1-1/2N).$

Since the game has $N$ rounds, the probability to win the game is just

$$ P(\text{no collisions}) \approx \left(1-\frac{1}{2N}\right)^N $$

which approaches $ 1/\sqrt{e} $ in the limit.

### $52$ card decks

We can find the exact probability for $N$-card decks through recursion. 

Call a "type" any of the $N=52$ cards in the deck and call $P(s,d)$ the probability that the game has no collisions given that, in the remaining cards, there are $s$ types where one of the two cards has been drawn and $d$ types where neither of the cards have been drawn.

For example, after the first draw, a game that didn't have a collision would be in state $(s=2,d=50),$ and a game that had a collision would be in state $(s=0,d=51).$

If we are in state $(s,d)$ in a game that hasn't ended, we can form the next game-continuing pair from

- two singlets, moving to state $(s-2, d),$ or from
- a singlet and a doublet, moving to state $(s, d-1)$ (one singlet goes away, but one is formed from the doublet), or from
- two doublets, moving to state $(s+2, d-2).$

So, the probability that the $(s,d)$ game results in no collisions is 

$$ 
    \begin{align}
        P(s,d) =\ &\frac{s(s-1)}{(2d+s)(2d+s-1)}P(s-2,d) \\
                &+ 2\frac{sd}{(2d+s)(2d+s-1)}P(s,d-1) \\
                &+ \frac{2d(2d-2)}{(2d+s)(2d+s-1)}P(s+2,d-2). 
    \end{align}
$$

Running this recursion, we get 

$$ \begin{align}
    P(0,52) &= \frac{335561727225862936774353972738829595013743745454800896090990716254443717947031552}{555926557447585078813889409645210912590669690718980253197612210789777133544921875} \\
    &\approx 0.60361\ldots 
  \end{align} 
$$

```python
import sys
sys.setrecursionlimit(10 ** 9)
from functools import lru_cache
from fractions import Fraction as F

@lru_cache(maxsize=10 ** 9)
def P(s, d):

  denom = (2 * d + s) * (2 * d + s - 1)
  
  if s < 0 or d < 0:
    return 0
  
  if s == 0 and d == 0:
    return 1
  
  else:
    return F( s * (s - 1) * P(s - 2, d) \
             + 2 * s * (2 * d) * P(s, d - 1) \
             + (2 * d) * (2 * d - 2) * P(s + 2, d - 2) \
           , denom )
```


We can also use this to approximate the infinite limit, evaluating for an $N=10^4$ pair deck gets $P(0, 10^4) \approx 0.60652$ which is very close to $1/\sqrt{e}\approx 0.60653\ldots $



<br>


