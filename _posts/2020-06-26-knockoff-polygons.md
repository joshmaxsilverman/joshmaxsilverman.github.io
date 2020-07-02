---
layout: post
published: true
title: 
date: 2020/06/29
---

![](/img/2020-06-26-octagons.png){:width="600px" class="image-centered"}

{:.caption}
A set of $339$ unique octagons generated from the same $8$ points.

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

```mathematica
ccw[ptA_, ptB_, ptC_] := (
  Return[(ptB[[1]] - ptA[[1]]) (ptC[[2]] - ptA[[2]]) - (ptC[[1]] - 
       ptA[[1]]) (ptB[[2]] - ptA[[2]])]
  )

intersection[line1_, line2_] := (
  If[Length@DeleteDuplicates@Flatten[{line1, line2}, 1] != 4, 
   Return[False]];
  If[ccw[line1[[1]], line1[[2]], line2[[1]]]*
     ccw[line1[[1]], line1[[2]], line2[[2]]] > 0, Return[False]];
  If[ccw[line2[[1]], line2[[2]], line1[[1]]]*
     ccw[line2[[1]], line2[[2]], line1[[2]]] > 0, Return[False]];
  Return[True];
  )
  
hasNoIntersectionFast[setOfLines_] := (
  pairs = Subsets[setOfLines, {2}];
  For[i = 1, i <= Length@pairs, i++,
   If[intersection[pairs[[i]][[1]], pairs[[i]][[2]]], Return[False]];
   ];
  Return[True]
  )
```

<br>

