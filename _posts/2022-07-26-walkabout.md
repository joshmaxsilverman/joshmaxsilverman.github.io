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

in the kitchen, the lattice is bigger and it pays to be smart before diving in.

if andy starts from the marked tile, then his first options are to take a unit step — i.e. $\left(\cos\theta,\sin\theta\right)$ — in one of the directions $\\{\frac{\pi}{6}, \frac{5\pi}{6}, \frac{3\pi}{2}\\}.$ on the second step, his options are these reflected about the $x$-axis: $\\{-\frac{\pi}{6}, -\frac{5\pi}{6}, \frac{3\pi}{2}\\}.$

since andy's walks return to the origin, they'll have an even number of steps. this means that we can focus on tiles that are an even number of steps from the origin and ignore the others.

any $n$ step path on the reduced lattice is a path of length $2n$ on the original, and therefore has probability $1/3^(2n)$ of occurring. if we can count the number of $n$ step paths on the reduced lattice $\omega(n)$, then we will inherit the distribution of path lengths $p(n) = \omega(n)/3^{2n}.$

## count them up

we can count paths with a simple observation. if there is an $(n-1)$ step path to one of my neighbors, then there is an $n$ step path to me. in other words:

$$
  \omega_i^n = \sum\limits_{j\in\sigma(i)\setminus \boldsymbol{0}} \omega_j^{n-1}
$$

the number of steps to tile $i$ in $n$ steps is the sum of the number of paths to each of its neighbors in $(n-1)$ steps. we only want to count first returns to the origin, so we don't count the origin when it happens to be a neighbor.

with this recursion, we can count $\omega_\boldsymbol{0}^n,$ but we need the base case — the number of ways to step from the origin. we can get these from the first steps on the reduced lattice.

on the reduced lattice we have $9$ possible moves, formed by all possible pairs of first and second moves on the original lattice. there are $3$ ways to stay put (move in any of the $3$ first move directions followed immediately by the reverse) and $1$ way each to move in each of the $6$ directions on the reduced lattice.

now, we have everything we need.

```mathematica
(* form first moves on the original lattice *)
oddMoves = {{Cos[π/6], Sin[π/6]}, {Cos[5 π/6], 
    Sin[5 π/6]}, {0, -1}};

(* reflect to form the second moves on the original lattice *)
evenMoves = ({-1, -1} * #) & /@ oddMoves;

(* form the moves on the reduced lattice *)
twoStepMoves = Total /@ Tuples[{oddMoves, evenMoves}];

(* initialize ω *)
ω[pt_, 1] := 0;

(* use the two step moves to fill in the base case *)
Do[ω[twoStepMoves[[i]], 1] += 1, {i, 1, Length@twoStepMoves}];

(* one time step recursion over neighbors, excluding the origin *)
ω[pt_, t_] := ω[pt, t] = (
   neighbors = 
    Table[pt - twoStepMoves[[i]], {i, 1, Length@twoStepMoves}];
   neighbors = Select[neighbors, # != {0, 0} &];
   Return[
    Total[ω[#, t - 1] & /@ neighbors]
    ]
   )
```

with this in hand, we can find $p(\text{kitchen longer than }\langle T\rangle_\text{soccer}):$

$$
  1 - \sum\limits_{n=1}^{10}\frac{\omega_\boldsymbol{0}^n}{3^{2n}}.
$$







<br>
