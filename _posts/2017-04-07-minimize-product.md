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

After the first move, you've either placed a low number on the left or a high one on the right. Suppose it's a low one. Then, if you get a high second number (one at least as large as the average of the remaining numbers), you should place it somewhere on the right, because you have two more chances with equal numbers of low and high numbers remaining and so are likely to land a low number with at least one of them. And if you get a low second number, it should go on the bottom-left, because, with the low numbers depleted, you're otherwise taking a big ($5/14$) risk of ending up with a high number on the bottom-left. Similar reasoning applies to a high first number: if the second number is low it should go somewhere on the left, and if high, on the bottom-right. 

If the first-second sequence is high-high or low-low, there is no further decision to make about the placement of the second number. However, if it is high-low or low-high there will be two choices as to where to put the second number. Here, we want to maximize the chances that, in the end, the bigger number on the right is paired with the bigger number on the left.

Why? Call the four numbers, in order of smallest-to-largest, $A$, $B$, $C$, and $D$. The two natural candidate products are $AC \times BD$ and $AD \times BC$. The two products are:

$$100 A\cdot B + 10 A \cdot D + 10 B \cdot C + C \cdot D $$

$$100 A\cdot B + 10 A \cdot C + 10 B \cdot D + C \cdot D $$

The latter minus the former is $10\times ((B(D-C))-(A(D-C))$, which is positive, and so it is the former product that we should aim for.

So here's what we do. Let $7$, $8$, and $9$ be the high-high numbers, $5$ and $6$ be the low-high numbers, and similarly for low-low ($0$, $1$, $2$) and high-low ($3$, $4$). Suppose our first number is high-high; then, chances are it will be our highest number so we don't want our lowest number next to it. So if we get a low-low second number, it goes in the bottom-left. A high-low number goes in the top-left. If our first number was low-high, chances are it will not be our highest number, so it should be paired only with a low-low or mid-low number.  Similarly for a low first number.

That brings us to the third number. Here, the only question is whether the fourth number is likelier to be higher or lower. If we have two numbers on the left or on the right, we place the third so that we are likely to pair the biggest left-number with the biggest right-number. If one number is on the left and one on the right, we place the third so that the bigger of the third and fourth numbers is likely to be on the left.

And that's it. This strategy has an expectation of $1063.64$, which is $45.47\%$ of the expectation for random placements. I arrived at that figure computationally, but not by random Monte Carlo simulation. Instead, the code considers all $5040$ possible sequences of four numbers and averages the products that result from following this strategy.

### Code:

```python
{% include MinimizeProductStrategy.py %}
```

<br>
