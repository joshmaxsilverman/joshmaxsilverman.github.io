---
layout: post
published: true
title: Matching Cards
date: 2018/06/15
---

>I have a matching game app for my 4-year-old daughter. There are 10 different pairs of cards, each pair depicting the same animal. That makes 20 cards total, all arrayed face down. The goal is to match all the pairs. When you flip two cards up, if they match, they stay up, decreasing the number of unmatched cards and rewarding you with the corresponding animal sound. If they don’t match, they both flip back down. (Essentially like Concentration.) However, my 1-year-old son also likes to play the game, exclusively for its animal sounds. He has no ability to match cards intentionally — it’s all random.
>
>If he flips a pair of cards every second and it takes another second for them to either flip back over or to make the “matching” sound, how long should my daughter expect to have to wait before he finishes the game and it’s her turn again?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-many-phones-do-you-need-to-win-hq-trivia/))

## Solution

Let $E(n)$ be the expected number of turns remaining when there are $p$ pairs of cards still face-down.  Clearly,

$$E(1) = 1$$

If there are $n+1$ pairs still face-down, then on a given turn, whichever card is turned first, there is a $1$ out of $2n+1$ chance of matching it with the second card. Given that "it's all random," the turns are independent, and so the expected number of turns before matching is $1$ divided by the chance of matching on a single turn. So that expectation is $2n+1$.  It follows that,

$$E(n+1) = (2n+1) + E(n)$$

Notice that $E(1)$ is $1^2$. We'll now prove that for all $n$, $E(n)$ is $n^2$.  Our proof will employ mathematical induction: we have shown that it's true for the base case of $n=1$, and so we show that, if it's true for any given value of $n$, it's also true for $n+1$.  So we assume:

$$E(n) = n^2$$

Then,

$$E(n+1) = (2n+1) + E(n) = n^2 + 2n +1 = (n+1)^2$$

So with $10$ pairs of cards, we expect to take $100$ turns, or $200$ seconds, to finish.

We relied on the fact that the expected number of probabilistically-independent turns it will take to succeed, where each turn has a $1/k$ chance of success, is $k$.  Had we not already known that, we could have proved it as follows.  Before a given turn, there is a $1/k$ chance that we will succeed in $1$ turn, and a $1-1/k$ chance that we won't, and so after that $1$ turn be right back where we started, expecting just as many more turns as we expected initially.  That is:

$$ E = \frac{1}{k} \cdot 1 + (1-\frac{1}{k})(1 + E) $$

Solving this, we find that,

$$ E = k $$

<br>
