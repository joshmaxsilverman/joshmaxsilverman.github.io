---
layout: post
published: true
title: Cornhole Connoisseur
date: 2021/05/02
---

>**Question**: 

<!--more-->

([FiveThirtyEight](URL))

## Solution

In the cornhole game, we have complete freedom to choose between our **aggressive** thrower, our **conservative** thrower, and our **wasted** thrower. If we make three additional points by game's end, then the game has value $V = 1,$ but if we score any other amount of additional points, then the game has value $V = 0.$ With $4$ throws left, the optimal sequence of moves is a little opaque. 

However, it's easier to see the right move when we have $1$ throw left. 

### The last throw

Of course, it depends on how many points we have. 

If we've $0$ points, then we should do whatever makes the probability of hitting the hole the highest, since it will get us the full $3$ points we're after. In this case, the clear move is to send the **aggressive** thrower to the line.

If we have $2$ points then the best move is whatever makes the probability of hitting the board the highest, so the best move is to send the **conservative** thrower to the line.

If we have $3$ points then we can only spoil our win by scoring another point, so we should send the wasted thrower to the line.

If we have $1$ point then there is absolutely no chance to win the game, so the best move doesn't matter, we can only lose no matter what we do, and we will.

### The choice

In the first case, we have probability $p_\text{agg}(3) = \frac{4}{10}$ of reaching a score of $3$ with no moves left, so the expected value of taking the aggressive shot is $p_\text{agg}(3)times 1 = \frac{4}{10}.$ Had we taken the **conservative** shot, the expected value of the shot would be $\frac{1}{10},$ and zero had we taken the **wasted** shot.

Likewise, the expected value of the second case is $p_\text{cons}(1) \times 1 = \frac{8}{10},$ while the third case is $p_\text{waste}(0) \times 1 = 1.$ As we said before, there is no chance to win in the fourth scenario so its expected value is just zero.

### What have we done

The logic here is that we looked at all of the options before us, found their value, and then chose the option with the highest value. 

Whenever we find ourselves in those scenarios, i.e. one turn remaining with $0$ points accumulated, one turn remaining with $1$ point accumulated, one turn remaining with $2$ points accumulated, or one turn remaining with $3$ points accumulated, the optimal choice will be as we just found it. So, if we find ourself in those positions again, we should make those same decisions. 

<br>
