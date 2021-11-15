---
layout: post
published: false
title: Stick it to the Genie
subtitle: How much can you bilk the genie for?
date: 2021/11/14
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

The potential here is that, by choosing our cuts just right, we can squeeze extra expected value out of subsequent turns. 

If we had just one turn, the chance that our stick of length $\ell$ is bigger than the genie's is $a$ while our payoff is $(1-a).$ So, our expected return is $a(1-a).$ 

This reaches its greatest value at $a=\frac12$ where 

$$\langle \text{payoff}_1\rangle = \frac14.$$

Suppose we could outdo this, by betting something less than $a = \frac12$ on the first turn, boosting our return, and keeping the option to bet something more on the second turn, for less return, if the first bet doesn't turn out.

This means we'll pick another cutpoint, $b,$ and bring a stick of length $(b-a)$ and value $(1-b)$ to the genie for a second try. So, with two attempts, our expected payoff is

$$
\begin{align}
\langle\text{payoff}_2\rangle &= a(1-a) + P(a < \ell < b-a)(1-b) \\
&= a(1-a) + (b-2a)(1-b)
\end{align}
$$

Sadly, this factors to $(b-a)(1-(b-a))$ which has the same form as the first round and maxes out at the same value

$$\langle\text{payoff}_2\rangle = \frac14.$$

So, the best two round policy is to set $b = a + \frac12,$ which guarantees $\langle\text{payoff}_2\rangle = \frac14$ independent of the choice of $a.$

What about a third round? A failure on the second round would mean that $\ell \geq \frac12.$ However, since $b = a + \frac12,$ it must be that $b \geq \frac12,$ which means the length that remains to play with is $(1-b)\leq \frac12.$ 

So, we can't do better than the optimal one round policy, and our expected winnings are $\frac14\times\$1,000,000 = \$250,000.$

<br>
