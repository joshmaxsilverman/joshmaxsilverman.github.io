---
layout: post
title: Rug Rejection
published: true
date: 2018/08/12
---

>A manufacturer, Riddler Rugs™, produces a random-pattern rug by sewing 1-inch-square pieces of fabric together. The final rugs are 100 inches by 100 inches, and the 1-inch pieces come in three colors: midnight green, silver, and white. The machine randomly picks a 1-inch fabric color for each piece of a rug. Because the manufacturer wants the rugs to look random, it rejects any rug that has a 4-by-4 block of squares that are all the same color. (Its customers don’t have a great sense of the law of large numbers, or of large rugs, for that matter.)
>
>What percentage of rugs would we expect Riddler Rugs™ to reject? How many colors should it use in the rug if it wants to manufacture a million rugs without rejecting any of them?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/where-on-earth-is-the-riddler/))

## Solution

There are $97 \times 97$, or $9409$, 4-by-4 blocks in a rug.  The probability of a given 4-by-4 block being monochromatic, where there are $c$ colors, is $c$ times the probability ($1/c^{16}$) of all squares having some one color, and so it is $1/c^{15}$.

The expected number of monochromatic 4-by-4 squares in a given 4-by-4 block in a rug is just the probability of that region being monochromatic, and so it is also $1/c^{15}$. By the linearity of expectation, the expected number of monochromatic regions in a rug is the sum of the expected numbers of monochromatic regions in each given 4-by-4 region, and so it is $9409/c^{15}$. 

One way of reading the second question is, for what number of colors does a million times this expectation round to zero (i.e., dip below $.5$)? The answer to that is five colors, where the total expectation is $.308$ monochromatic regions.

To address the first question, I will only manage to generate an estimate.  It's easy to get a rough one: we know that the expected number of total monochrome blocks in a million rugs is $1000000 \times 9409/3^{15}$, or about $655.7$. If we assume that there are insignificantly many rugs with more than one block, that would mean about $.06557$ percent of the rugs are blocked.  But how realistic is that assumption? 

Not very. That idealization misses a not insignificant number of multiply-blocked rugs, because a rug with a block on it is significantly more likely to have a second block than an arbitrary rug is to have at least one block.  Take a given block on a given rug, and suppose that like most it's not along one of the edges.  Then there are four ways to create additional blocks by coloring four neighboring squares. Each of these ways has probability $1/81$, for a total probability of $1-(80/81)^4$, or about $.04848$ of there being an additional block. So we might estimate that $.02424$ of the blocked rugs have two such overlapping blocks. And of course there's a small chance that there is also a non-overlapping block, and a third such block, so we might estimate that there are $1.025$ blocks per blocked rug. We could do a little better by considering corner and edge blocks separately, and calculating a good estimate for non-overlapping blocks, but we won't.

Thus, where our expected $655.7$ blocks are on $n$ expected rugs, we have:

$$1.025n = 655.7$%$$

$$n = 639.7$$

And so our estimate of the probability that a rug has a block is $.06397$ percent.

<br>
