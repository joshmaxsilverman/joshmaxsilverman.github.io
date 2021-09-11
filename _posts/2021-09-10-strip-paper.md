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

If we multiply this through by x^m y^n and sum it over all values of m and n, we get the function $G(x,y) = \sum\limits{m,n=1}^{\infty} x^my^n\text{cuts}(m,n).$ by design, the coefficient of, e.g., the $x^my^n$ term in this series is equal to expect number of cuts for the $m\times n$ piece of paper. carrying out this sum for both sides:

$$
\begin{align}
G(x,y) &= \sum\limits_{m,n=1}^{\infty} x^my^n + \frac12\sum\limits_{m,n=1}^{\infty} x^my^n\text{cuts}(m,n-1) + \frac12\sum\limits_{m,n=1}^{\infty} x^my^n\text{cuts}(m-1,n) \\
&= \sum\limits_{m,n=1}^{\infty} x^my^n + \frac12xG(x,y) + \frac12yG(x,y),
\end{align}
$$

or 

$$
\boxed{G(x,y) = \dfrac{\frac12\sum\limits{m,n=1}^{\infty} x^my^n}{1-\dfrac{x+y}{2}}
$$

writing out the first few terms in each piece, we get

$$
G(x,y) = \left(1+x+y+xy+x^2y+xy^2+\ldots\right)\cdot\left(1 + \frac{x+y}{2} + \left(\frac{x+y}{2}\right)^2 + \left(\frac{x+y}{2}\right)^3 + \ldots\right)
$$

<br>
