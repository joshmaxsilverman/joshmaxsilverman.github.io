---
layout: post
published: true
title: Choice Odds
date: 2019/10/06
---

>You’ve made it to the $1 million question, but it’s a tough one. Out of the four choices, A, B, C and D, you’re 70 percent sure the answer is B, and none of the remaining choices looks more plausible than another. You decide to use your final lifeline, the 50:50, which leaves you with two possible answers, one of them correct. Lo and behold, B remains an option! How confident are you now that B is the correct answer?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/who-wants-to-be-a-riddler-millionaire/))

## Solution

Let $B$ (also) name the proposition that choice $B$ is the answer, and let $b$ name the proposition that choice $B$ is one of the two $50/50$ choices. Then, because $P(B)$ is $.7$, and $B$ is true iff $b \,\&\, B$ is true:

$$P(b \,\&\, B) = .7$$

If $B$ is not true (with probability $.3$), then one of the other choices is correct and will be one of the $50/50$ choices. Assuming that all incorrect choices have the same chance of being picked, $B$ has a $1/3$ chance of being the other choice selected. So:

$$P(b \,\&\, \neg B) = .3 \cdot \frac{1}{3} = .1$$

This lets us compute $P(b)$:

$$ P(b) = P(b \,\&\, B) + P(b \,\&\, \neg B) = .7 + .1 = .8$$

We are looking for the probability of $B$ conditional on $b$, which is the probability we'd assign to $B$ on learning that $b$ is true (in the Bayesian world, that's called "learning by conditionalization").  Here goes:

$$ P(B | b) = \frac{P(B\, \&\, b)}{P(b)} = \frac{.7}{.8} = .875$$

<br>
