---
layout: post
published: true
title: Twisted balkanization 
date: 2023/07/09
subtitle: How many different adventures does the Mobius prism have in store?
tags: maps dynamics measurement
---

>**Question**: Instead of a strip of paper, consider a three-dimensional prism whose bases are regular $N$-gons. I twist it and stretch it into a loop, before finally connecting the two bases. Suppose that my twist is by a random angle, such that the two bases are aligned when they are connected. I’m interested in how many distinct faces there are in the resulting “Möbius prism.”
>
>For example, let’s say the original figure is a square prism (i.e., $N = 4$). There are four kinds twists I can apply, all equally likely:
>
> - A one-quarter twist, which results in one distinct face
> - A two-quarter (or one-half) twist, which results in two distinct faces
> - A three-quarter twist, which results in one distinct face
> - A four-quarter (or whole) twist, which results in four distinct faces
> - A randomly twisted square prism will have, on average, $(1+2+1+4)/4$, or two distinct faces.
>
>Among all whole number values of $N$ less than or equal to $1,000$, for which value of $N$ will a randomly twisted regular $N$-gon prism have the most distinct faces, on average?

<!--more-->

([The fiddler on the proof](https://thefiddler.substack.com/p/can-you-escape-the-infinite-loop))

## Solution

The twist between the caps of the prism determines which prism face you end up on after one loop. 

**Note**: *Since the twist involves a shift by a discrete number of faces, we'll measure the twists by the size of the shift $t.$*

### No twist

For example, with no twist ($t=0$) each face maps to itself and, so, forms its own distinct side of the Möbius prism.

### Hexagon, with $t=2$

As another example, giving a hexagonal prism a twist $t=2$ sets up the map

$$
  \begin{array}{c}
    123456 \\
    \downarrow\downarrow\downarrow\downarrow\downarrow\downarrow \\
    345612
  \end{array}
$$

which splits the faces into two cycles $1 \rightarrow 3 \rightarrow 5 \rightarrow 1$ and $2 \rightarrow 4 \rightarrow 6 \rightarrow 2,$ giving the prism two sides.

### Cycles

Each face maps to another. This dynamic groups the faces into cycles. Because of the inherent symmetry, all of the cycles have the same size. 

Immediately, this tells us that prisms with a prime number of sides can't break into cycles (since primes are not divisible$\ldots$). For prime prisms, there are $N$ sides to the Möbius prism for a twist of zero and $1$ side for any other twist.

For non-primes, the cycle will close when some number of twists brings us back to the first side. In other words, at the least common multiple of $N$ and the size of the twist $t.$

So, for arbitrary $N$ and $t,$ each cycle will involve 

$$ \frac{\text{lcm}(N,t)}{t} $$ 

numbers. Dividing the total number of numbers $N$ by this yields $Nt/\text{lcm}(N,t)$ cycles.

The average number of "sides" for a Möbius prism is therefore

$$ \langle \text{sides}\rangle_N = \frac1N \sum_t \frac{Nt}{\text{lcm}(N,t)} = \sum_t \frac{t}{\text{lcm}(N,t)}. $$

Evaluating this for numbers between $N=1$ and $1000,$ we find a maximum at $N=840,$ where $\langle\text{sides}\rangle_{840} = 195/14 \approx 13.92857\ldots$ 

Unsurprisingly, $840$ is a [highly composite number](https://en.wikipedia.org/wiki/Highly_composite_number), having more prime factors than any number smaller than it.

<br>
