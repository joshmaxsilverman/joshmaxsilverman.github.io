---
layout: post
published: true
title: Stable tiles
date: 2024/11/17
subtitle: How to defy the laws of physics in service of age 3+ entertainment.
tags: symmetry optimization
---

>**Question**: 
<!--more-->

([Fiddler on the Proof](URL))

## Solution

## Orientation

The seemingly magic behavior of the tiles tell us a lot about how magnets A-H must be oriented. Because they are impervious to rotations, the orientations of A, C, E, and G are the same, as are B, D, F, and H. This symmetry means we can focus on the interactions on one side. How are A and B oriented?

Imagine we stack two tiles so that A is atop A and B is atop B. This is an attractive interaction so it must place N with S. This rules out horizontal arrangements for the magnets. Suppose magnet A was arranged with S on the left and N on the right. Then A on the bottom would have to have the opposite arrangement to A on top, a contradiction.

So, the orientation of the magnets must be vertical. Suppose we arrange A so that N points up and S down. Now, since the interaction is unchanged when we flip one of them, magnet B must have the opposite orientation to magnet A. Putting it altogether, each tiles' magnets are arranged like so:

```
   U — D
  D     U
  |     |
  U     D
   D — U
```

## Stable attachments

Two magnatiles snap tightly together when they're perfectly overlapped.

But if you push them out of this configuration, and slide one tile over the other, you feel attraction to a few other configurations. Likewise, if you try to slide them out of these configurations you'll feel resistance.

This is stability: a configuration is stable if the tiles resist small movements away from it.

The reason a configuration is stable is that, compared to all its neighboring configurations, the N and S magnet heads are as close together as possible while keeping the Ns and the Ns, and the Ss and the Ss as separated as possible. 

To explore other configurations, we just need to translate and rotate one tile while keeping the other one fixed.

But to find alternate configurations, we have to be able to specify them. We can specify a configuration by the displacement of the sliding tile's center of mass $\mathbf{r} = \left(x,y\right)$, and its rotation about its center of mass $\theta.$

Given the arrangement of magnets we figured out in the first past, their orientations are

```mathematica
ors = {1, -1, 1, -1, 1, -1, 1, -1};
```

and their locations on the tile are given by

```mathematica
locs[z_]:= {
   {0.25, 1, z}, {0.75, 1, z}, {1, 0.75, z}, {1, 0.25, z}
   ,{0,75, 0, z}, {0.25, 0, z}, {0, 0.25, z}, {0, 0.75, z}
};
```

where $z$ keeps track of the vertical separation between the planes of the two tiles.

As we said above, sliding the tile around amounts to spinning, and translating all the coordinates of the tile:

```mathematica
rotAndTransLocs[x_, y_, theta_, locs_]:=(
   COM = {0.5, 0.5, 0};
   locsCOM = Table[locs[[j]] - COM, {j, 1, 8}];
   locsCOMRot = RotationMatrix[theta, {0, 0, 1}].locsCOM[[j]], {j, 1, 8}];
   locsRot = Table[locsCOMRot[[j]] + COM, {j, 1, 8}];
   locsRotTrans = Table[locsRot[[j]] + {x, y, 0}, {j, 1, 8}];
   Return[locsRotTrans];
)
```

The interaction between tiles is the sum of the interactions between the magnets on either tile. 

$$ E = \sum\limits_{i,j\in\{A\,\ldots,H\}} \frac{o_io_j}{\ell_{ij}} $$

where the $o$ are the orientations we defined above, and the $\ell$ are the locations we defined above:

```mathematica
   rtl = rotAndTransLocs[x, y, theta, locs[-0.05]];
    E = Sum[
         ors[[i]] * ors[[j]] / Norm[locs[0.05][[i]] - rtl[[j]]]
         , {i, 1, 8}
         , {j, 1, 8}
      ];
```

With all this out of the way, we have the two tiles' interaction energy $E$ parameterized in terms of $x$, $y$, and $\theta$: $E(x,y,\theta).$ This forms a landscape of energies where the depressions in the landscape correspond to the stable arrangements we're trying to find. 

So, to find them we can just follow the gradient, i.e. start at a random initial position $(x,y,\theta)$ and then take small steps in the direction of steepest descent:

$$
   \left(x, y, \theta\right)_t = \left(x, y, \theta\right)_{t-1} - \eta \nabla E(x, y, \theta).
$$

Since there are multiple minima, we'll have to run gradient descent many times, from random starting positions, until we're pretty sure we've found them all (the common ones at least).

Doing this, we find the four confgurations below. 

The first is the original ultra stable configuration with energy $-54.27$. The second features the red tile pushing a side across the corner of the purple tile, until the red side is just past the purple diagonal. This places two pairs of magnets in close proximity for an overall energy of $-13.31$. This is followed closely in third place by an arrangment where adjacent sides overlap so that two monopoles are also in close proximity with overall energy $-12.74$. Finally, there is an arrangement that is basically the second had we stopped sliding the red tile early. This also places two monopoles in close proximity, but loses the long distance attractive interactions of the first two, yielding an overall energy of $-9.34$.

As it happens, these closely match the stable arrangements you find by sliding two magnatiles in real life. It is really neat how well the model works given the monopole approximation.

However, with real magnatiles you'll also find that there is an even more stable arrangement formed by placing two magnatiles side by side. However, as constructed our model cannot find it. The first reason is that our model stipulates the $z$-separation of the tile to be nonzero. The second is that our model puts the monopoles directly at the edge which means there'd be zero distance between the magnets when placed side by side. To accomodate this configuration, we made a second model where the monopoles are pushed in by a small amount from the sides. 

When this is done, we find the original stable arrangements with approximately the same energies, but we can also quantify the stability of the side by side arrangement, which jumps into second place with $E = -25.xx$.

<br>
