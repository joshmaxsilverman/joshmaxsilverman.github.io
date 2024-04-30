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

$$ \left(\ell_e - r\right)^2 - \left(\ell_a(r)^2 + r^2 - 2r\ell_a)r_\cos\theta\right)

<br>
