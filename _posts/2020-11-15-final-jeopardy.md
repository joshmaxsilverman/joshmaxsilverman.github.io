---
layout: post
published: true
title: Final jeopardy
date: 2020/11/15
subtitle: Which board order wins more money if you ace every clue?
source: fivethirtyeight
theme: probability
---

>**Question**: it's your last chance to be on Jeopardy and you want to leave it all on the field. You've trained for years and are confident that you can answer every question correctly and beat your competitors to the buzzer every time. Your only issue is how to order your guesses. The Daily Double tile is placed randomly on the board, so you can't predict its location. The two strategies you've narrowed it down to are guessing all the tiles in succession (all $\\$200$ tiles then all $\\$400$ tiles and so on) or to guess tiles randomly. What is the expected value of each strategy, assuming you have the whole "getting the answers right" part covered?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-snatch-defeat-from-the-jaws-of-victory/))

## Solution

In both strategies, the thresholded bonus rule is in play: if the player has accumulated less than $\\$1,000$ by the time they hit the Daily Double, they get house money to bet with in the amount of $\\$1,000,$ otherwise they can use their own winnings to bet. The row by row strategy has just $30$ cases to consider since there is one guessing order and $30$ possible locations for the Daily Double. However, the random strategy has $30! \approx 2.7\times 10^{32}$ possible orderings, each of which can be interrupted by the Daily Double at $30$ different points. 

## Row by row

For the row by row strategy, we can just go one tile at a time. If the accumulated winnings by the Daily Double tile are less than $\\$1,000,$ then we get $\\$1,000$ to bet with. Otherwise, we bet all our accumulated winnings, doubling our money. Also, we do not get the face value of the tile we hit the Daily Double on. Saving the math for the second case, we can just code up the logic above with a short Python script. It shows that the expected value of this strategy is $\\$23,800:$

