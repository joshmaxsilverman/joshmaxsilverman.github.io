---
layout: post
published: true
title: Robot Weightlifters
date: 2021/07/05
---

>**Question**

The Robot Weightlifting World Championship’s final round is about to begin! Three robots, seeded 1, 2, and 3, remain in contention. They take turns from the 3rd seed to the 1st seed publicly declaring exactly how much weight (any nonnegative real number) they will attempt to lift, and no robot can choose exactly the same amount as a previous robot. Once the three weights have been announced, the robots attempt their lifts, and the robot that successfully lifts the most weight is the winner. If all robots fail, they just repeat the same lift amounts until at least one succeeds.

Assume the following:

1. all the robots have the same probability $p(w)$ of successfully lifting a given weight $w$;
2. $p(w)$ is exactly known by all competitors, continuous, strictly decreasing as the w increases, $p(0) = 1,$ and $p(w) \rightarrow 0$ as $w \rightarrow \infty$; and
3. all competitors want to maximize their chance of winning the RWWC.

If $w$ is the amount of weight the 3rd seed should request, find $p(w).$ Give your answer to an accuracy of six decimal places.

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/robot-weightlifting-index/))

## Solution

$$
\begin{array}{c|c|c|c} \hline
\text{Best bet} & \text{Player 1} & \text{Player}\, x & \text{Player}\, y \\ \hline
1 & x & y(1-x) & (1-x)(1-y) \\ \hline
x & \dfrac{x}{1-(1-x)^2(1-y)} & \dfrac{x(1-x)}{1-(1-x)^2(1-y)} & \dfrac{y(1-x)^2}{1-(1-x)^2(1-y)} \\ \hline
y & \dfrac{y(1-x)}{1-(1-x)(1-y)^2} & \dfrac{x}{1-(1-x)(1-y)^2} & \dfrac{y(1-x)(1-y)}{1-(1-x)(1-y)^2} \\ \hline
\end{array}
$$

<br>
