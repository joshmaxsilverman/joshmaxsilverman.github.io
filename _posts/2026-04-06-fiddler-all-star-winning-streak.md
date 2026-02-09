---
layout: post
published: true
hide_from_recent: true
title: All star winning streaks
date: 2026/02/06
subtitle: What would be an impressive win streak in a hypothetical new all star game format?
source: fiddler
kind: puzzle
theme: probability
tags: linearity-of-expectation
---

>**Question**: The Fiddler Basketball Association’s All-Star Game consists of two teams: “East” and “West.” Every year these two teams play a game, each with a $50$ percent chance of winning that’s independent of the outcomes of previous years.
>
>Many, many years into the future, you look at the most recent results of the All-Star Game. On average, what is the longest current winning streak that one of the teams is on? (Here, having won only the most recent game still counts as a “streak” of one game.)
>
>**Extra credit**
>
>To spice up the All-Star Game, the commissioner of the FBA has decided that there will now be three teams competing in All-Star Games: “Stars,” “Stripes,” and “International.” Each year, two of the three teams play each other. If one year has Stars vs. Stripes, the next year has Stripes vs. International, the year after that has International vs. Stars, and then the cycle repeats with Stars vs. Stripes.
>
>Many, many years after this new format has been adopted, you look at the most recent results of the All-Star game. On average, what is the longest current winning streak that one of the teams is on? (As before, having won one game counts as a “streak.” Also, note that the team with the longest winning streak might not be one of the two teams that played in the most recent All-Star Game.)

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/how-long-is-the-all-star-streak))

## Solution

The two player game is a special case of the three player game, so we'll do three first.

### Three player game

Since we're deep in the game, the current game has no dependence on the initial conditions. 

If the maximum active streak is $2$ or more, then the leader is unique. That's because the only win the other two players can have is from playing each other, before immediately losing to the leader. So, when the leader is steamrolling, the other two can't "catch up" and we can focus on the leader extending their own streak.

For the leader to have a streak of $2$ or more, they need to have won their last two games. Any of the three players can be the leader, so ${P(S\geq 1) = 3\cdot\frac12\cdot\frac12 = \frac34.}$ Likewise, the chance that the maximum active streak is $1$ is ${\left(1-\frac34\right) = \frac14.}$

The expected number of additional wins for the leader (beyond $2$) is

$$ 
    \begin{align}
        W &= \frac12\cdot 0 + \frac12\cdot(1 + W) \\
          &= 1.
    \end{align}
$$

So, the expected maximum active streak is 

$$
    \begin{align}
        \langle S\rangle  &= \frac14\cdot 1 + \frac34\cdot(2+1) \\
        &= \frac52.
    \end{align} 
$$

This closely matches a $N=100,000$ trial simulation which got $2.49729.$

```mathematica
trial3[] := (
  {s1, s2, s3} = {0, 0, 0};
  Do[
   If[Mod[j, 3] == 1,
    If[RandomReal[] > 1/2, s1 += 1; s2 = 0, s1 = 0; s2 += 1];
    ];
   If[Mod[j, 3] == 2,
    If[RandomReal[] > 1/2, s2 += 1; s3 = 0, s2 = 0; s3 += 1];
    ];
   If[Mod[j, 3] == 0,
    If[RandomReal[] > 1/2, s3 += 1; s1 = 0, s3 = 0; s1 += 1];
    ];
   , {j, 1, 5000}
   ];
  Return[{s1, s2, s3}]
  )

answer = Mean@ParallelTable[Median@trial3[], {j, 1, 100000}]
```

From the calculation above, we can extract the distribution which is $1/4$ for $S=1$ and $3/4\times 1/2^{S-1}$ for $S\geq 2$ (prediction in gold, simulation in blue)

![](/img/2026-02-09-fiddler-all-star-winning-streak-histogram.png){:width="600 px" class="image-centered"}

### Two player game

The current leader has at least $1$ game won and they're expected to win $1$ more, so ${\langle S \rangle = 1 + 1 = 2.}$

<br>