```python

import numpy as np

tiles = 6 * [200] + 6 * [400] + 6 * [600] + 6 * [800] + 6 * [1000]
prizes = []

for _ in range(len(tiles)):
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

We can make a first pass at the answer with an audacious approximation. The cases where the thresholded bonus gets applied (handing the player $\\$1,000$ to bet with) are relatively few, so if we ignore them it shouldn't have a huge impact on the answer.

Putting them to the side, we can focus on the core of the bonus mechanism: allowing the player to bet their accumulated winnings. 

In this case, the player gets the combined total of all the tiles on the board plus the total of the tiles they'd won by the time they hit the daily double. Ignoring the discrete nature of the tiles, we can say that the player hit the daily double when they were a fraction $f$ to accumulating all the value on the board. If each tile's value is $t_i$ then the total value is $T = \sum_i t_i$ and the player's winnings come to

$$W^\prime = T + f\times T$$

Because the daily double is placed randomly, the expected value of $f$ is $1/2$ and 

$$\begin{align}
\langle W^\prime \rangle &= \frac{3}{2}\times T \\
&= \$27,000.
\end{align}$$


### Small fixes

Of course, this is wrong. We've neglected a few things: we do not get the value of the Daily Double tile, the tiles are discrete, and the threshold ensures that nobody bets with less than $\\$1,000$ at their disposal.

Let's deal with the first thing first. The total value of the tiles is $T = \sum_i t_i,$ but we don't get the full value of $T,$ we skip out on the value of the Daily Double tile $t_d.$ Since $t_d$ is equally likely to be any of the tiles, which are evenly split between $\\$200,$ $\\$400,$ $\\$600,$ $\\$800,$ and $\\$1,000,$ we have to subtract off the average value of a single tile:

$$ \boxed{\langle \text{Base value of tiles}\rangle = T - \frac{\$200 + \$400 + \$600 + \$800 + \$1,000}{5} = \$17,400} $$

To get a handle on the bonus we can split it into two pieces, the core winnings betting piece, and the adjustment for the players who are under the threshold. Concretely, if a player has $\\$400$ when they hit the daily double, we can imagine that they bet their $\\$400,$ win it, and then receive a one-time bonus of $\\$600$ to make up for the gap between their accumulated winnings and the $\\$1,000$ floor. 

So, everyone gets to double their winnings. The daily double can fall at any point between Tile $0$ (when the player would have $\\$0$ accumulated) and Tile $30$ (when the player would be close to the maximum amount they could accumulate). On Tile $30$ the player will have collected all but one of the tiles, so they'd have an average of $\\$18,000 - \\$600 = \\$17,400.$ 

The distribution is symmetric about the middle, so the average amount gained by betting their winnings is 

$$ \boxed{\text{Core bonus} = \frac{\$0 + \$17,400}{2} = \$8,700}. $$


### Big fixes

So far, we've calculated the base amount that any player can expect due to collecting the tiles and the winnings betting mechanism and those contributions come to $\\$17,400 + \\$8,700 = \\$26,100,$ slightly under the level of the naive model. However, we still have to add in the adjustments due to the players who hit the Daily Double when they were under the threshold. 

$$\begin{align}
\text{Winnings} &= \text{Base value of tiles} + \text{Bonus} \\
\text{Bonus} &= \text{Core bonus} + \text{Adjustment for threshold}
\end{align}$$

In particular, all players who hit the Daily Double on their first guess will have had $\\$0$ at that point, and therefore need to be credited a full $\\$1,000.$ Players who hit the Daily Double on their second tile will also be under the threshold unless they happened to land on a $\\$1,000$ tile on their first turn. 

In general, this is a combinatorics problem, counting the number of ways a player could have been under the threshold when they hit the Daily Double.

**First tile Daily Double**

$$\{\boxed{t_1}\}$$

As we said, all players who hit the Daily Double on their first tile will receive the full $\\$1,000.$ 

**Second tile Daily Double**

$$\{t_1, \boxed{t_2}\}$$

For players who hit the Double on their second tile, there are $24$ ways for them to be under the betting threshold: if they hit one of the six $\\$200$ tiles, one of the six $\\$400$ tiles, one of the six $\\$600$ tiles, or one of the six $\\$800$ tiles on their first tile. 

$$\begin{array}{|c|c|c|} \hline
W & \text{ways} & \Delta \\ \hline
\$200 & 6 & \$800 \\ \hline
\$400 & 6 & \$600 \\ \hline
\$600 & 6 & \$400 \\ \hline
\$800 & 6 & \$200 \\ \hline
\end{array}$$

Since there are $30$ ways to pick the first tile, this bonus has an expected value of

$$\frac{6\times \$200 + 6\times \$400 + 6\times \$600 + 6\times \$800}{30} = \$400.$$


**Third tile Daily Double**

$$\{t_1, t_2, \boxed{t_3}\}$$

The number of ways to subsume the threshold expands when a player hits the Double on their third tile, at which point they can have $\\$400,$ $\\$600$ or $\\$800.$ Having $\\$400$ corresponds to getting a $\\$200$ tile on each of the first two tiles, which can be done $6\times 5$ different ways. Getting $\\$600$ means drawing a $\\$200$ and a $\\$400$ for the first two tiles (in any order) which can happen in $6\times 6\times 2$ different ways. Getting an $\\$800$ can happen in one of two ways, the first is similar to $\\$400$ and has $6\times 5$ distinct ways to occur, while the second consists of getting a $\\$600$ and a $\\$200$ in either order, which has $2\times 6\times 6$ ways to occur. 

$$\begin{array}{|c|c|c|} \hline
W & \text{ways} & \Delta \\ \hline
\$400 & 6\times 5 & \$600 \\ \hline
\$600 & 6\times 6\times 2 & \$400 \\ \hline
\$800 & 6\times 5  + 6\times 6\times 2 & \$200 \\ \hline
\end{array}$$

Since there are $30\times 29$ different ways to pick the first two tiles this bonus has an expected value of

$$ \frac{30\times \$600 + 72 \times \$400 + 102\times \$200}{30\times 29} = \$2240/29 \approx \$77.24.$$

**Fourth tile Daily Double**

$$\{t_1, t_2, t_3, \boxed{t_4}\}$$

At the fourth tile, the possibilities start to tighten up. At this point, a player can only have $\\$600$ or $\\$800$ while subsuming the threshold. $\\$600$ means getting a $\\$200$ tile for each of the first three tiles, and $\\$800$ gettings two $\\$200$s and a $\\$400$ in any order

$$\begin{array}{|c|c|c|} \hline
W & \text{ways} & \Delta \\ \hline
\$600 & 6\times 5\times 4 & \$400 \\ \hline
\$800 & 6\times5\times6\times3 & \$200 \\ \hline
\end{array}$$

This bonus has an expected value of

$$ \frac{120\times\$400 + 540\times \$200}{30\times29\times28} = \$1300/203 \approx \$6.40 $$


**Fifth tile Daily Double**

$$\{t_1, t_2, t_3, t_4, \boxed{t_5}\}$$

Finally, the player could hit the Double on their fifth tile. There is only one way to subsume the threshold this way, which is by getting four $\\$200$ tiles on the first four tiles. This bonus has $6\times5\times4\times3$ ways to happen and has a small expected value

$$\frac{360\times \$200}{30\times29\times28\times27} = \$200/1827 \approx \$0.11$$


### Putting it all together

To recap, we broke up the expected value into the base value of the tiles and the bonus. We further split the bonus up into the part that comes from betting your winnings and the history dependent subsidy issued to players who hit the Daily Double before they'd accumulated $\\$1,000.$ 

Adding it all up, we have

$$\begin{align}
\langle W\rangle &= \overbrace{\$17,400}^\text{Base value of tiles} + \overbrace{\$8,700}^\text{core bonus} + \frac{1}{30}\overbrace{\left(\$1000 + \$400 + \$2240/29 + \$1300/203 + \$200/1827\right)}^\text{ways to subsume threshold} \\
&= \$26,100  + \$38726/783 \\
&\approx \$26,149.46
\end{align}
$$

### Is it real?

The $30$-tile board has too any orderings to exhaustively simulate, but an $N = 2,000,000$ round simulation produced an estimate of $\approx\\$26,149.43$ for the expected value of the random strategy. A $9$-tile version of the Jeopardy board (three $\\$200$ tiles, three $\\$400$ tiles, three $\\$600$ tiles) only has $9!$ orders and can be exactly simulated. Doing the same analysis we just did for the $30$-tile board gives an expected value of $\\$105100/21\,$[$\approx\\$5004.76$](https://www.wolframalpha.com/input/?i=3600+-+1%2F3*%28200%2B400%2B600%29+%2B+%280+%2B+3200%29%2F2+%2B+1%2F9*1000+%2B+1%2F9*1%2F9*%283*800%2B3*600%2B3*400%29+%2B+1%2F9*1%2F%289*8%29*%286*600%2B18*400%2B24*200%29+%2B+1%2F9*1%2F%289*8*7%29*%286*400%2B54*200%29), which agrees exactly with the exhaustive simulation.

```python

import numpy as np
from itertools import permutations

prices = 3 * [200] + 3 * [400] + 3 * [600]
perms = list(permutations(prices))

prizes = []

for round in range(len(perms)):
    
    temp_tiles = perms[round]
    winnings = []

    for _ in range(len(temp_tiles)):
        
        DD_winning = sum(temp_tiles[:_])
        
        if DD_winning < 1000:
            DD_winning = 1000
        
        round_winnings = DD_winning + sum(temp_tiles) - temp_tiles[_]
        winnings.append(round_winnings)
    
    prizes.append(winnings)

np.mean([item for lst in prizes for item in lst])

```

<br>
