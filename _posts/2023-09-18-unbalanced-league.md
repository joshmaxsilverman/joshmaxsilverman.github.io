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

take the case of $3$ divisions. the probability of one or more dominance relationships is 

$$ \begin{align}
 P(\text{dominance}) &= P(\text{one domination}) - P(\text{two dominations}) + P(\text{one dominations}) \\
                     &= P(\text{one division dominates another}) \\
                     &\, - \left[P(\text{one division dominates two}) + P(\text{two divisions dominate one})\right] \\
                     &\, + P(\text{one division dominates another, which dominates another}) 
\end{align} $$

in pictures:

![](){:width="450 px" class="image-centered"}

So, how do we find these probabilities?

## How to count

the key fact is that if we have a dominance relationship between two divisions, it means that the teams separate in non-interacting chunks. we can swap the winning percentages between the teams in one division as many times as we like and the dominance relationships won't change. 

similarly, if two teams are dominated by one team, but don't necessarily dominate each other, we can do swaps among all the teams in the dominated divisions without changing the dominance relationship.

this tells us all we need in order to find the probabilities.

### $a \text{dom} b, c$

suppose there are three divisions, with $g$ teams per division and two divisions dominate a third. generically, $a$ and $b$ dominate $c.$

first, we can assign the division identities (e.g. East, Central, West) in $3\times 2\times 1$ ways. 

since divisions $a$ and $b$ are on the same level in the drawing, we can shuffle their teams without changing the facts of the matter. similarly, we can shuffle the teams in division $c$ without changing anything either. 

finally, there is no distinction between $a$ and $b$ (their order is arbitrary), so we divide by $2!$

altogether, this makes $3\times 2\times 1(2g)!g!$ ways to order the teams. there are $(3g)!$ total ways to order the teams in the league, so the probability of two teams dominating a third is

$$ P(\text{two teams dominate one}) = 3\times2\times1\times\frac{(2g)!\times g!}{(3g)!}\frac{1}{2!}. $$

this is just one term, but it contains all the crucial ingredients:
- for each layer with $m$ divisions, multiply by a factor of $(m\times g)!/m!,$ 
- divide by the total number of orders, $(n\times g)!.$
- - multiply by the number of ways to name the divisions,
  
in general there are many possible dominance relationships. happily, we can enumerate them by drawing diagrams.

we can go one level at a time, focusing on the total number of dominance relationships ...

## Four divisions

we can use the case of four divisions to do our first calculation. 

with four divisions, the fewest dominations we can have is zero, and the most is $6$ (if $a$ dominates $b$ dominates $c$ dominates $d,$ we have $3 + 2 + 1 = 6$ total dominations).

from the top, there is only one drawing with one domination.

for two, we can have $a$ and $b$ dominate $c$, $a$ dominate $b$ and $c$, or we can have $a$ dominate $b$ while $c$ dominates $d.$

plumbing the depths of our imagination, we get the following expansion in drawings:

![](/img/2023-09-18-diagram-expansion.png){:width="450 px" class="imaged-centered"}

now, we just have to go term by term and convert these drawings into probabilities. 

most of them follow the rules above in a straightforward way. 

for example, the first diagram in the third row has three divisions dominating another, the first layer contributes a $(3g)!/3!,$ the second layer contribues a $g!$ there are $4\times 3\times 2$ ways to label the divisions. making the expression $4\times3\times2\frac{(3g)!g!}{(4g)!}\frac{1}{3!}.$

likewise, the third diagram in the third row has two divisions dominating two other divisions. each layer contributes a factor of $(2g)!/2!$ making the expression $4!\left(\frac{(2g)!}{(4g)!(2!)^2}.$

a few are more interesting like the third diagram in the second row. this has two independent copies of the very first diagram. each one contributes a factor $(g!)^2/(2g)!.$ there is no significance to the order of the two sub-drawings, so we divide by $2!,$ making the overall expression $4!\frac{(g!)^2}{(2g)!}\frac{(g!)^2}{(2g)!}\frac{1}{2!}.$

going through the rest of the drawings and doing the same, we generate the beautiful expression

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
