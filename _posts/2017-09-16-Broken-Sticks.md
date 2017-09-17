---
layout: post
published: true
title: Breaking Sticks
---

>1. If you break a stick in two places at random, forming three pieces, what is the probability of being able to form a triangle with the pieces?
>2. If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form a triangle with them?
>3. If you break a stick in two places at random, what is the probability of being able to form an acute triangle — where each angle is less than 90 degrees — with the pieces?
>4. If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form an acute triangle with the sticks?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/will-you-be-a-ghostbuster-or-a-world-destroyer/))

## Solutions

This group of puzzles has the interesting feature that they initially seem geometric---to do with stick triangles---then quickly turn into problems about random numbers, which in turn admit of simple solutions that employ geometry---but not the geometry of stick triangles!

### 1

>1. If you break a stick in two places at random, forming three pieces, what is the probability of being able to form a triangle with the pieces?

This sounds like a question about geometry, but it turns out to be a question about numbers that is most simply construed as a _different_ question about geometry. The question is, if $x$ and $y$ are random numbers between $0$ and $1$ (with the obvious unstated assumption that the distribution of probabilities is uniform), how likely is it that the difference between them and $0$ and $1$ are such that none is greater than the sum of the other two? If $x$ is less than $y$, those differences are $x$, $y-x$, and $1-y$. We can focus on that case because the other case is symmetrical, just swapping $y$ for $x$. The three constraints are:

$$ x < (y-x) + (1-y) \rightarrow x < 1/2$$

$$ y-x < x + (1-y) \rightarrow y < x+1/2$$

$$ 1-y < x+ (y-x) \rightarrow y > 1/2$$

