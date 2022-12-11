---
layout: post
published: false
title: 
date: 2022/12/11
subtitle:
tags:
---

>**Question**: Speaking of “football,” the Riddler Football Playoff (RFP) consists of four teams. Each team is assigned a random real number between 0 and 1, representing the “quality” of the team. If team A has quality $a$ and team B has quality $b,$ then the probability that team A will defeat team B in a game is $a/(a+b).$

In the semifinal games of the playoff, the team with the highest quality (the “1 seed”) plays the team with the lowest quality (the “4 seed”), while the other two teams play each other as well. The two teams that win their respective semifinal games then play each other in the final.

On average, what is the quality of the RFP champion?

<!--more-->

([FiveThirtyEight](URL))

## Solution

any of the $4$ players can end up on top and to do it they have to win their bracket, followed by the championship. take player A for example, to triumph they need to first defeat player D and then win the championship which would be against player B or player C. this means 

$$ P(\text{A wins it all}) = P(\text{A wins bracket})\left[P(\text{B wins bracket})P(\text{A beats B}) + P(\text{C wins bracket})P(\text{A beats C})\right] $$

there are corresponding expressions for players B, C, or D winning it all, tracking the probabilities of the events that lead them to top the podium. if we multiply them by the quality of the victor and add them up, then we have the expectation value for the quality of the victor for a given draw of $a, b, c,$ and $d:$

$$ \langle q\rangle_{(a,b,c,d)} = a P(\text{A wins it all}) + b P(\text{B wins it all}) + c P(\text{C wins it all}) + d P(\text{D wins it all}). $$

by symmetry, the expected quality of players A, B, C, and D are $\left(\frac{8}{10}, \frac{6}{10}, \frac{4}{10}, \frac{2}{10}\right).$ if we plug these values into the expression, we get $P(\text{A wins it all})\approx 0.64\ldots$ which isn't far off from the true value (see below).

to get the true value, we have to average this expectation value over all possible qualities $a, b, c$ and $d.$ because we assume the players are ranked first to last, $d$ can vary from $0$ up to $c,$ while $c$ can vary from $0$ up to $b,$ $b$ from $0$ up to $a,$ and $a$ can be anything from $0$ to $1.$

incorporating these limits, the expected quality of the victor is

$$ \langle q\rangle = \int\limits_0^1\text{d}a\ \int\limits_0^a\text{d}b\ \int\limits_0^b\text{d}c\ \int\limits_0^c\text{d}d\ \langle q\rangle_{(a,b,c,d)} $$

by the magic of computers, we can evaluate this numerically or symbolically, and find

$$ \langle q\rangle = \frac25\left[23-\pi^2\log4 -\log2\left(29+\log2\left(\log256 -39\right)\right) - 3\zeta(3)\right] $$ 

which is approximately $0.6735\ldots$ not far off from what we get using the mean-field values of $a, b, c$ and $d.$

<br>
