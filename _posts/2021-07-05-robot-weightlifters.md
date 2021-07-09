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

$$
\begin{array}{|c|l|l|l|} \hline
\text{Player 1's best bet} & \text{Player 1 odds} & \text{Player}\, x\,\text{odds} & \text{Player}\, y\,\text{odds} \\ \hline
1 & P_1(1) = (1-x)(1-y) & P_1(x) = x & P_1(y) = y(1-x) \\ \hline
x & P_x(1) = \dfrac{x}{1-(1-x)^2(1-y)} & P_x(x) = \dfrac{x(1-x)}{1-(1-x)^2(1-y)} & P_x(y) = \dfrac{y(1-x)^2}{1-(1-x)^2(1-y)} \\ \hline
y & P_y(1) = \dfrac{y(1-x)}{1-(1-x)(1-y)^2} & P_y(x) = \dfrac{x}{1-(1-x)(1-y)^2} & P_y(y) = \dfrac{y(1-x)(1-y)}{1-(1-x)(1-y)^2} \\ \hline
\end{array}
$$


### $1$ or $x$, it's all the same

There's a symmetry between the $1$-lead and $x$-lead situations. The chance for Player $x$ to win in the $x$-lead situation is the same as the $1$-lead situation, multiplied by the factor

$$ f(x,y) = \dfrac{1-x}{1-(1-x)^2(1-y)}. $$

The same is true for Player $y$'s chances. Multiplying Player 1's odds by $(1-x)/(1-x)$ the chances in the $x$-lead scenario become

$$ \mathbf{P_x} = f(x,y) \langle \dfrac{x}{1-x} , x , y(1-x)\rangle. $$

If $f(x,y) > 1,$ then Players $x$ and $y$ will have their chances raised compared to the $1$-lead scenario. Since $\sum_i P_x(i) = 1,$ this means that Player 1's chances would be lessened. Likewise, if $f(x,y) < 1,$ Player 1's chances will be smaller than in the $1$-lead scenario. 

Either way, Player 1 can make a choice to enrich themselves at the expense of Players $x$ and $y.$

<!-- $\sum_i P_x(i) = 1,$ so if $f(x,y) > 1,$ then Player 1's odds will be better betting on $1,$ and if $f(x,y) < 1,$ then Player $1$'s odds will be better betting on $x.$ In either case, this choice is to the detriment of Players $x$ and $y.$  -->

So, Players $x$ and $y$ are incentivized to set $f(x,y)$ to $1.$ This means that each player's odds are the same whether Player 1 bets $x$ or $1.$

Setting $f(x,y) = 1$ gets us

$$ \boxed{y = 1 - \frac{x}{(1-x)^2}}. $$

### $x$ and $y$ in balance

In any situation, Player 1 will be attracted to bet $x,$ $y,$ or $1.$

<!-- If the chance to win by undercutting $x$ is bigger than the chance to win at $y$ or $1,$ then Player 1 will bet $x.$  -->

When undercutting Player $x$, $P_x(1),$ is the most attractive option to Player 1, Player $y$ can increase their odds, $P_x(y),$ by increasing $y.$ They can do this up until the chance to win by undercutting Player $y$ becomes equal to the chance to win by undercutting Player $x,$ i.e. when $P_y(1) = P_x(1).$ 

After this point, Player 1 would be incentivized to switch their bet to $y,$ which moves Player $y$ from $P_x(y)$ to $P_y(y).$ This replaces the $(1-x)$ in Player $y$'s numerator with the smaller factor $(1-y).$ 

This crossover happens before $P_x(y) > P_x(1).$ 

So, $y$'s best chance in the $x$-leading scenario comes when the chance for Player 1 to win at $y$ is just a tad less than the chance to win at $x.$ 

The same is true for Player $x$ in the $y$-lead scenario.

So, Players $x$ and $y$ are incentivized to increase their bets up until the point where they make themself the more attractiveone  to undercut, i.e. they will set $P_x(1) = P_y(1).$

This gives us a second condition:

$$
\boxed{
\dfrac{x}{1-(1-x)^2(1-y)} = \dfrac{y(1-x)}{1-(1-x)(1-y)^2}
}
$$


<br>
