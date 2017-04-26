---
layout: post
published: true
title: Highest Card
date: 2017/04/22
---

>From a shuffled deck of 100 cards that are numbered 1 to 100, you are dealt 10 cards face down. You turn the cards over one by one. After each card, you must decide whether to end the game. If you end the game on the highest card in the hand you were dealt, you win; otherwise, you lose.
>
>What is the strategy that optimizes your chances of winning? How does the strategy change as the sizes of the deck and the hand are changed?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/pick-a-card-any-card/))

## Solution

Without changing anything important, let's restate the generalized situation as your being dealt a certain number $T$ of cards, one at a time, from a deck of $S$ cards. You can "hold" just once, and you win if the card you hold is higher than the cards dealt before or after it.

At every decision point (i.e., when you have a card higher than any others that have been dealt and need to decide whether to hold), whatever values $S$ and $T$ have, the important facts you know are that you have been dealt a given card $C$, that there are $D$ cards left to be dealt, $L$ cards lower than this one still in the deck (where $L$ is $C-1$ minus the number of cards already dealt), and $N$ cards total still in the deck.  Since $L$ and $N$ are simple functions of the variables $C$ and $D$ (and the constants $S$ and $T$), it's those latter two variables that your decision depends on entirely. Nonetheless, we will also it will also be useful in our calculations to keep track of the highest card $H$ so far seen (including $C$) as we define $P(C,D,H)$, which labels the probability that you will ultimately win if you get $C$ with $D$ cards still to be dealt and $H$ the highest so far.

If $C$ itself is the highest card so far, the probability of winning by holding it is the chance that it is higher than the $D$ cards left to be dealt, which in turn is the chance $L/N$ that it's higher than the first of them, times the chance $(L-1)/(N-1)$ that it's also higher than the second, and so on until the chance $(L-(D-1))/(N-(D-1))$ that it is higher than the last. Thus the probability that the current card is the highest is:

$$P_{\mbox{Hold}}(C,D) = \prod_{i=0}^{D-1} \frac{L-i}{N-i} =
\frac{L!(N-D)!}{N!(L-D)!}$$

This has to be compared with the probability that you will win if you discard this card and play optimally afterwards; you will of course choose the option with the higher probability of winning. We can compute this value $P_{\mbox{Discard}}(C,D,H)$ recurrently, based on averaging the chances $P(C',D-1,H')$ of winning given all the possible cards $C'$ in the next round, when there will be $D-1$ cards still to be dealt. Where $K$ is the number of cards remaining lower than $H$ (which is $H$ minus the number, $T-D$, of cards already dealt---or 0 if that's negative), and relying on the fact that the precise values of those cards doesn't matter:

$$P_{\mbox{Discard}}(C,D,H) = \frac{1}{N}\left( KP(1,D-1,H) 
+ \sum_{C'= H+1}^{S} P(C',D-1,C') \right)$$

And our recurrence is as follows:

$$P(C,0,H) = 1, \mbox{ for } C=H\mbox{, and }0 \mbox{, for } C \lt H$$

And for $D\geq 1$, if $C \lt H$:

$$P(C,D,H) = P_{\mbox{Discard}}(C,D,H)$$

And if $C=H$:

$$P(C,D,H) = \max(P_{\mbox{Hold}}(C,D),P_{\mbox{Discard}}(C,D,H))$$

In the case of a deck of $100$ cards with $10$ to be dealt, you will make up to $9$ decisions. Here are the thresholds below which you should discard each of the first nine cards dealt, even if it's the highest so far:

 | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9   |
 |----|----|----|----|----|----|----|----|-----|
 | 93 | 92 | 91 | 89 | 87 | 84 | 80 | 72 | 55  |
 
Numerically averaging the values of $P(C,9,C)$ for all possiblel first cards $C$ shows that the strategy wins about $62.2\%$ of the time.
 
 [Note: this solution replaces one that was shown to be "alternatively correct" by a helpful commenter!]
 
### Code (Python):

```python
{% include PickACardSecondTry538.py %}
```

<br>
 
