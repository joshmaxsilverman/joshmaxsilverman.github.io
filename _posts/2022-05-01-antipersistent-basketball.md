---
layout: post
published: false
title: Antipersistent Basketball
date: 2018/04/21
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

- intuition for the winner
- the moves // reducing to volleys // master equation
- big picture // tail intuition // assumptions // symmetries (P2 <> P-2, P2 <> P4)
- solving the center // symmetry
  - plot theory <> experiment

### Who is going to win?

first, let's figure out which side has the natural advantage — is it the team that goes first or the one that goes second? 

once either team gets a two basket lead, the game is symmetric. but when the game is close, things get interesting.

after one possession, the nicks can be ahead if they score a basket at even odds, followed by the noughts missing their basket at less than even odds. the noughts can be up after one possession if the nicks miss at even odds, followed by the noughts scoring at even odds. advantage noughts: $\text{unlikely}\times\text{even odds} < \text{even odds}\times\text{even odds}.$ $\frac12r_{-} < \frac12\times\frac12$

this advantage is compounded on the next possession. if the nicks are up 2, the game can return to a tie if the nicks miss (better than even odds, since they're ahead), and then the noughts make (better than even odds, since they're underdogs). on the other hand, the noughts lose their lead if the nicks (better than even odds), followed by the noughts missing (even odds). advantage noughts: $\text{likely}\times\text{likely} > \text{even odds}\times\text{likely}.$ $r_{+}\times r_{+} > \frac12 r_{+}.$

all in all, the team that goes second will win a greater fraction of games.

### The setup

the game alternates turns between the Firsts and the Seconds. on first read, it may seem like we need to model things that way. but it's simpler to zoom out and think about pairs of turns, or "rounds". this way, at the end of each round, the game can move one step to the left, stay put, or move one step to the right. 

this gives us a board like:

[drawing of a board with no rates]

the probability of a tie is equal to $P(\text{tie}).$ the first player wins if the game ends anywhere to the right of the origin, so the probability that the first player wins is equal to 

$$
  S_+ = \sum_{n=i}^{100} P(n)
$$

in the same way, the probability that the second player wins is 

$$
  S_- = \sum_{n=-1}^{-100} P(n)
$$

away from the origin, the transition rates are simple. for the game to move away from the origin in a turn, the person with disadvantage has to make their shot followed by a miss from the person with advantage. this has probability 

$$ 
  r_-(1-r_+) = r_-^2.
$$

similarly, for the game to move back toward tied, the person with disadvantage needs to miss their shot, followed by a make from the person with advantage. this has probability

$$
  r_+(1-r_-) = r_+^2.
$$

this symmetry is broken near the origin, which is what gives the problem its structure.

from a tie, we can move to $g = 2$ if the Firsts make their shot, follower by a miss from the advantaged Seconds. because the game is tied when the Firsts shoot, the probability of a make is $\frac12.$ the probability of the Second's miss is $(1-r_+) = r_-.$ so, the overall probability is $\frac12 r_-.$

the game can move back from $g = 2$ to a tie if the disadvantaged Firsts miss followed by a make by the advantaged Seconds. so, the probability is $r_+^2.$

following the same sort of reasoning, the rates to and from $g=-2$ are $\frac12\times\frac12$ and $\frac r_+\times\frac12,$ respectively.

so, in the wings the game looks like:

[drawing of the wings]

and near the origin, the structure of the game is:

[drawing near the origin]

<br>
