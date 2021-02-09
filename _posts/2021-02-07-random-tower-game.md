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

Liberated from the burden of strategy, we are free to be our true selves and write down the state space for the arrangements of the tower, of which there are $27$ valid game states: ($\left(123,-,-\right)$ three ways, $\left(13, 2, -\right)$ six ways, $\left(12, 3, -\right)$ six ways, $\left(23, 1, -\right)$ six ways, and $\left(1, 2, 3\right)$ six ways). Each state can only reach $3$ other states unless it's a solved state in which case it has just $2$ neighbors. writing them all out, we get the interesting topology of a Sierpinski gasket:

![](/img/2021-02-08-game-board.png){:width="400px" class="image-centered"}

The symmetry in the graph suggests that it can be massively simplified, reminiscent of [many a resistor puzzle](http://yaroslavvb.com/papers/zemanian-infinite.pdf). At first I looked for ways to join similar edges, reducing the topology to a line, in hopes to map onto gambler's ruin, like I did in the [thanksgiving puzzle](https://joshmaxsilverman.github.io/2020-11-22-pass-cranberry-sauce/), but I couldn't get that to go. 
  
I then looked for a recursion, after all the graph has three identical subgraphs (ignoring the peg states). In fact, the expected time to arrive at an endstate from a node does have a nice relationship with the expected time to arrive at an endstate from one of its neighbors, though it isn't recursive. 

Writing down the time it takes to get from node $x$ to node $y,$ we get 

$$T(x \rightarrow y) = \frac{1}{d(x)} \sum_n \left(1 + T(n \rightarrow y)\right),$$

where the sum is over all the neighbors $n$ of $x.$
This is a harmonic function (nearest neighbors average), just like the voltage in a resistor circuit.

This suggests there's a mapping from $T(x, y)$ onto an equivalent resistor circuit wherein $T$ amounts to a reduction through the symmetries of series and parallel combinations of edges.

At a node $x$ in a circuit, the current from neighbor $n$ is equal to $(v(n) - v(x))/r_{xn}$ or $(v(n) - v(x))$ with unit resistors, and the total current flowing out of a node is $\sum_n (v(n) - v(x))$ which has to be zero. So $v(x) \times d(x) = \sum_n v(n)$ leads to $v(x) = \frac{1}{d(x)} \sum_n v(n).$ Inspecting, we can substract the voltage at node $y$ from both sides to get

$$v(x) - v(y) = 1 + \frac{1}{d(x)} \sum_n (v(n) - v(y)).$$

$T(x \rightarrow y) - (v(x) - v(y))$ is also harmonic and zero when $x$ is $y$ ($v(x)$ and $v(x)$ have the same voltage, $T(x \rightarrow x)$ takes no time), so, they are the same function.

If we can find a situation where we know the current from node $x$ to node $y,$ then we can use Ohm's law $(v(x) - v(y)) = I R_{xy}$ to find $T(x \rightarrow Y)$
we can do this by superposition, e.g.

- first inject an amount of current to the graph when node $x$ is held to zero voltage, all nodes will have some voltage relative to $x$
- then switch node $y$ to zero voltage and collect from there, then reverse all voltages (so we're injecting at $y$)
- overlay the two grids

But how much current should we inject? We can rearrange the Harmonic mean connecting neighboring voltages to get

$$\begin{align}
d(j) &= d(j)v(j) - \sum_n v(n) \\
&= \sum_n \left(v(j) - v(n)\right))
\end{align}$$

But the sum of $(v(j) - v(n))$ over all neighbors $n$ is just the current emerging from the node $j$ when the set of voltages is maintained. So, $d(j) = i_\text{inject at $j$}.$

If we inject $d(j)$ to every node $j,$ then in the overlaid circuits 

$$\sum_j d(j) = \text{number of edges}$$ 

will be injected at node $x$ and $\text{number of edges}$ will be extracted at node $y.$

so $T(x \rightarrow y) = \text{number of edges}\times R_{xy}.$

At the end, we just have to find the resistance between the top and bottom corner of the state space. And, since we can go to either corner, this means that 

$$T(\text{pole 1} \rightarrow \text{pole 2 or 3}) = 1/2 \times T(\text{pole 1} \rightarrow \text{pole 2}) = 1/2 \times T(\text{pole 1} \rightarrow \text{pole 3}).$$

In the first three steps below, we reduce the upper third of the game board diagram to a three-way junction. The next step pieces three of those together (to form the full $3$ peg + $3$ disk board) and the last step reduces that to its own three way junction. 

![](/img/2021-02-07-random-towers.png){:width="400px" class="image-centered"}

The resistance between pegs $1$ and $3$ $R_{13}$ is then the series sum of resistance along the path:

$$\frac{r}{3}\sum\limits_0^{n-1} \left(\frac{5}{3}\right)^n = \frac{r}{3} \dfrac{1 - \left(\frac{5}{3}\right)^n}{1-\frac{5}{3}} = \frac{r}{2}\left(\frac{5}{3}\right)^n - 1.$$

<br>
