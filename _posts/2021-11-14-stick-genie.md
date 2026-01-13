---
layout: post
published: true
title: Stick it to the genie
subtitle: How much can you bilk the genie for?
source: fivethirtyeight
tags: probability algebra invariance
date: 2021/11/14
theme: probability
---

>**Question**: One day you stumble across a magic genie, who says that if you play a simple game with him, you could win fabulous riches. You take the genie up on his offer, and he hands you a stick of length 1. He says that behind his back is another stick, with a random length between 0 and 1 (chosen uniformly over that interval).
>
>Next, you must break your stick into two pieces and present one of those pieces to the genie. If that piece is longer than the genie’s hidden stick, then you win a prize of $\\$1$ million times the length of your remaining piece. For example, if you present to the genie a length of 0.4, and that’s longer than the genie’s stick, then you win $\\$1$ million times 0.6, or $\\$$600,000. However, if the genie’s stick is longer, then you win nothing.
>
>Being a regular reader of The Riddler, you crunch some numbers and prepare to break your stick in half. But then you have a thought. You ask the genie if you can have more than one turn. For example, if you present the genie with a length of 0.4, but the genie’s stick is longer, can you break off a piece of the remaining length of 0.6 — say, a length of 0.5 — and then present that to the genie? To keep things fair, your winnings will still be proportional to the leftover length. So had the genie’s length indeed been between 0.4 and 0.5, your first and second guesses, then the remaining length would have been 0.1, and you would have won $\\$$100,000.
>
>The genie doesn’t think any of this really matters and says you can have as many turns as you desire. If your goal is to maximize your expected winnings, what will your strategy be? And how much money would you expect to win on average?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-stick-it-to-the-genie/))

## Solution

The potential here is that, by choosing our cuts just right, we can squeeze extra expected value out of subsequent turns. 

### One round

If we had just one turn, the chance that our stick of length $\ell$ is bigger than the genie's is $a$ while our payoff is $(1-a).$ So, our expected return is $a(1-a).$ 

This reaches its greatest value at $a=\frac12$ where 

$$\langle \text{payoff}_1\rangle = \frac14.$$

### Do better?

Suppose we could outdo this, by betting something less than $a = \frac12$ on the first turn, boosting our return, and keeping the option to bet something more on the second turn, for less return, if the first bet doesn't turn out.

This means we'll pick another cutpoint, $b,$ and bring a stick of length $(b-a)$ and payoff $(1-b)$ to the genie for a second try. So, with two attempts, our expected payoff is

$$
\begin{align}
\langle\text{payoff}_2\rangle &= P(\text{win first})(1-a) + P(\text{lose first, win second})(1-b)\\
&=a(1-a) + P(a < \ell < b-a)(1-b) \\
&= a(1-a) + (b-2a)(1-b)
\end{align}
$$

Sadly, this factors to $(b-a)(1-(b-a))$ which has the same form as the first round and maxes out at the same value

$$\langle\text{payoff}_2\rangle = \frac14.$$

So, the best two round policy is to set $b = a + \frac12,$ which guarantees $\langle\text{payoff}_2\rangle = \frac14$ independent of the choice of $a.$

### Third time's a charm?

What about a third round? A failure on the second round would mean that $\ell \geq \frac12.$ However, since $b = a + \frac12,$ it must be that $b \geq \frac12,$ which means the length that remains to play with is $(1-b)\leq \frac12.$ 

So, we can't do better than the optimal one round policy, and our expected winnings are $\frac14\times\\$1,000,000 = \\$250,000.$

<br>
