---
layout: post
published: true
title: How many rides can you reserve?
date: 2025/05/04
subtitle: How many rides will you get if you throw Mickey a little money on the side?
tags: recursion
---

>**Question**:

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/how-many-rides-can-you-reserve))

## Solution

we're going to start backward and deal with the extra credit first.

### Extra credit

after the initial selections are made, the rider is equally likely to add any of the remaining time slots to their schedule, even if it starts before one of their currently scheduled rides.

consider the set of all possible schedules given $N$ total time slots, $\mathcal{S}_N$, and pick one at random. 

if you didn't pick the first time slot (probability $(1-3/N)$), then you're in a situation you could have been in with $(N-1)$ time slots. but, if you did pick the first timeslot (probability $3/N$) you now have an extra ride since after you finish your first ride, you will be in a valid situation from $\mathcal{S}_{N-1}.$

for example, take $N=6$ and an initial schedule $(2,4,6).$ this is a situation we could have been in with $N=5$ time slots, since we have effectively wasted the first time slot by not picking it. by contrast, if our initial schedule is $(1,4,6)$, then after the first ride we will draw another time slot at random (either $2$, $3$, or $5$), giving schedules $(2,4,6)$, $(3,4,6)$ or $(4,5,6)$ plus one ride already completed.

call $R_N$ the number of rides we expect with $N$ timeslots, the above argues

$$ 
  \begin{align}
    R_N &= \frac3N \left(1 + R_{N-1}\right) + \left(1-\frac3N\right)R_{N-1} \\
         &= R_{N-1} + \frac3N.
  \end{align} 
$$

so, adding an $N^\text{th}$ timeslot adds $3/N$ extra rides in expectation.

following the recursion down, [we get](https://www.wolframalpha.com/input?i=3+harmonicnumber%2812%29+-+5%2F2)

$$ 
  \begin{align}
    R_N &= \frac3N + R_{N-1} \\
         &= \frac3N + \frac3{N-1} + R_{N-2} \\
         &= 3\left(\frac1N + \frac1{N-1} + \ldots + \frac15 + \frac14\right) + R(3) \\
         &= 3\left(H_{N} - \frac13 - \frac12 - 1\right) + 3 \\
         &= 3H_{N} - \frac52 \\
  \end{align}
$$

which for $N=12$ is equal to 

$$
  \begin{align}
    R_{12} &= 3H_{12} - 5/2 \\
           &= \frac{62921}{9240} \\
           &\approx 6.80963\,\text{rides}
  \end{align}
$$

plotting the calculation (gold points) alongside an $N=10^6$ trial simulation (blue points), there is good agreement:

![](/img/2025-05-04-fiddler-lightning-lane-next-free.png){:width="450 px" class="image-centered"}

the standard problem is actually more complicated. whereas in the extra credit, we keep playing the same game with fewer time slots, the standard credit transitions you between fundamentally different games.

### Standard credit

after you take your first ride, you're playing a new game where you have $r$ remaining timeslots, and you continue drawing from the remainder until you reach the final timeslot — let's call this the endgame, with value $E_r$. the number of time slots $r$ in the endgame is determined by the highest time slot you got in your original allotment of $3$ random timeslots. 

the probability that your largest time slot in the original draw is $r$ is $P(r) = \binom{r-1}{2}/\binom{12}{3}.$

so, the expected number of rides is

$$ R_N = \sum_{r=3}^{N}\left(3 + E_{N-r}\right)P(r). $$

as with the extra credit, we can find the value of the endgame by comparing the situation with $r$ remaining to the one with $(r-1)$ remaining:

$$ 
  \begin{align}
    E_r &= 1/r \left(1 + E_{r-1}\right) + \left(1-1/r\right)E_{r-1} \\
                      &= \frac1r + E_{r-1}
  \end{align}
$$

and $E_r = 1/r + 1/(r-1) + \ldots + 1/2 + 1 = H_r. $

so the expected number of rides [is](https://www.wolframalpha.com/input?i=sum_%7Br%3D3%7D%5E%7B12%7D%28binomial%28r-1%2C2%29%2Fbinomial%2812%2C3%29%283+%2B+harmonicnumber%2812-r%29%29%29), 

$$ R_N = \sum_{r=3}^N \dfrac{\binom{r - 1}{2}}{\binom{N}{3}}\left(H_{N - r} + 3\right) $$

which for $N=12$ equals $118361/27720 \approx 4.26988$ rides.
plotting the series summation (gold points) alongside an $N=10^6$ trial simulation (blue points), there is good agreement once again.

![](/img/2025-05-04-fiddler-lightning-lane-after-last.png){:width="450 px" class="image-centered"}



<br>
