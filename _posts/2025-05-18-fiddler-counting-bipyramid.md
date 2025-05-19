---
layout: post
published: false
title: Can you permeate the bipyramid?
date: 2025/05/18
subtitle: How many paths can you find?
tags:
---

>**Question**:

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-permeate-the-pyramid))

## Solution

the side steps connect the layer nodes with unique paths so they don't icnrease the multiplicity. the overall number of paths is just the product of downward paths at each level. so, 

$$ \Omega(\text{endpoint}, \ell = 6) = 2\times 4\times 6\times 6\times 4\times 2 = 2034. $$

and in general

$$ \Omega(\text{endpoint}, L) = \left(\left(\frac12 L\right)!!\right)^2. $$



$$ \Omega(i, \ell) = \sum\limits_{j\elem\text{layer}}T(i\leftarrow j, \ell)W(j,\ell). $$

$$ W(i, \ell) = \sum\limits_{j\elem\text{last layer neighbors}}\Omega(j, \ell-1). $$

Find $T(i\leftarrow k, \ell)$ by depth first search at each layer.


<br>
