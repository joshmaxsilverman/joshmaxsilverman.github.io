---
layout: post
published: true
title: Unbalanced league
subtitle: How often will geography rob your team of a playoff berth?
date: 2023/09/18
tags: diagrams counting inclusion-exclusion
---

>**Question**:
>Among all six divisions in Fiddler League Baseball (with five teams per division), what is the probability that there exist two divisions such that every team in one division has a higher winning percentage than every team in another division?
>
>(Note that this includes cases where multiple divisions are better or worse than others, such as having two divisions that both have higher winning percentages than some third division.)

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/how-likely-is-a-lopsided-league))

## Solution

in order for one division to dominate another, all teams in one need to be better than all the teams in another. we can represent this in a drawing by drawing an arrow from $a$ to $b$.

when there are more than two divisions, we have the potential for multiple dominance relationships (e.g. division $a$ dominates divisions $b$ and $c$) or for the teams in a third divison to intermingle with two teams in a dominance relationship $\left(\text{e.g.}\,$a_1 > c_1 > a_2 > b_1 > c_2 > b_2\right)$. we can represent these similarly, the first by drawing arrows from $a$ to $b$ and $c$ while the second is just the original drawing again. 

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

### Example: $a\ \text{dom}\ \\{b, c\\}$

suppose there are three divisions, with $g$ teams per division and two divisions dominate a third. generically, $a$ and $b$ dominate $c.$

first, we can assign the division identities (e.g. East, Central, West) in $3\times 2\times 1$ ways. 

since divisions $a$ and $b$ are on the same level in the drawing, we can shuffle their teams without changing the facts of the matter. similarly, we can shuffle the teams in division $c$ without changing anything either. 

finally, there is no distinction between $a$ and $b$ (their order is arbitrary), so we divide by $2!$

altogether, this makes $3\times 2\times 1(2g)!g!$ ways to order the teams. there are $(3g)!$ total ways to order the teams in the league, so the probability of two teams dominating a third is

$$ P(\text{two teams dominate one}) = 3\times2\times1\times\frac{(2g)!\times g!}{(3g)!}\frac{1}{2!}. $$

### Counting rules

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

![](/img/2023-09-18-diagram-expansion.png){:width="650 px" class="image-centered"}

now, we just have to go term by term and convert these drawings into probabilities. 

most of them follow the rules above in a straightforward way. 

for example, the first diagram in the third row has three divisions dominating another, the first layer contributes a $(3g)!/3!,$ the second layer contribues a $g!$ there are $4\times 3\times 2$ ways to label the divisions. making the expression $4\times3\times2\frac{(3g)!g!}{(4g)!}\frac{1}{3!}.$

likewise, the third diagram in the third row has two divisions dominating two other divisions. each layer contributes a factor of $(2g)!/2!$ making the expression $4!\left(\frac{(2g)!}{2!}\right)^2\frac{1}{(4g)!}.$

a few are more interesting like the third diagram in the second row. this has two independent copies of the very first diagram. each one contributes a factor $(g!)^2/(2g)!.$ there is no significance to the order of the two sub-drawings, so we divide by $2!,$ making the overall expression $4!\frac{(g!)^2}{(2g)!}\frac{(g!)^2}{(2g)!}\frac{1}{2!}.$

going through the rest of the drawings and doing the same, we generate the beautiful expression

$$ 
\begin{align}
P(\text{domination}) &= 4\times 3\frac{g!\cdot g!}{(2 g)!} \\
 &\ -\left(4\times3\times2\frac{g!\cdot (2 g)!}{(3 g)!}\frac{1}{2!} + 4\times3\times2\frac{g!\cdot (2 g)!}{(3 g)!}\frac{1}{2!} + 4!\left[\frac{g!}{(2 g)!}\right]^2\frac{1}{2!}\right)
 \end{align}
$$

this expansion should be an exact solution for the case of four divisions. plotting it against an $N=10^7$ round simulation, we see good agreement:

![](/img/2023-09-17-4-division.png){:width="450 px" class="image-centered"}

$$
\begin{array}{c|c|c}
 g & \text{Simulation} & \text{Prediction} \\ \hline
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
$$

## Six divisions

in principle, we ought to generate a new expansion for $d = 6,$ since more exotic arrangements are possible. however, it isn't necessary as inspection reveals. 

our series for four divisions is numerically dominated by the two and three division terms. this is because it's rare to achieve the sorts of orderings necessary to have the higher order domination relationships. 

to take an extreme example, the case of six dominations with four divisions amd three teams per division is only achieved if the winning percentages are ordered like 

$$a,a,a,b,b,b,c,c,c,d,d,d.$$ 

as we add more divisions to the mix, the chance of forming these sorts of intricate chunkings is low.

this argument does not hold when $g$ is one or two, and we should still expect the exotic arrangements. the disappearance of these terms is determined by the value of the ordering factors. 

for example, a new term that has five teams getting dominated by one has a factor 

$$ \frac{(5g)!g!}{(6g)!}\frac{1}{5!} $$ 

which is $2\times10^{-5}$ by $g=3.$ in general, higher order terms that are simply extensions of lower order terms (like this five way "fan") make the greatest contributions, but even they are very rare.

with that said, the only changes we need to make to our four division expansion is to adjust the counting factors such as $4\times 3\times 2$ to $6\times5\times4.$

we can plot the prediction against a simulation. as expected, the ignorance of exotic contributions bites us for $g=2$ but by $g=3$ the prediction is within $1%$ of the simulation.

![](/img/2023-09-17-6-division.png){:width="450 px" class="image-centered"}

6

$$
\begin{array}{c|c|c}
 g & \text{Simulation} & \text{Prediction} \\ \hline
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
$$

<br>
