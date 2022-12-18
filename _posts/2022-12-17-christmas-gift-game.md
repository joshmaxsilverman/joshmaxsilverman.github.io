---
layout: post
published: true
title: White elephant
date: 2022/12/17
subtitle: How long must you wait to pawn your candle off on some poor relative?
tags: approximation linearity-of-expectation 
---

>**Question**: Every Christmas, Gary’s family has a gift exchange. And every year, there is a big fight over how much folks should spend on the gifts. This year, they decided to pair up. So if Virginia gives Justin a gift, then Justin gives Virginia a gift. This way, while there will still be arguments, only two people will be involved in each argument.
>
>There are $20$ people in the gift exchange. In the first round, everyone writes down the name of a random person (other than themselves) and the names go in a hat. Then if two people randomly pick each other’s names out of that hat, they will exchange gifts, and they no longer participate in the drawing. The remaining family members go on to round two. Again, they write down the name of anyone left, and again, any two people who pick each other exchange gifts.  
>
>This continues until everyone is paired up. And yes, if exactly two people remain, they still go through the process of selecting each other, even though they know who their partner will be.
>
>On average, what is the expected number of rounds until everyone is paired up?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-make-it-to-2023/))

## Solution

This problem is hard because the connections formed by earlier draws preclude certain potential pairs for later draws. 

I'm going to make the simplifying assumption that each pair is independent. In this scheme, we can calculate the probability that any given pair forms a loop in a round of the game, and simply multiply it by the number of possible pairs.

First of all, with two players, the probability that a pair forms is $P_2 = \frac12.$

With four players, there are two potential pairs. Since anyone can draw anyone from the hat, the chance that the first person doesn't pick themself is $\frac34.$ Similarly, the probability that the first person's pick picks them back is approximately $\frac14.$ Finally, there are two possible pairs. So, the probability that a pair forms is

$$ P_4 \approx 2\times\frac34\times\frac14 = \frac38\approx 37.5\\% $$

In general, for $n$ players, the probability that a pair forms in a round

$$ P_n = \frac{n}{2}\frac{n-1}{n^2} = \frac{n-1}{2n}. $$

So, at each stage of the game, we should expect to wait $P_n^{-1} = \frac{2n}{n-1}$ rounds for a pair to form.

The expected duration of the game is then just 

$$\begin{align}
  \langle T\rangle &= P_2^{-1} + P_4^{-1} + \ldots + P_{20}^{-1} \\
  &= 2 + \sum\limits_{j=2}^{10} P_{2j}^{-1} \\
  &= 2 + \sum\limits_{j=1}^{9} P_{2(j+1)}^{-1} \\
  &= 2 + \sum\limits_{j=1}^{9} \frac{4j+4}{2j+1} \\
  &= 2 + 18 + 2\sum\limits_{j=1}^9\frac{1}{2j+1} \\
  &\approx 22.26651
\end{align}$$

Using an $N = 10^8$ round simulation to estimate each $P_n$ produces $\hat{\langle T\rangle} \approx 22.13.$ Pretty good.

Ploting the approximation (gold points) against the high-$N$ simulation (blue)

![](/img/2022-12-17-christmas-game.png){:width="450 px" class="image-centered"}

we can see that the approximation gets asymptotic quickly and so, in general, the waiting time for an $n$ guest game is

$$ \langle T_n\rangle = 2n + 2\sum\limits_{j=1}^n\frac{1}{2j+1}. $$

The sum is much smaller than $n,$ so the waiting time is approximately linear in the number of guests.

<br>
