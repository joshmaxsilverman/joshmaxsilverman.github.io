---
layout: post
published: true
title: Can You or “Cantor” You Find the Distance?
date: 2026/03/15
subtitle: Random geometry from the Cantor distribution
tags: fractals
source: writeup
kind: probability
theme: probability
---

>**Question**: I start with a number line from 0 to 1, and then I remove the middle third. Then I take each of my remaining pieces (the segment from 0 to 1/3 and the segment from 2/3 to 1) and remove their middle thirds. Now I have four segments (from 0 to 1/9, 2/9 to 1/3, 2/3 to 7/9, and 8/9 to 1) and remove their middle thirds. I do this over and over again, infinitely many times.
>
>The points I’m left with are collectively known as the Cantor set. The Cantor set is not empty; in fact, it contains infinitely many points on the number line, such as 0, 1, 1/3, and even 1/4.
>
>It’s possible to pick a random point in the Cantor set in the following way: Start with the entire number line from 0 to 1. Then, every time you remove a middle third, you give yourself a 50 percent chance of being on the left remaining third and a 50 percent chance of being on the right remaining third. Then, when you remove the middle third of that segment, you again give yourself a 50 percent chance of being on the left vs. the right, and so on.
>
>Suppose I independently pick two random points in the Cantor set. On average, how far apart can I expect them to be?
>
>**Extra credit**: Suppose I independently pick three random points in the Cantor set. Each point has some value between 0 and 1.
>
>What is the probability that these three values can be the side lengths of a triangle?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-or-cantor-you-find-the-distance))

## Solution

let the two points start at the middle of the intact unit line, and find their positions by repeatedly picking, at random, the midpoint of the left or right third of the line they're currently on. the sum of all these displacements for each point is the selected cantor point.

the points are together to start, and can either stay together or move apart. if they stay together then they gain no relative displacement and restart the process at the center of a cantor line one third the length of the original. if they move apart, then they pick up relative distance $\frac23$ and start a new process separated from each other on the two sublines of length $\frac13.$ 

starting the next step apart, the points can have no relative movement with probability $\frac12,$ move together with probability $\frac14,$ or move apart with probability $\frac14.$ because the movements are symmetric, the expected additional separation is zero!

so, we just have the equation describing the 

$$ 
    \begin{align}
        d_\text{together}(1) &= \frac12 d_\text{apart}(\frac13) + \frac12\left(\frac23 + d_\text{apart}(\frac13)\right) \\
        &= \frac12\frac13 d_\text{apart}(1) + \frac12\frac23 \\
        \frac56 d_\text{together}(1) &= frac13 \\
        d_\text{together}(1) &= \frac25.
    \end{align}
$$

## Extra credit

three side lengths form a triangle if each pair of sides satisfies the triangle inequality with the third side, i.e.

$$ \begin{align}
a &\leq b+c \\
b &\leq c+a \\
c &\leq a+b
\end{align}$$

a triangle will not obtain if one of these is broken like $a > b+c.$ at the very most, one of a trio of numbers can be bigger than the sum of the other two. so, if we can find out the probability that one of the numbers is too big, $P(\text{too big}),$ the probability that a triangle forms will be $1-3P(\text{too big}).$

when we pick cantor numbers the first division decides if a number is on the left or the right side of the cut. because each side is a scaled down copy of the cantor set, we can relate the original problem to its cases.

when we make the first decision for the three numbers, we can get eight different outcomes, $\{\text{LLL},\text{LLR}, \text{LRL}, \text{RLL}, \text{LRR}, \text{RLR}, \text{RRL}, \text{RRR}\}.$

if we get $\text{RRR}$ then all three numbers will be greater than $\frac23$ and less then $1$ which means a triangle is guaranteed, and there is no probability of failure. 

if we get $\text{LLL}$ then we have the same problem again, playing out at a smaller scale. the probability that a triangle does not form is once again $p.$

if we get any of the other scenarios where $a$ is $\text{L},$ the probability $a$ is too long is zero since either of $b$ or $c$ is $R$ and therefore greater than an $\text{L}$ number. 

if we get $\text{RRL}$ or $\text{RLR}$ then $a$ is at least $\frac23$ as is one of the other numbers, while the third number is between $0$ and $\frac13.$ writing $a$ as $\frac23 + x,$ $b$ as $\frac23 + y,$ and $c$ as $z,$ the condition for $a$ being too big is $\frac23 + x > \frac23 + y+z,$ or $x > y+z.$ because $x,$ $y,$ and $z$ are scaled down cantor numbers, this is just the original event and so has probability $p.$ 

the case $\text{RLL}$ has probability $1$ to fail since $b$ and $c$ are less than $\frac13$ and $a>\frac23.$

putting it all together, we have one case with probability $\frac18\left(1 + 3p\right).$ 

$$ p = \frac38\left(1+3p\right). $$

solving this, we get $P(\text{too big})=\frac15$ and the probability to form a triangle is $1-3P(\text{too big}) = \frac25.$

<br>
