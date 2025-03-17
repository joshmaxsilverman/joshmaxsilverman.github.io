---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>**Question**: You are planning a picnic on the remote tropical island of 𝜋-land. The island’s shape is a perfect semi-disk with two beaches, as illustrated below: Semicircular Beach (along the northern semicircular edge of the disk) and Diametric Beach (along the southern diameter of the disk).
>
>If you pick a random spot on 𝜋-land for your picnic, what is the probability that it will be closer to Diametric Beach than to Semicircular Beach? 
>
>**Extra Credit**: now suppose the island of $\pi$-land, as described above, has a radius of $1$ mile. That is, Diametric Beach has a length of $2$ miles.
>
>Again, you are picking a random point on the island for a picnic. On average, what will be the expected shortest distance to shore?
>
>>**Extra Extra Credit**: what is the median shortest distance to the shore?

<!--more-->

([Fiddler on the Proof](URL))

## Solution

At any position $(x,y)$ on the island, the distance to diametric beach (the southern diameter) is $y$ and the distance to semicircle beach is $1-\sqrt{x^2 + y^2}.$

There is a curve such that, on its northern side, the semicircular beach is closer, and on its southern side, diametric beach is closer. 

$$
  \begin{align}
    y &= 1 - \sqrt{x^2 + y^2} \\
    (y-1)^2 &= x^2 + y^2 \\
    1 - 2y &= x^2 \\
    y = \frac12\left(1 - x^2\right)
  \end{align}
$$

The probability that diametric beach is closer is just the area under this curve relative to the entire semicircle:

$$ P(\text{diametric}) = \frac{2}{\pi}\int\limits_{-1}^1\frac12(1 - x^2) = \frac{4}{3\pi}.$$

To find the average area, we could take the weighted average of $(1-r)$ in the upper region, and of $y$ in the lower region. However, we are going to get the probability density function of $r$ so that we can go for the median.


<br>
