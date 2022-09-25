---
layout: post
published: false
title: Letters from the sea
date: 2022/09/25
subtitle: How many letters are you going to have to read?
tags: 
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
  \langle L\rangle = \frac12\langle L|\text{monster seen before day $N$}\rangle + \frac12\langle L|\text{monster not seen before day $N$}\rangle. 
$$

If G didn't put a cutoff on the number of ways he was willing to wait, then D would expect to receive $\langle L\rangle_\text{no cutoff} = 1/p$ letters altogether.

When there's a cutoff, $\langle L|\text{monster not seen before day $N$}\rangle$ is equal to $N,$ the number of letters sent by the time G gives up on day $N.$ But when there's no cutoff, this expectation is $N$ (the number of days without a sighting) plus $\langle L\rangle_\text{no cutoff}$ (since our fortunes after day $N$ are not effected by our efforts before day $N$).

<br>
