---
layout: post
published: true
title: Final Jeopardy
date: 2020/11/15
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

In both strategies, the thresholded bonus rule is in play: if the player has accumulated less than $\\$1,000$ by the time they hit the Daily Double, they get house money to be with in the amount of $\\$1,000,$ otherwise they can use their own winnings to bet. The row by row strategy has just $30$ cases to consider since there is one guessing order and $30$ possible locations for the Daily Double. However, the random strategy has $30! \approx 2.7\times 10^{32}$ possible orderings, each of which can be interrupted by the Daily Double at $30$ different points. 

## Row by row

For the row by row strategy, we can just go one tile at a time. If the accumulated winnings by the Daily Double tile are less than $\\$1,000,$ then we get $\\$1,000$ to bet with. Otherwise, we bet all our accumulated winnings, doubling our money. Also, we do not get the face value of the tile we hit the Daily Double on. Saving the math for the extra credit, we can just code up the logic above with a short Python script. It shows that the expected value of this strategy is $\\$23,800:$

```python
import numpy as np

tiles = 6 * [200] + 6 * [400] + 6 * [600] + 6 * [800] + 6 * [1000]
prizes = []

for _ in range(0, len(tiles)):
    (temp_total, DD_bonus) = (0, 0)
    if sum(tiles[:_]) < 1000:
        DD_bonus = 1000
    else:
        DD_bonus = sum(tiles[:_])
    temp_total = DD_bonus + sum(tiles[:_]) + sum(tiles[(_+1):])
    prizes.append(temp_total)
    
print(np.mean(prizes))
```

## Random guessing

For random guessing, there are a bunch of cases to consider — between the orderings and the Daily Double placement, there are some $30\times 30!$ possible games. Our task is to calculate the average winnings, which is a sum of the base value of the tiles and the bonus:

$$W = \text{Base value of tiles} + \text{Daily Double bonus}.$$

### Simple model

We can make a first pass at the answer with an audacious approximation. The number of cases where the thresholded bonus gets applied (handing the player $\\$1000$ to bet with) are relatively few, so if we ignore them it shouldn't have a huge impact on the answer.

Putting them to the side, we can focus on the core of the bonus mechanism: allowing the player to bet their accumulated winnings. 

In this case, the player gets the combined total of all the tiles on the board plus the total of the tiles they'd won by the time they hit the daily double. Ignoring the discrete nature of the tiles, we can say that the player hit the daily double when they were a fraction $f$ to accumulating all the value on the board. If each tile's value is $t_i$ then the total value is $T = \sum_i t_i$ and the player's winnings come to

$$W^\prime = T + f\times T$$

Because the daily double is placed randomly, the expected value of $f$ is $1/2$ and 

$$\langle W^\prime \rangle = 3T/2 = \\$27,000.$$


<br>
