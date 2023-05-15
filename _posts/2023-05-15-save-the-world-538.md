---
layout: post
published: false
title: Save the world
date: 2023/05/15
subtitle: 
tags: approximation 
---

>**Question**: Later this year, aliens will visit Earth and announce that they intend to blow up the planet. (Lovely.)
>
>However, they present you with a challenge. If you successfully complete the challenge, they’ll blow up another planet instead (probably Neptune, because why not).
>
>The aliens have telepathically assigned each of the 8 billion human beings on Earth a unique random number, uniformly distributed between $0$ and $1.$ Each human being knows their own number, but no one else’s. Your challenge is to identify the person with the highest number.
>
>The aliens will allow you to ask a single yes-or-no question to all $8$ billion people. This question must be the same for everyone and will be answered simultaneously by everyone. The aliens have courteously agreed to aggregate the data for you as to who answers your question yes or no.
>
>What question would you ask, and what are your chances of saving the world?

<!--more-->

([FiveThirtyEight](URL))

## Solution

with one question and no interaction between Earthlings, our question has to be about the size of the interviewees number, i.e. "Is your number bigger than $t$?"

if we set $t$ too low, then we risk multiple people responding "yes", forcing us to pick at random between all those who did. but if we set $t$ too low (something much less than $1/(8\times10^9),$ we risk there being nobody able to answer "yes".

the chance that we can find the person with the top number is the sum of all these possibilities.

the chance that only one person's number is bigger than $t$ is

$$ \binom{N}{1}(1-t)t^{N-1}. $$

in this case, we are guaranteed to find the person with the top number.

if there are two "yes" then either one could be bigger than the other, and we have to choose at random between them

$$ \frac12 \binom{N}{2}(1-t)^2 t^{N-2} .$$

carrying on, the probability that we find the person with the top number is 

$$ \begin{align}
  P(\text{find top}|t) &= \binom{N}{1}(1-t)t^{N-1} + \frac12 \binom{N}{2}(1-t)^2 t^N + \frac13 \binom{N}{3}(1-t)^3 t^{N-3} + \ldots \\
  &= \sum\limits_j \frac{1}{j}\binom{N}{j}(1-t)^jt^{N-j}
\end{align}$$

with $N$ large, we can make a couple of approximations. 

first, the binomial factors $\binom{N}{j}$ become $\approx N^j/j!.$ second, we expect $t$ to be close to $1,$ so the factors $t^{N-j}$ become $N^j$ (for powers of $j$ where that doesn't hold, the $(1-t)^j$ will have already supressed the term).$

so, we can write the total probability as

$$
  P(\text{find top}|t) = t^N\left[N(1-t) + \frac12\frac{1}{2!}N^2(1-t)^2 + \frac13\frac{1}{3!}N^3(1-t)^3 + \ldots\right] 
$$

the series on the inside is almost $\exp N(1-t)$ but for the fractions $1/2, 1/3, \ldots,$ and with a little massaging, we can write the series in terms of it. if we introduce a dummy variable $z,$ then divide by it, then integrate it out, we get the original series for $P(\text{find top}|t).$

$$ 
  \begin{align}
e^{N(1-t)z} - 1 &= t^N\left[N(1-t)z + \frac{1}{2!}N^2(1-t)^2z^2 + \frac{1}{3!}N^3(1-t)^3z^3 + \ldots\right] \\
\frac{e^{N(1-t)z} - 1}{z}&= \frac{t^N}{z}\left[N(1-t) + \frac{1}{2!}N^2(1-t)^2z + \frac{1}{3!}N^3(1-t)^3z^2 + \ldots\right] \\
\int\limits_0^1 dz\, \frac{e^{N(1-t)z} - 1}{z} &= \frac{t^N}{z}\left[N(1-t) + \frac12\frac{1}{2!}N^2(1-t)^2z + \frac13\frac{1}{3!}N^3(1-t)^3z^2 + \ldots\right] \\
\int\limits_0^1 dz\, \frac{e^{N(1-t)z} - 1}{z} &= P(\text{find top}|t)
\end{align} 
$$

performing the integral, we get

$$ P(\text{find top}|t) = t^N\left(\log\frac{1}{N(1-t)} - \Gamma(0, -N(1-t)) - \gamma\right). $$

plotting $P(\text{find top}|t),$ we see a sharp peak which we can find with binary search

![](/img/2023-05-15-save-world-plot2.png){:width="450px" class="image-centered"}

```mathematica
P[t_, n_] := -t^
    n (EulerGamma + Gamma[0, n (-1 + t)] + Log[n (-1 + t)]);
NMaximize[{P[t, 8 10^8], 1 - 10^-5 <= t <= 1}, t, 
 WorkingPrecision -> 15]
```

which gives $t^* \approx 1-1.879\times10^{-9}$ and $P(\text{find top}|t^*) \approx 51.735%$

<br>
