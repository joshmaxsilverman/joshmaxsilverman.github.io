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

The dissenter wins if at least one lane is open (but not all — the equilibrists will be in at least one race). But we need to avoid doublecounting, the chance for lane $1$ to be open includes the case where lane $2$ is also open, and vice versa.

The chance that at least one lane is empty, but not all, is 

$$
P(\text{lane 1} \cup \text{lane 2} \cup \ldots \cup \text{lane }N) - P(\text{lane 1} \cap \text{lane 2} \cap \ldots \cap \text{lane }N),
$$

which isn't so useful, since unions are hard to calculate. Intersections are easy, though, and we can break it up into disjoint intersections.

If we had just two events, then the chance that one or the other happens is the sum of their individual probabilities less the probability that they both happen

$$
P(A\cup B) = P(A) + P(B) - P(A\cap B).
$$

We can apply this iteratively to reduce each union in turn (taking $A = \left(1\cup 2\right)$ and $B=3$ to begin)

$$
\begin{align}
P(1\cup 2\cup 3) &= P(1\cup 2) + P(3) - P((1\cup 2)\cap 3) \\
&= P(1) + P(2) - P(1\cap 2) + P(3) - P((1\cap3)\cup(2\cap3)) \\
&= P(1) + P(2) + P(3) - P(1\cap2) - \left[P(1\cap3) + P(2\cap3) - P(1\cap2\cap3)\right] \\
&= P(1) + P(2) + P(3) -  P(1\cap2) - P(1\cap3) - P(2\cap3) + P(1\cap2\cap3) \\
&= \binom{3}{1}P(\text{one lane open}) - \binom{3}{2}P(\text{two lanes open}) + P(\text{three lanes open})
\end{align}
$$

In other words, we sum the chance for all single lanes to be empty, then subtract the chance that any two lanes are empty, then add the chance that any three lanes are empty, and so on, up until the chance that all $3N$ lanes are empty. From this, we subtract the chance for all lanes to be empty.

This is 

$$
\begin{align}
P(\text{a lane empty}) &= P(\bigcup\limits_{i=0}^{N}i) - P(\bigcap\limits_{i=0}^{3N}i) \\
&= \sum\limits_{i=0}^{N-1}\binom{N}{i}(\frac{n-j}{n})^{3n-j}(-1)^{j+1}$
\end{align}
$$
 
 
<br>
