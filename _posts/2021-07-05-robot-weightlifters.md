---
layout: post
published: true
title: Robot Weightlifters
date: 2021/07/05
---

>**Question**: The Robot Weightlifting World Championship’s final round is about to begin! Three robots, seeded 1, 2, and 3, remain in contention. They take turns from the 3rd seed to the 1st seed publicly declaring exactly how much weight (any nonnegative real number) they will attempt to lift, and no robot can choose exactly the same amount as a previous robot. Once the three weights have been announced, the robots attempt their lifts, and the robot that successfully lifts the most weight is the winner. If all robots fail, they just repeat the same lift amounts until at least one succeeds.
>
>Assume the following:
>
>1. all the robots have the same probability $p(w)$ of successfully lifting a given weight $w$;
>2. $p(w)$ is exactly known by all competitors, continuous, strictly decreasing as the w increases, $p(0) = 1,$ and $p(w) \rightarrow 0$ as $w \rightarrow \infty$; and
>3. all competitors want to maximize their chance of winning the RWWC.
>
>If $w$ is the amount of weight the 3rd seed should request, find $p(w).$ Give your answer to an accuracy of six decimal places.

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/robot-weightlifting-index/))

## Solution

When the first seed's time comes, they find a game set by the bets of $x$ and $y.$ They can bet in three materially different ways: frontrun $x,$ frontrun $y,$ or bet behind $y.$

Player 1's chances in these situations are

$$ \frac{z}{1-(1-x)(1-y)(1-z)}, $$

$$ \frac{z(1-x)}{1-(1-x)(1-y)(1-z)},$$

and

$$ z(1-x)(1-y). $$

These are monotonically increasing in $z,$ so Player 1 only has to consider $x,$ $y,$ and $1.$ When this is done, the chances for each player in the three scenarios are

$$
\begin{array}{|c|l|l|l|} \hline
\text{Player 1's best bet} & \text{Player 1 odds} & \text{Player}\, x\,\text{odds} & \text{Player}\, y\,\text{odds} \\ \hline
1 & P_1^1 = (1-x)(1-y) & P_1^X = x & P_1^Y = y(1-x) \\ \hline
x & P_X^1 = \dfrac{x}{1-(1-x)^2(1-y)} & P_X^X = \dfrac{x(1-x)}{1-(1-x)^2(1-y)} & P_X^Y = \dfrac{y(1-x)^2}{1-(1-x)^2(1-y)} \\ \hline
y & P_Y^1 = \dfrac{y(1-x)}{1-(1-x)(1-y)^2} & P_Y^X = \dfrac{x}{1-(1-x)(1-y)^2} & P_Y^Y = \dfrac{y(1-x)(1-y)}{1-(1-x)(1-y)^2} \\ \hline
\end{array}
$$


Player 1 will pick whichever of their three options is greatest, given the values of $x$ and $y:$

$$ \text{Player 1's bet} = \max\{P_X^1(x,y), P_Y^1(x,y), P_1^1(x,y)\}. $$

For small $x$ and $y,$ $P_1^1(x,y)$ is the best choice. In this regime, Player X and Player Y's chances are simply $x$ and $y(1-x)$ and both can increase their chances by setting their lift probability as high as possible. 

Player X will follow this strategy up until the boundary $P_1^1(x,y) = P_X^1(x,y).$ What then?

Inspecting the probabilities, Player X's chance in the $x$-lead is equal to the chance in the $1$-lead multiplied by $f(x,y) = (1-x)/(1-(1-x)^2(1-y)).$ 

In other words, $P_1^X(x,y) = f(x,y)\times P_X^X(x,y).$ Likewise, $P_1^Y(x,y) = f(x,y)\times P_X^Y(x,y).$ 

Along the boundary, $(1 - P_1^1(x,y)) = (1 - P_X^1(x,y))$ which means that 

$$\begin{align}
P_1^X(x,y) + P_1^Y(x,y) &= P_X^X(x,y) + P_X^Y(x,y) \\
&= f(x,y)\left( P_1^X(x,y) + P_1^Y(x,y)\right),
\end{align}$$ 

or, $f(x,y) = 1.$

$f(x,y)$ is monotonically decreasing in $x$ and $y,$ so on the $1$-lead side of the border, $f(x,y) > 1$ and on the other side, $f(x,y) < 1.$ 

In $x$-lead, Player Y will set $y$ as high as possible without crossing the $P_1^1(x,y) = P_Y^1(x,y)$ border. 

Across the border, 

$$ P_Y^Y(x,y) = \frac{y(1-y)(1-x)}{1-(1-x)(1-y)^2} = y(1-y)\times g(x,y).$$ 

At the point where the border intercepts the $y$-axis, $g(x,y) = 1$ and it decreases monotonically in $x$ and $y$ from there. This means that $P_Y^1(x,y) \leq 1/4.$ 

The $y$-intercept of the $P_1^1(x,y) = P_Y^1(x,y)$ border is $(3-\sqrt{5})/2 \approx 0.382,$ so Player Y will never veer into the $y$-lead regime. 

But along the border, $P_Y^1(x,y) = P_X^1(x,y),$ so

$$ \dfrac{y(1-x)}{1-(1-x)(1-y)^2} = \dfrac{x}{1-(1-x)^2(1-y)}. $$

Since $1-x > 1-y,$ this means that $y(1-x) > x,$ or $y > x/(1-x).$ Plugging this in to $P_X^X(x,y),$ we get 

$$ P_X^X(x,y) = \dfrac{x-1}{2x-3} $$

which decreases monotonically. So, Player X will never move beyond the $P_1^1(x,y) = P_X^1(x,y)$ border.

This means that the point where the $P_1^1(x,y) = P_Y^1(x,y)$ and $P_1^1(x,y) = P_X^1(x,y)$ borders intersect is optimal for Players X and Y.

## Strategy recap

To recap, Player X sets $x$ as high as they can, knowing that it never benefits them to go into the $x$-lead regime. 

