---
layout: post
published: true
title: Capture the Flag
subtitle: How often can you win when you have a number and they have an arrow?
tags: geometry game-theory expectation
date: 2024/05/01
---

>**Question**: It’s been a while and change, but the Robot Games are back once again. This time it’s Capture the Flag!
>
>Two robots, Aaron and Erin, have made it to this year’s final! Initially they are situated at the center of a unit circle. A flag is placed somewhere inside the circle, at a location chosen uniformly at random. Once the flag is placed, Aaron is able to deduce its distance to the flag, and Erin is only able to deduce its direction to the flag. (Equivalently: if $(r, \theta)$ are the polar coordinates of the flag’s location, Aaron is told $r$ and Erin is told $\theta.$)
>
>Both robots are allowed to make a single move after the flag is placed, if they wish. Any move they make is without knowledge of what the other robot is doing. (And they may not move outside the circle.)
>
>Whichever robot is closer to the flag after these moves captures the flag and is declared the winner!
>
>During the preliminaries it was discovered that Erin is programmed to play a fixed distance along the detected angle $\theta.$ Assuming otherwise optimal play by both robots, can you determine the probability that Aaron will win? 
<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/robot-capture-the-flag-index/))

## Solution

Though Aaron can move however he likes, not having any angular information, anything he does will be averaged over all angles relative to the target. So, his strategy must be to move a given distance from the center. Knowing the radius of the target, he can pick the best value $\ell_a(r)$ for each value of $r.$

So, without losing generality, we can put Aaron at radius $\ell_a(r)$ along $\theta=0$ and Erin will be at distance $\ell_e$ at the angle of the target, $\theta_T.$

With this context, we can outline Aaron and Erin's planning.

### Planning

- For each value of $r$, $\theta,$ $\ell_e,$ and $\ell_a(r)$ Aaron can calculate the probability that he wins a round. After averaging this probability over $\theta$ (because he doesn't know it), he can pick the optimal value for $\ell_a(r).$ Averaging this over all values of $r$ after this he will know his expected winning percentage given a value for $\ell_e$
- Knowing all this, Erin can calculate the same and minimize it with respect to $\ell_e,$ (which Aaron can and will also do).
- All together, this ensures that Aaron will do the best he can, given that Erin is minimizing him perfectly. If either one of them deviates from the resulting $\ell_e$ and $\ell_a(r),$ the other will do even better.

In general, Erin has the advantage since she at least moves in the direction of the target, even if she passes it. If Aaron chooses to move, there is a $50\%$ chance that he furthers himself from it.

### Finding $P(\text{Aaron wins}\rvert r,\ell_e)$

Still, for any given $(r, \ell_e)$ there will be a range of target angles $\theta$ such that Aaron ends up closer to it.

Aaron is closer to the target when Erin's squared distance minus Aaron's squared distance is positive:

$$ \left(\ell_e - r\right)^2 - \left(\ell_a(r)^2 + r^2 - 2r\ell_a(r)\cos\theta\right) > 0. $$

We can solve for the $\theta$ where this switches from positive to negative and get 

$$ \theta_+ = \cos^{-1} \frac{2r\ell_e - \ell_e^2 + \ell_a(r)^2}{2\ell_a(r)r}. $$

Aaron will win whenever $-\theta_+ < \theta < \theta_+,$ so the probability he wins is just 

$$ 
  \begin{align} 
    P(\text{Aaron wins}\rvert r,\ell_e) &= \frac{2\theta_+}{2\pi} \\
    &= \frac{1}{\pi}\cos^{-1} \frac{2r\ell_e - \ell_e^2 + \ell_a(r)^2}{2\ell_a(r)r}.
  \end{align}
$$

With this, we can find Aaron's optimal value of $\ell_a(r).$ Setting the derivative with respect to $\ell_a(r,)$ equal to zero and solving for $\ell_a(r),$ we get

$$ \ell_a(r) = \sqrt{\ell_e(2r-\ell_e)}. $$

This is the optimal policy for Aaron, and it is zero for $\ell_e > 2r.$ This makes sense since if $\ell_e$ is more than $2r$ from the origin, Aaron doesn't have to muck about with moving, he will be closer to the target if he just stays put at the origin.

![](/img/2024-05-02-leplot.gif){:width="350px" class="image-centered" }

So, Aaron's probability to win given $r$ is

$$ P(\text{Aaron wins}\rvert r,\ell_e) = \frac{1}{\pi}\cos^{-1} \frac{\sqrt{\ell_e(2r-\ell_e)}}{r}. $$

All that's left is to average it over all possible radii. The probability of a given radius is the area of the annulus of radius $r$ relative to the area of the circle, $2\pi r\, dr/\pi = 2r\,dr.$

This gets us 

$$ P(\text{Aaron wins}\rvert \ell_e) = \int\limits_0^1\,dr\, 2r\, P(\text{Aaron wins}\rvert r,\ell_e) $$

Now, when $2r<\ell_e$ Aaron is guaranteed to win, so we can split up the integral to the interval from $r=0$ to $\frac12\ell_e$ and the interval from $\frac12\ell_e$ to $1.$

The first half is just $\frac14\ell_e^2.$ The second half is more complicated, and I couldn't find an analytic expression for it. 

So 

$$ P(\text{Aaron wins}\rvert \ell_e) = \frac14\ell_e^2 + \int\limits_{\frac12\ell_e}^1\,dr\, 2r\, P(\text{Aaron wins}\rvert r, \ell_e). $$

![](/img/2024-05-02-P_aaron.png){:width="350px" class="image-centered" }

### Finding $\ell_e^*$

In complete possession of all the same information, Erin also calculates the expression and is now tasked with optimizing it. Thankfully, it can be done numerically.

A practical person, she chooses interval halving.

```mathematica
aaronWinProb[le_] := 
  le^2/4 + NIntegrate[2 r ArcCos[Sqrt[le (2r - le)] / r]/π, {r, le/2, 1}];

FindMinimum[aaronWinProb[le], {le, 0.5}]

```

So, the best Aaron can manage is to win $\approx 16.61864864740\%$ of the time and Erin's optimal distance is $\ell_e^* \approx 0.50130699421.$

<br>
