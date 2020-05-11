---
layout: post
published: true
title: Apple Bites
date: 2020-04-12
---

>A spherical cap is a portion of the sphere's surface bounded by a circle. Given a sphere of radius $R$, how many randomly-placed caps are needed on average to cover the sphere? Assume each cap measures $R/2$ across its curved surface. (See the original framing in terms of bites of an apple at the link below.)

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/can-you-eat-an-apple-like-a-toddler/))

## Solution

This seems to be an explored, but unsolved problem in math, and so perhaps a wee bit unfair to pose as a "Riddle!" There are published results about bounds and limits, but rather than dig into those, let's just do a simulation and get a ballpark answer.

The simulation makes two simplifications: first, that there are a finite number of points on the surface (in particular, $500^2$), and second, that the surface is not a sphere at all but a 2-dimensional flat, square space that is wrapped around like a cylinder, except in both dimensions (like a torus topologically), so that a circle placed on it that goes past the right (or top) edge covers also part of the left (or bottom) part of the square. This surface is like a sphere in that apart from an arbitrary (in this case $(x,y)$) coordinate system, there really are no distinguished points, but its geometry is different (e.g., familiar Euclidean principles are true of its triangles, unlike those on a sphere). This makes things simpler because, unlike on a sphere, there is a very natural way to evenly populate this surface with $500^2$ points, i.e., in a $500 \times 500$ grid, and also because we can drop circles on it rather than three-dimensional caps. 

We'll randomly drop circles onto this surface, where the ratio of the area of a circle to that of the surface is the same as that of a cap to the sphere as specified in the problem.

Using the code below, the $1000$-repetition average was about $567$ (and not very stable at that many reps). Surprisingly high!

```python
from random import randint
from math import sqrt,pi,cos

resolution = 500
reps = 1000

pointsList = [(x,y) for x in range(resolution) for y in range(resolution)]

def distance(p1,p2):
  return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

r = sqrt((1-cos(.25))*resolution**2/(2*pi))

deltas = set([])
for x in range(int(-r),int(r+1)+1):
  for y in range(int(-r),int(r+1)+1):
    if distance((x,y),(0,0)) <= r:
      deltas.add((x,y))

accum = 0

for rep in range(reps):
  remainingPoints = set(pointsList)
  nBites = 0
  while bool(remainingPoints):
    nBites += 1
    x,y = randint(0,resolution), randint(0,resolution)
    for delta in deltas:
      pointToNuke = ( (x+delta[0])%resolution, (y+delta[1])%resolution )
      remainingPoints.discard(pointToNuke)
  accum += nBites
print("Average bites in",reps,"reps:",accum/reps)
```

<br>