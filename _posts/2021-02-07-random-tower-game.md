---
layout: post
published: true
title: Random Towers
date: 2021/02/07
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

Liberated from the burden of strategy, we are free to be our true selves and write down the state space for the arrangements of the tower, of which there are $27$ valid game states: ($\left(123,-,-\right)$ three ways, $\left((13, 2, -\right)$ six ways, $\left(12, 3, -\right)$ six ways, $\left(23, 1, -\right)$ six ways, and $\left(1, 2, 3\right)$ six ways). Each state can only reach $3$ other states unless it's a solved state in which case it has just $2$ neighbors. writing them all out, we get the interesting topology of a Sierpinski gasket:

<img>

The symmetry in the graph suggests that it can be massively simplified, reminiscent of [many a resistor puzzle](http://yaroslavvb.com/papers/zemanian-infinite.pdf). At first I looked for ways to join similar edges, reducing the topology to a line, in hopes to map onto gambler's ruin, like I did in the [thanksgiving puzzle](https://joshmaxsilverman.github.io/2020-11-22-pass-cranberry-sauce/), but I couldn't get that to go. 
  
I then looked for a recursion, after all the graph has three identical subgraphs (ignoring the peg states). In fact, the expected time to arrive at an endstate from a node does have a nice relationship with the expected time to arrive at an endstate from one of its neighbors, though it isn't recursive. 

Writing down the time it takes to get from node $x$ to node $y,$ we get  $T(x \rightarrow y)$, is $\frac{1}{d(x)} \sum_n \left(1 + T(n \rightarrow y)\right),$ summed over all the neighbors $n$ of $x.$
This is a harmonic function (nearest neighbors average), just like the voltage in a resistor circuit.

This suggests there's a mapping from $T(x, y)$ onto an equivalent resistor circuit wherein $T$ amounts to a reduction through the symmetries of series and parallel combinations of edges.

at a node x in a circuit, the current from neighbor n is equal to (vn - vx)/rxn or (vn - vx) with unit resistors, and the total current flowing out of a node is sum_n (vn - vx) which has to be zero. so vx * d(x) = sum_n vn -> vx = 1/d(x) sum_n vn. inspecting, we can substract the voltage at node y from both sides to get
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
