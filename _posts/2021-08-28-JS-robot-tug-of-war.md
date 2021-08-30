---
layout: post
published: true
title: Robot Tug of War
date: 2021/08/28
---

>**Question**: The Robot Weightlifting World Championship was such a huge success that the organizers have hired you to help design its sequel: a Robot Tug-of-War Competition!
>
>In each one-on-one matchup, two robots are tied together with a rope. The center of the rope has a marker that begins above position 0 on the ground. The robots then alternate pulling on the rope. The first robot pulls in the positive direction towards 1; the second robot pulls in the negative direction towards $-1.$ Each pull moves the marker a uniformly random draw from $\left[0,1\right]$ towards the pulling robot. If the marker first leaves the interval $\left[-\frac12,\frac12\right]$ past $\frac12,$ the first robot wins. If instead it first leaves the interval past $-\frac12,$ the second robot wins.
>
>However, the organizers quickly noticed that the robot going second is at a disadvantage. They want to handicap the first robot by changing the initial position of the marker on the rope to be at some negative real number. Your job is to compute the position of the marker that makes each matchup a $50:50$ competition between the robots. Find this position to seven significant digits—the integrity of the Robot Tug-of-War Competition hangs in the balance!

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/current-puzzle/))

## Solution

First, let's get acquainted with the setup. 

![](/img/2021-08-28-tug-of-war-diagram.png){:width="450 px" class="image-centered"}

Each robot pulls the middle of the rope toward their side a random distance between $0$ and $1.$ If the first player gets it past $\frac12,$ then they win (and likewise for Player 2). 

<!-- This means that each player has the potential to end the game in one turn (since $\frac12 - \left(-\frac12\right) = 1$).  -->

If it's Player 1's turn, they can win the game in one of two ways:

1. they can immediately move the game past $+\frac12,$ or
2. they can move somewhere less than $\frac12,$ and then go on to win.

For the second way to happen, Player 1's first move will have to go somewhere to the right that's less then $\frac12,$ then Player 2 will have to move somewhere to the left that's more than $-\frac12,$ and then go on to win. 

$$
P_\text{win}(x) = P(\text{win immediately})(x) + P(\text{win eventually})(x).
$$

If they win immediately, Player 1 has to move beyond $\frac12$ which has probability $1 - (\frac12 - x),$ so

$$
P(\text{win immediately})(x) = \frac12 + x.
$$

If they win eventually, Player 1 has to move somewhere less then $\frac12,$ then Player 2 has to move somewhere greater than $-\frac12,$ and then Player 1 has to win from there. 

$$
\begin{align}
P(\text{win eventually})(x) &= P(x\rightarrow\text{somewhere}\rightarrow\text{somewhere else})\cdot P_\text{win}(\text{somewhere else}) \\
&= P(x\rightarrow\text{somewhere})\cdot P(\text{somewhere}\rightarrow\text{somewhere else})\cdot P_\text{win}(\text{somewhere else})
\end{align}
$$

We nearly have an equation for $P_\text{win}(x),$ we just need to sum over all the possibilities for $\text{"somewhere"}$ ($x_1$) and $\text{"somewhere else"}$ ($x_2$).

$$
P_\text{win}(x) = \frac12 + x + \int dx_1 P(x\rightarrow x_1) \int dx_2 P(x_1\rightarrow x_2)P_\text{win}(x_2).
$$

From the diagram below, $x_1$ can take on any value from $x$ to $\frac12$ without ending the game. Likewise, $x_2$ can take any value from $x_1$ down to $-\frac12.$ 

![](/img/2021-08-28-tug-of-war-integration-bounds.png){:width="450 px" class="image-centered"}

Since $P(x_0\rightarrow x_1$)$ and $P(x_1\rightarrow x_2)$ are uniform probabilities on the unit interval, we get:

$$
P_\text{win}(x) = \frac12 + x + \int\limits_x^{\frac12} dx_1 \left[\int\limits_{-\frac12}^{x_1} dx_2 P_\text{win}(x_2)\right].
$$

This is an integral equation for $P_\text{win}(x),$ but we can solve it without resorting to, e.g., kernel methods.

Taking the derivative with respect to $x,$ we get

$$
\frac{\partial}{\partial x}P_\text{win}(x) = 1 - \int\limits_{-\frac12}^{x} dx_2 P_\text{win}(x_2).
$$

Taking another, we get

$$
\frac{\partial^2 }{\partial x^2} P_\text{win}(x) = - P_\text{win}(x).
$$

So, the general form for $P_\text{win}(x)$ is, incredibly, the sum of sinusoids

$$
P_\text{win}(x) = A\sin x + B\cos x.
$$

When the game starts at $x=\frac12,$ the chance that Player 1 wins is $1.$ This means that $A\sin\frac12 + B\cos\frac12 = 1.$

We also have the first derivative of the integral equation, that has to be satisfied:

$$
\begin{align}
A\cos x - B\sin x &= 1 - \left[-A\cos x + B\sin x +A\cos\frac12 + B\sin\frac12\right] \\
&= 1 + A\cos x - B\sin x - A\cos\frac12 - B\sin\frac12
\end{align}
$$

or $1 = A\cos\frac12 + B\sin\frac12.$

Putting these together, we have $A = B = \left(\sin\frac12 + \cos\frac12\right)^{-1},$ and

$$
P_\text{win}(x) = \dfrac{\sin x + \cos x}{\sin\frac12 + \cos\frac12}.
$$

This can be written more tidily as a single $\cos$ term. Using the complex representation

$$
\begin{align}
A\sin x + B\cos x &= \Re\left(Ae^{ix} + Be^{i(x - \frac{\pi}{2})}\right) \\ 
&= \Re\left(e^{ix}\left[A - iB\right]\right) \\
&= \Re(e^{ix}\sqrt{A^2 + B^2}e^{i\phi}) \\
&= \sqrt{A^2 + B^2}\cos{(x-\phi)}
\end{align}
$$

where $\phi = \cos^{-1}\frac{A}{\sqrt{A^2 + B^2}}.$

For $A$ and $B$ above, this yields $\phi = \frac{\pi}{4}$ and so

$$
P_\text{win}(x) = \dfrac{\cos\left(x - \frac{\pi}{4}\right)}{\cos\left(\frac12 - \frac{\pi}{4}\right)}.
$$

The fair starting point for Player 1 is whatever value of $x$ makes $P_\text{win}(x) = \frac12$ so

$$
\begin{align}
x &= \pi/4 + \cos^{-1}\left[\frac12 \cos\left(\frac12 - \frac{\pi}{4}\right)\right] \\
&\approx -0.285
\end{align}
$$

<br>