<!-- 

The matchups go $(A,B),$ $(B,C),$ $(C,A)$ in sequence. Since we're deep in the sequence, we're equally likely to be in one of these matchups, and $A,$ $B,$ and $C$ are equally likely to be one of the current streak leaders.

Suppose $A$ currently has the maximum streak, $S$ (possibly tied with another player).

- (`A-|A`) if $A$ didn't play in the last game, then the other two teams have streaks of $0$ and $1,$ and $A$ will play one of them in the next game at random.
- (`-A|A`) if $A$ played in the last game but not the one before it, then $A$ is about to play a team with a streak of $0$ or $1$ (depending on if they won the game 2 games ago) at random. 
- (`AA|-`) if $A$ played in the last game and the one before it then they won the last game and may have won the one before it. If they won both, then neither team can improves on $S$ in the next game. If they won just the second one, then both them and the other team has $1$ game winning streak.

$$ \frac23\frac12((S+1)+(1+2)) + \frac13(\frac12S+\frac12(1+2)). $$

- if $A$ didn't play in the last game played, then one of the other teams has a streak of $1$ and the other has a streak of $0,$ making the setup is $(S,1,0).$ $A$ will play one of them in the next game.
- if $A$ played in the last game and the game before it, then both other teams have a streak of $0,$ making the setup $(S,0,0).$ They will play each other in the next game, and $S$ will remain in the lead.
- if $A$ played in the last game, but not the one before it, then one of the teams has a streak of $0,$ and the other one has a streak of $0$ or $1$ with $50\%$ odds, making the setup $\frac12(S,1,0) + \frac12(S,0,0).$ $A$ will play one of them in the next game. 

The game is equally likely to be in one of these situations, so the expected maximum streak is

$$
    \begin{align} 
        S &= \frac13\left(\frac12(S+1) + \frac12(1+1)\right) + \frac13\left(\frac12(S+1) + \frac12(0+1)\right) + \frac13 S. \\
        &= \frac{4S + 5}{6} \\
        &= \frac52.
    \end{align}
$$

In the next match, $2/3^\text{rds}$ of the time A will play. If $A$ wins, then the current maximum streak goes up by $1.$ If they lose, then the current high streak becomes $1$ or $2$ with equal likelihood. $1/3^\text{rd}$ of the time, B plays C and the current maximum streak will not change, regardless of who wins.


<br>


<!-- The matchups go $(A,B),$ $(B,C),$ $(C,A)$ in sequence. Since we're deep in the sequence, we're equally likely to be in one of these matchups, and $A,$ $B,$ and $C$ are equally likely to be the current streak leader.

Suppose $A$ currently has the maximum streak, $S$ (possibly tied with another player).

- if $A$ didn't play in the last game played, then one of the other teams has a streak of $1$ and the other has a streak of $0,$ making the setup $(S,1,0).$ $A$ will play one of them in the next game.
- if $A$ played in the last game and the game before it, then both other teams have a streak of $0,$ making the setup $(S,0,0).$ They will play each other in the next game, and $S$ will remain in the lead.
- if $A$ played in the last game, but not the one before it, then one of the teams has a streak of $0,$ and the other one has a streak of $0$ or $1$ with $50\%$ odds, making the setup $\frac12(S,1,0) + \frac12(S,0,0).$ $A$ will play one of them in the next game. 

The game is equally likely to be in one of these situations, so the expected maximum streak is

$$
    \begin{align} 
        S &= \frac23\left[\frac12(S+1) + \frac12\left(\frac12\cdot 0 + \frac12\cdot 1+1\right)\right] + \frac13 S. \\
        &= \frac{4S + 5}{6} \\
        &= \frac52.
    \end{align}
$$

<!-- In the next match, $2/3^\text{rds}$ of the time A will play. If $A$ wins, then the current maximum streak goes up by $1.$ If they lose, then the current high streak becomes $1$ or $2$ with equal likelihood. $1/3^\text{rd}$ of the time, B plays C and the current maximum streak will not change, regardless of who wins. -->
