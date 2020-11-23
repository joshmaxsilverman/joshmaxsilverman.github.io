---
layout: post
published: true
title: Pass the Cranberry Sauce
date: 2020/11/22
---

>**Question**: it's Thanksgiving and your family is gathered 'round the circular dinner table, Tofurkey in the middle, as is tradition. When the time comes, your Aunt Riddla brings out her famous cranberry sauce, handing it to you to place on the table. Wherever you place it, the person sitting there will take some sauce and then pass it randomly to one of their neighbors with probability $r$ to the right, and probability $\ell$ to the left. 
>
>This placement is no small decision though. You want to punish your naughty Uncle Zach so that he gets the cranberry sauce last! Where should you start the sauce off on its journey if you want Uncle Zach to be the most likely to be the last person to get that famous cranberry sauce?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-pass-the-cranberry-sauce/))

## Solution

the cranberry sauce on the table sweeps out a widening arc of diners who've had it, dividing the table into two sections. if the sauce wanders inside the arc, then nobody new gets the sauce, and if it reaches the egde then the arc expands. 

by construction, the section of people who have not had the sauce is continous, and winnows from each side until there's only one person left. 

### Neighbor to neighbor

for someone to be the last person remaining, the arc of the visited has to broaden til it reaches their neighbors, one after the other.

for instance, if the sauce meandered its way from position $1$ to position $11$ (without hitting position $9$ in the process) before turning around and meandering its way to position $9$ (without hitting position $10$ in the process), then the person at position $10$ would be the last to receive the sauce. 

we can call the probability of the first path segment $\require{cancel}\Gamma(1\xrightarrow{\cancel{9}} 11)$ signifying that it goes from $1$ to $11$ without bumping into $9.$ likewise, the probability of the second half is $\Gamma(11\xrightarrow{\cancel{10}} 9).$

(image of this path)

of course it could also have happened in the reverse order, meandering clockwise to visit $9$ (without hitting $11$) before meandering back to $11$ (without hitting $10$). this has total probability $\Gamma(1\xrightarrow{\cancel{11}} 9)\times \Gamma(9\xrightarrow{\cancel{10}} 11).$

the probability for the person at $i$ to be the last one visited is the sum of the probability of these two events

$$\require{cancel} L(10) = \Gamma(1\xrightarrow{\cancel{11}} 9)\times \Gamma(9\xrightarrow{\cancel{10}} 11) + \Gamma(1\xrightarrow{\cancel{9}} 11)\times \Gamma(11\xrightarrow{\cancel{10}} 9) $$

in general, the probability for the person at position $i$ to be the last to get the sauce is 

$$\require{cancel} L(i) = \Gamma(1\xrightarrow{\cancel{i+1}} (i-1))\times \Gamma((i-1)\xrightarrow{\cancel{i}} (i+1)) + \Gamma(1\xrightarrow{\cancel{(i-1)}} (i+1))\times \Gamma((i+1)\xrightarrow{\cancel{i}} (i-1)) $$

### Unrolling the table

it's easier to think about this problem if we "unroll" the circle. there are $N$ positions in total and we unroll them so that we have a line going from position $1$ to $N.$ since almost all trajectories will cross between $1$ and $N,$ we add a redundant copy of positions $x$ to $N$ to the left of $1$:

(image of the unrolled line)

all possibile trajectories we're interested in will take place along this line.

### Cliff dancing

each factor $\require{cancel}\Gamma(i\xrightarrow{\cancel{k}} j)$ is the total probability that, starting from position $i$, we end up at position $j$ without ever touching position $k.$ each term has its own start and terminus as well as its own position to avoid, but the problem is generic. 

essentially, we start out some number of steps from a cliff, and we want to know how likely we are to make it another $\lvert j-i\rvert)$ steps away from the cliff. if we step off the cliff at any point then the path doesn't count. 

as we said above, the original problem breaks into four cases of this cliff problem. if we solve it then the original problem is a calculation. let's call $P_N(m)$ is the probability that we make it to $N$ steps from the cliff given that we start out $m$ steps from the cliff. 

by definition $P_N(0)=0$ as it means we start in freefall from the cliff, and $P_N(N)=1$ since it means we're at position $N$ already. with these boundary values, we can solve the problem by finding a recurrence relationship connecting the survival probability from adjacent positions. 

the probability that we make it to step $m$ is the probability that we make it to step $(m+1)$ and the take a step toward the cliff (probability $\gamma_\text{b}$), plus the probability that we make it to step $(m-1)$ and then take a step away from the cliff (probability $\gamma_\text{f}$):

$$P_N(m) = P_N(m-1)\cdot\gamma_\text{f} + P_N(m+1)\cdot\gamma_\text{b}$$

the two transition probabilities add to $1$ so we can turn this into a relationship between consecutive differences:

$$
\left(\gamma_\text{f} + \gamma_\text{b}\right)\cdot P_N(m) = \gamma_\text{f}\cdot P_N(m-1) + \gamma_\text{b}\cdot P_N(m+1)
$$

and, so

$$\begin{align}
\gamma_\text{b}\cdot P_N(m+1) - \gamma_\text{b}\cdot P_N(m) &= \gamma_\text{f}P_N(m) - \gamma_\text{f}\cdot P_N(m-1) \\
\left(P_N(m+1) - P_N(m)\right) &= \frac{\gamma_\text{f}}{\gamma_\text{b}}\left(P_N(m) - P_N(m-1)\right)
\end{align}$$

we can plug this equation back in to itself so that after one step we have 

$$ \left[P_N(m+1) - P_N(m)\right] = \left(\frac{\gamma_\text{f}}{\gamma_\text{b}}\right)^2\left[P_N(m-1) - P_N(m-2)\right]. $$

it recurses all the way down to 

$$ \left[P_N(m+1) - P_N(m)\right] = \left(\frac{\gamma_\text{f}}{\gamma_\text{b}}\right)^m\left[P_N(1) - P_N(0)\right]. $$

if we add the left hand side from $m=0$ to $m=j$ then we get

$$\begin{align}
P_N(j+1) &= P_N(1)\left(\left(\frac{\gamma_\text{f}}{\gamma_\text{b}}\right) + \left(\frac{\gamma_\text{f}}{\gamma_\text{b}}\right)^2 + \ldots + \left(\frac{\gamma_\text{f}}{\gamma_\text{b}}\right)^j\right) \\
&= P_N(1) \frac{1 - \left(\frac{\gamma_\text{f}}{\gamma_\text{b}}\right)^{j+1}}{1 - \left(\frac{\gamma_\text{f}}{\gamma_\text{b}}\right)}
\end{align}$$

### Being last

### Cases and graphs

### A time to be alone

<br>
