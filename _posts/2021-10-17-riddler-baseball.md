---
layout: post
published: true
title: Free Pete Rose
date: 2021/10/18
---

>**Question:** 
>Over in the National League Championship Series, the Washington Rationals and the St. Louis Ordinals (known as the “Ords” for short) are also evenly matched. Again, both teams are equally likely to win each game of the best-of-seven series.
>
>You enter a competition in which you must predict the winner of each of the seven games before the series begins. If any or all of the fifth, sixth or seventh game are not played, you are not credited with predicting a winner.
>
>You win the competition if you predict at least two games correctly. If you optimize your strategy for picking winners, what is the probability you will win the competition?
>
>Extra credit: You enter a second competition in which you must pick the winner of the first game and then of each next game, knowing who won in all the previous games. Again, if you optimize your strategy, now what is the probability you will predict at least two games correctly?

<!--more-->

([FiveThirtyEight](URL))

## Solution

In the standard credit problem, there are $4$ solutions that perform optimally. 

One such solution is to always bet on player A in the first 4 games, then player A in the last 3 games. This only fails to produce 2 correct predictions in the case where player B sweeps the series, or player B wins in 5 games by winning the first three games, then losing, then winning the fifth. So, the chance to win with it is $1 - \frac{8}{128} - \frac{4}{128} = 90.625\%.$

### The main event

After each game, we have the opportunity to play our best, so long as we're not in a **hopeless position**.

### Hopeless positions

Hopeless positions are exactly those that we have no chance to win from. Concretely, any position where A or B have won more than half the games but we still have less than 2 correct guesses logged. 

If we use $S(c,\text{game})$ to represent the probability that a player wins from the position where they have $c$ correct guesses logged, and the current win-loss record is $\text{game}$ (for example, one value this could take would be $\text{AAAB},$ the series where A wins the first three games and loses the third) then these hopeless positions are described by:

$$
S(\text{less than 2 correct guesses}, \text{4 games won by a team}) = 0.
$$

### Doing our best

If we're not in a hopeless position, then we have a choice to bet on A or B in the next game. In this case, the best thing to do is whatever we _expect_ the best thing to do is.

If we currently have $c$ correct guesses, and we bet on A, we could guess right or wrong, so our expected value is 

$$
\frac12 \overbrace{\langle S(c, \text{game : B})\rangle}^\text{we bet on A and are wrong} + \frac12 \overbrace{\langle S(c + 1, \text{game : A})\rangle}^\text{we bet on A and are right}
$$

On the other hand, we could bet B, which is worth

$$
\frac12 \overbrace{\langle S(c, \text{game : A})\rangle}^\text{we bet on B and are wrong} + \frac12 \overbrace{\langle S(c + 1, \text{game : B})\rangle}^\text{we bet on A and area right}
$$

We choose the best of these two options.

### Recursion

So, the expectation that we make at least two successful predictions follows the recursion relation:

$$\begin{align}
\langle S(c,\text{game})\rangle = \max \{ &\frac12 \langle S(c, \text{game : A})\rangle + \frac12 \langle S(c + 1, \text{game : B})\rangle, \\
&\frac12 \langle S(c, \text{game : B})\rangle + \frac12 \langle S(c + 1, \text{game : A})\rangle
\}
\end{align}$$

Coding this up in Python:

```python
def S(correct_guesses, series, n, m):
  if correct_guesses < m and contains_four(series, n):
    return 0
  if correct_guesses == m:
    return 1
  return 0.5 * max(
        S(correct_guesses, series + 'A', n, m) 
        + S(correct_guesses + 1, series + 'A', n, m)
      , S(correct_guesses, series + 'B', n, m) 
        + S(correct_guesses + 1, series + 'B', n, m)
      )
```

we calculate for the case at hand $\left(n=7, m=2\right),$ there's a $93.75\%$ chance to win. 

<br>
