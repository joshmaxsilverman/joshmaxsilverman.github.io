---
layout: post
published: true
title: Maximum dice
date: 2021/08/16
subtitle: How high can your score get with optimal freeze-and-reroll?
source: fivethirtyeight
theme: probability
---

>**Question**: You have four standard dice, and your goal is simple: Maximize the sum of your rolls. So you roll all four dice at once, hoping to achieve a high score.
>
>But wait, there’s more! If you’re not happy with your roll, you can choose to reroll zero, one, two or three of the dice. In other words, you must “freeze” one or more dice and set them aside, never to be rerolled.
>
>You repeat this process with the remaining dice — you roll them all and then freeze at least one. You repeat this process until all the dice are frozen.
>
>If you play strategically, what score can you expect to achieve on average?
>
>**Extra credit**: Instead of four dice, what if you start with five dice? What if you start with six dice? What if you start with $N$ dice?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/are-you-clever-enough/))

## Solution

It's clear that if we get a good result early, like an extra $6,$ then we should opportunistically freeze it. The tricky decision is whether to freeze a middle-of-the-road result like a $5.$

It helps to think about what we'd do with many or few die. 

### Many

If, somehow, we rolled one hundred die and only got one $6,$ it would be overwhelmingly likely that on the next roll, we get a bunch of $6$s, so it would make sense to re-roll all but the $6.$

### Few

On the other hand, if we rolled two die and got $\\{4,4\\},$ it would make sense to freeze both $4$s since the expected value of a re-roll is just $\frac72.$ 

## The best strategy

To make the best decisions, we simply need to make the best decisions. 

If we roll five die and get $d_1 \geq d_2 \geq d_3 \geq d_4 \geq d_5,$ then we could

- Choice 1: keep $d_1$ and re-roll four die
- Choice 2: keep $\\{d_1, d_2\\}$ and re-roll three die
- Choice 3: keep $\\{d_1, d_2, d_3\\}$ and re-roll two die
- Choice 4: keep $\\{d_1, d_2, d_3, d_4\\}$ and re-roll one die
- Choice 5: keep all five die and the game is over.

If $\langle S_n \rangle$ is the expected value of rolling $n$ die, then the expected value of each of these choices are

- $d_1 + \langle S_4 \rangle$
- $d_1 + d_2 + \langle S_3 \rangle$
- $d_1 + d_2 + d_3 + \langle S_2 \rangle$
- $d_1 + d_2 + d_3 + d_4 + \langle S_1 \rangle$
- $d_1 + d_2 + d_3 + d_4 + d_5$

Which choice should we make? Whichever has the highest value. 

The value of $\langle S_5\rangle$ is the average value of this maximization over all possible sets $\\{d_1, d_2, d_3, d_4. d_5\\}.$

In general,

$$
\langle S_n \rangle = \bigg\langle \max_{u=1}^n\langle S_{n-u}\rangle + \sum\limits_{j=1}^u d_j \bigg\rangle_{d_1,\ldots,d_n}.
$$

## Organizing the calculation

Evidently, we need the values of $\langle S_1\rangle$ through $\langle S_{n-1}\rangle$ before we can calculate $\langle S_n\rangle.$

We can build up the calculations in order, first treating all the one die cases, then all two die cases, then all three die cases, and so on.

```python
import random
import itertools
from fractions import Fraction

expected_scores = [0]

def SN(n):
    total = 0
    for roll in itertools.product(range(1, 6 + 1), repeat=n):
        roll = list(roll)
        roll.sort()
        total += max(sum(roll[m:]) + expected_scores[m] for m in range(0, n)) 
    return(Fraction(total , 6 ** n))

for num_die in range(1, 9 + 1):
    expected_scores.append(SN(num_die))
```

Running the code, we get the following expected scores under the optimal strategy:

$$
\begin{array}{c|c}
\text{Case} & \text{Optimal score} \\ \hline
\langle S_1\rangle & \frac{7}{2} \approx3.5 \\
\langle S_2\rangle & \frac{593}{72} \approx 8.236 \\
\langle S_3\rangle & \frac{13049}{972} \approx 13.425 \\
\langle S_4\rangle & \frac{989065}{52488} \approx 18.844 \\
\langle S_5\rangle & \frac{1108166095}{45349632} \approx 24.436 \\
\langle S_6\rangle & \frac{332273594663}{11019960576} \approx 30.152 \\
\langle S_7\rangle & \frac{4621176159903031}{128536820158464} \approx 35.952 \\
\langle S_8\rangle & \frac{9026399212157210195951}{215892499727278669824} \approx 41.810 \\ 
\langle S_9\rangle & \frac{51897773343582111932203623017}{1087849490465798670885322752} \approx 47.707
\end{array}
$$

<br>
