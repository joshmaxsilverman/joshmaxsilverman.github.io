---
layout: post
published: false
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

([Jane Street](https://www.janestreet.com/puzzles/current-puzzle/))

## Solution

though aaron can move however he likes, not having any angular information, anything he does will be averaged over all angles relative to the target. so, his strategy must be to move a given distance from the center. knowing the radius of the target, he can pick the best value $\ell_a(r)$ for each value of $r.$

so, without losing generality, we can put aaron at radius $\ell_a(r)$ along $\theta=0$ and erin will be at distance $\ell_e$ at the angle of the target, $\theta_T.$

with this context, we can outline aaron and erin's planning.

### planning

- for each value of $r$, $\theta,$ $\ell_e,$ and $\ell_a(r)$ aaron can calculate the probability that he wins a round. after averaging this probability over $\theta$ (because he doesn't know it), he can pick the optimal value for $\ell_a(r).$ averaging this over all values of $r$ after this he will know his expected winning percentage given a value for $\ell_E$
- knowing this, erin can calculate the same and minimize it with respect to $\ell_e$
- all together, this ensures that aaron will do the best he can, given that erin is minimizing him perfectly. if either one of them deviates from the resulting $\ell_e$ and $\ell_a(r),$ the other will do even better.

in general, erin has the advantage since she at least moves in the direction of the target, even if she passes it. if aaron chooses to move, there is a $50\%$ chance that he furthers himself from it, and even still, he will still be at a disadvantage.

### finding $P(\text{Aaron wins}\rvert r,\ell_e)$

still, for any given $(r, \ell_e)$ there will be a range of target angles $\theta$ such that aaron ends up closer to it.

aaron is closer to the target when erin's squared distance minus aaron's squared distance is positive:

$$ \left(\ell_e - r\right)^2 - \left(\ell_a(r)^2 + r^2 - 2r\ell_a(r)\cos\theta\right) > 0. $$

we can solve for the $\theta$ where this switches from positive to negative and get 

$$ \theta_+ = \cos^{-1} \frac{2r\ell_e - \ell_e^2 + \ell_a(r)^2}{2\ell_a(r)r}. $$

aaron will win whenever $-\theta_+ < \theta < \theta_+,$ so the probability he wins is just 

$$ 
  \begin{align} 
    P(\text{Aaron wins}\rvert r,\ell_e) &= \frac{2\theta_+}{2\pi} \\
    &= \frac{1}{\pi}\cos^{-1} \frac{2r\ell_e - \ell_e^2 + \ell_a(r)^2}{2\ell_a(r)r}
  \end{align}
$$

with this, we can find aaron's optimal value of $\ell_a(r).$ setting the derivative with respect to $\ell_a(r,)$ equal to zero and solving for $\ell_a(r),$ we get

$$ \ell_a(r) = \sqrt{\ell_e(2r-\ell_e)}. $$

this is the optimal policy for aaron, and it is zero for $\ell_e > 2r.$ this makes sense since if $\ell_e$ is more than $2r$ from the origin, aaron doesn't have to muck about with moving, he will be closer to the target if he just stays put at the origin.

< plot of l_a(r) vs r for several values of l_e >

so, aaron's probability to win given $r$ is

$$ P(\text{Aaron wins}\rvert r,\ell_e) = \frac{1}{\pi}\sec^{-1} \frac{r}{\sqrt{\ell_e(2r-\ell_e)}}. $$

all that's left is to average it over all possible radii. the probability of a given radius is the area of the annulus of radius $r$ relative to the area of the circle, $2\pi r\, dr/\pi = 2r\,dr.$

this gets us 

$$ P(\text{Aaron wins}\rvert \ell_e) = \int\limits_0^1\,dr 2r P(\text{Aaron wins}\rvert r,\ell_e) $$

now, when $2r<\ell_e$ aaron is guaranteed to win, so we can split up the integral to the interval from $r=0$ to $\frac12\ell_e$ and the interval from $\frac12\ell_e$ to $1.$

the first half is just $\frac14\ell_e^2.$ the second half is more complicated, and i couldn't find an analytic expression for it. 

so 

$$ P(\text{Aaron wins}\rvert r,\ell_e) = \frac14\ell_e^2 + \int\limits_{\frac12\ell_e}^1\,dr 2r \frac{1}{\pi}\sec^{-1} \frac{r}{\sqrt{\ell_e(2r-\ell_e)}}. $$

thankfully for erin, we can minimize this numerically.

<plot of numerical result>

### finding $\ell_e^*$

in complete possession of all this information, erin calculates the same expression and is now tasked with optimizing. a practical person, she chooses interval halving.

```mathematica
policy[le_] := 
  le^2/4 + 

NIntegrate[ArcCos[Sqrt[-le (le - 2 r)]/r]/π 2 r, {r, le/2, 1}];
FindMinimum[policy[le], {le, 0.5}]

---

{0.1661864864740085199460374511368681039851926960842942958672125424901\
0065334172239, {le -> 
   0.50130699421275306976228988957319879985763547355821149107985261064\
716190275921967}}
```

so, the best aaron can manage is to win $\approx 16.619\%$ of the time and erin's optimal distance is $\ell_e^* \approx 0.50131.$

<br>
