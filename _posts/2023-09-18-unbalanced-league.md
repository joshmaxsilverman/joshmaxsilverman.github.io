---
layout: post
published: false
title: Unbalanced league
date: 2023/09/18
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

in order for one division to dominate another, all teams in one need to be better than all the teams in another. we can represent this in a drawing by drawing an arrow from $a$ to $b$.

when there are more than two divisions, we have the potential for multiple dominance relationships (e.g. division $a$ dominates divisions $b$ and $c$) or for the teams in a third divison to intermingle with two teams in a dominance relationship (e.g. $a_1 > c_1 > a_2 > b_1 > c_2 > b_2$). we can represent these similarly, the first by drawing arrows from $a$ to $b$ and $c$ while the second is just the original drawing again. 

taking a step back, we just saw that "A dominates B" is a relationship that can be embedded in more complicated relationships. this means that when we talk about "A dominating B" we are counting cases where that is the only dominance relationship, as well as every other situation where division "A" dominates division "B".

to properly count the instances where one or more dominance relationships is present, we need to remove double counting.

as a warm up, take the case of $3$ divisions. the probability of one or more dominance relationships is 

$$ \begin{align}
 P(\text{dominance}) &= P(\text{one division dominates another}) \\
                     &\ - \left[P(\text{one division dominates two}) + P(\text{two divisions dominate one})\right] \\
                     &\ + P(\text{one division dominates another, which dominates another}) 
\end{align} $$

## How to count

we can swap the winning percentages between the teams in one division as many times as we like and the dominance relationships won't change. this tells us how to count.

for example, suppose there are three divisions, with $g$ teams per division and two divisions dominate a third. generically, $a$ and $b$ dominate $c.$

first, we can assign the divisions $3\times 2\times 1$ ways. since $a$ and $b$ are on the same level, we can exchange their orders without changing the facts of the matter. similarly, we can shuffle the teams in division $c$ without changing anything either. altogether, this makes $3\times 2\times 1(2g)!g!$ ways to order the teams. altogether, there are $(3g)!$ to order the league, making the probability of two teams dominating a third equal to

$$ 3\times2\times1\times\frac{(2g)!\times g!}{(3g)!}. $$

this is just one term, and in general there are many possible dominance relationships. happily, we can enumerate them by drawing diagrams.

we can go one level at a time, focusing on the total number of dominance relationships ...


![](/img/2023-09-18-diagram-expansion.png){:width="450 px" class="imaged-centered"}

$$ -4\ 3\ 2 \left(\frac{(2 g)! g! g!}{2! (4 g)!}+\frac{(2 g)! (g!)^3}{2! g! (4 g)!}+\frac{(2 g)! (g!)^3}{2! g! (4 g)!}+\frac{(2 g)! (2 g)!}{(2!)^2 (4 g)!}\right)-\left(\frac{2\ 3\ 4 (g! g!)}{2! ((2 g)! (2 g)!)}+\frac{2\ 3\ 4 (g! (2 g)!)}{2! (3 g)!}+\frac{2\ 3\ 4 (g! (2 g)!)}{2! (3 g)!}\right)+2\ 3\ 4 \left(\frac{(2 g)! g! g!}{2! (4 g)!}+\frac{g! (2 g)! g!}{2! (4 g)!}+\frac{g! g! (2 g)!}{2! (4 g)!}\right)+\frac{3\ 4 (g! g!)}{(2 g)!}+\left(\frac{2\ 3\ 4 (g!)^3}{(3 g)!}+\frac{2\ 3\ 4 (g! (3 g)!)}{3! (4 g)!}+\frac{2\ 3\ 4 (g! (3 g)!)}{3! (4 g)!}\right)-\frac{4\ 3\ 2 (g!)^4}{(4 g)!} $$

4

$$\left(
\begin{array}{ccc}
 1 & 1. & 1. \\
 2 & 0.771508 & 0.77381 \\
 3 & 0.356963 & 0.357543 \\
 4 & 0.127776 & 0.127561 \\
 5 & 0.0401775 & 0.0401423 \\
 6 & 0.0117458 & 0.0117528 \\
 7 & 0.0033413 & 0.00329677 \\
 8 & 0.000885 & 0.000900522 \\
 9 & 0.0002418 & 0.000241776 \\
 10 & 0.0000636 & 0.0000641611 \\
\end{array}
\right)$$


6

$$\left(
\begin{array}{ccc}
 1 & 1. & -50. \\
 2 & 0.93066 & -0.0595238 \\
 3 & 0.575292 & 0.577435 \\
 4 & 0.246519 & 0.248482 \\
 5 & 0.086732 & 0.0864987 \\
 6 & 0.026888 & 0.0268687 \\
 7 & 0.007714 & 0.00780867 \\
 8 & 0.00231 & 0.00217911 \\
 9 & 0.00062 & 0.000592692 \\
 10 & 0.000149 & 0.000158523 \\
\end{array}
\right)$$

<br>
