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

First, study the large deck limit with a mean-field approach, and then we'll find the exact probability for two $52$ card decks by recursion.

### Large deck limit

As the deck gets large the probability $P(\text{no collisions})$ tends to $1/\sqrt{e}\approx 0.60653\ldots$

To see this, let's build a game one pair of draws at a time. With $N$ cards in each deck, the probability that the first pair doesn't collide is $(2N-2)/(2N-1)$ which can be written as

$$ \left(1 - \frac{1}{2N-1}\right). $$

The probability that there is no collision on the second pair is likewise $(2N-4)/(2N-3)$ which can be written as 

$$ \left(1 - \frac{1}{2N-3}\right). $$

and so on. As $N$ gets large, all $N$ of these factors are approximately $(1-1/2N)$ and so the overall probability to win becomes

$$ P(\text{no collisions}) \approx \left(1-\frac{1}{2N}\right)^N $$

which approaches $ 1/\sqrt{e} $ in the limit.

### $52$ card decks

We can find the exact probability through recursion. 

Call a "type" any of the $N=52$ cards in the deck and call $P(s,d)$ the probability that the game has no collisions given that, in the remaining cards, there are $s$ types where one of the two cards has been drawn and $d$ types where neither of the cards have been drawn.

If we are in state $(s,d)$ we form the next pair from

- two singlets, moving to state $(s-2, d),$ or from
- a singlet and a doublet, moving to state $(s, d-1)$ (one singlet goes away, but one is formed from the doublet), or from
- two doublets, moving to state $(s+2, d-2).$

So, the probability that the $(s,d)$ game results in no collisions is 

$$ P(s,d) = \frac{s(s-1)}{(2d+s)(2d+s-1)}P(s-2,d) + \frac{sd}{(2d+s)(2d+s-1)}P(s,d-1) + \frac{2d(2d-2)}{(2d+s)(2d+s-1)}P(s+2,d-2). $$

Running this recursion, we get 

$$ \begin{align}
    P(0,52) &= \frac{335561727225862936774353972738829595013743745454800896090990716254443717947031552}{555926557447585078813889409645210912590669690718980253197612210789777133544921875} \\
    &\approx 0.60361\ldots 
  \end{align} 
$$

```python
import sys
sys.setrecursionlimit(10 ** 6)
from functools import lru_cache
from fractions import Fraction as F

@lru_cache(maxsize=10 ** 7)
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