Each of these inequalities tells us that the points in the $x-y$ plane lie to one side of a straight line. Together they determine a triangle of area $1/8$ (it's half of a quarter of the unit square). 

![Broken sticks that form a triangle.](/img/BrokenSticks1.png)

Since our assumption that $x>y$ determines a region of area $1/2$, and the case of $y>x$ is symmetrical, we conclude that the proportion of $(x,y)$ pairs suited to making triangles is $1/4$.

### 2

>2. If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form a triangle with them?

Now we've got three numbers, $x$, $y$, and $z$, so we are working in the unit cube. Each of the three constraints now tell us that the triangle-making points is on one side of a plane:

$$ x < y+z$$

$$ y < x+z$$

$$ z < x+ y$$

These planes each "lop off" a pyramidal corner of the cube (non-overlapping ones, because at most one of the inequalities can be false). 

![Lopped off cube corner.](/img/BrokenSticks2.png)

For instance, the first lops off the pyramid that has the cube corner $(1,0,0)$ as its apex and the three adjacent corners as the corners of its triangular base. The volume of any pyramid is one-third of the base area times the height.  The base area is $1/2$ and the height is $1$, so the lopped-off volume is $1/6$. Three of these lop off a volume of $1/2$, and so we conclude that half of the triples of random lengths allow us to form a triangle.

### 3

>3. If you break a stick in two places at random, what is the probability of being able to form an acute triangle — where each angle is less than 90 degrees — with the pieces?

We're back to the unit square in the $x-y$ plane, and again assuming that we're in the $1/2$ probability region where $x<y$, if we can form any triangle, the point $(x,y)$ has to be inside the triangle we found in the first problem. Acuteness forces three new constraints, because each side of the triangle has to be too short to be the hypotenuse of a right triangle:

$$x^2 < (y-x)^2 + (1-y)^2 \Longleftrightarrow x < y + \frac{1}{2y} -1$$

$$(y-x)^2 < x^2 + (1-y)^2 \Longleftrightarrow y < \frac{1}{2-2x} $$

$$(1-y)^2 < x^2 + (y-x)^2$$

These tell us that the triangle-prone points are inside a curvy triangle formed by three hyperbolas.

![Curvy triangle.](/img/BrokenSticks3.png)

The three areas trapped between the hyperbolas and the outer triangle must have equal areas. The right-most and lowest regions are obviously simple translations of each other. The upper-left and rightmost regions are not, but they have the same width (in the $x$ dimension) at every value of $y$ (namely $1/(2y) - 1/2$), and therefore, by the ever-useful [Cavalieri's Principle](https://en.wikipedia.org/wiki/Cavalieri%27s_principle), have the same area.

So it will suffice to find the area of one of them, and we will focus on the upper left. That hyperbola (which has the equation $(1-x)y = 1/2$) is just the ordinary $xy=1$, except scaled linearly by a factor of $1/\sqrt{2}$, mirrored about the $y$ axis, and shifted to the right by $1$. Thus the area in question is half of the area of the geometrically similar region in the hyperbola $xy=1$.

![Translated to unit rectangular hyperbola.](/img/BrokenSticks3a.png)

The area of the shaded region (called a [hyperbolic sector](https://en.wikipedia.org/wiki/Hyperbolic_sector)) is the natural logarithm of the $x$ coordinate of point $A$; so it is $\ln(\sqrt{2})$, or $\ln(2)/2$. The area of the triangle $\triangle OAB$ is $\overline{AM}$ times $\overline{OM}$, or $1/2$ times $3/2$, or $3/4$. so the area of the trapped region of interest is $\frac{3}{4} - \ln(2)$. Scaling that back to actual size, we get:

$$ \frac{3}{8} - \frac{\ln(2)}{2}$$

Thus, the area of the curvy triangle is the area of the straight triangle minus three of those regions:

$$\frac{1}{8} - 3\left(\frac{3}{8} - \frac{\ln{2}}{2}\right) = \frac{3\ln{2}}{2} - 1$$

And the proportion of the region of area $1/2$ in which $x<y$ that it occupies, and hence the probability that we can form an acute triangle, is twice that, or:

$$3\ln{2}-2 \approx .07944$$

(The one somewhat arcane fact we've relied on is that the area of a hyperbolic sector of $y=1/x$ is the natural logarithm of its greatest $x$ coordinate. To deduce that from scratch, we'd have to rely on a little calculus, namly the fact that the integral of $1/x\ dx$ is $\ln(x)+C$.)

### 4

>4. If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form an acute triangle with the sticks?

Let the lengths of the sticks be $x$, $y$, and $z$, where $z$ is the largest of the three. They form an acute triangle so long as this inequality holds:

$$A: x^2 + y^2 > z^2$$

If we think of the space of possible triples $(x, y, z)$ as points in the unit cube, then we can think of the constraint that $z$ is the largest as meaning that the point lies in the volume $1/3$ portion $P$ of the cube in which $z$ is greater than both $x$ and $y$. And we can think of the inequality $A$ as meaning that the point must lie outside of the cone $z^2=x^2+y^2$ (whose intersection with the cube is entirely within $P$).

![Cone cuts through cube.](\img\BrokenSticks4.png)

The volume inside $P$ that is also inside the cone is a one-quarter pie-slice of a cone of height $1$ and base radius $1$. The volume of a cone is $\pi r^2 h/3$, and so the volume of the region outside of the cone in $P$ is:

$$\frac{1}{3} - \frac{\pi}{12}$$

Multiplying by three to account for points where $x$ or $y$ is the largest coordinate, we find that the volume within the unit cube of all points lying outside the cone determined by the largest of the point's coordinates is:

$$1 - \frac{\pi}{4} \approx 21.46\%$$

### Empirical Verification

For sanity-checking, the following Python code agrees with the above results:

```
from random import random
Reps = 10000000
Accum = [0,0,0,0]
for _ in range(Reps):
	a,b,c = random(),random(),random()
	x,y = min(a,b),max(a,b)
	v,u,w = x,y-x,1-y
	S = [a,b,c]
	S.sort()
	Accum[0] += not (x > .5 or y < .5 or y-x <.5)
	Accum[1] += a < b+c and b<a+c and c<a+b
	Accum[2] += w**2<v**2+u**2 and u**2<v**2+w**2 and v**2<u**2+w**2
	Accum[3] += S[2]**2 < S[0]**2+S[1]**2
print [1.0*Accum[i]/Reps for i in range(4)] 
```

<br>
