---
layout: post
published: true
title: Cornhole Connoisseur
date: 2020/05/02
---

>**Question**: 

<!--more-->

([FiveThirtyEight](URL))

## Solution

In the cornhole game, we have complete freedom to choose between our **aggressive** thrower, our **conservative** thrower, and our **wasted** thrower. If we make three additional points by game's end, then the game has value $V = 1,$ but if we score any other amount of additional points, then the game has value $V = 0.$ With $4$ throws left, the optimal sequence of moves is a little opaque. 

However, it's easier to see the right move when we have $1$ throw left. 

### The last throw

Of course, it depends on how many points we have. 

$$
\begin{array}{|c|c|c|c|} \hline
\textbf{thrower} & p(3) & p(1) & p(0) \\ \hline
\text{aggressive} & 0.4 & 0.3 & 0.3 \\ \hline
\text{conservative} & 0.1 & 0.8 & 0.1 \\ \hline
\text{wasted} & 0.0 & 0.0 & 1.0 \\ \hline
\end{array}
$$

If we have $0$ points, then we should do whatever makes the probability of hitting the hole the highest, since it will get us the full $3$ points we're after. In this case, the clear move is to send the **aggressive** thrower to the line since 

$$
p_\text{agg}(3) = \max\{p_\text{agg}(3),\, p_\text{cons}(3),\, p_\text{wasted}(3)\}
$$

Likewise, if we have

- $2$ points then the best move is whatever makes the probability of hitting the board the highest, so we send the **conservative** thrower to the line.
- $3$ points then we can only spoil our win by scoring another point, so we send the **wasted** thrower to the line.
- $1$ point then there is absolutely no chance to win the game, so the best move doesn't matter, we can only lose no matter what we do, and we will.

### The choice

In the first case, the best choice we can make has probability $p_\text{agg}(3) = \frac{4}{10}$ of ending the game with $3$ more points, so the expected value of taking the aggressive shot is $p_\text{agg}(3)\times 1 = \frac{4}{10}.$ 

Had we taken the **conservative** shot, the expected value of the shot would be $\frac{1}{10},$ and $0$ had we taken the **wasted** shot.

Likewise, the best choice in the second case has an expected value of $p_\text{cons}(1) \times 1 = \frac{8}{10},$ and the best move in the third case yields $p_\text{waste}(0) \times 1 = 1.$ As we said before, there is no chance to win in the fourth scenario so its expected value is just zero.

### What have we done

The logic here is that we looked at all of the options before us, found how much value we expect them to provide, and then chose the option with the highest value. 

We found that with $S = 2$ total accumulated points, and $T = 1$ turn remaining, the expected value of our position is $\frac{4}{10}.$ In other words, $V(2,1) = \frac{4}{10}.$ 

If we ever find ourselves in those scenarios again, i.e. one turn remaining with $0, 1, 2$ or $3$ points accumulated, the optimal choices will be as we just found them, and their expected value will be $V(s,1)$. So, if we find ourself in those positions again, we should make those same decisions. 

$$
\begin{array}{|c|c|c|} \hline
\textbf{Scenario} & \textbf{Decision} & \textbf{Value} \\ \hline
S=0, T=1 & \text{aggressive} & V(0,1) = 0.4 \\ \hline
S=1, T=1 & \text{N/A} & V(1,1) = 0.0 \\ \hline
S=2, T=1 & \text{conservative} & V(2,1) = 0.8 \\ \hline
S=3, T=1 & \text{wasted} & V(3,1) = 1.0 \\ \hline
\end{array}
$$

### Another choice

We can build on this logic to find the best decision when we have $2$ throws left.

Whatever happens on our second to last throw, we can't finish the game (unless we get to $s \geq 4$). Instead, we'll arrive at one of the positions we just calculated: $V(0,1),\, V(1,1),\, V(2,1),\,$ or $V(3,1).$ 

So, we should choose the move that maximizes the expected value of our next position. After all, this is the best move we have available to us with $2$ moves left, and we can calculate it since already know the best moves available to us with $1$ move left. 

Suppose, for example, we're calculating $V(0,2).$ 

If we use the aggressive coin, then we can move into 

- the state $V(3,1)$ with probability $p_\text{agg}(3),$ 
- the state $V(1,1)$ with probability $p_\text{agg}(1),$ or 
- the state $V(0,1)$ with probability $p_\text{agg}(0).$ 
- 
- In all, using the aggressive coin in this situation has an expected value of 

$$
\begin{align}
\langle V(0,2)\rangle_\text{agg} &= p_\text{agg}(3)\times V(3,1) + p_\text{agg}(1)\times V(1,1) + p_\text{agg}(0)\times V(0,1) \\
&= \frac{4}{10}\times 1 + \frac{3}{10}\times 0 + \frac{3}{10}\times 0.4 \\
&= 0.52
\end{align}
$$

Calculating in the same way, we get $\langle V(0,2)\rangle_\text{cons} = 0.14$ and $\langle V(0,2)\rangle_\text{wasted} = 0.0.$ So, the expected value of the position $V(0,2)$ is

$$
\begin{align}
\langle V(0,2)\rangle &= \max_a\sum_{\delta s}P_a(\Delta s)V(0+\Delta s,1) \\
&= \max_a\langle V(0+\Delta s, 1)\rangle_a \\
&= \langle V(0,2)\rangle_\text{agg} \\
&= 0.52
\end{align}
$$

### All the way

We can follow this same approach back in time as far as we would like. At each stage, our calculation depends on values $V(i,j)$ that we found in the round before, meaning that, at most, we have $(S+1)\times(T+1)$ items to calculate.

In general, if we have $s$ accumulated points, and $t$ turns remaining, then the value of our position is 

$$
V(s,t) = \max_a\langle V(s+\Delta s, t-1)\rangle_a \\
$$

### Computing

Translating this into Python, we have 

```python
from functools import lru_cache

Pthrower = {
          'aggressive'   : {3 : 0.4, 1 : 0.3, 0 : 0.3}
        , 'conservative' : {3 : 0.1, 1 : 0.8, 0 : 0.1}
        , 'wasted'       : {3 : 0.0, 1 : 0.0, 0 : 1.0}
    }
    
def EV(S, T, thrower):
    return sum(prob * V(S + k, T - 1) for k, prob in Pthrower[thrower].items())
    
@lru_cache(maxsize=10000)
def V(S, T):
    if (S, T) == (3, 0):
        return 1
    elif T == 0 and S != 3:
        return 0
    else:
        return max(EV(S, T, thrower) for thrower in Pthrower.keys())
```

which gets $V(0,4) = 0.8548$

<br>
