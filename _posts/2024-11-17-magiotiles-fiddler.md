---
layout: post
published: true
title: Stable tiles
date: 2024/11/17
subtitle: How to defy the laws of physics in service of age 3+ entertainment.
tags: symmetry optimization
---

>**Question**: My kids love Magna-Tiles. After some time playing around with them myself, I began to appreciate how they always seem to stick together, regardless of how they are rotated—a property I wouldn’t typically associate with magnets.
>
>Every magnet has a north pole and a south pole. If you have two magnets and put their two north poles together, they repel. But rotate one of the magnets, and now you have a north pole near a south pole, so they’ll attract.
>
>But Magna-Tiles are somehow impervious to rotation. Put one square tile on top of another and they stick together very well. Rotate one of the squares 90 degrees, they still stick. Flip one over, they still stick.
>
>The tiles even stick together (though not as strongly) when placed side by side. Again, rotating or flipping a tile results in the same attraction.
>
>Clearly, the eight magnets embedded along each square’s perimeter must be very cleverly oriented.
>
>Consider the diagram below, which shows eight magnets along a square tile’s perimeter, labeled A through H in a counterclockwise manner. The tile lies in the $x-y$ plane, and the $z-$axis is coming out of the screen toward you.
>
>![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8d559f1-75fa-4177-8d6a-ee2cd0c694c7_1296x880.png){:width="350 px" class="image-centered"}
>
>Given the square tiles’ imperviousness to rotation, what must the orientation of these eight magnets be? For each tile, you should describe the direction from its south pole to its north pole. (More than one answer is possible here.)
>
>**Extra credit**
>When you place one square Magna-Tile perfectly atop another, they stick together really well. Suppose each square has side length 1 unit and a thickness of $0.1$ units.
>
>We can model each tile’s eight magnets as monopoles that are either “north” or “south.” (Yes, I know magnetic monopoles don’t exist, but they’re a sufficient approximation for the following puzzle.) Let’s also assume these monopoles are points, rather than bars. They lie on each edge, one- and three-quarters of the way from one end to the other.
>![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdff3aa5-4976-4965-8805-f9faaf52193e_966x804.png){:width="350 px" class="image-centered"}
>
>Assume that the energy between any two magnetic monopoles is $q_1q_2/r$, where $r$ is the distance between them, and $q_i$ is $+1$ for “north” and $-1$ for “south.”
>
>When one square lies in a plane directly above another (i.e., the planes are parallel and vertically separated by a distance of $0.1$), the lowest-energy arrangement is when the top square is directly above the bottom one. This arrangement is stable, meaning a slight translation or rotation of either square won’t lower the energy. You should assign north vs. south polarity to each monopole on the bottom square based on your work in this week’s Fiddler. The corresponding monopoles on the top square should have the opposite polarity, so that the two squares stick together. If you did this correctly, you should be able to confirm that this arrangement has a magnetic energy between the squares of approximately $-54.27$. (Note: This figure does not include any magnetic energy within a square.)
>
>Your Extra Credit challenge is to determine the stable arrangement with the next-lowest energy. Again, you should assume that the monopoles from one square and the other are vertically separated by $0.1$, but that the squares are otherwise free to translate or rotate in their respective planes.
>
>What is this next-best arrangement, and what is its corresponding magnetic energy between the squares?
>
>(Hint: If you have any Magna-Tiles at home, try making different arrangements with one atop the other and seeing when they stick together.)


<!--more-->

([Fiddler on the Proof](URL))

## Solution

The seemingly magic behavior of the tiles tell us a lot about how magnets A-H must be oriented. Because they are impervious to rotations, the orientations of A, C, E, and G are the same, as are B, D, F, and H. This symmetry means we can focus on the interactions on one side. How are A and B oriented?

Imagine we stack two tiles so that A is atop A and B is atop B. This is an attractive interaction so it must place N with S. This rules out horizontal arrangements for the magnets. Suppose magnet A was arranged with S on the left and N on the right. Then A on the bottom would have to have the opposite arrangement to A on top, a contradiction.

![](/img/2024-11-16-tile-flip.png){:width="450 px" class="image-centered"}

### Orientation

So, the orientation of the magnets must be vertical. Suppose we arrange A so that N points up and S down. Now, since the interaction is unchanged when we flip one of them, magnet B must have the opposite orientation to magnet A. 

![](/img/2024-11-16-tile-fields.png){:width="450 px" class="image-centered"}

Putting it altogether, each tiles' magnets are arranged like so:

![](/img/2024-11-17-tile-orientation-diagram.png){:width="450 px" class="image-centered"}

## Stable attachments

Two magnatiles snap tightly together when they're perfectly overlapped.

But if you push them out of this configuration, and slide one tile over the other, you feel attraction to a few other configurations. Likewise, if you try to slide them out of these configurations you'll feel resistance.

This is stability: a configuration is stable if the tiles resist small movements away from it.

