---
layout: post
published: true
title: Can You Play Hide-and-Seek?
date: 2026/05/18
subtitle: Minimize the time to find your hiding nephew, or don't, I'm not your dad.
tags: game-theory minimax optimization
source: fiddler
kind: puzzle
theme: probability
hide_from_recent : true
---

> **Question**: I am playing hide-and-seek with my nephew. I start at point O, whereas my nephew can hide at point A, B or C. I can walk from O to A in 2 minutes, from O to B in 3 minutes, from O to C in 4 minutes, and from B to C in 5 minutes. To get from A to B or from A to C, I must pass through O.
>
> My goal is to minimize the time it takes to find him, no matter how clever his strategy might be. What is this optimal time?
>
> **Extra Credit**: My nephew can no longer hide at C, and is instead limited to A and B. But this time, he has a teleporter that can instantaneously transport him from A to B or from B to A. He can use the teleporter as many times as he wants. However, he can’t react to my approach, and must instead plan out his transport schedule ahead of time. That said, he does know the precise time when the game starts.
>
> My goal is to minimize the average time it takes to find him, no matter how clever his strategy might be. What is this optimal time?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-play-hide-and-seek))

## Solution

The first part of this problem is to figure out what the problem is.


We don't know where the nephew will hide in any given game, and search strategies have different costs based on hiding spot, so there's no way to strategize at the single game. What's happening is that we're playing many hide-and-seek games with little nephew. In that case, he has a probability distribution determining where he hides, and we have one on our search strategies.

With $3$ hiding spots to check we have $3! = 6$ search strategies, each with their own cost based on little nephew's hiding spot. If we check the hiding spots in the order $ABC$ then hiding at $A$ costs $2,$ hiding at $B$ costs $7$ ${(2+2+3)}$ and hiding at $C$ costs $12$ ${(2+2+3+5)}$ using the msot efficient paths. 

Carrying out this exercise for all search orders and hiding spots we get the cost structure shown in the table below. 

$$
    \begin{array}{c|ccc}
    \text{Order} & c_\text{A} & c_\text{B} & c_\text{C} \\ \hline
    \text{ABC} & 2 & 7 & 12 \\
    \text{ACB} & 2 & 13 & 8 \\
    \text{BAC} & 8 & 3 & 14 \\
    \text{BCA} & 14 & 3 & 8 \\
    \text{CAB} & 10 & 15 & 4 \\
    \text{CBA} & 14 & 9 & 4
    \end{array}
$$

Our goal as the seeker is to make the cost insensitive to the probability distribution of little nephew's hiding strategy. Say that is given by $\\{p_A, p_B, p_C\\},$ then we want an average cost that has equal coefficients for all three probabilities.

Looking at the table one way immediately jumps out, an equal blend of $\text{ABC}$ and $\text{CBA},$ which gives us 

$$\frac12\left(2p_A+7p_B+12p_C\right)+\frac12\left(14p_A+9p_B+4p_C\right) = 8. $$

The same can also be achieved using an equal blend of $\text{ACB}$ and $\text{BCA}.$

Is this the most efficient indifferent strategy possible? If we want to get lower than $8$ we would need to use a blend of three strategies. However, this leads to contradictory conditions on the weights of the cost vectors. So, $8$ is the most efficient strategy of indifference.

## Extra credit

Again, we want a strategy that's indifferent to the behavior of little nephew, the hider. 

If were move at the first possible time, then little nephew can just plan to be where we can't possibly be for the whole game. Go to $\text{B}$ until $t=3$ then go to $\text{A}$ and hang out for $5$ s and so on. 

To bust this behavior, we need to take away little nephew's ability to anticipate where we'll be. We can do this by making each move take the same amount of time. 

Starting from $0$ at time $t=0$ we flip a coin and go to $\text{A}$ is heads and $\text{B}$ if tails. If we pick $\text{A}$ then we wait $1$ s before leaving, so that movement to $\text{A}$ and $\text{B}$ take the same amount of time. Once we get to that destination, we flip the coin again and either go to the other hiding spot, or wait $5$ at the current one. 

At each interval, we have $50\%$ chance to find little nephew so the [expected time to find them is](https://www.wolframalpha.com/input?i=+sum%28%283%2B5%28j-1%29%29%2F2%5Ej%2C+%7Bj%2C+1%2C+1000%7D%29)

$$ 
    \begin{align}
        T &= 3\frac12 + 8\frac14 + 13\frac18 + 18\frac{1}{16} + \ldots \\
          &= \frac32 +\left(\frac34 + \frac54\right) + \left(1 + \frac58 \right) \\
          &= 8
    \end{align}
$$


