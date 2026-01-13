---
layout: post
published: true
title: Keep on singing
date: 2023/02/03
subtitle: Will you get to zero bottles of beer on the wall before someone loses their cool?
source: fivethirtyeight
tags: recursion expectation markov
theme: probability
---

>**Question**: You and your friends are singing the traditional song, “99 Bottles of Beer.” With each verse, you count down the number of bottles. The first verse contains the lyrics “$99$ bottles of beer,” the second verse contains the lyrics “$98$ bottles of beer,” and so on. The last verse contains the lyrics “$1$ bottle of beer.”
>
>There’s just one problem. When completing any given verse, your group of friends has a tendency to forget which verse they’re on. When this happens, you finish the verse you are currently singing and then go back to the beginning of the song (with $99$ bottles) on the next verse.
>
>For each verse, suppose you have a $1$ percent chance of forgetting which verse you are currently singing. On average, how many total verses will you sing in the song?
>
>**Extra credit**: Instead of “$99$ Bottles of Beer,” suppose you and your friends are singing “N Bottles of Beer,” where $N$ is some very, very large number. And suppose your collective probability of forgetting where you are in the song is $1/N$ for each verse. If it takes you an average of $K$ verses to finish the song, what value does the ratio of $K/N$ approach?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-take-down-all-the-bottles-of-beer/))

## Solution

at each step, the song can either proceed to the next step (with probability $(1-f)$) or return to $N = 99$ bottles (with probability $f$). so, the expectation number of verses to finish from "$j$ bottles of beer on the wall" is

$$ T_j = 1 + (1-f)T_{j-1} + fT_{N}. $$

plugging this back into itself a few times, and using the fact that $T_0 = 0$, we get

$$
  \begin{align}
      T_j &= 1 + (1-f)T_{j-1} + fT_{N} \\
          &= 1 + \left[(1-f) + (1-f)^2T_{j-2}\right] + \left[(1-f)f + f\right]T_{N} \\
          &= 1 + \left[(1-f) + (1-f)^2 + (1-f)^3T_{j-3}\right] + \left[(1-f)^2f + (1-f)f + f\right]T_{N} \\
          &= \left[1 + (1-f) + (1-f)^2 + \ldots + (1-f)^{j-1}\right] + f\left[1 + (1-f) + (1-f)^2 + \ldots + (1-f)^{j-1}\right]T_{N} \\
          &= \dfrac{1 - (1-f)^j}{f} + \left[1 - (1-f)^{j}\right]T_{N}
  \end{align}
$$

so, 

$$ T_{N-1} = \dfrac{1 - (1-f)^{N-1}}{f} + \left[1 - (1-f)^{N-1}\right]T_{N} $$

plugging this into the equation for $T_{N},$ we get

$$
  \begin{align}
    T_{N} &= \frac{1}{1-f} + T_{N-1} \\
    &= \frac{1}{1-f} + \dfrac{1-(1-f)^{N-1}}{f} + \left[1-(1-f)^{N-1}\right]T_{N} \\
    &= \dfrac{1-(1-f)^{N}}{(1-f)f} + \left[1-(1-f)^{N-1}\right]T_{N} \\
    &= \dfrac{1-(1-f)^N}{(1-f)f}\dfrac{1}{(1-f)^{N-1}} \\
    &= \frac{1}{f}\left[\dfrac{1}{(1-f)^{N}}-1\right] 
  \end{align}
$$

since the probability of forgetting is staked to $f=1/N,$ $T_N$ becomes

$$ T_N = N\left[\dfrac{1}{(1-1/N)^{N}}-1\right], $$

so $T_N/N$ approaches $(e-1)$ as $N$ gets big.


<br>
