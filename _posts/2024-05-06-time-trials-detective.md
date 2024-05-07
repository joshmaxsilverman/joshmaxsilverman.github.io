---
layout: post
published: true
title: Can you beat the heats?
date: 2024/05/06
subtitle: A good old racetrack whodunit.
tags: information-theory trees
---

>**Question**: There are $25$ sprinters at a meet, and there is a well-defined order from fastest to slowest. That is, the fastest sprinter will always beat the second-fastest, who will in turn always beat the third-fastest, and so on. However, this order is not known to you in advance.
>
>To reveal this order, you can choose any $10$ sprinters at a time to run in a heat. For each heat, you only know the ordinal results, so which runner finishes first, second, third, and so on up to $10^\text{th}.$ You do not know the specific finishing time for any runner, making it somewhat difficult to compare performances across heats.
>
>Your goal is to determine with absolute certainty which of the $25$ sprinters is fastest, which is second-fastest, and which is third-fastest. What is the fewest number of heats needed to guarantee you can identify these three sprinters?
>
>**Extra credit**: At a different meet, suppose there are six sprinters that can race head-to-head. (In other words, there are only two sprinters per heat.) Again, they finish races in a consistent order that is not known to you in advance.
>
>This time, your goal is to determine the _entire_ order, from the fastest to the slowest and everywhere in between. What is the fewest number of head-to-head races needed to guarantee you can identify this ordering?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-beat-the-heats))

**Note**: this has two major modifications from the first version of this post. 
- The standard credit solution gave the insight for a $3$ race approach, but did not carefully implement it. The correct structure is now given.
- The extra credit approach ignored pathway dependence and so, missed out on one removable race.

## Standard credit

In the $25$ person race, we want to find the three fastest people. 

It isn't possible to find the three fastest people without racing all of the sprinters. Since we can't rank someone in the absence of information, and each race takes $10$ people, $3$ is the absolute minimum number of races we can hope to use.

Happily, this threshold can be saturated.

- First, we can race any $10$ of the sprinters to identify the top three ouf of them $A_1, A_2,$ and $A_3.$
- Next, pick any $9$ of the un-raced sprinters and race them with the third fastest sprinter from the first race.
  - If $A_2$ wins, race $A_1, A_2, A_3$ and the fastest of the new runners, $B_1,$ against the $6$ unraced runners.
  - If $A_2$ comes in second, race $A_1,A_2,$ and the fastest of the new runners, $B_1,$ against the $6$ remaining unraced sprinters.
  - If $A_2$ comes in third, race $A_1, A_2$ and the winners of race two, $B_1$ and $B_2$ against the $6$ unraced sprinters.
  - If $A_2$ places outside the top three, race $A_1,B_1,$ and $B_2$ against the $6$ unraced sprinters. 

The top three finishers of the third race will be the three fastest sprinters overall.

Big thanks to Emilie Mitchell (and Dave Moran) for pointing out the earlier oversight.

## Extra credit

Before we start, it pays to think about the information we seek. 

There are $6! = 720$ possible orderings of the six runners which is $\log_2 6! \approx 9.49$ bits of information.

If, in each race, we ran halved the number of possibilities (a perfect "binary question"), we would get $\log_2 2 = 1$ bit each time. So, we should expect to run $10$ races at the very least.

### By symmetry

At the outset, the possible orderings are fully symmetric with respect to the runners. So, pick any two runners, say $A$ and $B$ and race them against each other. The result of this race will either have $A$ or $B$ winning. This will remove half of all possibilities, leaving $360$ orders. $1$ bit down, $\approx 8.49$ to go!

Since we haven't touched runners $C$ and $D,$ or $E$ and $F,$ we can pair them off for races two and three and remove half of all outstanding possibilities each time. This brings us down to $90$ orders. $3$ bits down.

Now, running these three races has removed the symmetry between those who won their race and those who lost their race. However, there is still symmetry within the winners and losers. For argument's sake, say $A,$ $C,$ and $E$ won their races while $B,$ $D,$ and $F$ lost theirs. If we pair $A$ and $C$ in a race of their own, we can eliminate another half of all orders, leaving $45$ orders.

From here, we can't make any easy binary divisions, and we have to find the races that come as close as possible to dividing the field. The best race to run will depend on the information we have at our disposal. 

To find the shallowest worst-case sequence of races, we can search over all possible races to run, and log the number of remaining possibilities for the two possible outcomes. From these, we can pick the one that gets the two numbers as close as possible. This will give us the best race to run, between sprinters $s_1$ and $s_2$.

This will give us two lists $L_{s_1}$ and $L_{s_2},$ corresponding to the possibilities that remain if $s_1$ or $s_2$ wins.

From here, we can return $1 + \max(\text{depth}(L_{s_1}), \text{depth}(L_{s_2}))$ so the problem is defined recursively like

$$ \text{depth}(L) = 1 + \min_{\lvert\lvert L_{s_1}\rvert - \lvert L_{s_2}\rvert\rvert}\max\left(\text{depth}(L_{s_1}),\text{depth}(L_{s_2})\right). $$

Coding this up, we have 

```python
import math
from itertools import permutations, combinations
import string
letters = string.ascii_uppercase

n = 6
sprinters = letters[:n]
orders = set(permutations(sprinters))
pairs = set(combinations(sprinters, 2))

def find_depth(orders):

    if len(orders) == 1:
        return 0

    races = dict()

    for p in pairs:
        x, y = p
        remaining = len([ o for o in orders if o.index(x) < o.index(y) ])
        races[p] = abs(len(orders) / 2 - remaining)

    best_race = min(races, key=races.get)
    best_x, best_y = best_race

    orders_x = set(o for o in orders if o.index(best_x) < o.index(best_y))
    orders_y = orders.difference(orders_x)

    return 1 + max(find_depth(orders_x), find_depth(orders_y))

```

Now, this approach is greedy and it does not consider the possibility that e.g. sub-optimally dividing the possibilities at stage $n$ sets us up better overall sub-division at a subsequent level of the recursion. So, we should only believe our result if it matches the theoretical minimum from above, $\lceil \log_2 N!\rceil.$

For $N=1$ to $7,$ it does and we get

$$ 
  \begin{array}{c|c}
    N & \text{depth}(N) \\ \hline
    1 & 0 \\
    2 & 1 \\
    3 & 3 \\
    4 & 5 \\
    5 & 7 \\
    6 & 10 \\
    7 & 13
  \end{array} 
$$

Sadly, for $N=8,$ the greedy approach no longer saturates the bound. 

Thanks to Tom Keith for pointing out the issue with the original approach.


<br>
