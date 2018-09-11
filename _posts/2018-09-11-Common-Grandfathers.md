---
layout: post
published: true
title: Common Grandfathers
date: 9/11/2018
---

>A problem from the 1996 mathematical olympiad of the Republic of Moldova:
>
>Twenty children attend a rural elementary school. Every two children have a grandfather in common. Prove that some grandfather has not less than 14 grandchildren in this school.

<!--more-->

[(futility closet)](https://www.futilitycloset.com/2018/09/11/forefathers/)

## Solution

The key will be to show that there can be at most three grandfathers.  It will follow, given that there are $40$ grandfatherings by $3$ grandfathers, that the minimum number of grandchildren had by the grandfather with the most grandchildren in the class is $\lceil \frac{40}{3} \rceil$, that is, the least integer greater than or equal to a third of forty, which is $14$.

Suppose there are four grandfathers, $a$, $b$, $c$, and $d$. Between them, there are six combinations, which we can write alphabetically as $ab$, $ac$, $ad$, $bc$, $bd$, and $cd$. Notice that if the combination $ab$ is witnessed by a grandchild, then the combination $cd$ cannot be (for then two kids would not share a grandfather).  Similar reasoning establishes that at least one combination in each of these three pairs (which exhaust the combinations) must go unwitnessed:

$$(ab,cd), (ac,bd), (ad,bc)$$

Choosing one combination from each of these pairs to be the witnessed one forces either having one grandfather belong to every student (which obviously we do not want), or leaving one of the grandfathers out. So there is no way to have a fourth grandfather. And we are done.

<br>