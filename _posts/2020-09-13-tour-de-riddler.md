---
layout: post
published: true
title: Tour de 538
date: 2020/09/13
subtitle: How bad is a bike race when your teammate rage-quits?
source: fivethirtyeight
theme: probability
---

>**Question**: You've entered the annual Tour de 538 but, like a fool, you've gotten into a blowout fight with your teammate just before the race. As a result, they refuse to cooperate with you, claiming "the team is dead." Not a day has passed, but you rue it already. The other two people in the race still have their team spirit intact, and they'll cooperate, allowing one another to draft up so that they always finish one after the other. If, drafting aside, all cyclists are equally skilled, and the point allotment goes $\\{5,3,2,1\\},$ what is your expected point total? 

<!--more-->

([FiveThirtyEight](URL))

## Solution

With a lot of time on the bike, our troubled rider has a think. Their inner voice, which is decent at mental arithmetic, says

- "if I start first I stay in first,
- if I start second I stay in second if the person in first is not on the team ($p=1/3$),
- if I start third I stay in third if the person in fourth is not on the team ($p=1/3$),
- if I start last I stay last."

According to this logic, their expected score is 

$$\begin{align}
\langle S\rangle &= \frac{5 + (1/3\times 3 + 2/3\times 2) + (1/3\times 2 + 2/3\times 1) + 1)}{4} \\
&= 29/12 \\
&\approx 2.42 
\end{align}$$

It would be fun to extend this problem to the more disastrous case where there are $N$ cooperating teams, your contemptuous erstwhile partner, and you. Maybe I'll do that sometime this week.

<br>
