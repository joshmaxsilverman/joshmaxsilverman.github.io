---
layout: post
published: true
title: Soccer buses
date: 2022/12/07
subtitle: How many trips will the poor saps have to make?
source: fivethirtyeight
tags: recursion symmetry linearity-of-expectation
theme: probability
---

>**Question**: A certain hotel in Qatar is hosting 11 American fans and seven Dutch fans. Since no alcohol is available inside the stadiums, the fans spend the afternoon at the hotel bar before shuttle buses will take them to a match. Then, they haphazardly write their room numbers on a big board by the concierge desk.
>
>To avoid any rowdiness between rival fans, shuttle bus drivers have been instructed to ferry American and Dutch fans separately. To ensure this, a shuttle pulls up in front of the hotel, and its driver calls out room numbers from the board, one by one at random. As long as they support the same team, each fan climbs aboard the bus and their room number is erased. Once the driver calls out the room number of a fan for the second team, the shuttle leaves with only the fans of the single team aboard. The next shuttle then pulls up and repeats the process.
>
>What is the probability that the last shuttle ferries American fans?
>
>Extra credit: On average, what is the expected number of shuttle buses needed to ferry all 18 fans?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-separate-the-world-cup-fans/))

## Solution

**A note**: *there are two ways to interpret the inter-group policy. One is that when a new group is triggered by switching from e.g. a run of American fans to a Dutch fan, the Dutch fan begins the next group. The other way is that the Dutch fan has only triggered the transition, but who begins the next group will be redrawn from random. We'll solve the problem both ways.*

# Interpretation 1

The order of the As and Ds is random and any random order is valid. For any particular random order we can cyclically permute the order (moving the first person to last, the second person to first, and so on) and make another valid order. As we cycle the order there will be $a$ orders that have an American bus going last and $d$ orders that have a Dutch bus going last, so the probability that the last bus is carrying American fans is just $a/(a+d)$ or $11/18\approx 61.1\%,$ for our problem.

For the second part, we want to figure out the number of groups. First, an intuitive argument.

### Intuitive argument

A new group occurs whenever there's a switch from As to Ds. Circularize the list, so that the first person is in back of the last person. There are $a$ American fans in the circle and so, $a$ positions behind Americans. By linearity, the probability that a Dutch is behind any given American is $d/(a+d-1).$ Likewise, there are $d$ positions behind Dutch players, and probability $a/(a+d-1)$ that an American is there. Putting it together, the expected number of identity switches is $2ad/(a+d-1).$ Since the circle is actually linear, we have to cut the circle back into a line, which introduces one more group if the first and last fans support the same team. The probability of that is $\frac{a}{a+d}\frac{a-1}{a+d-1} + \frac{d}{a+d}\frac{d-1}{a+d-1}.$

Adding it all up, the expected number of buses is one more than the harmonic mean of $a$ and $d$:

$$ \langle B\rangle = 1 + \dfrac{2ad}{a+d}. $$

For the problem in question, that's $\langle B\rangle = 86/9.$

![](/img/2022-12-08-circularized.JPG){:width="350px" class="image-centered"}

Now we'll argue this formally, which will be good setup work for the second interpretation.

### Rigorous argument

First some notation — $G(a,d)$ is the expected number of new groups given that a bus just left and composition of the remaining people is $(a,d),$ $A(a,d)$ is the expected number of new groups given that we're in the midst of adding people to an A-bus, and $D(a,d)$ is the corresponding quantity when we're adding people to a D-bus.

Suppose we're at the beginning of the process, then

- with probability $a/(a+d),$ the new group will be formed by an American. 
- with probability $d/(a+d),$ the new group will be formed by a Dutch.

This means

$$
  G(a,d) = \dfrac{a}{a+d}A(a-1,d) + \dfrac{d}{a+d}D(a,d-1)
$$

Now, when we're building an A-group, we can either:

- stay in the A-group with probability $a/(a+d)$, or
- start a new group of Ds with probability $d/(a+d).$

