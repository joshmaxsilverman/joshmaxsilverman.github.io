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

# soccer ball

whenever andy takes a step, he has a $\frac13$ chance to move onto some neighboring tile $j$ in the neighborhood of $i,$ $\sigma(i)$ which has an expected number of steps $\langle T_j\rangle$ before it returns to the origin for the first time. putting this to symbols gets the harmonic relationship

$$
  \langle T_i\rangle = 1 + \frac13\sum\limits_{j\in\sigma(i)} \langle T_j\rangle
$$

to get rolling, we just have to encode the neighbor relationships of the white tiles on the ball. taking its vitals, we see that the $20$ white tiles can be arranged into $4$ groups (A, B, C, and D). the top and bottom groups form connected rings while the middle two undulate, connecting to members of the other ring, and the top or bottom, but not amongst themselves.

putting this to a graph, we can generate the system of expectation equations like

```mathematica
edges = {A1 <-> A2, A2 <-> A3, A3 <-> A4, A4 <-> A5, A5 <-> A1, 
         A1 <-> B1, A2 <-> B2, A3 <-> B3, A4 <-> B4, A5 <-> B5, 
         B1 <-> C1, B1 <-> C5, B2 <-> C1, B2 <-> C2, B3 <-> C2, 
         B3 <-> C3, B4 <-> C3, B4 <-> C4, B5 <-> C4, B5 <-> C5, 
         C1 <-> D1, C2 <-> D2, C3 <-> D3, C4 <-> D4, C5 <-> D5, 
         D1 <-> D2, D2 <-> D3, D3 <-> D4, D4 <-> D5, D5 <-> D1};

(* form the expectation relations for each tile*)
equations = (# == 1 + 1/3 Total[AdjacencyList[g, #]]) & /@ VertexList[g];

(* set A1 to zero in all equations but its own *)
system = Join[{eqns[[1]]}, eqns[[2 ;; -1]] /. {A1 -> 0}];

(* solve the system *)
sols = First@Solve[system, VertexList[g]]

> {A1 -> 20, A2 -> 19, A3 -> 27, A4 -> 27, A5 -> 19, 
>  B1 -> 19, B2 -> 27, B3 -> 32, B4 -> 32, B5 -> 27, 
>  C1 -> 27, C2 -> 32, C3 -> 34, C4 -> 32, C5 -> 27, 
>  D1 -> 32, D2 -> 34, D3 -> 35, D4 -> 34, D5 -> 32}
```

putting these back on the ball, we see that the expected waiting time increases as we move away from the starting point, up until a maximum at the furthest point, $D_3.$ as expected, the expected waiting time at each of $A_1$'s neighbors is $1$ less than $T(A_1).$

so, we're looking for the probability that his kitchen walk goes longer than $\langle T\rangle_\text{soccer} = 20.$

# kitchen constitutional

in the kitchen, the lattice is bigger and it pays to be smart before diving in. since andy's walks return to the origin, they'll have an even number of steps. this means that we focus on tiles that are an even number of steps from the origin. 

if andy starts from the marked tile, then his first options are to step in one of the directions $\\{\frac{\pi}{6}, \frac{5\pi}{6}, \frac{3\pi}{2}\\}.$ on the second step, his options are these reflected about the $x$-axis: $\\{-\frac{\pi}{6}, -\frac{5\pi}{6}, \frac{3\pi}{2}\\}.$

<br>
