---
layout: post
published: false
title: 
date: 2018/04/21
---

>**Question**: You are walking along a perfectly straight road one day. One hundred feet in front of you, and then another 100 feet to the left of the road, there is a lamppost (see the diagram below). You can’t be sure, but you briefly spot a doppelgänger on the other side of the lamppost, the same distance away. You look again, but now all you see is the lamppost. Perhaps your eyes were playing tricks on you.

You are 100 feet south and 100 feet west of a lamppost. You will be walking 200 feet due east. Meanwhile, there is a doppelgänger who is twice as fast as you, currently 100 feet east and 100 feet north of the same lamppost.
Or perhaps your doppelgänger is now obscured by the lamppost. You start walking along the road, getting closer to the lamppost, but your doppelganger remains hidden. Feeling outmaneuvered, you suspect that your doppelgänger moves precisely twice as fast as you at all times. However, unlike you, they are not constrained to a straight road, and can move more freely in two dimensions.

You walk a total of 200 feet (always forward, never backward), so that the lamppost is now 100 feet back and 100 feet left of the road. Still no sign of the speedy doppelgänger, who is assuredly still obscured by the lamppost.

At this point, you contemplate chasing down the doppelgänger more directly. But before doing so, you wonder: What is the farthest the doppelgänger could be from the lamppost? (Again, assume they move precisely twice as fast as you at all times, that they started symmetrically opposite from you and that they were obscured by the lamppost at all times.)

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-evade-your-evil-twin/))

## Solution

By and large, I decided to forego the learnings of Newton. 

Instead, I wrote an extremely inefficient routine that constantly assess the two points a distance $2\Delta t$ to the doppelganger (that's how far they'd move in one timestep) on the line, and choose the one that increased their distance to the original.

This greedy approach gets the start of the curve but quickly gets the doppelganger into spicy territory, where they can't move quickly enough to stay behind the line. 

This indicated that the greedy approach was a bit too stupid. 

Thinking about a fulcrum, the furthest we can venture vertically is $y = 300\text{ ft}.$ Because the doppelganger and the original make the same angle with the lamppost, the intercept at $y = 300\text{ ft}$ will move at $2 \text{ ft/s}$ (since it is twice as far from the lamppost as the original, who maintains their speed at $1 \text{ ft/s}$), and so, the doppelganger can comfortably move horizontally once they reach $y=300\text{ ft}.$  Moreover, if they go any higher, they'll need to move faster than $2\text{ ft/s}$ simply to keep up with the horizontal position of the line. 

So, they'll be at $y = 300\text{ ft}$ when the line of sight crosses the vertical, at which point they'll have $100\text{ s}$ left. This means they'll end up $200 \text{ ft}$ to the left of the origin, or a total of $\sqrt{(200\text{ ft})^2 + (200\text{ ft})^2} = 200\sqrt{2}\text{ ft}$ away from the original.

!(/img/2021-10-11-doppelganger-path.png)[]{:.width="400 px" class="image-centered"}

<!-- Once we're there, we might be in a tricky spot. How fast do we need to move to stay on the line? To start, the vertical line at 300 ft is moving at $2 \text{ft/s}$ when it passes vertical. But how fast does the intercept at $y = 300\text{ ft}$ move in general?  -->

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import scipy as sp

doppelganger = np.array([100, 200])
o = -100
dt = 0.01

def line(o, x):
  return((o - x) / o * 100)

def find_next(o, current_loc):
  relation = lambda x : (line(o + dt, x) - current_loc[1]) ** 2 + (x - current_loc[0]) ** 2 - (2 * dt) ** 2

  x_initial_guess = current_loc[0]
  x_solution = fsolve(relation, [-2000, 2000])
  return(x_solution)
  
path = []
for o in np.arange(-100, 100, dt):
  sols = find_next(o, doppelganger)
    
  (sol1, sol2) = sols
  starting_distance = np.sqrt((doppelganger[1] - 0) ** 2 + (doppelganger[0] - o) ** 2)

  distance1 = np.sqrt((line(o + dt, sol1) - 0) ** 2 + (sol1 - o) ** 2)
  distance2 = np.sqrt((line(o + dt, sol2) - 0) ** 2 + (sol2 - o) ** 2)

  if doppelganger[1] <= 299.5:
    if distance1 > starting_distance:
      new_x = sol1
    else:
      new_x = sol2
  else:
    new_x = doppelganger[0] - 2 * dt

  new_y = line(o + dt, new_x)

  delta = np.sqrt((doppelganger[0] - new_x) ** 2 + (doppelganger[1] - new_y) ** 2)

  doppelganger = np.array([new_x, new_y])
  path.append(doppelganger)

```


<br>
