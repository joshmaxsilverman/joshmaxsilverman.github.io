---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>**Question**: Great news! The variety of robotic competition continues to grow at breakneck pace! Most recently, head-to-head long jump contests have been all the rage.
>
>These contests consist of rounds in which each robot has a single attempt to score. In an attempt, a robot speeds down the running track (modeled as the numberline) from $0,$ the starting line, to $1,$ the takeoff point. A robot moves along this track by drawing a real number uniformly from $\left[0,1\right]$ and adding it to the robot’s current position. After each of these advances, the robot must decide whether to jump or wait. If a robot crosses the takeoff point (at $1$) before jumping its attempt receives a score of $0.$ If the robot jumps before crossing $1,$ it draws one final real number from $\left[0,1\right]$ and adds it to its current position, and this final sum is the score of the attempt.
>
>In a head-to-head contest, the two robots each have a single attempt without knowing the other’s result. In the case that they tie (typically because they both scored $0$), that round is discarded and a new round begins. As soon as one robot scores higher than the other on the same round, that robot is declared the winner!
>
>Assume both robots are programmed to optimize their probability of winning and are aware of each other’s strategies. You are just sitting down to watch a match’s very first attempt (of the first round, which may or may not end up being discarded). What is the probability that this attempt scores $0$? Give this probability as a decimal rounded to $9$ digits past the decimal point.

<!--more-->

([FiveThirtyEight](https://www.janestreet.com/puzzles/current-puzzle/))

## Solution

the jumper's decision can't depend on anything but their current position since that's all the information they have.

so, each jumper's strategy takes the form
- if current position $z$ is less than a threshold $t$, take another step
- if $z\geq t$, take the jump

each player advances down the track, step by step, until they pass $t.$ the biggest $t$ that should be considered is $1,$ or else they'll always score zero. since the steps are uniform draws from zero to $1,$ the greatest realizable score, regardless of $t,$ is $2$ (the first step can land at $z=1$, and a jump of $1$ from there would land at $2$).

player $b$ wins if, eventually, they score higher than player $a.$ this can happen if

- both players don't score in the present round, and player $b$ goes on to win later, or
- player $b$ scores in the present round, but player $a$ does not.
- both players score in the present round and $s_b > s_a$,



calling the probability to not score with threshold $t$, $P_\text{zero}(t),$ and the probability of getting score $s$ given that they use threshold $t$ and given that they score $P_\text{score}(s, t),$ this means

$$ 
  P(b\ \text{wins}|t_a, t_b) = P_\text{zero}(t_a)P_\text{zero}(t_b)P(b\ \text{wins}|t_a, t_b) + P_\text{zero}(t_a)(1-P_\text{zero}(t_b)) + 
  \int\limits_{t_a}^2 \text{d}s_a\, \int\limits_{s_a}^{2} \text{d}s_b\, P_\text{score}(s_a|t_a)P_\text{score}(s_b|t_b),
$$

or after solving for $P(b\ \text{wins})|t_a, t_b)$,

$$ P(b\ \text{wins}|t_a, t_b) = \dfrac{P_\text{zero}(t_a)(1-P_\text{zero}(t_b)) + 
  \int\limits_{t_a}^2 \text{d}s_a\, \int\limits_{s_a}^{2} \text{d}s_b\, P_\text{score}(s_a|t_a)P_\text{score}(s_b|t_b)}{1 - P_\text{zero}(t_a)P_\text{zero}(t_b)}.
$$

the chance to win, $P(b\ \text{wins}|t_a, t_b)$ depends on both their thresholds. 

strategically, player $b$ should set $t_b$ so that $P(b\ \text{wins})$ has the greatest minimum with respect to $t_a.$ the same is true in the other direction. 

the game is symmetric for both players, so both players will pick the same $t=t_a=t_b$ so it suffices to find $t_b$ where

$$ \dfrac{\partial P(b\ \text{wins}|t_a,t_b)}{\partial t_b}\Bigr|_{t_a=t_b} = 0. $$

<!-- the game is symmetric for both players, so both players will pick the same $t=t_a=t_b.$ strategically, player $b$ should set $t_b$ so that $P(b\ \text{wins}|t_a, t_b)$ is maximal with respect to $t_b,$ and minimal with respect to $t_a.$ -->


<br>
