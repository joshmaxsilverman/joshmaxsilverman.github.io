---
layout: post
published: true
title: Descending Die
date: 2019/11/16
---


>You are given a fair, unweighted 10-sided die with sides labeled 0 to 9 and a sheet of paper to record your score. (If the very notion of a fair 10-sided die bothers you, and you need to know what sort of three-dimensional solid it is, then forget it — you have a random number generator that gives you an integer value from 0 to 9 with equal probability. Your loss — the die was a collector’s item.)
>
>To start the game, you roll the die. Your current “score” is the number shown, divided by 10. For example, if you were to roll a 7, then your score would be 0.7. Then, you keep rolling the die over and over again. Each time you roll, if the digit shown by the die is less than or equal to the last digit of your score, then that roll becomes the new last digit of your score. Otherwise you just go ahead and roll again. The game ends when you roll a zero.
>
>For example, suppose you roll the following: 6, 2, 5, 1, 8, 1, 0. After your first roll, your score would be 0.6, After the second, it’s 0.62. You ignore the third roll, since 5 is greater than the current last digit, 2. After the fourth roll, your score is 0.621. You ignore the fifth roll, since 8 is greater than the current last digit, 1. After the sixth roll, your score is 0.6211. And after the seventh roll, the game is over — 0.6211 is your final score.
>
>What will be your average final score in this game?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-low-can-you-roll/))

## Solution

### Via Recurrence

Suppose I initially roll a $5$. Then I will score $.5$ plus, on average, a tenth of what I'd score if I was using a $6$-sided die numbered $0$ to $5$. Where $E_n$ is the average score with an $n$-sided die:

$$E_n = \sum_{i=1}^{n-1} \frac{1}{n}\left( \frac{i}{10} + \frac{1}{10}E_{i+1} \right)
= \frac{1}{10n}\sum_{i=1}^{n-1} ( i + E_{i+1} )
$$

We can then express $E_n$ in terms of $E_{n-1}$ as follows:

$$E_n =  \frac{n-1}{n} E_{n-1} + \frac{1}{10n}(n - 1 + E_n)$$

$$E_n = \frac{(n-1)(10E_{n-1} + 1)}{10n - 1}$$

Since we know that $E_1$ is $0$ (a one-sided die is, I guess, a sphere with a zero on it), this lets us calculate $E_n$ for arbitrary $n$. For instance, $E_2$ is $1/19$. 

Suppose that, as in the case of $E_2$, for some $n$, $E_{n-1}$ is $(n-2)/19$. Then:

$$E_n = \frac{(n-1) \left( \frac{10(n-2)}{19} + 1\right)}{10n - 1)}
= \frac{n-1}{19}
$$

Thefore, for all $n$, $E_n$ is $(n-1)/19$, and in particular the average score with a $10$-sided die is $9/19$.

### Via Infinite Sum

Assuming an $n$-sided die numbered from $0$ to $n-1$, the first digit will be $(n-1)/2$ on average, contributing a value of $(n-1)/20$ to the score. Whatever it is, the second digit will be half of it, on average, contributing an average of $1/20$ as much. Similarly for the third and subsequent digits. By the linearity of expectation, the expectation of a sum is the sum of the expectations.  Therefore the average score is the sum of the expected contributions of the digits, which start at $(n-1)/20$, decreasing every digit by a factor of $1/20$:

$$E_n = (n-1)/20 \sum_{i = 0}^\infty \left(\frac{1}{20}\right)^i$$

The infinite sum is a geometric series with ratio $1/20$, and hence a value of $1/(1 - 1/20)$, or $20/19$. Therefore $E_n$ is $(n-1)/19$. 

<br>