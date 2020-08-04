---
layout: post
published: true
title: Frustrated Graduation
date: 2020/08/03
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

First I found a repeatable approach for odd numbers of students. since any exchange of positions is rotationally symmetric, we can trivially keep one student in their original spot. hold them in their spot and swap every subsequent even/odd student pair. that will put the odd register ahead of the even register, breaking all their relative orders, but preserving all the relative orders within the even and odd registers. 

from there, remove the middle swap and move the remaining swaps toward the middle, this will break up the edge of the odd and even registers. ratcheting the swaps like this eats the even and odd registers from the outside in, eventually moving all the odd numbered students to the front of the line (in order) and all the even numbered students to the back (in order). this manifestly destroys all the original orderings. 

for a while, all i had beyond that was the apparent difficulty of constructing a case for _any_ even number of students whatsoever. it seemed impossible, even.

but the fact that the first student can trivially be kept in place got me thinking about the trajectories of the other students.

if all the students are in new spots relative to each other, after they move, then they should all be distinct distances from their original spot

in other words, their new position minus their old position should be distinct for all of them

let’s say we have an even number of students, $6$ for argument’s sake, the first student is going to trivially remain in the “same place”.

the others need to move $1$, $2$, $3$, $4$, or $5$ places from where they currently are (since the first student already used the $``0"$-move. Student $6$ can’t move $1$ spot (or they’d overlap with Student $1$), Student $5$ can’t move $2$ spots, etc. in other words, those last $5$ students have to map among themselves. for that to be true that sum of the new positions has to equal the sum of the original positions:

$$\overbrace{(2+3+4+5+6) + (1+2+3+4+5)}^\text{new positions} = \overbrace{(2+3+4+5+6)}^\text{old positions} \bmod 6.$$

the sum $\left(2+3+4+5+6\right)$ disappears from both sides. The other sum $\left(1+2+3+4+5\right)$ has an odd number of odd numberwhich is odd $\bmod 6$, which means the equation is false. 

That means there can't exist a rearrangement of the $5$ students that maps onto their original positions while moving them all distinct distances from their starting positions.

/img/2020-08-03-remapping-calculation.jpg
/img/2020-08-03-move-mapper.jpg
/img/2020-08-03-valid-moves.jpg
/img/2020-08-03-odd-swaps.jpg

<br>
