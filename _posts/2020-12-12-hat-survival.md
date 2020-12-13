---
layout: post
published: false
title: 
date: 2020/12/12
---

>**Question**: another day, another demented hostage situation whose only salvation is twisted hat logic. The potentate of puzzles has kidnapped, blindfolded, and placed a red, green, or blue cap upon the head of you and $4$ of your unluckiest friends. Furthermore, they've split you up into two rows of $3$ and $2$ apiece. On opening your eyes, you can see the colors of the hats of the people in the opposite row. With nothing more than this information, and knowledge of your own position in the arrangement, you have to guess the color of your hat. If at least one person guesses correctly you all survive, otherwise it's time for the long nap. Is there a strategy that guarantees your survival?

<!--more-->

([FiveThirtyEight](URL))

## Solution

if everybody guesses blue for all inputs, then there will be someone correct in every case where someone has a blue hat. there are just 2^5 ways to build red-green ONLY patterns, so we start of with 3^5 - 2^5 = 211 correct guesses.

not coincidentally, this is the expected number of survival cases when everyone guesses at random.

we need to move relocate some correct guesses from the cases that have multiple correct guesses to those that have none. 

### A number of good guesses

If we follow a deterministic strategy, then each player will make the same number of correct guesses across the $243$ cases.

If I'm in the $3$-person row, then all I see is the color status of the people in the $2$ person row, $\left(C_4, C_5\right).$ There are $9$ possibilities for this pair of colors, so I will see each of them $243/9=27$ times and make the same guess every time. Across those occasions, my color will be right $\frac13\times9\times27 = 81$ times and wrong in the other $162.$

If I'm in the $2$-person row, then all I see is the color status of the people in the $3$ person row, $\left(C_1, C_2, C_3\right).$ There are $27$ possibilities for this pair of colors, so I will see each of them $243/27=9$ times and make the same guess every time. Across those occasions, my color will be right $\frac13\times27\times9 = 81$ times and wrong in the other $162.$

So, each person guesses correctly $81$ times, always. This makes $5\times81=405$ total correct guesses, which is more than enough to have $1$ in each of the $243$ cases. We just need to distribute these 405 correct guesses so that they pattern the rows.

### Row life

If we only adjust the guesses of the people in the first row, we can't outperform the $211$ benchmark of random guessing. Whatever adjustments we make are random with respect to the guesses of the people in the second row. The same is true if we only adjust the strategies of the people in the second row. 




<br>
