---
layout: post
published: true
title: Can you play hide-and-seek?
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
>![](/img/2026-05-19-fiddler-hide-seek-course.webp){:width="450 px" class="image-centered"}
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

We don't know where little nephew will hide in any given game, and search strategies have different costs based on hiding spot, so there's no way to strategize at the single gam level. But if we play many hide-and-seek games with little nephew, then we can analyze our own deception in light of little nephew's. In that case, he has a probability distribution determining where he hides, and we have one on our search strategies.

With $3$ hiding spots to check we have $3! = 6$ search strategies, each with their own cost based on little nephew's hiding spot. If we check the hiding spots in the order $\text{ABC}$ then hiding at $\text{A}$ costs $2,$ hiding at $\text{B}$ costs $7$ ${(2+2+3)}$ and hiding at $\text{C}$ costs $12$ ${(2+2+3+5)}$ using the most efficient path. 

Carrying out this exercise for all search orders and hiding spots we get the cost structure shown in the table below. 

$$
    \begin{array}{c|ccc}
    \text{Search order} & c_\text{A} & c_\text{B} & c_\text{C} \\ \hline
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

$$\frac12\left(2p_A, 7p_B, 12p_C\right)+\frac12\left(14p_A, 9p_B, 4p_C\right) = 8\left(p_A,p_B,p_C\right) $$

for a total expectation of $8$ regardless of the specific hiding distribution.

The same can also be achieved using an equal blend of $\text{ACB}$ and $\text{BCA}.$

Is this the most efficient indifferent strategy possible? If we want to get lower than $8$ we would need to use a blend of three strategies since no other weighted pair form a flat strategy. However, this leads to contradictory conditions on the weights of the cost vectors. 

For example, let's try to form a weighted blend of $\text{ABC},$ $\text{BAC},$ and $\text{CBA}.$

This gives us three expressions that have to come out less than $8$

$$\begin{align}
    2\alpha+8\beta+10\gamma&\leq8\\
    7\alpha+3\beta+15\gamma&\leq8\\
    12\alpha+14\beta+4\gamma&\leq8
\end{align}$$

The first equation leads to the inequality $4\alpha+\beta \geq 1,$ the second leads to $\beta \geq \frac12,$ and the third to $\frac38 \geq \beta.$ The second two are contradictory which means this is impossible. The same sort of contradictions pop up with all other possible combinations of strategy (or it collapses down to the original two we found).

This means that $8$ is the minimum average hiding time, regardless of how the hider sets their distribution.

## Extra credit

Again, we want a strategy that's indifferent to the behavior of little nephew, the hider. 

If were move at the first possible time, then little nephew can just plan to be where we can't possibly be for the whole game. For example, the could go to $\text{B}$ until just before $t=3$ then switch to $\text{A}$ and hang out for $5$ s (when we would be in transit from $\text{A}$) and so on. 

To bust this behavior, we need to take away little nephew's ability to anticipate where we'll be. We can do this by making each move take the same amount of time.  

Starting from $\text{O}$ at time $t=0$ we flip a coin and go to $\text{A}$ if heads and to $\text{B}$ if tails. If we pick $\text{A}$ then we wait $1$ s before leaving, so that movement to $\text{A}$ and $\text{B}$ take the same amount of time. Once we get to that destination, we flip the coin again and either go to the other hiding spot, or wait $5$ at the current one. Knowing that we can't possibly get to $\text{B}$ before $t=3,$ there is no chance they'll leave $\text{B}$ before $t=3.$

By taking away the connection between time and location, little nephew has no way to counter us. At each interval, our position will be random and we will therefore have a $50\%$ chance to find little nephew. Starting from the beginning, there is a $50\%$ chance to end on the first hiding spot taking $3$ time steps, and a $50\%$ chance to require another inspection, adding $5$ steps plus whatever time it takes to find them from there on:

$$ \begin{align}
    T^\text{start}_\text{find} &= \frac12 \times 3 + \frac12\times T^\text{after start}_\text{find} \\
    T^\text{after start}_\text{find} &= \frac12\times 0 + \frac12 \times \left(T^\text{after start}_\text{find} + 5\right)
\end{align}$$

Solving the equations for $T^\text{start}_\text{find}$ we get $8$ again.


