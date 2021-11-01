---
layout: post
published: true
title: Robot Races
date: 2021/10/31
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

While the discrete strategy reigns as the Nash equilibrium, there are $3N$ racers and $N$ distinct winners of the $N$ races, so the chance for any given player to win is $p=\frac13.$

### Disturbing the equilibrium

The discrete strategy is all-or-nothing, so any departure from it will lose a race with discrete competition. 

The only hope for a dissenter to win is to put fuel on a race that nobody else does. Any non-zero amount will do in an empty race, so the dissenter puts a non-zero amount on every race.

### Chance to win

As the number of races grows, it should get easier for the system to fluctuate into a state where one race goes empty among the $3N-1$ Nash equilibrists. The question is, when do the dissenter's prospects overcome the equilibrists?

Working in three lanes, the dissenter wins if lanes $1,$ $2,$ or $3$ are open. However, the chance for lane $1$ to be open includes the case where lane $2$ is also open. To avoid doublecounting, we need to find the chance that one or more lanes are open.

The chance that at least one lane is empty is 

$$
P(\text{lane 1} \cup \text{lane 2} \cup \ldots \cup \text{lane }N),
$$

which isn't so useful. But we can break it up iteratively.

If we had just two events, then the chance that one or the other happens is the sum of their individual probabilities less the probability that they both happen

$$
P(A\cup B) = P(A) + P(B) - P(A\cap B).
$$

We can use this to reduce each union in turn (taking $A = 1\cup 2\cup 3$ and $B=4$ to begin)

$$
\begin{align}
P(1\cup2\cup3\cup4) 
&= P(1\cup 2\cup 3) + P(4) - P(1\cup 2\cup 3\cap 4) \\
&= P(1\cup 2\cup 3) + P(4) - P((1\cap 4)\cup(2\cap 4)\cup(3\cap 4)) \\
&= P(1\cup 2) + P(3) - P(1\cup 2\cap 3) + P(4) - (P((1\cap 4)\cup (2\cap 4)) + P(3\cap 4) - P((1\cap 4\cap 3)\cup(2\cap3\cap 4))) \\
&= P(1) + P(2) - P(1^2) + P(3) - P((1^3)v(2^3)) + P(4) - (P(1^4) + P(2^4) - P(1^2^4)) - P(3^4) - (P(1^4^3) + P(2^3^4) - P(1^2^3^4)) \\
&= P(1) + P(2) + P(3) + P(4) - (P(1^4) + P(2^4) + P(3^4) + P(1^3) + P(2^3) + P(1^2)) + P(1^2^4) + P(2^3^4) + P(1^3^4) + P(1^2^3) - P(1^2^3^4)
\end{align}
$$

In other words, we sum the probabilities for all single lanes to be empty, then subtract the probability that any two lanes are empty, then add the probability that any three lanes are empty, and so on, up until the chance that (n-1) lanes are empty.  

This is 

$P(a lane empty) = \sum\limits_{i=0}^{N-1}\binom{N}{i}(\frac{n-j}{n})^{3n-j}(-1)^{j+1}$
 
 
<br>
