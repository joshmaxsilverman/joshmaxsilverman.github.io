---
layout: post
published: false
title: It's Pumpkin Time
date: 2020/11/1
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

_Disclaimer_: Through studious indifference, I have managed to $30$ virtually undisturbed by any known results in number theory. So I am able to document here a voyage of personal discovery, stumbling through basic ideas about how the integer numbers relate to themselves.

### The Pumpkin Shuffle

A round constitutes $N$ people counting themselves off around the circle until the last of them says $``N''$ and is eliminated for getting caught holding the David S. Pumpkin's hot pumpkin, and the next round begins with the person to their left. We're told that the first three people to be eliminated are positioned $18,$ $31,$ and $0$ positions to the left of the person who started their round and that there are $61$ people in the circle at the beginning of the game. 

Evidently, $N$ is bigger than the number of people, since it doesn't skip an equal number of people in the first three rounds. So, that counting $N$ positions ends the first round at position $19$ means that $N$ is equal to $19$ plus some number of multiples of the number of people, $P$. In other words

$$ N = 18 + \text{some integer}\times P. $$

Likewise, the other two facts lead to

$$\begin{align}
N &= 31 + \text{some other integer}\times (P - 1) \\
N &= 0 + \text{yet another integer}\times (P - 2).
\end{align}$$

This tells us that there are three equivalent representations for $N.$ My first instinct was to set them equal to each other to find a relationship between the undetermined integers. 

But, before doing this, let's settle on some symbols. We'll call the remainders (like $18,$ $31,$ and $0$) $r_1,$ $r_2,$ and $r_3,$ and the modular bases (like $61,$ $60,$ and $59$) $m_1,$ $m_2,$ and $m_3.$ Also, we'll call the undetermined integers $x_1,$ $x_2,$ and $x_3.$



<br>
