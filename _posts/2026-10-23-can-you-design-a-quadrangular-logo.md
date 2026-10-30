---
layout: post
published: true
title: Can you design a quadrangular logo?
date: 2026/10/23
subtitle: How long is the set that makes your logo a beautiful arithmetic progression?
tags: geometry probability expectation
source: fiddler
kind: puzzle
theme: geometry
hide_from_recent: true
---

> **Question**: Inspired by Delta Airlines, you and a graphic designer colleague are crafting a new logo for Fiddler Airlines. Your colleague starts with an equilateral triangle with a side length of 1 unit. Next, you pick a random point inside the triangle, giving you four points: the three corners of the triangle and this fourth point inside. There are several ([simple](https://en.wikipedia.org/wiki/Simple_polygon)) quadrilaterals that can be drawn whose four vertices are these four points. Your colleague picks one of these quadrilaterals at random, with each having an equal probability. This quadrilateral will be the new logo.
>
> On average, what can you expect the area of the quadrilateral to be?
>
> **Extra Credit**: While picking random points inside the equilateral triangle with side length 1, you and your colleague notice that some points are “special.” When one of these special points is connected with the triangle’s three vertices, it creates three smaller triangles whose areas form an arithmetic sequence.
>
> After further investigation, you realize these special points all belong to a locus, the total length of which is $L$. What is this length $L$?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-design-a-quadrangular-logo))

## Solution

the way i went about it the standard problem was a straightforward consequence of the extra credit, so we'll do that first.

### Extra credit

the equilateral triangle is defined by three points $\mathbf{p}_1 = \langle -\frac12, \frac{\sqrt{3}}{2}\rangle$, $\mathbf{p}_2=\langle \frac12, \frac{\sqrt{3}}{2}\rangle$, and the origin $\mathbf{o} = \langle 0,0\rangle$ with the variable point $\mathbf{v}=\langle x, y\rangle$. $\mathbf{p}_1$ and $\mathbf{p}_2$ are both of unit length, so $\mathbf{p}_j\cdot\mathbf{p}_j = 1$.

we can divide it into three triangles $A, B$ and $C$ as shown in the diagram.
since the base of each triangle is $1$, the relative area of each triangle is proportional to its height.

![](/img/2026-10-25-fiddler-triangular-logo.png){:width="450 px" class="image-centered"}

we can find the height of triangles $A$ and $B$ by finding the projection of $\mathbf{v}$ along point $\mathbf{p}_1$ and subtracting it from $\mathbf{v}$

$$
	\begin{align}
		h_A &= \mathbf{v} - \left(\mathbf{v}\cdot \mathbf{p}_1\right)\mathbf{p}_1 \\
		h_A^2 &= x^2 + y^2 - \left(-\frac{1}{2}x+\frac{\sqrt{3}}{2}y\right)^2 \\
		&= \frac34 x^2 + \frac14 y^2 + \frac{\sqrt{3}}{2} xy \\
		&= \left(\frac{\sqrt{3}}{2}x + \frac12 y\right)^2
	\end{align}
$$

so that $h_A = \frac{\sqrt{3}}{2} x + \frac12y.$

doing the same calculation for $h_B$ we get

$$ 
	h_B = \frac12 y - \frac{\sqrt{3}}{2}x. 
$$

we can just write down $h_c = \frac{\sqrt{3}}{2} - y$ by inspection of the diagram.

if the triangles form an arithmetic progression, it means we can order them such that the largest and smallest areas differ from the middle area by the same amount 

$$ 
	\{A-r, A, A+r\}. 
$$

if we restrict ourselves to the one sixth of all cases where $x \lt 0$ and $y \gt \frac{1}{2\sqrt{3}}$ (above and to the left of the centroid) then $C$ will be the smallest triangle, $A$ will be second biggest, and $B$ will be biggest.
this means that

$$ 
	h_B - h_A = h_A - h_C. 
$$

writing that down, and solving for $y$ we get

$$ 
	y = -\sqrt{3}x + \frac{1}{\sqrt{3}} 
$$

which is a line from the centroid to some maximal point.
this line describes one sixth of the value for $\mathbf{v}$ that form triangles in an arithmetic progression.

to figure out the length of this line, we can find the value of $x$ that would put $y = \frac{\sqrt{3}}{2}$ (the top of the enclosing equilateral triangle)
this leads to $\frac{\sqrt{3}}{2} + \frac{1}{\sqrt{3}} = -\sqrt{3}x$ or $x=-\frac16.$

this makes the length of this partial locus $\frac16 \ell = \sqrt{\left(\frac16\right)^2 + \left(\frac{\sqrt{3}}{2} - \frac{1}{\sqrt{3}}\right)^2} = \frac13$ which makes the overall length of the locus $\ell = 2.$

### Standard credit

the standard problem asks what the area of the average simple quadraliteral will be.
each simple quadrilateral is formed by leaving out one of the triangles $A, B$, or $C$, so the average area will be the area of the equilateral triangle minus the average area of the missing triangle. 
as the heights are $h_A, h_B$, and $h_C$, the average area of the missing triangle will be $\frac12\frac13\left(h_A + h_B + h_C\right) = \frac16 \frac{\sqrt{3}}{2} = \frac1{4\sqrt{3}}$ which makes the average area of the simple quadrilateral twice that or $\frac{1}{2\sqrt{3}} \approx 0.2887$

### Extra extra credit

we can also ask about the locus of points that form a geometric progression, $h_A = \gamma h_B = \gamma^2 h_C.$


the extremes of this are the centroid itself which produces three triangles with $\gamma 1,$ and the vertices of the triangle with $\gamma = 0$ which produces one triangle with area equal to the equilateral triangle and two with area zero.

we have

$$ \frac{h_B}{h_A} = \frac{h_A}{h_C} $$

or $h_Bh_C = h_A^2.$ 
this leads to 

$$ x^2 + x + y^2-\frac{1}{\sqrt{3}}y = 0. $$

if we complete the squares, this is equivalent to

$$ \left(x + \frac12\right)^2 + \left(y-\frac{1}{2\sqrt{3}}\right)^2 = \frac13. $$

which is a circle center at $\left(-\frac12, \frac{1}{2\sqrt{3}}\right)$ of radius $1/\sqrt{3}.$ 
so we have an arc through two vertices and the centroid.
there are two equivalent arcs rotated $2\pi/3$ and $4\pi/3$ through the other two vertex pairs.

this locus is rendered beautifully below.

![](/img/2026-10-29-fiddler-triangular-logo-geometric.png){:width="450px" class="image-centered"}


<br>
