---
layout: post
published: false
title: Judging gymnastics
date: 2024/08/11
subtitle: How often are we penalizing our bravest gymnasts?
tags: geometry 
---

>**Question:**

<!--more-->

([Fiddler on the Proof](URL))

## Solution

The premise reasonably claims that each "unit" of execution should be valued based on its difficulty, rather than what's done, which is to crudely add execution and difficulty.

Let's take up the mantle of this alternative scoring system and see how often it would turn the tide. Call the execution and difficulty scores of the two gymnasts $(e_1, d_1)$ and $(e_2, d_2).$

For the two systems to come up with different results, we'd need either player to win in either system. 

Let's say Player 1 wins in the additive scheme and Player 2 in the multiplicative one, then 

$$ e_1 + d_1 > e_2 + d_2, $$

and

$$ e_1 d_1 < e_2 d_2. $$

We can solve either of these for $e_1$ in terms of $e_2$ and the difficulty scores, giving $e_1 + (d_1 - d_2) > e_2 $ and $ e_2 > \frac{d_1}{d_2} e_1 $ which gives us upper and lower bounds on $e_2.$ 

The first one is a line of slope $1$ that leaves the $e_2$-axis from intercept $(d_1 - d_2)$ while the second is a line from the origin with slope $d_1/d_2.$ So, the two bounds approach each other, and form a wedge in $(e_1,e_2)$ space corresponding to Player 1 winning the additive scoring and Player 2 under multiplicative. 

The lines converge at $e_1 = d_2,$ then cross. For $e_1 > d_2,$ the lines bound another wedge region that corresponds to Player 2 winning under additive scoring and Player 1 under multiplicative. 

So, the area corresponding to the multiplicative scheme making a difference are the two triangles in the diagram above. 

The lower triangle has base $(d_1 - d_2)$ and height $d_2$ while the upper triangle has base $(10 - d_1 + d_2 - 10\frac{d_2}{d_1})$ and height $(10-d_1).$

$$ P(\text{winner changes}\rvert d_1,d_2) = \frac{1}{10^2}\left[\frac12(d_1-d_2)d_2 + \frac12(10-d_1)\left(10-(d_1-d_2)-\frac{d_2}{d_1}10\right)\right] $$

which comes to $23/600$ for $(d_1,d_2) = (6,5).$

To find the overall probability of the winner changing, we can integrate over all $d_1$ and $d_2$. The cases for $d_2 > d_1$ are symmetric, so we can just
integrate over $10 > d_1 > d_2$:

$$ 
   \begin{align} 
    P(\text{winner changes}) &= \int\limits_0^{10} \text{d}d_1\int\limits_0^{d_1} \text{d}d_2\, P(\text{winner changes}\rvert d_1,d_2) \\
    &= \frac{1}{12}.
   \end{align}
$$


<br>
