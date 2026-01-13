---
layout: post
published: true
title: Sicilian solitaire
date: 2023/02/19
subtitle: There's nothing to do and there's nothing to win
source: fivethirtyeight
tags: recursion approximation
theme: probability
---

>**Question**: There’s a version of solitaire played in southern Italy with a deck of $40$ Neapolitan cards, with four suits numbered from $1$ to $10.$ The deck is shuffled and then cards are turned over one at a time. Flipping over the first card you say “one,” the second card “two” and the third card “three.” You repeat this, saying “one” for the fourth card, “two” for the fifth card and “three” for the sixth card. You continue your way through the deck, until you at last say “one” for the $40^\text{th}$ card.
>
>If at any point the number you say matches the value of the card you flip over, you lose.
>
>What is your probability of winning the game?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/how-many-rectangles-can-you-make/))

## Solution

this puzzle has two questions. the first is, what is the probability of winning? the second is, what is the probability someone would choose to play this game?

we'll approach the first question in two ways — by a simple approximation, and by exact recursion.

### approximation

in the deck, there are $12$ cards whose positions we care about: the four $1$s, the four $2$s, and the four $3$s. because the deck is scrambled, on average, each of those cards has probability $\frac23$ to not be placed into one of its own slots.

generalizing to $s$ suits and $r$ ranks, and $c$ counts, this gives

$$ P_\text{win} = \left(1-\frac{1}{c}\right)^{sc}. $$

this is a good approximation that gets better as $r$ increases.

### recursion

we can imagine placing numbers one at a time, starting from the first slot. 

suppose we've already placed $m$ cards, still have $n_1$ $1$s, $n_2$ $2$s, and $n_3$ $3$s, haven't lost yet, and are currently on a "$1$" slot. 

this means we can remain a winner so long as we place anything but a $1$ on the present turn. we can do this by placing a $2$ (probability $n_2/(40 - m)$), a $3$ (probability $n_3/(40-m)$), or any number from $4$ to $10$ (probability $(40 - m - n_1 - n_2 - n_3)/(40 - m)$).

this gives us 

$$
\begin{align}
P(n_1, n_2, n_3, m) &= \dfrac{n_2}{40-m}P(n_1, n_2-1, n_3, m+1) \\
                    &+ \dfrac{n_3}{40-m}P(n_1, n_2, n_3-1, m+1) \\
                    &+ \dfrac{40-m-n_1-n_2-n_3}{40-m}P(n_1, n_2, n_3, m+1) 
\end{align}
$$

when $m\bmod 3 = 1,$ with similar relationships for the $m\bmod 3 = 2$ and $m\bmod 3 = 0$ cases.

generalizing, we get

$$ P(\vec{n}, m) = \left[\sum_{j\neq \left(m\,\bmod\,c\right)} \frac{n_j}{rs - m}P(\vec{n} - \hat{e}_j, m+1)\right] + \dfrac{rs - m -\sum_j n_j}{rs -m}P(\vec{n}, m+1) $$

with $P(0,0,0,rs) = 1$ as the base case.

with $\vec{n} = \left(n_1 = 4, n_2 = 4, n_3 = 4\right),$ we get 

$$ P(\vec{n}, 0) = \dfrac{1124550557}{135373757400} \approx 0.008307 $$

### trends

we can use the recursive result to confirm two trends:

- as $r$ increases, $P_\text{win}$ does indeed tend toward $(1-1/c)^{sc}.$

![](/img/2023-02-19-vary-r-prime.png){:width="450 px" class="image-centered"}

- $P_\text{win}$ plummets to zero as the number of suits $s$ increases.

![](/img/2023-02-19-vary-s-prime.png){:width="450 px" class="image-centered"}

finally, $P_\text{win}$ tends toward $e^{-s}$ as $c$ gets large $($with $c=3$, the example in the problem underwhelms $e^{-4}\approx 0.0183\ldots$ for $s=4).$
<br>
