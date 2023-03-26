---
layout: post
published: true
title: NCAA census bracket
date: 2023/03/26
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

there are $4$ equivalent subtournaments (crudely, four geographic regions of the US), and each will send $4$ teams to the sweet sixteen.

![](put sub-bracket drawing here)

if a team makes it to the sweet sixteen, it means that they won their sub-bracket of $4$ teams.

for example, a $1$-seed's sub-bracket has them play a $16$-seed, followed by the winner of the $8$ and $9$-seed.

so, if the probability of team $i$ beating team $j$ is $P(i,j),$ the probability of any given $1$-seed making the sweet sixteen is 

$$ P_\text{sweet sixteen}(1) = P(1,16)\left[P(1,8)P(8,9) + P(1,9)P(9,8)\right]. $$

likewise, if a team's sub-bracket looks like this:

![](put drawing here)

the probability of team $i$ making the sweet sixteen is

$$ P_\text{sweet sixteen}(i) = P(i,j)\left[P(i,m)P(m,n) + P(i,n)P(n,m)\right]. $$

we're interested in the case where one of each seed makes the sweet sixteen (quota bracket), so the probability of any given realization is just

$$ P(\text{any given quota bracket}) = \prod\limits_{s=1}^{16} P_\text{sweet sixteen}(s). $$

since we have to pick one of each kind of seed, there are $4!$ ways to choose seeds $\{1,16,8,9\}$ and likewise for the other initial groupings. 

![](put overall bracket drawing here)

this makes $4!^4$ possible ways to select seeds $1$ throught $16,$ and so, the overall probability is

$$ P(\text{quota bracket}) = 4!^4 \prod\limits_{s=1}^{16} P_\text{sweet sixteen}(s). $$

when the teams are evenly matched, this is just $4!^4/4^{16},$ or $\approx 0.0077\%$ of the time. 

when they're not evenly matched, we need to set up some accounting to handle all the substitutions. as the advantage to the better team grows, the likelihood of a quota bracket drops to zero:

```mathematica
put code here
```

![](put graph here)

<br>
