---
layout: post
published: true
title: Multiverse Carpentry
date: 2021/02/28
---

>**Question**: a regular staircase is built from blocks and the blocks in each level are different colors. The staircase can be built in whatever order that's physically possible. In addition, the surface the stairs are built on is slightly sloped, so that any placed block slides forward until it hits the wall. How many possible ways are there to build a $4$-level staircase? An $n$-level staircase?

<!--more-->

([FiveThirtyEight](URL))

## Solution

I got started by building some staircases. 

For the two level staircase, there's no choice for the first block, we **have** to start with an "A" block, since every other block needs a foundation on which to be placed. Once the first "A" block is placed, we have a choice for what to do second, we can either place the "B" block on top of the first "A" block, or we can place the second "A" block and then place the "B" block last. This makes for a total of $2$ ways to build the $N = 2$ level staircase.

Moving to the three level staircase, we again need to kick things off with an "A" block. From there we can either place a "B" block (on top of the first "A" block) or we can place another "A" block, extending the first level. In the situation where we placed a "B" block second, we now have the option to place a "C" block, or to place another "A" block. 

### Some observations

You can carry on like this, but it gets out of control fast. At this point I noticed a couple of patterns. 

1. we can always place an unplaced "A" block.
2. we can place a "B" block if the number of unplaced "A" blocks is equal to or less than the number of placed "B" blocks (and the same condition for "C" compared to "B").
3. if multiple blocks have legal placements, then form a branch for each possibility.
4. if we have filled out column, say by placing "A-B-C" in a stack, then the remaining $2$ "A" blocks and $1$ "B" block present the same problem as if we had the $2$-stair problem. 
5. if we have $1$ block left, then there's only one way to place it.

On account of the Observation $3$, I started using a notation in hopes to find a recursion: $\Omega(a,b,c)$ is the number of ways that $a$ remaining "A" blocks, $b$ remaining  "B" blocks, and $c$ remaining "C" blocks can be placed in the staircase.

### Using the notation

Let's use the notation to recreate the two stairs result, and get a number for the three stairs result.

**Two stairs**

Starting with $2$ "A" blocks, and $1$ "B" block, we are trying to calculate $\Omega(2,1).$ With no blocks placed, we are obligated to place an "A", so we get

$$ \Omega(2,1) = \Omega(1,1).$$

Since $a = b$ we are free to place an "A" or a "B". According to Observation $2$, this means that

$$ \Omega(1,1) = \Omega(1,0) + \Omega(0,1). $$

According to Observation $5$, $\Omega(1,0)$ and $\Omega(0,1)$ are both equal to $1.$ Altogether, this shows that $\Omega(2,1) = 2.$

**Three stairs**

Now let's do the three stair case, moving a little more quickly this time. We start with $\Omega(3,2,1).$ To start, we're forced to place an "A," so 

$$ \Omega(3,2,1) = \Omega(2,2,1). $$

Now, we can place an "A" or a "B," so we form two branches:

$$ \Omega(2,2,1) = \Omega(1,2,1) + \Omega(2,1,1). $$

By Observations $1$ and $3,$ we get

$$ 
\begin{align}
\Omega(1,2,1) &= \Omega(0,2,1) + \Omega(1,1,1) \\
\Omega(2,1,1) &= \Omega(2,1,0) + \Omega(1,1,1)
\end{align} 
$$

By Observation $4,$ we get $\Omega(0,2,1) = \Omega(2,1,0).$ Also by Observation $4,$ these problems are equivalent to the original $2$ stair case, so $\Omega(2,1,0) = \Omega(0,2,1) = 2.$ Both terms share $\Omega(1,1,1)$ which we carry on calculating. 

Since the agruments are equal, $\Omega(1,1,1)$ gives three choices for placement:

$$ \Omega(1,1,1) = \Omega(1,1,0) + \Omega(1,0,1) + \Omega(0,1,1). $$

Again, each of these has been calculated previously as all are equal to $\Omega(1,1) = 2$ from the two stair problem. 

Propagating back up the chain, this shows that $\Omega(1,1,1) = 6,$ $\Omega(2,1,1) = 8,$ $\Omega(1,2,1) = 8,$ and $\Omega(3,2,1) = \Omega(2,2,1) = 16.$

### Translating

We can translate from the list of observations into a formal rules. For an arbitrary number of stairs, we have

$$ 
\begin{align}
\Omega(a,b,c,\ldots) &= \Omega(a-1,b,c,\ldots) + \Omega(a,b-1,c,\ldots) + \Omega(a,b,c-1,\ldots) + \ldots \\
\Omega(a,b,c,\ldots) &= 0 \text{ if } \min(a,b,c,\ldots) < 0 \\
\Omega(a,b,c,\ldots) &= 0 \text{ if } (a > b + 1)\,\mathbf{OR}\, (b > c + 1)\, \mathbf{OR}\, \ldots
\end{align}
$$

Coding this up (using memoization), we get $\boxed{\Omega(4,3,2,1) = 768}.$

The code easily extends to higher numbers of staircases, and we find:

$$
\begin{array}{|c|c|}\hline
  N & \Omega \\ \hline
  1 & 1 \\ \hline
  2 & 2 \\ \hline
  3 & 16 \\ \hline
  4 & 768 \\ \hline
  5 & 292,864 \\ \hline
  6 & 1,100,742,656 \\ \hline
  7 & 48,608,795,688,960 \\ \hline
\end{array}
$$

Searching the first few terms on the OEIS, this is a known series for the number of ways to build out a triangular Young tableaux. A Young tableaux is a grid shape where numbers are filled out such that they increase long the rows and up the columns which, if we numbered our blocks according to when they were placed, is the case with our staircases as well. So, this makes sense.

There's some very beautiful combinatorics that shows the number of ways to build a Young tableaux for a grid of any shape is equal to the factorial of the number of grid cells, divided by the product of the number of lesser values that each cell sees in its row and column. In our staircase, this means $(2n+1)$ for the first "A" placed, $(2n-1)$ for the second "A" placed, $(2n-3)$ for the third "A", and so on down to $1$ for the last "A" placed. Similarly, starting from the left, the "B" blocks see $(2n-1),$ $(2n-3),$ $\ldots$, $1$ lesser values.

All told, these "lesser values seen leftward and upward" yield $N$ powers of $1$, $(N-1)$ powers of $3,$ $(N-2)$ powers of $5,$ and so on, until the $N^\text{th}$ odd number which has a single power. 

We can check this for the $N=4$ staircase, where the prediction is

$$ \Omega = \dfrac{10!}{1^4\times 3^3\times 5^2\times 7} = 768 $$

as expected. In general, the number of ways to build the $N$ level staircase is

$$ \boxed{\Omega = \dfrac{\binom{N+1}{2}!}{\prod_i (2i-1)^(n-i)}} $$

<br>
