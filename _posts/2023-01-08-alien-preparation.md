---
layout: post
published: false
title: Alien Preparation
date: 2023/01/08
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

Whether we have $1$ assembler, or $1$ billion of them, the decision of what to do with each one is independent of the others.

The tradeoff between assemblers and spaceships is this: 

- if we invest the time to make another assembler, then we can make spaceships twice as fast, but
- while the assembler was getting made, we could have built $144$ spaceships

So, if we have a lot of time, we should use some of it to make assemblers. If we have a little time, we should forget assemblers and just build spaceships.

We can quantify this tradeoff to find the tipping point.

### Calculation

Suppose we have $h$ hours left. If we set an assembler to make as many assemblers as possible, and then make starships with the time left over, they'll make devote $\lfloor \frac{h}{144}\rfloor\times 144$ hours to make assemblers, yielding $2^{\lfloor h/144\rfloor}(h-144\lfloor \frac{h}{144}\rfloor)$ starships, whereas if we let the original start making starships, it would have made $h$ of them. So, if $2^{\lfloor h/144\rfloor}(h-144\lfloor h/144\rfloor) \geq h,$ we should devote all available assemblers to double. 

The tipping point occurs when $h = 288$ hours. So, if the time remaining is less than $288$ hours, we should devote all assemblers to make starships, otherwise we should have them make assemblers, waiting to make the switch to starship assembly when $h < 288.$

This means we will maximally make

$S(h) = (h-144t)2^t$ starships, where $t=\lfloor \frac{h}{144}-1\rfloor.$

For $h = 2400,$ this is equal to

$$ \begin{align} S(2400) &= \left(2400 - 144 \times 15\right) 2^{15} \\ &= 7,864,320. \end{align} $$

### Optimal policy

We can check the intution here by finding the maximum with dynamic programming. If we have $H$ hours left and $A$ assemblers, then we have the choice to apportion them to spaceships or assemblers any way we like. If we have less then $144$ hours left, then we can't finish any new assemblers, and we should just devote the assemblers we have to starship production. 

Mathematically, this is

$$
S(H,A) = \begin{cases} H\times A & H\leq 144 \\
                       \max\limits_{0\leq x\leq A} S(H-144,2x) + (A-x) + S(H-1, A-x) & \text{otherwise}
         \end{cases}
$$


<br>
