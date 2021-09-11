---
layout: post
published: true
title: Strip Paper
date: 2018/04/21
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

whenever myra cuts a strip from an $m \times n$ sheet of paper, she converts it to an $m \times (n-1)$ or $(m-1) \times n$ sheet of paper, with equal probability. so, the expected number of cuts in the $m \times n$ paper is 1 plus the average number of cuts remaining:

$$
\langle c_{m,n}\rangle = 1 + \frac12 \langle c_{m,n-1}\rangle + \frac12 \langle c_{m-1,n}\rangle.
$$

since the strips short side equal to $1,$ this has base values of $c_{m,1} = c_{1,m} = 0.$

If we multiply this through by $x^m y^n$ and sum it over all values of $m$ and $n,$ we get the function 

$$
C(x,y) = \sum\limits_{m=2}^{\infty} \sum\limits_{n=2}^{\infty} x^my^n \langle c_{m,n}\rangle.
$$

By design, the coefficient of the, e.g., $x^my^n$ term in this series is equal to expect number of cuts for the $m\times n$ piece of paper. Carrying out this sum for both sides:

$$
\begin{align}
C(x,y) &= \sum\limits_{m=2}^{\infty}\sum\limits_{n=2}^{\infty} \left[x^my^n + x^my^n \langle c_{m,n-1}\rangle + x^my^n \langle c_{m-1,n}\rangle\right] \\
&= \frac{x^2y^2}{\left(1-x\right)\left(1-y\right)} + \frac12 xC(x,y) + \frac12 yC(x,y),
\end{align}
$$

or 

$$
C(x,y) = \dfrac{x^2y^2}{\left(1-x\right)\left(1-y\right)} \cdot \dfrac{1}{1-\dfrac{x+y}{2}}
$$

To find the expected number of cuts for an $m\times n$ sheet of paper, we need the coefficient of the $x^my^n$ term in $C(x,y).$

Writing out the first few terms in each piece, we get

$$
\begin{align}
C(x,y) = x^2y^2&\left(1+x+y+xy+x^2y+xy^2+\ldots\right)\cdot\\
&\left[1 + \frac{x+y}{2} + \left(\frac{x+y}{2}\right)^2 + \left(\frac{x+y}{2}\right)^3 + \ldots\right]
\end{align}
$$

What are the contributions to the $x^my^n$ term?

The first series contains one copy of every term $x^my^n,$ so, it is able to promote every term in the second series, from $x^0y^0$ up to $x^{m-2}y^{n-2},$ into a $x^my^n$ term. 

The coefficients of the terms in the second series are the binomial coefficients divided by a power of $2,$ so the $x^my^n$ coefficient of $C(x,y)$ is simply

$$
\boxed{\langle c_{m,n}\rangle = \sum\limits_{m^\prime=0}^{m-2}\sum\limits_{n^\prime=0}^{n-2}\dfrac{\binom{n^\prime+m^\prime}{m^\prime}}}{2^{m^\prime+n^\prime}}
$$

plugging in the values for the $8.5\text{ in}\times 11\text{ in}$ piece of paper, we get

$$\langle c_{9,11}\rangle = \frac{234137}{16384} $$

<br>
