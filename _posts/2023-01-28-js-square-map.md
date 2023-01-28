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

we want to find the starting configuration $(a,b,c,d)$ that takes the most map iterations to reach the $\left(0,0,0,0\right)$ square. 

from the map, we can see two properties of $f$:

1. $f$ is invariant under uniform translations

$$ f(a,b,c,d) = f(a+k,b+k,c+k,d+k) $$
  
2. $f$ is invariant to uniform scaling

$$ f(a,b,c,d) = f(\gamma a, \gamma b, \gamma c, \gamma d). $$

the second property shows that we can think of $(a,b,c,d)$ as a relative composition (normalize it so that its components sum to $1$). in principle, if we can find a composition $(a,b,c,d)$ that maps back to itself, the value of $f$ would be infinite. 

we will look for such a composition, and then look for the closest integer approximation we can find. the bigger numbers we use, the more closely we should expect to get.

if $(a,b,c,d)$ maps to itself, then, up to an overall multiplicative constant,

$$ (a,b,c,d) = \left(\lvert a-b\rvert, \lvert b-c\rvert, \lvert c-d\rvert, \lvert d-a\rvert\right). $$

<br>
