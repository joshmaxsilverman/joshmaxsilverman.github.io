---
layout: post
published: true
title: Soccer brackets
date: 2022/12/11
subtitle: Who will win when anything is possible?
source: fivethirtyeight
tags: uniform-probability rankings tournaments
theme: probability
---

>**Question**: Speaking of “football,” the Riddler Football Playoff (RFP) consists of four teams. Each team is assigned a random real number between 0 and 1, representing the “quality” of the team. If team A has quality $a$ and team B has quality $b,$ then the probability that team A will defeat team B in a game is $a/(a+b).$
>
>In the semifinal games of the playoff, the team with the highest quality (the “1 seed”) plays the team with the lowest quality (the “4 seed”), while the other two teams play each other as well. The two teams that win their respective semifinal games then play each other in the final.
>
>On average, what is the quality of the RFP champion?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-win-the-riddler-football-playoff/))

## Solution

Any of the $4$ players can end up on top. To do it they have to win their bracket, followed by the championship. Take player A for example, to triumph they need to first defeat player D and then win the championship which would be against player B or player C. This means 

$$ 
  \begin{align}
    P(\text{A wins it all}) &= P(\text{A wins bracket})\left[P(\text{B wins bracket})P(\text{A beats B}) + P(\text{C wins bracket})P(\text{A beats C})\right]\\
    &= \frac{a}{a+d}\left[\frac{b}{b+c}\frac{a}{a+b} + \frac{c}{b+c}\frac{a}{a+c}\right]
\end{align}    
$$

There are corresponding expressions for players B, C, or D winning it all, tracking the probabilities of the events that lead them to top the podium. 

### Local expectation value

If we multiply them by the quality of the victor and add them up, then we have the expectation value for the quality of the victor for a given draw of $a, b, c,$ and $d:$

$$ \langle q\rangle_{(a,b,c,d)} = a P(\text{A wins it all}) + b P(\text{B wins it all}) + c P(\text{C wins it all}) + d P(\text{D wins it all}). $$

By symmetry, the expected qualities of players A, B, C, and D are $(\frac{8}{10}, \frac{6}{10}, \frac{4}{10}, \frac{2}{10}).$ If we plug these values into the expression, we get $P(\text{A wins it all})\approx 0.6429\ldots$

<!-- which isn't far off from the true value (see below). -->

### Ensemble average

To get the true value, we have to average this expectation value over all possible qualities $a, b, c$ and $d.$ Because we assume the players are ranked first to last, $d$ can vary from $0$ up to $c,$ while $c$ can vary from $0$ up to $b,$ $b$ from $0$ up to $a,$ and $a$ can be anything from $0$ to $1.$ 

To account for this assumption, we have to multiply by the $4!$ possible orderings.

Incorporating these insights, the expected quality of the victor is:

$$ \langle q\rangle = 4! \int\limits_0^1\text{d}a \int\limits_0^a\text{d}b \int\limits_0^b\text{d}c \int\limits_0^c\text{d}d\ \langle q\rangle_{(a,b,c,d)} $$

By the magic of computers, we can evaluate this numerically or symbolically, and find the simple expression

$$ \langle q\rangle = \frac25\left[23-\pi^2\log4 -\log2\left(29+\log2\left[\log256 -39\right]\right) - 3\zeta(3)\right] $$ 

which is approximately $0.6735\ldots,$ not far off from what we get using the mean-field values of $a, b, c$ and $d.$

<br>