The reason a configuration is stable is that, compared to all its neighboring configurations, the N and S magnet heads are as close together as possible while keeping the Ns and the Ns, and the Ss and the Ss as separated as possible. 

To explore other configurations, we just need to translate and rotate one tile while keeping the other one fixed.

But to find alternate configurations, we have to be able to specify them. We can specify a configuration by the displacement of the sliding tile's center of mass $\mathbf{r} = \left(x,y\right)$, and its rotation about its center of mass $\theta.$

### Setting up the tiles

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

### Rotations and translations

As we said above, sliding the tile around amounts to spinning, and translating all the coordinates of the tile:

```mathematica
locsRotAndTrans[x_, y_, theta_, locs_]:=(
   COM = {0.5, 0.5, 0};

   locsCOM = Table[
               (locs[[j]] - COM)
               , {j, 1, 8}];

   locsCOMRot = Table[
                  RotationMatrix[theta, {0, 0, 1}].locsCOM[[j]]
                  , {j, 1, 8}];

   locsRot = Table[
               (locsCOMRot[[j]] + COM)
               , {j, 1, 8}];

   locsRotTrans = Table[
                     (locsRot[[j]] + {x, y, 0})
                     , {j, 1, 8}];

   Return[locsRotTrans];
)
```

The interaction between tiles is the sum of the interactions between the magnets on either tile. 

$$ E = \sum\limits_{i,j\in\{A\,\ldots,H\}} \frac{o_io_j}{\ell_{ij}} $$

where the $o$ are the orientations we defined above, and the $\ell$ are the locations we defined above:

```mathematica
   locsRT = rotAndTransLocs[x, y, theta, locs[-0.05]];
    E = Sum[
         ors[[i]] * ors[[j]] / Norm[locs[0.05][[i]] - locsRT[[j]]]
         , {i, 1, 8}
         , {j, 1, 8}
      ];
```

### Exploring configuration space

With all this out of the way, we have the two tiles' interaction energy $E$ parameterized in terms of $x$, $y$, and $\theta$: $E(x,y,\theta).$ This forms a landscape of energies where the depressions in the landscape correspond to the stable arrangements we're trying to find. 

For example, if we hold $\theta$ fixed at zero and vary the position of the second tile's center of mass, the energy landscape look like

![](/img/2024-11-18-surface-blue-a.png){:width="450 px" class="image-centered"}

The deep well in the middle is the configuration where the two tiles overlap exactly, and it's surrounded by shallower wells that correspond to lesser stable states.

If, instead, we hold $\theta$ fixed at $\pi/4$ and vary the center of mass, we see a huge repulsive peak at the center that's surrounded by shallow wells 

![](/img/2024-11-18-surface-blue-b.png){:width="450 px" class="image-centered"}

However, these are snapshots at specific values of $\theta$, mere projections of the full space.

In general, we can find the stable configurations by following the gradient downhill — start at a random initial position $(x_0, y_0, \theta_0)$ and then take small steps in the direction of steepest descent:

$$
   \left(x, y, \theta\right)_t = \left(x, y, \theta\right)_{t-1} - \eta \nabla E(x, y, \theta).
$$

Since there are multiple minima, we'll have to run gradient descent many times, from random starting positions, until we're pretty sure we've found them all (the common ones at least).

### Behold the configurations

Doing this, we find the four confgurations below:

![](/img/2024-11-17-grid-no-offset.png){:width="450 px" class="image-centered"}

The first is the original ultra stable configuration with energy $-54.27$. The second features the red tile pushing a side across the corner of the purple tile, until the red side is just past the purple diagonal. This places two pairs of magnets in close proximity for an overall energy of $-13.31$. This is followed closely in third place by an arrangment where adjacent sides overlap so that two monopoles are also in close proximity with overall energy $-12.74$. Finally, there is an arrangement that is basically the second had we stopped sliding the red tile early. This also places two monopoles in close proximity, but loses the long distance attractive interactions of the first two, yielding an overall energy of $-9.34$.

As it happens, these closely match the stable arrangements you find by sliding two magnatiles in real life. It is really neat how well the model works given the monopole approximation.

### Meet the real number two

With real magnatiles you'll also find that there is an even more stable arrangement formed by placing two magnatiles side by side. However, as constructed our model cannot find it. The first reason is that our model stipulates the $z$-separation of the tile to be nonzero. The second is that our model puts the monopoles directly at the edge which means there'd be zero distance between the magnets when placed side by side. To accomodate this configuration, we made a second model where the monopoles are pushed in by a small amount ($\delta = 0.03$) from the edge. 

When this is done, we find the original stable arrangements with approximately the same energies:

![](/img/2024-11-17-grid-offset.png){:width="450 px" class="image-centered"}

but we can also quantify the stability of the side by side arrangement, which jumps into second place with $E = -25.57$:

![](/img/2024-11-17-grid-offset-side.png){:width="300 px" class="image-centered"}

<br>
 