Similar logic applies if we're in a D-group, and we get

$$
  \begin{align}
    A(a,d) &= \frac{a}{a+d}A(a-1,d) + \frac{d}{a+d}\left[D(a,d-1) + 1\right] \\
    D(a,d) &= \frac{a}{a+d}\left[A(a-1,d) + 1\right] + \frac{d}{a+d}D(a,d-1).
  \end{align}
$$

Using the first equation, these two become

$$
  \begin{align}
    A(a,d) &= G(a,d) + \dfrac{d}{a+d} \\
    D(a,d) &= G(a,d) + \dfrac{a}{a+d}.
  \end{align}
$$

Plugging these back in to the first, we get a self-consistent equation that $G(a,d)$ needs to satisfy:

$$
  \begin{align}
    G(a,d) &= \dfrac{a}{a+d}\left[G(a-1,d) + \dfrac{d}{a+d-1}\right] + \dfrac{d}{a+d}\left[G(a,d-1) + \dfrac{a}{a+d-1}\right] \\
    &= \dfrac{1}{a+d-1}\dfrac{2ad}{a+d} + \dfrac{a}{a+d}G(a-1,d) + \dfrac{d}{a+d}G(a,d-1).
  \end{align}
$$

Multiplying through by $(a+d)$ we get the cleaner form

$$
  (a+d)G(a,d) = \dfrac{2ad}{a+d-1} + aG(a-1,d) + dG(a,d-1),
$$

By inspection (or plugging in our result from the intuitive argument), we can see that this is solved by $G(a,d) = 2ad/(a+d).$ At the beginning there is already one group (the first one), so the expected of buses is 

$$ \langle B\rangle = 1 + \dfrac{2ad}{a+d}. $$

# Interpretation 2

In the second interpretation the fans are scrambled after each bus leaves, opening up the possibility for e.g. $2$ American buses in a row. 

At some point, the system will get to the point where the Dutch or the Americans only have $1$ fan left, and the other team has $N$ left. For argument's sake, let's assume the team with $1$ left is the Americans. 

There is a $1/(N+1)$ chance that we get to the end of the line without hitting the American, and a $1/(N+1)$ chance to restart the game from any of the $(N-1)$ possible number of remaining Dutch fans between $1$ and $(N-1):$

$$ P(N) = \frac{1}{N+1} + \frac{1}{N+1}\left[P(1) + P(2) + \ldots + P(N-1)\right] $$

which is solved by $P(N) = \frac12.$

To find the number of buses, we can use the same equations from the formal argument above, now less analyzable. Instead of immediately starting a new bus when a fan from the opposite team is called, we now reset the game. That means that the equation for $A(a,d)$ becomes 

$$ A(a,d) = \frac{a}{a+d}A(a-1,d) + \frac{d}{a+d} \left[\frac{d}{a+d} D(a,d-1) + \frac{a}{a+d} A(a-1,d) + 1\right] $$

With the equivalent modification for $D(a,d).$ 

Implementing this and evaluating it for $(a,d)=(11,7),$ we get $\langle B\rangle \approx 9.54538,$ which is nearly identical to the result under the non-reset rules. This is quite close, but as fan counts increase, the divergence is more striking.

```python
@lru_cache
def A(a,d):
  if a > 0 and d == 0:
    return 0
  if a == 0 and d > 0:
    return 1
  return a/(a+d) * A(a-1,d) + d/(a+d) * (d/(a+d) * D(a,d-1) + a/(a+d) * A(a-1,d) + 1)

def D(a,d):
  if a > 0 and d == 0:
    return 1
  if a == 0 and d > 0:
    return 0
  return a/(a+d) * (a/(a+d) * A(a-1,d) + d/(a+d) * D(a,d-1)+ 1) + d/(a+d) * D(a,d-1)

def G(a,d):
  return 1 + a/(a+d) * A(a-1,d) + d/(a+d) * D(a,d-1)
```

<br>
