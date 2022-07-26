---
layout: post
published: false
title: Morning walkabout
date: 2022/07/26
---

>Question

<!--more-->

([Jane Street]([URL](https://www.janestreet.com/puzzles/current-puzzle/)))

## Solution

andy walks in two kinds of places, the finite surface of the soccer ball and the (infinite?) kitchen floor.

on the ball, he can only walk so far into the forest before he starts to walk out. but on the kitchen floor, his walks are much more likely to range up in length. the further he gets, the more likely he is to get further. 

we want to know if he'll have an exceptional experience in the kitchen. since this depends on knowing the expected walk on his soccer ball, we'll start there.

# Soccer ball

whenever andy takes a step, he has a $1/3$ chance to move onto some neighboring tile, each of which has an expected number of steps before it returns to the origin for the first time. this results in the harmonic relationship

$$
  \langle T_i\rangle = 1 + \frac13\sum\limits_{j\in\sigma(i)} T_j
$$

to get rolling, we have to encode the surface of the ball 

<br>
