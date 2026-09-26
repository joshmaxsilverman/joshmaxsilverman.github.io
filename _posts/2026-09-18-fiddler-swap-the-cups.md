---
layout: post
published: true
title: Can you swap the cups?
date: 2026/09/18
subtitle: How long will you swap before you see all the swaps?
tags: expectation permutations random-walk breadth-first-search state-space
source: fiddler
kind: puzzle
theme: probability
hide_from_recent: true
---

> **Question**: My friend has three cups, labeled “A,” “B,” and “C” in a row. She randomly picks two different cups and swaps their positions. Then she does this again and again, picking a random pair each time, until all three cups are back in their original order. For example, here is one such sequence of swaps:
>
> - A, B, C (original)
> - C, B, A (first and third were swapped)
> - B, C, A (first and second were swapped)
> - B, A, C (second and third were swapped)
> - A, B, C (first and second were swapped)
>
> In this example, the cups returned to their original order after *four* swaps.
>
> On average, how many swaps would you expect until the cups return to their original order?
>
> **Extra Credit**: In total, there are six possible orders of the cups. Without any swaps, one of those orders (A, B, C) has already been achieved.
>
> On average, how many swaps would you expect until the remaining five orders (and thus, all six) are also achieved?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-swap-the-cups))

## Solution

This is an interesting problem because there is no fixed target among the scrambles. 
We could finish on a particular scramble if it's the last one we happen to visit, but not if we visit it before we visit the others.
So, there's not an obvious stopping condition without memory.

But if we do remember where we've been then there is.
So, let's abstract from the physical reality of our scrambles and consider our state to be the scramble we're currently on, along with the list of scrambles we've seen already

