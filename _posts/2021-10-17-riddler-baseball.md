---
layout: post
published: true
title: Free pete rose
subtitle: Guess what happens in two world series games to win it all.
source: fivethirtyeight
tags: "probability recursion"
date: 2021/10/17
theme: probability
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

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-hit-these-riddles-out-of-the-park/))

## Solution

In the standard credit problem, there are $4$ solutions that perform optimally. 

One such solution is to bet on player A in the first four games, then player B in the last three games, $\tt{AAAABBB}.$ This only fails to produce $2$ correct predictions in the case where player B sweeps the series, or if player A wins in seven games while winning the last three games $\left({\tt BBBAAAA, BBABAAA, \ldots}\right)$.

So, the chance to win with it is 

$$1 - \frac{1}{2^4} - \binom{4}{1}\times\frac{1}{2^7} = 90.625\%.$$

### The main event

After each game, we have the opportunity to play our best, so long as we're not in a **hopeless position**.

### Hopeless positions

Hopeless positions are exactly those that we have no chance to win from. Concretely, any position where A or B have won more than half the games but we still have less than 2 correct guesses logged. 

If we use $S(c,\text{game})$ to represent the probability that a player wins from the position where they have $c$ correct guesses logged, and the current win-loss record is $\text{game}$ (for example, one value this could take would be $\tt{AAAB},$ the series where A wins the first three games and loses the third) then these hopeless positions are described by:

$$
S(\text{less than 2 correct guesses}, \text{4 games won by a team}) = 0.
$$

### Doing our best

If we're not in a hopeless position, then we have a choice to bet on A or B in the next game. In this case, the best thing to do is whatever we _expect_ the best thing to do is.

If we currently have $c$ correct guesses, and we bet on A, we could guess right or wrong, so our expected value is 

$$
\frac12 \overbrace{\langle S(c, \text{game : }{\tt B})\rangle}^\text{we bet on A and are wrong} + \frac12 \overbrace{\langle S(c + 1, \text{game : }{\tt A})\rangle}^\text{we bet on A and are right}
$$

On the other hand, we could bet B, which is worth

$$
\frac12 \overbrace{\langle S(c, \text{game : }{\tt A})\rangle}^\text{we bet on B and are wrong} + \frac12 \overbrace{\langle S(c + 1, \text{game : }{\tt B})\rangle}^\text{we bet on B and are right}
$$

We choose the best of these two options.

### Recursion

So, the expectation that we make at least two successful predictions follows the recursion relation:

$$\begin{align}
\langle S(c,\text{game})\rangle = \frac12\max \{ &\langle S(c, \text{game : }{\tt A})\rangle + \langle S(c + 1, \text{game : }{\tt B})\rangle, \\
&\langle S(c, \text{game : }{\tt B})\rangle + \langle S(c + 1, \text{game : }{\tt A})\rangle\}
\end{align}$$

Coding this up in Python:

```python
def contains_four(series, N):
  count = max(series.count('A'), series.count('B'))
  if count == 1/2 + N/2:
    return True
  else:
    return False

def S(correct_guesses, series, N, m):
  if correct_guesses < m and contains_four(series, N):
    return 0
  if correct_guesses == m:
    return 1
  return 0.5 * max(
        S(correct_guesses, series + 'A', N, m) 
        + S(correct_guesses + 1, series + 'A', N, m)
      , S(correct_guesses, series + 'B', N, m) 
        + S(correct_guesses + 1, series + 'B', N, m)
      )
```

we calculate for the case at hand $\left(N=7, m=2\right),$ there's a $93.75\%$ chance to win. 

As $N$ increases, the optimal success rate grows as

$$
\langle S(N)\rangle_\text{optimal} = 1 - \dfrac{N+1}{2^{N}}
$$

![](/img/2021-10-17-baseball-riddler.JPG){:width="500px" class="image-centered"}

<br>
