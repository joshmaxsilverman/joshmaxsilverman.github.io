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

whenever myra cuts a strip from an m by n sheet of paper, she converts it to an m by (n-1) or (m-1) by n sheet of paper, with equal probability. so, the expected number of cuts in the m by n paper is 1 plus the average number of cuts remaining:

$$
\text{cuts} (m,n) = 1 + \frac12 \text{cuts}(m,n-1) + \frac12 \text{cuts}(m-1,n).
$$

since the strips short side equal to $1,$ this has base values of $\text{cuts}(m,1) = \text{cuts}(1,m) = 0.$

If we multiply this through by x^m y^n and sum it over all values of m and n, we get the function $G(x,y) = \sum\limits_{m,n=1}^{\infty} x^my^n\text{cuts}(m,n).$ by design, the coefficient of, e.g., the $x^my^n$ term in this series is equal to expect number of cuts for the $m\times n$ piece of paper. carrying out this sum for both sides:

$$
\begin{align}
G(x,y) &= \sum\limits_{m,n=2}^{\infty} \left[x^my^n + x^my^n\text{cuts}(m,n-1) + x^my^n\text{cuts}(m-1,n)\right] \\
&= \frac{x^2y^2}{\left(1-x\right)\left(1-y\right)} + \frac12xG(x,y) + \frac12yG(x,y),
\end{align}
$$

or 

$$
G(x,y) = \dfrac{x^2y^2}{\left(1-x\right)\left(1-y\right)} \cdot \dfrac{1}{1-\dfrac{x+y}{2}}
$$

to find the expected number of cuts for an $m\times n$ sheet of paper, we need the coefficient of the $x^my^n$ term.

writing out the first few terms in each piece, we get

$$
\begin{align}
G(x,y) = x^2y^2\left(1+x+y+xy+&x^2y+xy^2+\ldots\right)\\
&\left(1 + \frac{x+y}{2} + \left(\frac{x+y}{2}\right)^2 + \left(\frac{x+y}{2}\right)^3 + \ldots\right)
\end{align}
$$

the first series contains one copy of every term $x^my^n,$ so, it is able to promote every term in the second series from $x^0y^0$ up to $x^{m-2}y^{n-2}.$ the coefficients of the terms in the second series are the binomial coefficients divided by a power of $2,$ so the $x^my^n$ coefficient of $G(x,y)$ is simply

$$
\boxed{\langle C(m,n)\rangle = \sum\limits_{m,n=2}^{M-2,N-2}\frac{1}{2^{m+n}}\binom{n+m,m}}
$$

plugging in the values for the $8.5\text{ in}\times 11\text{ in}$ piece of paper, we get

$$\langle C(9,11)\rangle = \frac{234137}{16384} $$

<br>
