layout: post
published: true
title: Hammer golf
date: 2025/04/21
subtitle: Live by the hammer, die by the hammer.
tags: game-theory recursive-games strategy
---

>**Question**: Here’s a puzzle that’s inspired by one of the rules from TGL golf:
>
>You and your opponent are competing in a golf match. On any given hole you play, each of you has a $50$ percent chance of winning the hole (and a zero percent chance of tying). That said, scorekeeping in this match is a little different from the norm.
>
>Each hole is worth $1$ point. Before starting each hole, either you or your opponent can “throw the hammer.” When the hammer has been thrown, whoever did not throw the hammer must either accept the hammer or reject it. If they accept the hammer, the hole is worth $2$ points. If they reject the hammer, they concede the hole and its $1$ point to their opponent. Both players can throw the hammer on as many holes as they wish. (Should both players decide to throw the hammer at the exact same time—something that can’t be planned in advance—the hole is worth $2$ points.)
>
>The first player to reach $3$ points wins the match. Suppose all players always make rational decisions to maximize their own chances of winning.
>
>Good news! You have won the first hole, and now lead $1-0.$ What is your probability of winning the match?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-throw-the-hammer))

## Solution

On each turn, we need to decide whether to throw the hammer.

First, let's set the convention for valuing the end states of the game. If Player A wins, then the game is worth $1,$ and if Player B wins then the game is worth $0.$ Therefore, Player A will be trying to maximize the value of the end state while Player B will be trying to minimize it.

If Player A throws the hammer, Player B will get a choice between accepting or rejecting it, and they'll pick whichever option gives the end state the least expected value. That means Player A should only throw the hammer if the minimum value possible by hammer is greater than the value of playing a normal $1$-pt hole.

Likewise, Player B will choose to throw the hammer if the maximum possible value of Player A rejecting or accepting is less than the value of playing a normal $1$-pt hole.

If neither of these result, then the players will play a normal hole. If both of them result, the players will play a $2$-pt hole.

Putting this logic to code, we have

```python
def V(score_A, score_B):
  
  if score_A >= TARGET_SCORE:
    return 1

  if score_B >= TARGET_SCORE:
    return 0

  A_rejects = V(score_A, score_B + 1)
  B_rejects = V(score_A + 1, score_B)
  accept = 1/2 * ( V(score_A + 2, score_B) + V(score_A, score_B + 2) )
  normal = 1/2 * ( V(score_A + 1, score_B) + V(score_A, score_B + 1) )

  A_throws = min(B_rejects, accept) > normal
  B_throws = max(A_rejects, accept) < normal

  if A_throws and B_throws:
    return accept

  if A_throws:
    return min(B_rejects, accept)

  if B_throws:
    return max(A_rejects, accept)

  else:
    return normal

```

Running the function shows that a $1$-pt advantage to start the game gives a $3/4 = 75\%$ chance to win when the target score if $3$, and a $11/16 = 68.75\%$ chance to win when the target is $5.$ As the target score grows, the initial advantage is less consequential. Curiously, when the target score is even, there is no advantage. The reason is essentially that the person leading and the person trailing require the same number of $2$-pt shots to make it to the target. 

With a score gap of $1$, the up player is not incentivized to throw the hammer. If they don't, the worst that can happen is the game ends up tied. If they do, the other player will accept the hammer, since they don't want the certain chance to fall into a deeper hole. 

On the other hand, the down player will elect to throw the hammer since it either ties them or puts them ahead. The lead player will accept.

This means that with a $1$-pt gap, the lead and trail player are locked into a series of $2$-pt games which means they have the same number of holes to win to win the game and, so, the odds are even.

The results for setting the target score up to $15$ are:

$$
\begin{array}{|c|c|} \hline
 \text{Target score} & V(1,0) \\ \hline
 1 & 1 \\
 2 & \frac12 \\
 3 & \frac34 = 0.75 \\
 4 & \frac12 \\
 5 & \frac{11}{16} \approx 68.8\% \\
 6 & \frac12 \\
 7 & \frac{21}{32} \approx 65.6\% \\
 8 & \frac12 \\
 9 & \frac{163}{256} \approx 63.7\% \\
 10 & \frac12 \\
 11 & \frac{319}{512} \approx 62.3\% \\
 12 & \frac12 \\
 13 & \frac{1255}{2048} \approx 61.3\% \\
 14 & \frac12 \\
 15 & \frac{2477}{4096} \approx 60.5\% \\ \hline
\end{array}
$$
