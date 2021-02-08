---
layout: post
published: false
title: Random Towers
date: 2021/02/07
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

the time it takes to get from node x to node y, T(x -> y), is 1/d(x) * sum_n (1 + T(n -> y)), summed over all the neighbors n of x.
this is a harmonic function and just like the voltage in an electric circuit
at a node x in a circuit, the current from neighbor n is equal to (vn - vx)/rxn or (vn - vx) with unit resistors. the total current flowing out of a node is sum_n (vn - vx) which has to be zero. so vx * d(x) = sum_n vn -> vx = 1/d(x) sum_n vn. inspecting, we can substract the voltage at node y from both sides to get
vx - vy = 1 + 1/d(x) sum_n (vn - vy).

T(x -> y) - (vx - vy) is harmonic and both are zero when x is y (vx and vx have the same voltage, T(x -> x) take no time), so, they are the same function.

if we can find a situation where we know the current from node x to node y, then we can use ohm's law (vx - vy) = I R_{xy} to find T(x -> Y)
we can do this by superposition, e.g.
- first inject an amount of current to the graph when node x is held at zero voltage, all nodes will have some voltage relative to x
- then switch node y to zero voltage and collect from there, then reverse all voltages (so we're injecting at y)
- overlay the two grids
how much current should we inject?

we can rearrange
d(j) = d(j)vj - sum_n vn = sum_n (vj - vn) = i_{inject at j}

so inject d(j) to every node j, which means that in the overlaid circuits sum_j d(j) = 2m will be injected at node x and 2m will be extracted at node y.

so T(x -> y) = 2m R_{xy}

so, we just have to find the resistance between the top and bottom corner of the game. and since we can go to either corner, T(pole 1 -> pole2 or 3) = 1/2 * T(pole 1 -> pole 2) = 1/2 * T(pole 1 -> pole 3).

<br>
