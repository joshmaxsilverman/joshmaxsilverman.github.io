---
layout: post
published: false
title: Crescent Observatory
date: 2021/04/18
---

>**Question**: 

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-crack-the-case-of-the-crescent-moon/))

## Solution

The reason we don't see the Moon during the day because it's on the other side of the Earth. The Moon takes $\sim 30$ days to orbit Earth, so we are effectively sampling it once a day throughout its orbit. 

The reason we see the Moon at night is that it's illuminated by the Sun. Since the Moon's orbital plane isn't the the plane of Earth's orbit around the Sun, sunlight fully illuminates one side of the Moon.

The reason that Moon's shape seems to change throughout the month is that its illuminated half changes the angle it makes with Earth. When Moon, Earth, and Sun we perfectly lined up (in that order), we see a full Moon. 

Finally, since the Moon's orbit takes a fixed amount of time, the angle that the Moon-Sun line makes with Earth varies uniformly throughout the month.

### Patchwork Moon

If we want to measure the illuminated area of the Moon, we can divide the Moon up into patches, and count which ones are lit up. 

First, let's worry about the surface area of the patch, i.e., the area it would present to us if we looked at it flat. 

We can introduce some coordinates to measure along the surface. First of all, the patch is located at some angle $\phi$ away from the direct line of sight from Earth to the center of the Moon. Additionally, it is located at another angle $\theta$ above the equator established by the line of sight from Earth. The patch itself has some angular extent $d\phi$ and $d\theta.$ Even thought the Moon is curved, since these angles are small, the patch is effectively a rectangle, and its area is just $r\,d\theta$ by $r\cos\theta\,d\phi,$ or $dA = r^2\cos\theta\,d\theta\,d\phi.$ 

### Tilting at patches

Now, we don't see the patches straight on from where we are Earth. Instead, we see them tilted by the angles $\theta$ and $\phi.$ As we'll see below, this affects the projected $2\text{D}$ area we see from Earth in a simple way.

To get started, take a book and stand it up perpendicular to the ground. This is the area $dA.$

Now, tilt the book backward so that it makes some angle $\theta$ with the ground. This will preserve the width of the book while shortening the height to $\cos\theta$ times its original height.

<br>
