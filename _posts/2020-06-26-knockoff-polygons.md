---
layout: post
published: true
title: 
date: 2020/06/29
---

![](/img/2020-06-26-octagons.png){:width="600px" class="image-centered"}

{:.caption}
A set of $339$ unique octagons generated from the same $8$ points.

>Suppose you have a pencil and absolutely nothing to do. What is the greatest number of hexagons you can draw using the same $6$ points? What about septagons? What about octagons? What about ...

<!--more-->

([FiveThirtyEight](URL))

## Solution

My basic approach to this problem is to generate all possible sequences of the $6$ vertices, connect the edges, check for intersections, and move on to the next one if an intersection is found. The trick is being able to tell when two lines have an intersection. 

If we draw two lines on a page, it's easy to come up with a condition for the crossing.

$$
\begin{align}
A_1.x &< B_1.x \\
A_1.y &> B_2.y \\
B_2.x &< A_2.y \\
B_1.y &> A_2.y
\end{align}
$$

But this is too naive since, when we generate the points randomly, we won't know what order the points will be in. With a little bit of care we can make it robust to order. 

It's always going to be the case that if we take two points from one of the lines and one point from the other, whichever way we do this, they'll have to have the same orientation (clockwise or counterclockwise). 

So, we can check if the orientations of $\\{A_1,B_1,A_2\\}$ and $\\{A_2,B_2,A_1\\}$ match. That's fine if the edges have the same length. But, if one is longer than the other, we can satisfy this without the lines actually crossing. To take care of that possibility we just have to do the same check for two points of line B and one point from line A.

Our final set of conditions for intersection is 

$$
O(\\{A_1,B_1,A_2\\}) = O(\\{A_2,B_2,A_1\\}) \mathbf{AND} O(\\{B_1,A_1,B_2\\}) = O(\\{B_2,A_2,B_1\\})
$$

```mathematica

intersection[lineA_, lineB_] := (
  If[Length@DeleteDuplicates@Flatten[{lineA, lineB}, 1] != 4, 
   Return[False]];
  If[orientation[lineA[[1]], lineA[[2]], lineB[[1]]]*
     orientation[lineA[[1]], lineA[[2]], lineB[[2]]] > 0, Return[False]];
  If[orientation[lineB[[1]], lineB[[2]], lineA[[1]]]*
     orientation[lineB[[1]], lineB[[2]], lineA[[2]]] > 0, Return[False]];
  Return[True];
  )
```

With that in place, we need a function that can determine the orientation of three points ($+1$ for counterclockwise, $-1$ for clockwise):

```mathematica
  
  ccw[ptA_, ptB_, ptC_] := (
  Return[(ptB[[1]] - ptA[[1]]) (ptC[[2]] - ptA[[2]]) - (ptC[[1]] - 
       ptA[[1]]) (ptB[[2]] - ptA[[2]])]
  )
```



```mathematica  
hasNoIntersectionFast[setOfLines_] := (
  pairs = Subsets[setOfLines, {2}];
  For[i = 1, i <= Length@pairs, i++,
   If[intersection[pairs[[i]][[1]], pairs[[i]][[2]]], Return[False]];
   ];
  Return[True]
  )
```

<br>

