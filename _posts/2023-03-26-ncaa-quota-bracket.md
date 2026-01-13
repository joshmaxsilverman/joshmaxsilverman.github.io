---
layout: post
published: true
title: NCAA quota bracket
date: 2023/03/26
subtitle: I'll take one of each.
source: fivethirtyeight
tags: counting symmetry tournaments
theme: probability
---

>**Question**: It feels like there’s more parity in college basketball’s March Madness than ever, with lower-seeded teams advancing further in the tournaments at the expense of the favorites. This year’s Sweet $16$ on the men’s side consists of two $1$ seeds, two $2$ seeds, two $3$ seeds, two $4$ seeds, a $5$ seed, a $6$ seed, a $7$ seed, an $8$ seed, a $9$ seed and a $15$ seed. This got Jeremy wondering about the likelihood that the Sweet 16 consists of exactly one of each seed: one $1$ seed, one $2$ seed, etc., up to one $16$ seed.
>
>Suppose each team is equally likely to win any given game. What are the chances that the Sweet $16$ does indeed consist of one of each seed?
>
>**Extra credit**: Looking at historical data on the men’s side, Jeremy estimates that the probability that seed A will defeat seed B is $\frac12 + 0.033 (B−A).$ Using these probabilities, what are the chances that the Sweet $16$ consists of one of each seed?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/the-riddler-meets-jeopardy/))

## Solution

In the NCAA tournament, there are $4$ equivalent subtournaments (crudely, four geographic regions of the US), and each will send $4$ teams to the "sweet sixteen".

![](/img/2023-03-26-regional-tournament.png){:width="550 px" class="image-centered"}

If a team makes it to the sweet sixteen, it means that they won their sub-bracket of $4$ teams.

For example, a $1$-seed's sub-bracket has them play a $16$-seed, followed by the winner of the $8$ and $9$-seed.

So, if we call $P(i,j)$ the probability of team $i$ beating team $j,$ the probability of any given $1$-seed making the sweet sixteen is 

$$ P_\text{sweet sixteen}(1) = P(1,16)\left[P(1,8)P(8,9) + P(1,9)P(9,8)\right]. $$

Likewise, for a general sub-bracket

![](/img/2023-03-26-sub-bracket.png){:width="550 px" class="image-centered"}

the probability of team $i$ making the sweet sixteen is

$$ P_\text{sweet sixteen}(i) = P(i,j)\left[P(i,m)P(m,n) + P(i,n)P(n,m)\right]. $$

We're interested in the case where one of each kind of seed makes the sweet sixteen (referred to from here on as a "quota bracket"), so the probability of any given realization is just

$$ P(\text{any given quota bracket}) = \prod\limits_{s=1}^{16} P_\text{sweet sixteen}(s). $$

Since we have to pick one of each kind of seed, there are $4!$ ways to choose seeds $\\{1,16,8,9\\}$ and likewise for the other sub-brackets. 

![](/img/2023-03-26-tournament.jpg){:width="550 px" class="image-centered"}

This makes $4!^4$ possible ways to select seeds $1$ throught $16$ and, so, the overall probability is

$$ P(\text{quota bracket}) = 4!^4 \prod\limits_{s=1}^{16} P_\text{sweet sixteen}(s). $$

When the teams are evenly matched, this is just $4!^4/4^{16},$ or $\approx 0.0077\%$ of the time. 

When they're not evenly matched, we need to set up some accounting to handle all the substitutions. Now the probability that seed $i$ beats seed $j$ is 

$$ P(i, j) = \frac12 + f(j-i). $$

First, we need to represent the structure of the sub-brackets:

<!-- {% raw %} -->
```mathematica
tournament = {
               {{1,16}, {9, 8}}
             , {{13, 4}, {12, 5}}
             , {{10, 7}, {15, 2}}
             , {{14, 3}, {11, 6}}
             }
```
<!-- {% endraw %} -->

Next, we need a function that takes a sub-bracket in the form $\\{\\{i,j\\},\\{m,n\\}\\}$ and calculates the probability of team $i$ winning:

```mathematica
p[{a_, b_}, f_] := 1/2 + f (b - a);

firstWinsBracket[b_, f_] :=
   p[b[[1]], f] *
    (p[{b[[1]][[1]], b[[2]][[1]]}, f] * p[b[[2]], f]
      + p[{b[[1]][[1]], b[[2]][[2]]}, f] * p[Reverse@b[[2]], f])
```

Next, we need a function that takes a sub-bracket and returns the four variants $\\{\\{i,j\\},\\{m,n\\}\\}, \\{\\{j,i\\},\\{m,n\\}\\}, \\{\\{m,n\\},\\{i,j\\}\\}$ and $\\{\\{n,m\\},\\{i,j\\}\\},$ corresponding to each team winning the sub-bracket:

```mathematica
makeWinners[b_] := 
      { 
        b
      , {Reverse@b[[1]], b[[2]]}
      , {b[[2]], b[[1]]}
      , {Reverse@b[[2]], b[[1]]}
      }
```

Finally, we need to form all $16$ sub-brackets, calculate the win probabilities, multiply them together, and scale by the number of ways to distribute them across the $4$ geographic sub-tournaments:

```mathematica
brackets = Flatten[makeWinners[#] & /@ tournament, 1];

pQuotaBracket[f_] := (
  winProbs = firstWinsBracket[#, f] & /@ brackets;
  pOverall = (4!)^4 Fold[Times, winProbs];
  Return[pOverall]
  )
```

As the advantage to the better team grows (to a maximum of $f = 1/30$), the likelihood of a quota bracket drops to zero: 

![](/img/2023-03-26-tournament-prob-f.png){:width="550 px" class="image-centered"}

At the empirical seed advantage, $f = 0.033,$ the probability of a quota bracket stands at a mere $8.53\times10^{-10}.$

<br>
