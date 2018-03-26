---
layout: post
title: Shifted Double
published: true
date: 2018/03/25
---

>Imagine taking a number and moving its last digit to the front. For example, 1,234 would become 4,123. What is the smallest positive integer such that when you do this, the result is exactly double the original number? (For bonus points, solve this one without a computer.)

<!--more-->

([fivethirtyeight.com](https://fivethirtyeight.com/features/can-you-shuffle-numbers-can-you-find-all-the-world-cup-results/)

## Solution:

Let the original number be $d_nd_{n-1}\ldots d_2d_1$. Since the doubled number does not grow a digit, digit $d_n$ is one of $\\{1,2,3,4\\}$, and $d_1$ is either $2d_n$ or $2d_n+1$.  So there are only eight possible $\\{d_n,d_1\\}$ pairs.

Based on $d_1$, we can easily find $d_2$ and subsequent (more significant) digits in the doubled number. For instance, if $d_1$ is 4, then $d_2$ must be 8, $d_3$ must be 6 (twice 8 is 16), and $d_4$ must be 3 (carrying the 1 from 16). Proceeding like this from any $d_1$, we find ourselves in the following 18-element doubling cycle (where the star reminds us that we are carrying a 1, and so the digit cannot be $d_1$, because $d_2$ comes from doubling $d_1$ without adding a carried 1):

$$1,2,4,8,6*,3*,7,4*,9,8*,7*,5*,1*,3,6,2*,5,0*,1,\ldots$$

(Not coincidentally, this is the repetend (repeating portion) of the decimal representation of $1/19$.)

We have a solution if we can travel along the doubling cycle from a possible (unstarred) $d_1$ to a corresponding $d_n$ that is followed by the same $d_1$. This is possible for each of the eight possible $\\{d_n,d_1\\}$ pairs. In each case a solution requires traversing the entire cycle at least once. Therefore, there are eight shortest solutions, of which all longer ones are simply repetitions, and of which the smallest is 105263157894736842.

<br>
