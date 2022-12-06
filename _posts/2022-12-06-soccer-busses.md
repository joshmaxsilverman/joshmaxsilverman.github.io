---
layout: post
published: false
title: Soccer Busses
date: 2022/12/06
subtitle: How many trips will the poor driver have to make?
tags: recursion symmetry
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

first some notation — $a$ is the number of Americans, $d$ is the number of Dutch, and $G(a,d)$ is the expected number of new groups given that a bus just left and composition of the remaining people is $(a,d).$

with probability $a/(a+d),$ the new group will be formed by an American. in that case, the expected number of new groups to form is $A(a-1,d).$ with probability $d/(a+d),$ the new group will be formed by a Dutch. in that case, the expected number of new groups to form is $D(a,d-1).$ this means

$$
  G(a,d) = \dfrac{a}{a+d}G(a-1,d) + \dfrac{d}{a+d}G(a,d-1)
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

plugging these back in to the first, we get

$$
  \begin{align}
    G(a,d) &= \dfrac{a}{a+d}\left[G(a-1,d) + \dfrac{d}{a+d-1}\right] + \dfrac{d}{a+d}\left[G(a,d-1) + \dfrac{a}{a+d-1}\right] \\
    &= \dfrac{1}{a+d-1}\dfrac{2ad}{a+d} + \dfrac{a}{a+d}G(a-1,d) + \dfrac{d}{a+d}G(a,d-1)
  \end{align}
$$

multiplying through by $(a+d)$ we get the cleaner equation

$$
  (a+d)G(a,d) = \dfrac{2ad}{a+d-1} + aG(a-1,d) + dG(a,d-1),
$$
  


<br>
