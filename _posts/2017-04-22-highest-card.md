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

Without changing anything important, let's restate the situation as your being dealt cards, one at a time, from a deck. You can "hold" just once, and you win if the card you hold is higher than the cards dealt before or after it.

At every decision point, you have not lost yet, and so your current card is the highest so far dealt. Whatever the size of the deck and however many cards in total you are being dealt, the important facts you know are that you have been dealt a given card, that there are $D$ cards left to be dealt, $L$ cards lower than this one still in the deck, and $N$ cards total still in the deck. The key question you face is how likely you are if you play optimally from here to end up holding a higher card than this one.

The chance that the current card is higher than the $D$ cards left to be dealt is the chance that it's higher than the first of them, which is $L/N$ times the chance that it's also higher than the second, which is $(L-1)/(N-1)$, and so on until the last, with probability $(L-(D-1))/(N-(D-1))$. Thus the probability that the current card is the highest is:

$$\prod_{i=0}^{D-1} \frac{L-i}{N-i} =
\frac{L!(N-D)!}{N!(L-D)!}$$

You should discard the current card if this probability is less than $1/2$.

In the case of a deck of $100$ cards with $10$ to be dealt, you will make up to $9$ decisions. Here are the thresholds below which you should discard each of the first nine cards dealt (if you get that far without holding):

 | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9   |
 |----|----|----|----|----|----|----|----|-----|
 | 94 | 94 | 94 | 94 | 93 | 91 | 87 | 79 | 59  |
 
 <br>
 
