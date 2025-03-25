---
layout: post
published: false
title: 
date: 2025/03/24
subtitle:
tags:
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

the chance player j makes it to level k+1 is the chance they make it to level k times the sum of the chance player i makes it to level k, times the chance they beat player i, over all players i in the other subtree:

$$ P(j\,\text{makes it to level}\, k) = \sum_i P(i\,\text{makes it to}\, k)P(j\,\text{beats}\, i). $$

<br>
