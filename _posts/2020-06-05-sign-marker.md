---
layout: post
published: true
title: Sign Markers
date: 2020/06/06
---

>You're making a sign using a marker to draw the letters. The marker tip is a circle that's $2\text{ cm}$ across. If you want the marks to be as uniform as possible (as measured by the standard deviation of the ink intensity), and you can't place the tip within $1\text{ cm}$ of where it's previously been, how far apart should you make the marks?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-pinpoint-the-planet/))

## Solution

The major insight here is that the marker leaves ink in proportion to the surface area it has dragged over the surface. If we drag the tip in a straight line, then the ink trail will be most intense at the center, and it will taper to zero intensity $1\text{ cm}$ from the center.

This intensity profile is described by some function $I^\prime(r)$ that's $1$ at the center and zero at the edge. What is it? The relative surface area that the tip drags a distance $r$ from the center is proportional to the length of the chord at that radius. Looking at the diagram, the triangle reveals that $I^\prime(r) \sim 2\sqrt{1-r^2}.$ If we add this up from one edge to the other, we get $\pi,$ so the normalized profile is 

$$I(r) = \frac{2}{\pi}\sqrt{1-x^2}.$$

This shows how the ink trail would look from above:

![aerial view](/img/2020-06-05-tip-intensity.png){: width="300px" class="image-centered"}

{:.caption}
*The intensity of the marker falls decays with the length of the chord that's swept out at radius* $r.$

### Close, but not too close

If we keep a distance of $1\text{ cm}$ between the marker trails, then the sign will be an undulating tapestry of varying intensity, disorienting all who gaze upon it. Overlapping the trails can even it out, but if we bring them too close together, the centers will be very thick and we'll be back in the bad sign hall of fame.

### Overlapping trails

So how far should we make them?

First of all, let's encapsulate the insight from above. If a marker tip is dragged over a point a distance $r_1$ from its center, then the ink intensity on that sport will be $I(r_1).$ By extension, if another tip drags over the same point a distance $r_2$ from its center, then the intensities add:

$$I_\text{total} = I_1(r_1) + I_2(r_2).$$

The standard deviation is equal to the square root of the average value of the squared intensity minus the square of the average intensity. 

$$\sigma^2 = \langle I_\text{total}^2\rangle - \langle I_\text{total}\rangle^2$$

If there's no undulation in the intensity then this will be zero, but if there are peaks and valleys, it will grow. Where is it least?

The average value of the intensity is sum of intensity from one tip center to the other, divided by the distance that separates them:

$$\langle I_\textrm{total}\rangle = \frac{1}{d} \int_0^d dr \left[I_1(r) + I_2(d-r)\right],$$

and the average squared value is

$$\langle I^2_\textrm{total}\rangle = \frac{1}{d} \int_0^d dr \left(I_1(r) + I_2(d-r)\right)^2,$$

and the standard deviation is

$$\sigma = \sqrt{\langle I_\text{total}^2\rangle - \langle I_\text{total}\rangle^2}.$$

We can calculate $\sigma$ like so:

```python
import numpy as np

def I(r, center):
  if 1 - (r - center)**2 >= 0:
    return 2 / np.pi * np.sqrt(1 - (r - center)**2)
  else:
    return 0
  
data = [
        {sep, [I(r, 0) + I(r, sep) for r in np.arange(0, sep, 0.001)]}
        for sep in np.arange(1, 2, 0.001) 
       ]
       
sigmas = np.array([(x, np.stddev(y)) for (x, y) in data])

smoothest_separation = sigmas[np.argmin(sigmas[:, 1])][0]
```

Which gives $d_\text{smoothest} \approx 1.692$ as seen in the plot of $\sigma^2$ vs $d$:

![plot of stddev vs d](/img/2020-06-05-stddev-sep.png){: width="400px" class="image-centered"}

{:.caption}
*The standard deviation is minimized around* $d = 1.69\text{ cm}.$

This is papable if we look at the post as $d$ changes. Bands of light and dark are present at all values, but they're diminished in the neighborhood of $d\approx 1.69\text{ cm}$:

![gif movie 9](/img/2020-06-05-poster-sign-movie-gray.gif){:width="600px" class="image-centered"}

{:.caption}
**Left**: *density plot of ink intensity in a region with a drawn letter.* **Right**: *zoom in on two overlapping marker trails, (red) and (blue) show the profiles of the left and right hand trails, (black) shows their superposition ($I_\text{total}$), and (gold) shows the mean intensity of ink in the letters. Around $d_\text{sep} \approx 1.69,$ the variation of $I_\text{total}$ about the mean is minimized.*

<br>

