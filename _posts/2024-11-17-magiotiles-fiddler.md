---
layout: post
published: false
title: Stable tiles
date: 2024/11/17
subtitle: How to defy the laws of physics in service of 3+ entertainment.
tags: symmetry optimization
---

>**Question**: 
<!--more-->

([Fiddler on the Proof](URL))

## Solution

## Orientation

The seemingly magic behavior of the tiles tell us a lot about how magnets A-H must be oriented. 

Because they are impervious to rotations, the orientations of A, C, E, and G are the same, as are B, D, F, and H.

This symmetry means we can focus on the interactions on one side. How are A and B oriented?

Imagine we stack two tiles so that A is atop A and B is atop B. This is an attractive interaction so it must place N with S. This rules out horizontal arrangements for the magnets. Suppose magnet A was arranged with S on the left and N on the right. Then A on the bottom would have to have the opposite arrangement to A on top. 

So, the orientation of the magnets must be vertical. Suppose we arrange A so that N points up and S down. Now, since the interaction is unchanged when we flip one of them, magnet B must have the opposite orientation to magnet A. 

So, the magnets are oriented like 

```
   U — D
  D     U
  |     |
  U     D
   D — U
```

## Stable attachments

The interaction between tiles is the sum of the interactions between the magnets on either tile. 

$$ E = \sum\limits_{i,j\in\\{A\,\ldots,H\\}} \frac{q_iq_j}{d_{ij}} $$

<br>
