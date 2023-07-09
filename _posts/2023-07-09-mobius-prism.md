---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

the twist between the ends of the prism determines what prism face you end up on after one loop. 

for example, with no twist you stay on the same face and, so, each face forms its own distinct side of the prism.

as another example, giving a hexagonal prism a twist of $2$ sets up the map

$$
  \begin{array}{c}
    123456 \\
    \downarrow \\
    345612
  \end{array}
$$

which splits the faces into two cycles $1 \rightarrow 3 \rightarrow 5 \rightarrow 1$ and $2 \rightarrow 4 \rightarrow 6 \rightarrow 2$ giving the prism two sides.

each face maps to another, and this dynamics groups the faces into cycles. because of the inherent symmetry, all cycles have the same size. 

immediately, this tells us that prisms with a prime number of sides cannot break into cycles. for such prisms, there are $N$ sides to the mobius strip for a twist of $0$ and $1$ side for any other twist.

for non-primes, the cycle will close when some number of twists brings us back to the first side. in other words, at the least common multiple of $N$ and the size of the twist $t.$

so, for arbitrary $N$ and $t,$ each cycle will involve $\text{lcm}(N,t)/t$ numbers. dividing the total number of numbers $N$ by this yields $Nt/\text{lcm}(N,t)$ cycles for arbitrary $N$ and $t$.

the average number of "sides" for a given mobius prism is therefore

$$ \langle \text{sides}\rangle = \frac1N \sum_t \frac{Nt}{\text{lcm}(N,t)} = \sum_t \frac{t}{\text{lcm}(N,t)}. $$

evaluating this from $N=1$ to $1000$ we get a max at $N=840$ where $\langle\text{sides}\rangle = 195/14 \approx 13.92857\ldots$

<br>
