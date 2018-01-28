---
layout: post
title: Four Squares
date: 2018-01-27
published: true
---

>The famous four-color theorem states, essentially, that you can color in the regions of any map using at most four colors in such a way that no neighboring regions share a color. A computer-based proof of the theorem was offered in 1976.
>
>Some 2,200 years earlier, the legendary Greek mathematician Archimedes described something called an Ostomachion. It’s a group of pieces, similar to tangrams, that divides a 12-by-12 square into 14 regions. The object is to rearrange the pieces into interesting shapes, such as a Tyrannosaurus rex. It’s often called the oldest known mathematical puzzle.
>
>Your challenge today: Color in the regions of the Ostomachion square with four colors such that each color shades an equal area. (That is, each color needs to shade 36 square units.)

<!--more-->

[(fivethirtyeight)](https://fivethirtyeight.com/features/how-often-does-the-senate-vote-in-palindromes/)

![Picture](/img/FourColors.png)

## Solution

See the previous post to learn more about the operation of Google's Constraint Solver that is used here as well.  In a flash we learn that there are 9 solutions with all four colors used and two with only three of the four used.  That's counting solutions as equivalent if colors are merely swapped.

```python
```

<br>
