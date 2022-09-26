---
layout: post
published: true
title: Letters from the sea
date: 2022/09/25
subtitle: How many letters are you going to have to read?
tags: expectation scaling translation
---

>**Question:** Graydon is about to depart on a boating expedition that seeks to catch footage of the rare aquatic creature, _F. Riddlerius_. Every day he is away, he will send a hand-written letter to his new best friend, David Hacker. But if Graydon still has not spotted the creature after $N$ days (where $N$ is some very, very large number), he will return home.
>
>Knowing the value of $N,$ Graydon confides to David there is only a $50\\%$ chance of the expedition ending in success before the $N$ days have passed. But as soon as any footage is collected, he will immediately return home (after sending a letter that day, of course).
>
>On average, for what fraction of the $N$ days should David expect to receive a letter?

<!--more-->

([FiveThirtyEight](URL))

## Solution

The number of letters D expects is equal to

$$
  \langle L\rangle = \frac12\langle L|\text{monster seen before day }N\rangle + \frac12\langle L|\text{monster not seen before day }N\rangle. 
$$

If G didn't put a cutoff on the number of days he's willing to wait, then D would expect to receive $\langle L\rangle_\text{no cutoff} = 1/p$ letters altogether. Likewise, the expectation $\langle L|\text{monster not seen before day }N\rangle$ is $N$ plus $\langle L\rangle_\text{no cutoff}$ (since our fortunes after day $N$ are not effected by our efforts before day $N$).

But when there's a cutoff, $\langle L|\text{monster not seen before day $N$}\rangle$ is equal to $N,$ the number of letters sent by the time G gives up on day $N.$ 

Whether or not there's a cutoff, the value of $\langle L|\text{monster seen before day }N\rangle$ is the same. Using the no cutoff case to solve for it, we get

$$
  \langle L|\text{monster seen before day }N\rangle = N - \frac1p
$$

So, when G has a cutoff, the expected number of letters is 

$$ 
  \begin{align}
    \langle L\rangle &= \frac12\langle L|\text{monster seen before day $N$}\rangle + \frac12\langle L|\text{monster not seen before day $N$}\rangle. \\
    &= \frac12 \left(N - \frac1p\right) + \frac12 N \\
    &= \dfrac{1}{2p}
  \end{align}
$$

Now, since there's just a $50\\%$ chance to see the monster by day $N,$ we can set $(1-p)^N = 1/2$ and get $p = 1 - 2^{-1/N}.$

Then, the fraction of days with a letter is

$$
  f = \dfrac{\langle L\rangle_\text{cutoff}}{N} = \dfrac{1}{2N}\dfrac{1}{1-2^{-1/N}}.
$$

Writing $2^{-1/N}$ as $e^{-\frac1N \log{2}}$ and expanding to first order, we get

$$
  \begin{align}
    f &= \dfrac{1}{2N}\dfrac{1}{1-(1 - \frac1N \log{2})} \\
    &= \frac{1}{2\log 2}
  \end{align}
$$

for big $N.$


<br>
