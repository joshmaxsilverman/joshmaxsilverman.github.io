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

in this solution i'm going to make the simplifying assumption that each pair is independent. in this scheme, we can calculate the probability that any given pair forms a loop, and multiply it by the number of pairs.

first of all, with two players, there's a $\frac12$ chance that a pair is formed.

for four players, there are two potential pairs. since anyone can draw anyone from the hat, the chance that the first person doesn't pick themself is $\frac14.$ similarly, the probability that the first person's pick picks them back is $\frac14.$ finally, there are two potential pairs. so, the expected number of pairs is 

$$ \langle P_2\rangle \approx 2\times\frac34\times\frac14 = \frac38\approx 37.5\\% $$

in general, for $2n$ players, the expected number of pairs is

$$ \langle P_n\rangle = \frac{n}{2}\frac{n-1}{n^2} = \frac{n-1}{2n} .$$

<br>
