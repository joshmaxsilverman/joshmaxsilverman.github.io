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

We can solve either of these for $e_1$ in terms of $e_2$ and the difficulty scores, giving $e_1 - (d_2 - d_1) > e_2 $ and $ e_2 > \frac{d_1}{d_2} e_1 $ which gives us upper and lower bounds on $e_2.$ 

The first one is a line of slope $1$ that leaves the $e_1$-axis from intercept $(d_2 - d_1)$ while the second is a line from the origin with slope $d_1/d_2.$ So, the two bounds approach each other, and form a wedge in $(e_1,e_2)$ space corresponding to Player 1 winning the additive scoring and Player 2 under multiplicative. 

The lines converge at $e_1 = d_2,$ then cross. For $e_1 > d_2,$ the lines bound another wedge region that corresponds to Player 2 winning under additive scoring and Player 1 under multiplicative. 

So, the area corresponding to the multiplicative scheme making a difference are the two triangles in the diagram above. 

The lower triangle has base $(d_2 - d_1)$ and height $d_1$ while the upper triangle has height

<br>
