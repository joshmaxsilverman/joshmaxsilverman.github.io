---
layout: post
published: false
title: Soccer Busses
date: 2022/12/06
subtitle: How many trips will the poor driver have to make?
tags: recursion symmetry
---

>**Question**: A certain hotel in Qatar is hosting 11 American fans and seven Dutch fans. Since no alcohol is available inside the stadiums, the fans spend the afternoon at the hotel bar before shuttle buses will take them to a match. Then, they haphazardly write their room numbers on a big board by the concierge desk.
>
>To avoid any rowdiness between rival fans, shuttle bus drivers have been instructed to ferry American and Dutch fans separately. To ensure this, a shuttle pulls up in front of the hotel, and its driver calls out room numbers from the board, one by one at random. As long as they support the same team, each fan climbs aboard the bus and their room number is erased. Once the driver calls out the room number of a fan for the second team, the shuttle leaves with only the fans of the single team aboard. The next shuttle then pulls up and repeats the process.
>
>What is the probability that the last shuttle ferries American fans?
>
>Extra credit: On average, what is the expected number of shuttle buses needed to ferry all 18 fans?

<!--more-->

([FiveThirtyEight](URL))

## Solution

**A note**: there are two ways to interpret the inter-group policy. one is that when a new group is triggered by switching from e.g. a run of American fans to a Dutch fan, the Dutch fan begins the next group. the other way is that the Dutch fan has only triggered the transition, but who begins the next group will be redrawn from random. we'll solve the problem both ways, starting with the first.

# Interpretation 1

the order of the As and Ds is random and any random order is valid. for any particular random order we can cyclically permute the order (moving the first person to last, the second person to first, and so on) and make another valid order. as we cycle the list there will be $a$ lists that have an American bus going last and $d$ lists that have a Dutch bus going last, so the probability that the last bus is carrying American fans is just $a/(a+d)$ or $11/18\approx 61.1\%,$ for our problem.

for the second part, we want to figure out the number of groups. first, an intuitive argument.

### Intuitive argument

a new group occurs whenever there's a switch from As to Ds. circularize the list, so that the first person is in back of the last person. there are $a$ American fans in the line and so, $a$ positions behind Americans. by linearity, the probability that a Dutch is behind any given American is $d/(a+d).$ likewise, there are $d$ positions behind Dutch players, and probability $a/(a+d)$ that an American is there. putting it together, the expected number of identity switches is $2ad/(a+d).$ since the list is actually linear, we have to cut the circle back into a line, which introduces one more group (the first one). all in all, the expected number of buses is one more than the harmonic mean of $a$ and $d$:

$$ \langle B\rangle = 1 + \dfrac{2ad}{a+d}. $$

for the problem in question, that's $\langle B\rangle = 86/9.$

now we'll argue this formally, which will be good setup work for the second interpretation.

### Rigorous argument

first some notation — $G(a,d)$ is the expected number of new groups given that a bus just left and composition of the remaining people is $(a,d),$ $A(a,d)$ is the expected number of new groups given that we're in the midst of adding people to an A-bus, and $D(a,d)$ is the corresponding quantity when we're adding people to a D-bus.

suppose we're at the beginning of the process, then

- with probability $a/(a+d),$ the new group will be formed by an American. 
- with probability $d/(a+d),$ the new group will be formed by a Dutch.

this means

$$
  G(a,d) = \dfrac{a}{a+d}A(a-1,d) + \dfrac{d}{a+d}D(a,d-1)
$$

now, when we're building an A-group, we can either:

- stay in the A-group with probability $a/(a+d)$, or
- start a new group of Ds with probability $d/(a+d).$

similar logic applies if we're in a D-group, and we get

$$
  \begin{align}
    A(a,d) &= \frac{a}{a+d}A(a-1,d) + \frac{d}{a+d}\left[D(a,d-1) + 1\right] \\
    D(a,d) &= \frac{a}{a+d}\left[A(a-1,d) + 1\right] + \frac{d}{a+d}D(a,d-1).
  \end{align}
$$

using the first equation, these two become

$$
  \begin{align}
    A(a,d) &= G(a,d) + \dfrac{d}{a+d} \\
    D(a,d) &= G(a,d) + \dfrac{a}{a+d}
  \end{align}
$$

plugging these back in to the first, we get a self-consistent equation that $G(a,d)$ needs t satisfy:

$$
  \begin{align}
    G(a,d) &= \dfrac{a}{a+d}\left[G(a-1,d) + \dfrac{d}{a+d-1}\right] + \dfrac{d}{a+d}\left[G(a,d-1) + \dfrac{a}{a+d-1}\right] \\
    &= \dfrac{1}{a+d-1}\dfrac{2ad}{a+d} + \dfrac{a}{a+d}G(a-1,d) + \dfrac{d}{a+d}G(a,d-1).
  \end{align}
$$

multiplying through by $(a+d)$ we get the cleaner form

$$
  (a+d)G(a,d) = \dfrac{2ad}{a+d-1} + aG(a-1,d) + dG(a,d-1),
$$

by inspection (or plugging in our result from the intuitive argument), we can see that this is solved by $G(a,d) = 2ad/(a+d).$ at the beginning there is already one group (the first one), so the expected of buses is 

$$ \langle B\rangle = 1 + \dfrac{2ad}{a+d}. $$

# Interpretation 2




<br>
