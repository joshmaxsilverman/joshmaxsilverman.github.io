---
layout: post
published: true
title: Traffic Groups
date: 2022/08/29
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

Each additional driver introduces an expected number of additional groups $\langle G_i\rangle$, making the total

$$\langle \text{num groups}\rangle = \langle G_1\rangle + \langle G_2\rangle + ... \langle G_N\rangle.$$

Now, the $i^\text{th}$ driver has a $1/i$ chance of being the $1^\text{st}$ fastest, or $2^\text{nd}$ fastest, all the way up to being the $i^\text{th}$ fastest driver.

If they are the first fastest, then they will only introduce a new group if all $(i-1)$ drivers before them are in increasing order. If they are $(i-1)$ fastest, they will only introduce a new group of the top i-2 drivers are in increasing order, and so on.

If those drivers weren't in increasing order, then at least one driver who is slower than them would have found it advantageous to switch lanes, meaning that both lanes already have a group moving slower than them, blocking them from making a new group at their own speed

So, 

$$\langle G_i\rangle = \frac{1}{i}\left[1 + 1 + 1/2! + ... 1/(i-1)!\right],$$

and

$$\langle\text{num groups}\rangle_N = \sum_{n=1}^N\frac1n\sum\limits_{i=0}^{n-1} \frac{1}{i!}.$$

<br>
