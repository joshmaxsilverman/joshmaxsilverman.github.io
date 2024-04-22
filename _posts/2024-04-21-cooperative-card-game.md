---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>**Question:** You and your friend both have standard decks of $52$ cards. First, you combine them into a single deck with $104$ cards, and you thoroughly shuffle it. Then, you randomly split this back into two decks with $52$ cards each—one for you, and one for your friend.
>
>Each of you draw one card at a time. If the two of you can make it through your entire decks without ever drawing the same card at the same time, you both win. Otherwise, you both lose.
>
>What is the probability that you and your friend will win this collaborative game?


<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-win-the-collaborative-card))

## Solution

first, we'll analyze the large deck limit, then we'll find the exact probability for two $52$ card decks.

### large deck limit

as the deck gets large the probability $P(\text{no collisions})$ will tend to $1/\sqrt{e}\approx 0.60653\ldots$

to see this, let's build the game one pair of draws at a time. if there are $N$ cards in each deck, the probability that the first pair collides is $(2N-2)/(2N-1)$ which can be written as

$$ \left(1 - \frac{1}{2N-1}\right). $$

the probability there is no collision on the second is likewise $(2N-4)/(2N-3)$ which can be written as 

$$ \left(1 - \frac{1}{2N-3}\right). $$

and so on. as $N$ goes to infinity, all $N$ of these factors are approximately $(1-1/2N)$ and so the overall probability to win is

$$ P(\text{no collisions}) \approx \left(1-\frac{1}{2N}\right)^N $$

which goes to $$ \frac{1}{\sqrt{e}}. $$

### $52$ card decks




<br>


