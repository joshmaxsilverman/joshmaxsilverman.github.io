---
layout: post
published: true
title: Robot Tug of War
date: 2021/08/28
---

>**Question**: The Robot Weightlifting World Championship was such a huge success that the organizers have hired you to help design its sequel: a Robot Tug-of-War Competition!
>
>In each one-on-one matchup, two robots are tied together with a rope. The center of the rope has a marker that begins above position 0 on the ground. The robots then alternate pulling on the rope. The first robot pulls in the positive direction towards 1; the second robot pulls in the negative direction towards $-1.$ Each pull moves the marker a uniformly random draw from $\left[0,1\right]$ towards the pulling robot. If the marker first leaves the interval $\left[-\frac12,\frac12\right]$ past $\frac12,$ the first robot wins. If instead it first leaves the interval past $-\frac12,$ the second robot wins.
>
>However, the organizers quickly noticed that the robot going second is at a disadvantage. They want to handicap the first robot by changing the initial position of the marker on the rope to be at some negative real number. Your job is to compute the position of the marker that makes each matchup a $50:50$ competition between the robots. Find this position to seven significant digits—the integrity of the Robot Tug-of-War Competition hangs in the balance!

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/current-puzzle/))

## Solution

First, let's get acquainted with the setup. 

![](/img/2021-08-28-tug-of-war-diagram.png){:width="450 px" class="image-centered"}

Each robot pulls the middle of the rope toward their side a random distance between $0$ and $1.$ If the first player gets it past $\frac12,$ then they win (and likewise for Player 2). 

<!-- This means that each player has the potential to end the game in one turn (since $\frac12 - \left(-\frac12\right) = 1$).  -->

If it's Player 1's turn, they can win the game in one of two ways:

1. they can immediately move the game past $+\frac12,$ or
2. they can move somewhere less than $\frac12,$ and then go on to win.

For the second way to happen, Player 1's first move will have to go somewhere to the right that's less then $\frac12,$ then Player 2 will have to move somewhere to the left that's more than $-\frac12,$ and then go on to win. 

$$
P_\text{win}(x) = P(\text{win immediately}) + P(\text{win eventually}).
$$

If they win immediately, Player 1 has to move beyond $\frac12$ which has probability $1 - (\frac12 - x),$ so

$$
P(\text{win immediately}) = \frac12 + x.
$$

If they win eventually, Player 1 has to move somewhere less then $\frac12,$ then Player 2 has to move somewhere greater than $-\frac12,$ and then Player 1 has to win from there. 

$$
P(\text{win eventually}) = P(x_0\rightarrow\text{somewhere}\rightarrow\text{somewhere else})\cdot P(\text{win from somewhere else})
$$

![](/img/2021-08-28-tug-of-war-integration-bounds.png){:width="450 px" class="image-centered"}

<br>
