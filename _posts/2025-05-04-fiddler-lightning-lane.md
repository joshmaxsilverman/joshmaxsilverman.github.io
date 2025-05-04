---
layout: post
published: true
title: Lightning lanes
date: 2025/05/04
subtitle: 
tags: recursion
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

we're going to start backward and deal with the extra credit first.

### Extra credit

after the initial selections are made, the rider is equally likely to add any of the remaining time slots to their schedule, even if it starts before one of their currently scheduled rides.

consider the set of all possible schedules given $N$ total time slots and pick one at random. 

if you did not pick the first timeslot (probability $(1-3/N)$), then you are in a situation you could have been in with $(N-1)$ time slots. but, if you did pick the first timeslot (probability $3/N$) you now have an extra ride since after you finish your first ride, you will be in a valid situation from R(n-1).

for example, take $N=6$ and an initial schedule $(2,4,6).$ this is a situation we could have been in with $N=5$ time slots, since we have effectively wasted the first time slot by not picking it. by contrast, if our initial schedule is $(1,4,6)$, then after the first ride we will draw another time slot at random (either $2$, $3$, or $5$), giving schedules $(2,4,6)$, $(3,4,6)$ or $(4,5,6)$ plus one ride already completed.

call $R(N)$ the number of rides we expect with $N$ timeslots, the above argues

$$ 
  \begin{align}
    R(N) &= \frac3N \left(1 + R(N-1)\right) + \left(1-\frac3N\right)R(N-1) \\
         &= R(N-1) + \frac3N.
  \end{align} 
$$

so, adding an $N^\text{th}$ timeslot adds $3/N$ extra rides in expectation.

following the recursion down, we get

$$ 
  \begin{align}
    R(N) &= \frac3N + R(N-1) \\
         &= \frac3N + \frac3{N-1} + R(N-2) \\
         &= 3\left(\frac1N + \frac1{N-1} + \ldots + \frac14 + \frac14\right) + R(3) \\
         &= 3\left(H_{12} - \frac13 - \frac12 - 1\right) + 3 \\
         &= 3H_{12} - \frac52
  \end{align}
$$

the standard problem is actually more complicated. whereas in the extra credit, we keep playing the same game with fewer time slots, the standard credit transitions you between fundamentally different games.

### Standard credit

after you take your first ride, you're playing a new game where you have $r$ remaining timeslots, and you continue drawing from the remainder until you reach the final timeslot — let's call this the endgame, with value $E(r)$. the number of time slots $r$ in the endgame is determined by the highest time slot you got in your original allotment of $3$ random timeslots. 

the probability that your largest time slot in the original draw is $r$ is $P(r) = \binom{r-1}{2}/\binom{12}{3}.$

so, the expected number of rides is

$$ R(N) = \sum_{r=1}^{N}\left(3 + E(N-r)\right)P(r). $$

as with the extra credit, we can find the value of the endgame by comparing the situation with $r$ remaining to the one with $(r-1)$ remaining:

$$ 
  \begin{align}
    E(r) &= \frac1r \left(1 + E(r-1)\right) + \left(1-\frac1r\right)E(r-1) \\
                      &= \frac1r + E(r-1)
  \end{align}
$$

and $E(r) = 1/r + 1/(r-1) + \ldots + 1/2 + 1 = H_r. $

so, 

$$\langle \text{rides} \rangle = \sum_{r=3}^{12} \dfrac{\binom{r - 1}{2}}{\binom{12}{3}}\left(H_{12 - r} + 3\right) = 118361/27720 $$






<br>
