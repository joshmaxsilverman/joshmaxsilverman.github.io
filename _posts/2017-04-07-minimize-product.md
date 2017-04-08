---
layout: post
published: true
title: Minimize Product
date: 2017/04/07
---

>Consider the following game. In front of you is a stack of 10 cards printed with the numbers 0 through 9, one per card. The stack is shuffled and, sight unseen, you draw a number from the top. You look at the number and place it somewhere in the multiplication equation below. You then draw another number, look at it, and place it somewhere else in the equation. You do that two more times, until all four slots are filled. Once a digit is placed, it can’t be moved, and it can’t be drawn again because it’s no longer in the stack.
>
> ![Equation](/img/equation.png)
>
>Your goal is to build a multiplication equation with the lowest possible product. What is the optimal strategy? And how much of this game is luck and how much is skill? In other words, how much does the expected product under the optimal strategy differ from simply placing the cards randomly?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/can-you-outsmart-our-elementary-school-math-problems/))

## Solution:

The expectation for a randomly chosen $AB \times CD$:

$$E = E(100A\cdot C + 10A \cdot D + 10 B \cdot C + B \cdot D)$$

$$= 121 E(A\cdot C)$$

$$= 121 \times \frac{1}{90}\left(\sum_{m=0}^9 \sum_{n=0}^9 mn - \sum_{n=0}^9 n^2\right) = 121 \times \frac{58}{3} \approx 2339.33 $$

The expectation for starting with the number $m$, placing it top-left, and then placing the others randomly:

$$E(m\mbox{ top-left}) = E(100m \cdot C + 10m \cdot D + 10B \cdot C + B  \cdot D)$$

$$ = 110 E(m \cdot C) + 11E(B \cdot C)$$

$$ E(m \cdot C) = \left(\sum_{n=0}^9 \frac{1}{9} mn\right) - \frac{1}{9}m^2 
= \frac{45m-m^2}{9}$$

$$ E(B \cdot C) = \frac{1}{72}\left(\left(\sum_{n=0}^9\sum_{k=0}^9 nk\right) - \left(\sum_{n=0}^9 n^2\right) - \left( 2\times \sum_{n=0}^9 mn\right) + 2m^2 \right) $$

$$ = \frac{1740-90m+2m^2}{72} $$

$$E(m\mbox{ top-left}) = 110 \times \frac{45m-m^2}{9} + 11 \times \frac{1740-90m+2m^2}{72}$$

$$= \frac{1595}{6} + \frac{2145}{4}m - \frac{143}{12}m^2$$

Similarly, the expectation for placing $m$ top-right and then proceeding randomly:

$$E = E(100A \cdot C + 10A \cdot D + 10C \cdot m + D \cdot m)$$

$$ = 110\times \frac{1740-90m+2m^2}{72} + 11 \times \frac{45m-m^2}{9}$$

$$= \frac{7975}{3} - \frac{165}{2}m + \frac{11}{6}m^2$$

This allows us to see that placing a first number less than or equal to $4$ on the top-left is the best bet, while placing one greater than or equal to $5$ on the right is the best bet.  This gives us a good, though admittedly not decisive, reason to think that whatever the optimal strategy is, it involves the same decision for the first move.

When you get your second card, there are three places to choose from. For each of these, there are $56$ equally proabable sequences of a third and fourth card to consider. The calculation of the three expectations will be straightforward, if tedious, amounting to doing $168$ two-by-two-digit multiplications and averaging three sets of $56$ numbers. Choose a location with the highest of these expectations, and then proceed the same way with the third card---with only two expectations based on only $7$ possibilities to calculalte. You're done!

The code below quickly finds the optimal strategy for all card sequences and yields an overall expectation of $1056.84$, which is about $45.18\%$ of the expectation of playing randomly.

### Code:

```python
{% include MinimizeProductStrategy.py %}
```

<br>
