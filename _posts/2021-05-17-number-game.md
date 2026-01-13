---
layout: post
published: true
title: Survivor
date: 2021/05/17
subtitle: Who survives the race-to-20 counting game?
source: fivethirtyeight
theme: games-logic
---

>**Question**: Players A, B, C, and D are playing a game which starts with A saying the number $1.$ From that point on, each player says a number between $1$ and $4$ greater than the number spoken by the preceding player. The player who says $20$ wins the round, the player after them is removed from the game, the player after them starts the next round. Any other players survive to the next round. Each player's top aim is to win the whole game but, if they realize that's impossible, they'll prioritize surviving to the next round. Who will survive the $4$ players game?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/are-you-smarter-than-a-fourth-grader/))

## Solution

In the forward direction, this is a tricky game. Ostensibly, I have to account for the possible choices of my opponents, which in most cases number $4.$ 

But in the backward direction, the fog evaporates. If the goal is to win the game, then there is no freedom in decisions. In fact, there is no freedom at all. Unless a player happens to start in the right position, there is no possibility to win.

## Winning the game

Suppose we want to win the game, i.e. be the player who says $"20"$ in the last round. What should we do?

Let's figure out our strategy throughout the game. We should keep track of what the current minimum number is, what number we will say given the current minimum, and what outcome we'll achieve. 

First, if the $\text{Start}$ is $19,$ then we will just say $20$ and win the game. The same is true when $\text{Start}$ is $16,$ $17,$ or $18.$ If we find ourselves in any of these positions, then we will win the game. 

By extension, if our $\text{Start}$ is $15$ then we are guaranteed to lose the game. We can only say a number that's $1,$ $2,$ $3,$ or $4$ more than $15,$ all of which would give the following player the opportunity to say $20.$ 

### Traps all the way down

After this, the same dynamic repeats. If we can force our opponent to start with $15,$ then they are guaranteed to lose. The same goes with $10$ and $5.$ So, whenever we have a choice in the matter, we should say the next reachable multiple of $5$ which forces the other player to start there. Putting the strategy to a table, we've got:

$$
\text{Round Three} \\
\begin{array}{|c|c|c|}\hline
\text{Start} & \text{Say} & \text{Outcome} \\ \hline
16 \rightarrow 19 & 20 & \text{Win} \\
15 & \text{doesn't matter} & \text{Lose} \\
11 \rightarrow 14 & 15 & \text{Win} \\
10 & \text{doesn't matter} & \text{Lose} \\
6 \rightarrow 9 & 10 & \text{Win} \\
5 & \text{doesn't matter} & \text{Lose} \\
1 \rightarrow 4 & 5 & \text{Win} \\
0 & 1 & \text{Lose} \\ \hline
\end{array}
$$

Working backward through the decision making, we see that the person to go second will win. 

## Second round

In the second round, our goal should be to position ourselves to start the final round second. Since there are just three people in the second round, that actually corresponds to winning the second round outright. 

As before, the same strategy applies. Whoever says $20$ will win, so the table starts off in the same fashion. However, the player behind the winner will also survive the second round. Therefore, anyone with $\text{Start}$ in the range $12 \rightarrow 15$ is incentivized to start the next player in a winning position (i.e. a position between $16$ and $19$). Whoever has $\text{Start}$ as $11$ is doomed to lose the round. This pattern repeats, so that $2$ is the next losing position. 

$$
\text{Round Two} \\
\begin{array}{|c|c|c|}\hline
\text{Start} & \text{Say} & \text{Outcome} \\ \hline
16 \rightarrow 19 & 20 & \text{Win} \\
12 \rightarrow 15 & 16 & \text{Survive} \\
11 & \text{doesn't matter} & \text{Lose} \\
7 \rightarrow 10 & 11 & \text{Win} \\
3 \rightarrow 6 & 7 & \text{Survive} \\
2 & \text{doesn't matter} & \text{Lose} \\
1 & 2 & \text{Win} \\
0 & 1 & \text{Survive} \\ \hline
\end{array}
$$

Again, this shows that the person who starts second will win the round (and, based on the analysis of the final roudn, the game). We still don't know which player will win, but we know that it's whoever goes second in the second round.

## First round

This is where the strategy gets interesting.

The goal of the first round is not to win the first round — it's to position oneself to go second in the second round.

Say the $4$ players are $P^\prime,$ $P^{\prime\prime},$ $P^{\prime\prime\prime},$ and $P^{\prime\prime\prime\prime}.$ If $P^\prime$ wins the first round, then $P^{\prime\prime}$ is eliminated, $P^{\prime\prime\prime}$ goes first in the next round, and $P^{\prime\prime\prime\prime}$ starts the next round second. So, the strategy in the first round is to make sure that the person in front of you wins.

Reasoning backward, if we do find ourselves with a $\text{Start}$ of $19$ then we don't have any choice but to win.

But if $\text{Start}$ is $15$ through $18,$ then we can ensure that the player after us wins the first round by saying $19.$

Someone with $\text{Start}$ between $11$ and $14$ can't win the round, and they can't  but they can survive by ensuring the the person in front of them has the opportunity to ensure that the person in front of _them_ survives. 

Following this logic back to the beginning, a $\text{Start}$ of $10$ will have no choice but to lose the round, and a $\text{Start}$ of $9$ will say $10$ to ensure their own survivalby winning the round (but losing the game). However, anyone within striking distance of forcing a $\text{Start}$ of $9$ will do it. From there, the dynamics of the end of the game repeat.

$$
\text{Round One} \\
\begin{array}{|c|c|c|}\hline
\text{Start} & \text{Say} & \text{Outcome} \\ \hline
19 & 20 & \text{Win round} \\
15 \rightarrow 18 & 19 & \text{Survive round, Win game} \\
11 \rightarrow 14 & 15 & \text{Survive round} \\
10 & 11 & \text{Lose} \\
9 & 10 & \text{Win round} \\
5 \rightarrow 8 & 9 & \text{Survive round, Win game} \\
1 \rightarrow 4 & 5 & \text{Survive round} \\
0 & 1 & \text{Lose} \\ \hline
\end{array}
$$

So, whoever goes third in the first round will win the whole game, i.e. **Player C**.


<br>