$$
 \text{state} = \left(\text{current scramble}, \left(\text{scrambles we've seen already}\right)\right)
$$

For ease of writing, let's number the scrambles like so

$$
\begin{align*}
	\text{ABC} &\rightarrow s_1 \\
	\text{ACB} &\rightarrow s_2 \\
	\text{BAC} &\rightarrow s_3 \\
	\text{BCA} &\rightarrow s_4 \\
	\text{CAB} &\rightarrow s_5 \\
	\text{CBA} &\rightarrow s_6.
\end{align*}
$$

Thinking about how the scrambles can turn into one another, the scrambles are neighbored up like 

$$
	\begin{align*}
		s_1 &: \left( s_2, s_3, s_6 \right) \\
		s_2 &: \left( s_1, s_5, s_4 \right) \\
		s_3 &: \left( s_1, s_4, s_5 \right) \\
		s_4 &: \left( s_2, s_3, s_6 \right) \\
		s_5 &: \left( s_2, s_3, s_6 \right) \\
		s_6 &: \left( s_1, s_4, s_5 \right) .
	\end{align*}
$$

Let that be the definition for the neighbor dictionary $\mathcal{N}.$

If, e.g., we're on scramble $s_4$ then we can move to scrambles $s_2,$ $s_3,$ or $s_6.$
However, our movement in the full state space is more restricted. 
We can move from state $\left(s_i, V_j\right)$ to state $\left(s_k, V_\ell\right)$ if $s_k$ is a neighboring scramble of $s_i$ 

$$ s_k \in \mathcal{N}(s_i), $$

and if the current visited set $V_j$ is subset or equal to the new one $V_\ell$, 

$$ V_\ell = V_j \cup \{s_k\} . $$

With these rules, we can build the graph of neighbors in the abstract state space and generate a system of equations for the expected waiting time before we hit the final scramble.

Call $T_{s_i, V_j}$ the expected waiting time before reaching the final scramble. 
The expected waiting time from $\left(s_i, V_j\right)$ is $1$ plus the weighted average of the expected waiting time from all of its neighbors.
Finally, the value $T_{j,\left(1,2,3,4,5,6\right)} = 0$ for all $j.$

Walking the graph by breadth-first search results in the following system of $99$ incredible equations for the expected waiting times

$$
\begin{align*}
T_{1,\left(1\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2\right)} + \frac{1}{3} T_{3,\left(1,3\right)} + \frac{1}{3} T_{6,\left(1,6\right)}  \\
T_{1,\left(1,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,6\right)} + \frac{1}{3} T_{3,\left(1,3,6\right)} + \frac{1}{3} T_{6,\left(1,6\right)}  \\
T_{1,\left(1,2\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2\right)} + \frac{1}{3} T_{3,\left(1,2,3\right)} + \frac{1}{3} T_{6,\left(1,2,6\right)}  \\
T_{1,\left(1,3\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3\right)} + \frac{1}{3} T_{3,\left(1,3\right)} + \frac{1}{3} T_{6,\left(1,3,6\right)}  \\
T_{3,\left(1,3\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3\right)} + \frac{1}{3} T_{4,\left(1,3,4\right)} + \frac{1}{3} T_{5,\left(1,3,5\right)}  \\
T_{6,\left(1,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,6\right)} + \frac{1}{3} T_{4,\left(1,4,6\right)} + \frac{1}{3} T_{5,\left(1,5,6\right)}  \\
T_{2,\left(1,2\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2\right)} + \frac{1}{3} T_{4,\left(1,2,4\right)} + \frac{1}{3} T_{5,\left(1,2,5\right)}  \\
T_{6,\left(1,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,5,6\right)} + \frac{1}{3} T_{4,\left(1,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,5,6\right)}  \\
T_{1,\left(1,3,4\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4\right)} + \frac{1}{3} T_{3,\left(1,3,4\right)} + \frac{1}{3} T_{6,\left(1,3,4,6\right)}  \\
T_{4,\left(1,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,6\right)} + \frac{1}{3} T_{3,\left(1,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,4,6\right)}  \\
T_{3,\left(1,3,4\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,4\right)} + \frac{1}{3} T_{4,\left(1,3,4\right)} + \frac{1}{3} T_{5,\left(1,3,4,5\right)}  \\
T_{2,\left(1,2,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,5\right)} + \frac{1}{3} T_{4,\left(1,2,4,5\right)} + \frac{1}{3} T_{5,\left(1,2,5\right)}  \\
T_{1,\left(1,3,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,6\right)} + \frac{1}{3} T_{3,\left(1,3,6\right)} + \frac{1}{3} T_{6,\left(1,3,6\right)}  \\
T_{2,\left(1,2,3\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3\right)} + \frac{1}{3} T_{4,\left(1,2,3,4\right)} + \frac{1}{3} T_{5,\left(1,2,3,5\right)}  \\
T_{1,\left(1,2,4\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4\right)} + \frac{1}{3} T_{3,\left(1,2,3,4\right)} + \frac{1}{3} T_{6,\left(1,2,4,6\right)}  \\
T_{2,\left(1,2,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,6\right)} + \frac{1}{3} T_{5,\left(1,2,5,6\right)}  \\
T_{1,\left(1,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,6\right)} + \frac{1}{3} T_{3,\left(1,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,4,6\right)}  \\
T_{6,\left(1,2,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,6\right)} + \frac{1}{3} T_{5,\left(1,2,5,6\right)}  \\
T_{5,\left(1,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,5,6\right)} + \frac{1}{3} T_{3,\left(1,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,5,6\right)}  \\
T_{5,\left(1,3,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5\right)} + \frac{1}{3} T_{3,\left(1,3,5\right)} + \frac{1}{3} T_{6,\left(1,3,5,6\right)}  \\
T_{3,\left(1,3,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,6\right)} + \frac{1}{3} T_{5,\left(1,3,5,6\right)}  \\
T_{1,\left(1,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,5,6\right)} + \frac{1}{3} T_{3,\left(1,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,5,6\right)}  \\
T_{5,\left(1,2,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,5\right)} + \frac{1}{3} T_{6,\left(1,2,5,6\right)}  \\
T_{1,\left(1,3,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5\right)} + \frac{1}{3} T_{3,\left(1,3,5\right)} + \frac{1}{3} T_{6,\left(1,3,5,6\right)}  \\
T_{3,\left(1,3,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,5\right)} + \frac{1}{3} T_{4,\left(1,3,4,5\right)} + \frac{1}{3} T_{5,\left(1,3,5\right)}  \\
T_{6,\left(1,3,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,6\right)} + \frac{1}{3} T_{5,\left(1,3,5,6\right)}  \\
T_{2,\left(1,2,4\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,4\right)} + \frac{1}{3} T_{4,\left(1,2,4\right)} + \frac{1}{3} T_{5,\left(1,2,4,5\right)}  \\
T_{4,\left(1,2,4\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4\right)} + \frac{1}{3} T_{3,\left(1,2,3,4\right)} + \frac{1}{3} T_{6,\left(1,2,4,6\right)}  \\
T_{4,\left(1,3,4\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4\right)} + \frac{1}{3} T_{3,\left(1,3,4\right)} + \frac{1}{3} T_{6,\left(1,3,4,6\right)}  \\
T_{6,\left(1,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,4,6\right)} + \frac{1}{3} T_{4,\left(1,4,6\right)} + \frac{1}{3} T_{5,\left(1,4,5,6\right)}  \\
T_{1,\left(1,2,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,5\right)} + \frac{1}{3} T_{6,\left(1,2,5,6\right)}  \\
T_{1,\left(1,2,3\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3\right)} + \frac{1}{3} T_{3,\left(1,2,3\right)} + \frac{1}{3} T_{6,\left(1,2,3,6\right)}  \\
T_{3,\left(1,2,3\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3\right)} + \frac{1}{3} T_{4,\left(1,2,3,4\right)} + \frac{1}{3} T_{5,\left(1,2,3,5\right)}  \\
T_{1,\left(1,2,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,6\right)} + \frac{1}{3} T_{6,\left(1,2,6\right)}  \\
T_{4,\left(1,3,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{3,\left(1,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,3,4,6\right)}  \\
T_{1,\left(1,3,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{3,\left(1,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,3,5,6\right)}  \\
T_{1,\left(1,2,3,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,5\right)} + \frac{1}{3} T_{6,\left(1,2,3,5,6\right)}  \\
T_{3,\left(1,2,3,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,5\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{5,\left(1,2,3,5\right)}  \\
T_{6,\left(1,4,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,4,5,6\right)} + \frac{1}{3} T_{4,\left(1,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,4,5,6\right)}  \\
T_{2,\left(1,2,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,4,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,6\right)} + \frac{1}{3} T_{5,\left(1,2,4,5,6\right)}  \\
T_{5,\left(1,2,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{6,\left(1,2,4,5,6\right)}  \\
T_{4,\left(1,4,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{3,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,4,5,6\right)}  \\
T_{4,\left(1,2,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,2,4,6\right)}  \\
T_{1,\left(1,2,3,4\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4\right)} + \frac{1}{3} T_{3,\left(1,2,3,4\right)} + \frac{1}{3} T_{6,\left(1,2,3,4,6\right)}  \\
T_{3,\left(1,2,3,4\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,4\right)} + \frac{1}{3} T_{4,\left(1,2,3,4\right)} + \frac{1}{3} T_{5,\left(1,2,3,4,5\right)}  \\
T_{6,\left(1,2,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,5,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,2,5,6\right)}  \\
T_{6,\left(1,2,3,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,6\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{5,\left(1,2,3,5,6\right)}  \\
T_{3,\left(1,3,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,5,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,3,5,6\right)}  \\
T_{1,\left(1,2,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{6,\left(1,2,4,5,6\right)}  \\
T_{5,\left(1,3,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{3,\left(1,3,4,5\right)} + \frac{1}{3} T_{6,\left(1,3,4,5,6\right)}  \\
T_{1,\left(1,2,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,2,4,6\right)}  \\
T_{6,\left(1,3,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,5,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,3,5,6\right)}  \\
T_{3,\left(1,3,4,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,4,5\right)} + \frac{1}{3} T_{4,\left(1,3,4,5\right)} + \frac{1}{3} T_{5,\left(1,3,4,5\right)}  \\
T_{5,\left(1,4,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{3,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,4,5,6\right)}  \\
T_{1,\left(1,3,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{3,\left(1,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,3,4,6\right)}  \\
T_{2,\left(1,2,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,5,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,2,5,6\right)}  \\
T_{3,\left(1,3,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,4,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,6\right)} + \frac{1}{3} T_{5,\left(1,3,4,5,6\right)}  \\
T_{2,\left(1,2,3,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,6\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{5,\left(1,2,3,5,6\right)}  \\
T_{2,\left(1,2,3,4\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,4\right)} + \frac{1}{3} T_{4,\left(1,2,3,4\right)} + \frac{1}{3} T_{5,\left(1,2,3,4,5\right)}  \\
T_{5,\left(1,2,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,5,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,2,5,6\right)}  \\
T_{1,\left(1,4,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{3,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,4,5,6\right)}  \\
T_{2,\left(1,2,3,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,5\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{5,\left(1,2,3,5\right)}  \\
T_{2,\left(1,2,4,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,4,5\right)} + \frac{1}{3} T_{4,\left(1,2,4,5\right)} + \frac{1}{3} T_{5,\left(1,2,4,5\right)}  \\
T_{4,\left(1,2,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{6,\left(1,2,4,5,6\right)}  \\
T_{5,\left(1,2,3,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,5\right)} + \frac{1}{3} T_{6,\left(1,2,3,5,6\right)}  \\
T_{5,\left(1,3,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{3,\left(1,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,3,5,6\right)}  \\
T_{1,\left(1,2,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,5,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,2,5,6\right)}  \\
T_{1,\left(1,2,3,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,6\right)} + \frac{1}{3} T_{6,\left(1,2,3,6\right)}  \\
T_{6,\left(1,2,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,4,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,6\right)} + \frac{1}{3} T_{5,\left(1,2,4,5,6\right)}  \\
T_{4,\left(1,3,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{3,\left(1,3,4,5\right)} + \frac{1}{3} T_{6,\left(1,3,4,5,6\right)}  \\
T_{4,\left(1,2,3,4\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4\right)} + \frac{1}{3} T_{3,\left(1,2,3,4\right)} + \frac{1}{3} T_{6,\left(1,2,3,4,6\right)}  \\
T_{3,\left(1,2,3,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,6\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{5,\left(1,2,3,5,6\right)}  \\
T_{6,\left(1,3,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,4,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,6\right)} + \frac{1}{3} T_{5,\left(1,3,4,5,6\right)}  \\
T_{5,\left(1,2,3,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,2,3,5,6\right)}  \\
T_{2,\left(1,2,3,4,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{5,\left(1,2,3,4,5\right)}  \\
T_{4,\left(1,2,3,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,5\right)}  \\
T_{1,\left(1,2,3,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{6,\left(1,2,3,5,6\right)}  \\
T_{5,\left(1,3,4,5,6\right)} &= 1 + \frac{1}{3} T_{3,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,3,4,5,6\right)}  \\
T_{3,\left(1,2,3,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{5,\left(1,2,3,5,6\right)}  \\
T_{2,\left(1,2,4,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,2,4,5,6\right)}  \\
T_{6,\left(1,2,4,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{4,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,2,4,5,6\right)}  \\
T_{4,\left(1,2,4,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,2,4,5,6\right)}  \\
T_{1,\left(1,3,4,5,6\right)} &= 1 + \frac{1}{3} T_{3,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,3,4,5,6\right)}  \\
T_{1,\left(1,2,3,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,2,3,4,6\right)}  \\
T_{3,\left(1,3,4,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,3,4,5,6\right)}  \\
T_{1,\left(1,3,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{3,\left(1,3,4,5\right)} + \frac{1}{3} T_{6,\left(1,3,4,5,6\right)}  \\
T_{5,\left(1,2,3,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,5\right)}  \\
T_{3,\left(1,2,3,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,6\right)}  \\
T_{6,\left(1,2,3,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{5,\left(1,2,3,5,6\right)}  \\
T_{1,\left(1,2,3,4,5\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,5\right)}  \\
T_{5,\left(1,2,4,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,2,4,5,6\right)}  \\
T_{3,\left(1,2,3,4,5\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,5\right)} + \frac{1}{3} T_{5,\left(1,2,3,4,5\right)}  \\
T_{6,\left(1,3,4,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{4,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{5,\left(1,3,4,5,6\right)}  \\
T_{2,\left(1,2,3,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,6\right)}  \\
T_{2,\left(1,2,3,5,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,5,6\right)} + \frac{1}{3} T_{5,\left(1,2,3,5,6\right)}  \\
T_{4,\left(1,3,4,5,6\right)} &= 1 + \frac{1}{3} T_{3,\left(1,3,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,3,4,5,6\right)}  \\
T_{6,\left(1,2,3,4,6\right)} &= 1 + \frac{1}{3} T_{1,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{4,\left(1,2,3,4,6\right)}  \\
T_{1,\left(1,2,4,5,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,4,5,6\right)} + \frac{1}{3} T_{6,\left(1,2,4,5,6\right)}  \\
T_{4,\left(1,2,3,4,6\right)} &= 1 + \frac{1}{3} T_{2,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{3,\left(1,2,3,4,6\right)} + \frac{1}{3} T_{6,\left(1,2,3,4,6\right)}.
\end{align*}
$$ 

Solving them with `sympy` we get 

$$ T_{1,\left(1\right)} = \frac{171}{14} \approx 12.2143 $$

There are symmetries and equivalences to exploit and collapse this down to a handful of equations, but I think this presentation exposes the hideous beauty of generating the equations from graph search.

### Standard credit

The answer to the standard problem is $6$ due to symmetry. 

To see this imagine we are in hell, doomed to traverse the scrambles for all eternity.
Each time we swap a pair of letters to get to a different scramble, we add it to the list of scrambles we've visited in order.

How much time do we expect there to be between visits to a given scramble?
Looking at the sequence we wrote down, it is the same question as "how often would we expect to land on a given scramble?"
Since there is no favor among them, one sixth of the entries in the list are the given tile, so the answer has to be "once every $6$ steps."


<br>
