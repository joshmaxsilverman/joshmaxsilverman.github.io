---
layout: post
published: true
title: Antipersistent Basketball
subtitle: Who will win if nobody cares until they're losing?
tags: coarse-graining scaling symmetry
date: 2022/05/01
---

>Question

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/who-wins-a-very-boring-basketball-game/))

## Solution

<!-- - intuition for the winner
- the moves // reducing to volleys // master equation
- big picture // tail intuition // assumptions // symmetries (P2 <> P-2, P2 <> P4)
- solving the center // symmetry
  - plot theory <> experiment
 -->
 
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

following the same sort of reasoning, the rates to and from $g=-2$ are $\frac12\times\frac12$ and $r_+\times\frac12,$ respectively.

so, in the wings the game looks like:

[drawing of the wings]

and near the origin, the structure of the game is:

[drawing near the origin]

### The big picture

we can build intuition about the dynamics by inspecting the diagrams. 

- because score gaps incentivize the underdog and relax the leader, the game feels pressure to stay near the origin. this tells us that the distribution will have thin tails and, also, that the distribution will quickly **become constant in time**. 

- comparing either side, the wings have identical structure so, up to an overall constant, we expect the distributions to be symmetric, e.g. $P(-2) = \gamma P(2),$ $P(-4) = \gamma P(4),$ and as a result, $S_- = \gamma \times S_+.$

- as we move away from the origin the game looks the same, whatever the score — each step sees the same transition rate imbalance, $r_-^2/r_+^2 < 1,$ so we expect the probability to decay like some decreasing function $f(r_-^2/r_+^2).$

with these insights on the table, we can analyze the equations for concrete results, starting with the wings.

if the probability of a score gap of $g$ after round $(t-1)$ is $P_{t-1}(g),$ its change after another round is

$$
  \Delta = P(g+2)_{t-1}r_-^2 + P(g-2)_{t-1}r_+^2 - (r_+^2 + r_-^2)P_{t-1}(g)
$$

we argued above that the games become constant in time. applying the equilibrium condition gets:

$$
  0 = P(g+2)r_-^2 + P(g-2)r_+^2 - (r_+^2 + r_-^2)P(g)
$$

this two-step recursion is really a one step recursion in disguise. we can see that from the slight rearrangement:

$$ 
  0 = r_-^2\left[P(g+2) - P(g)\right] - r_+^2\left[P(g) - P(g-2)\right]
$$

we can factor this using a shift operator $\mathbb{E}_g,$ (that acts on functions of $g$ like $\mathbb{E}_g f(g) = f(g+1)$) it becomes

$$
  0 = \left(\mathbb{E}_g-1\right)\left[r_-^2P(g) - r_+^2P(g-1)\right]
$$

or

$$
  \boxed{P(g) = \left(\frac{r_-}{r_+}\right)^2 P(g-2)}
$$

which is what we intuited above.

this immediately gets us $S_-.$ since $S_- = P(-2) + P(-4) + \ldots,$

$$
  \boxed{
  \begin{align}
  S_- &= P(-2)\left[1 + \frac{r_-^2}{r_+^2} + \left(\frac{r_-^2}{r_+^2}\right)^2 + \ldots\right] \\
      &= \dfrac{P(-2)}{1-r_-^2/r_+^2}
  \end{align}
  }
$$

similarly, 

$$
  \boxed{S_+ = \dfrac{P(2)}{1-r_-^2/r_+^2}.}
$$

now we can analyze $P(-2).$ following the diagram, the change in $P(-2)$ from one moment to the next is

$$
  \begin{align}
  \Delta &= \frac{1}{2^2} P(0) + r_+^2 P(-4) - \left(\frac12 r_+ + r_-^2\right)P(-2) \\
  &= 0
  \end{align}
$$

using the one-step recursion, this becomes

$$ 
  \boxed{P(-2) = \dfrac{P(0)}{2r_+}}
$$

the same analysis for $P(2)$ gets

$$
  P(2)\left[1 - r_-^2 -2r_-r_+\right] = \frac12 r_- P(0)
$$

here we can use the fact that $r_- + r_+ = 1$ to get $r_-^2 + r_+^2 + 2r_-r_+ = 1,$ so that the above becomes 

$$
  \boxed{P(2) = \dfrac{r_-}{2r_+^2} P(0)}.
$$

now we can solve for $P(0):$ 

$$
  \begin{align}
    1 &= P_0 + S_- + S_+ \\
      &= P_0 + \dfrac{P(-2)}{1 - \left(r_-/r_+\right)^2} + \dfrac{P(2)}{1 - \left(r_-/r_+\right)^2} \\
      &= P_0\left(1 + \dfrac{1}{2r_+}\dfrac{r_+^2}{r_+^2 - r_-^2} + \dfrac{r_-}{2r_+^2}\dfrac{r_+^2}{r_+^2 - r_-^2}\right)P(0) \\
      &= P_0\left(1 + \frac12 \dfrac{r_+ + r_-}{r_+^2 - r_-^2}\right) \\
      &= P_0\left(1 + \frac12 \dfrac{1}{r_+ - r_-}\right)
  \end{align}
$$

or

$$
  \boxed{P_0 = \dfrac{4x}{1+4x}}
$$

we're told that $P_0 = \frac12,$ so $x$ must be $\frac14.$

using the relationship between $P(-2)$ and $P(0),$ we get

$$
  \begin{align}
    S_- &= P(-2)\frac{r_+^2}{r_+^2 - r_-^2} \\
        &= \frac{P(0)}{2r_+} \frac{r_+^2}{r_+^2 - r_-^2} \\
        &= \frac12 P(0)\frac{r_+}{r_+ - r_-} \\
        &= \frac{4x}{1+4x}\frac12 \frac{\frac12 + x}{2x} \\
        &= \frac{1 + 2x}{2 + 8x}.
  \end{align}
$$

the same calculation for $S_+$ gets $(1-2x)/(2 + 8x).$

this result makes sense — when $x=0,$ there is no built in advantage to going first, and the game has even odds. likewise, when $x=\frac12,$ every point scored by the Firsts is matched by the Seconds, so the Firsts can never have a lead, they can only tie.

comparing $S_-$ and $S_+$ we see that $S_-/S_+ = \frac{1+2x}{1-2x},$ which is $3$ for $x = 1/2.$ 

so, given that the game wasn't a tie, there's a $75%$ chance the Seconds won the game. 

from these ingredients, we can get the steady state distribution of score gaps $P(g),$

$$
  P(g) = 
  \begin{cases}
    \frac{4x}{1+4x}\frac{1}{1 + 2x}\left(\dfrac{\frac12 - x}{\frac12 + x}\right)^{-2(g+1)} & g < 0 \\
    \frac{4x}{1+4x} & g = 0 \\
    \frac{4x}{1+4x}\frac{1}{1+2x}\left(\dfrac{\frac12 - x}{\frac12 + x}\right)^{2(g-1)} & g > 0
  \end{cases}
$$

<br>
