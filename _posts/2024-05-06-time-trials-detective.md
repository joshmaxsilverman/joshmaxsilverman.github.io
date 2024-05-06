---
layout: post
published: false
title: Can You Beat the Heats?
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

## Solution

In the $25$ person race, we want to find the three fastest people. 

It isn't possible to find the three fastest people without racing all of the sprinters since we can't rank someone in the absence of information. Since each race takes $10$ people, we can't fit $25$ sprinters in less than $3$ races. So, $3$ is the absolute minimum number of races we can hope to use.

Happily, this threshold can be saturated.

- First, we can race any $10$ of the sprinters, identifying the top three ouf of them.
- Next, pick another $8$ of the un-raced sprinters and race them with the second and third fastest sprinters from the first race.
- Now, take the two fastest from the second race, the winner of the first race, and the $7$ remaining un-raced sprinters and run them in a race.

The top three finishers of the last race are the three fastest sprinters.

### Extra credit

Before we start, it pays to think about the information we seek. 

There are $6! = 720$ possible orderings of the six runners which is $\log_2 6! \approx 9.49$ bits of information.

If each race we ran halved the number of possibilities (a perfect "binary question"), it would yield $1$ bit. So, without considering the constraints on our race design, we should expect to need $10$ races at the very least.

At the outset, the possible orderings are fully symmetric with respect to the runners. So, pick any two runners, say $A$ and $B$ and race them against each other. The result of this race will either have $A$ or $B$ winning. Since, at this stage, the orderings are symmetric with regard to $A$ and $B,$ this will remove half of all possibilities, leaving $360$ orders. $1$ bit down, $\approx 8.49$ to go!

Since we haven't touched runners $C$ and $D,$ or $E$ and $F,$ we can pair them off and remove half of all outstanding possibilities again each time. This brings us down to $90$ orders. $3$ bits down!

Now, running these three races has destroyed the symmetry between those who won the races and those who lost. However, there is still symmetry amongst the winners and losers. For argument's sake, say $A,$ $C,$ and $D$ won their races while $B,$ $D,$ and $F$ lost theirs. So, if we pair $A$ and $C$ in a race, we can eliminate another half of all orders, leaving $45$ orders.

Now, there are no symmetric choices left. Since $A$ and $C$ were winners, this race gives us information about $B$ and $D.$ If, e.g., $A$ beats $C,$ then it tells us $A$ can beat $D.$

We have to do our best to construct splits that come as close as possible to ruling out exactly half of all remaining possibilites. It is possible that after future races, we can restore symmetry.

In this spirit I wrote a greedy algorithm to find, at each stage, the race that comes closest to eliminating half of all outstanding possible orderings, which will minimize the number of races run.

```python
from copy import deepcopy
from itertools import permutations

orders = list(permutations('ABCDEF'))

def x_before_y(x, y, lst):
  x_pos, y_pos = lst.index(x), lst.index(y)
  return x_pos < y_pos

new_orders = deepcopy(orders)

while len(new_orders) > 1:

  trial_race = dict()
  current_length = len(new_orders)

  for x in 'ABCDEF':
    for y in 'ABCDEF':

      if x == y:
        pass

      else:
        remaining = len([ o for o in new_orders if x_before_y(x, y, o) ])
        trial_race[(x, y)] = abs(current_length/2 - remaining)

  best_race = min(trial_race, key=trial_race.get)
  best_x, best_y = best_race
  new_orders = [ o for o in new_orders if x_before_y(best_x, best_y, 0) ]

  fprint(f'{best_x} against {best_y}')
```

which yields the following $10$ races

```markdown
A against B
C against D
E against F
A against C
E against F
B against F
B against C
B against E
C against E
D against E
```

This saturates the idealized minimum, despite the constraints imposed by the loss of symmetry.




<br>
