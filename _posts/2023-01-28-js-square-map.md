---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

first of all, the map from one square to the next is 

$$ \left(a,b,c,d\right) \overset{M}{\longrightarrow} \left(\lvert a-b\rvert, \lvert b-c\rvert, \lvert c-d\rvert, \lvert d-a\rvert\right). $$

<!-- from this we can see two properties of the map:

1. the map is  -->

we can follow the map on a couple of squares to get the hang of it

![drawing of squares]()

we want to find the starting configuration that takes the most map iterations to reach the $\left(0,0,0,0\right)$ square. 

from the map, we can see two properties of $f$:

1. $f$ is invariant under uniform translations
  $$ f(a,b,c,d) = f(a+k,b+k,c+k,d+k) $$
2. $f$ is invariant to uniform scaling
  $$ f(a,b,c,d) = f(\gamma a, \gamma b, \gamma c, \gamma d). $$

ggg

<br>
