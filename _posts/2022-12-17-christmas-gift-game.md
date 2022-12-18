---
layout: post
published: false
title: White elephant
date: 2022/12/17
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

this problem is hard because the connections formed by earlier draws preclude certain potential pairs for later draws. 

in this solution i'm going to make the simplifying assumption that each pair is independent. in this scheme, we can calculate the probability that any given pair forms a loop in a round of the game, and multiply it by the number of pairs.

first of all, with two players, there's chance $P_2 = \frac12$ that a pair is formed.

for four players, there are two potential pairs. since anyone can draw anyone from the hat, the chance that the first person doesn't pick themself is $\frac14.$ similarly, the probability that the first person's pick picks them back is $\frac14.$ finally, there are two potential pairs. so, the probability that a pair forms is

$$ P_4 \approx 2\times\frac34\times\frac14 = \frac38\approx 37.5\\% $$

in general, for $n$ players, the probability that a pair forms

$$ P_n = \frac{n}{2}\frac{n-1}{n^2} = \frac{n-1}{2n}. $$

in each round of the game, we should expect to wait $\langle T_n \rangle = P_n^{-1} = \frac{2n}{n-1}$ attempts for a pair to form.

the expected duration of the game is then just 

$$\begin{align}
  \langle T\rangle &= \langle T_2\rangle + \langle T_4\rangle + \ldots + \langle T_{2n}\rangle \\
  &= 2 + \sum\limits_{j=2}^{10} \langle T_{2j}\rangle \\
  &= 2 + \sum\limits_{j=1}^{9} \langle T_{2(j+1)}\rangle \\
    &= 2 + \sum\limits_{j=1}^{9} \frac{2j+2}{j} \\
    &= 2 + 18 + 2\sum\limits_{j=1}^9\frac{1}{j} \\
    &= 20 + H_9 \\
    &\approx 
\end{align}$$

<br>
