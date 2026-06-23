---
layout: post
published: true
title: Can you fix the random number generator?
date: 2026/06/22
subtitle: Based on your friend's cryptic revelations, what's the biggest possible number?
tags: conditional-probability
source: fiddler
kind: puzzle
theme: probability
hide_from_recent : true
---

>**Question**
>
>I think the random number generator on my calculator might be malfunctioning. Oh no!
>
>Under normal conditions, it should generate random numbers between 0 and 1. But my suspicion is that the calculator is "tanked," meaning it only generates random numbers between 0 and some value $0 < a < 1$. Beyond that, I have no knowledge regarding the value of $a$. At the moment, it's equally likely to be any value from 0 to 1.
>
>As an experiment, I ask the calculator to generate one random number. It produces a value of exactly $0.5$. (While this is, admittedly, infinitely unlikely, let's roll with it!)
>
>Based on this result, what can I expect the value of $a$ to be, on average?
>
>**Extra Credit**
>
>Frustrated with my old calculator, I toss it in the trash and buy a new one. But now I'm concerned this second calculator is also "tanked." As before, every value of $a$ between 0 and 1 is equally likely at first.
>
>I ask my friend to generate one random number using this second calculator. My friend does so, and smirks. "I won't tell you what the number is," my friend says, "but it's somewhere between 0 and 0.5."
>
>On average, what can I expect the value of $a$ (for this second calculator) to be?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-fix-the-random-number-generator))

## Solution

This is a fun little job for Bayes' theorem. Since the two questions differ only in what information we hear from the friend, we will set things up generally before handling them.

We are told something about the observed value $x$ by the friend and need to figure out the expected value for $a$ based upon that information. This requires a probability distribution on $a$ in terms of our knowlegde about $x$ 

$$ P(a \rvert \text{knowledge about }x). $$

That distribution is not too clear to find directly but, but it can be expressed using Bayes' rule as

$$ \frac{P(\text{knowledge about }x \rvert a)P(a)}{P(\text{knowledge about }x)}. $$

which has three pieces. The distribution $P(a)$ is just $1,$ and the conditional probability $P(\text{knowledge about }x\rvert a)$ is easy to write down, but the distribution in the denominator is tricky. However, we can expand it in terms of the simple conditional probability in the numerator so that the final expression becomes

$$ P(a\rvert \text{knowledge about }x) = \frac{P(\text{knowledge about }x \rvert a)P(a)}{\int \text{d}a\, P(\text{knowledge about }x\rvert a)P(a)}. $$

## Standard credit

In the standard problem, we hear that the observed $x$ is equal to $\tfrac12.$ This means that the expression $P(\text{knowledge about }x\rvert a)$ is $P(x=\tfrac12\rvert a) = 1/a$ for $a \gt \tfrac12$ and zero below.

Plugging that in to the expression, we get 

$$ P(a\rvert x=\tfrac12) = \dfrac{P(x=\tfrac12\rvert a)}{\displaystyle\int_{\tfrac12}^1 \text{d}a P(x=\tfrac12\rvert a)} = \frac{1}{a\log 2}. $$

With that in our possession, we can take the expectation of $a$ like

$$ 
	\begin{align}
		\langle a\rangle &= \int_{\tfrac12}^1 \text{d}a\, a P(a\rvert x=\tfrac12) \\
		&= \int_{\tfrac12}^1 \text{d}a\, \frac{1}{\log 2} \\
		&= \frac{1}{2\log 2} \\
		&\approx 0.72134752 
	\end{align} 
$$

This makes sense, $a$ can be anything from $\tfrac12$ to $1,$ but $0.5$ is more likely when $a$ is small than when $a$ is large, so we expect a bias toward the lower end of the range.

## Extra credit

In this situation, the information we hear about $x$ is that it is $\tfrac12$ or smaller, so $P(\text{knowledge about }x\rvert a)$ is $P(x \leq \tfrac12\rvert a).$ This distribution is piecewise. If $a \leq \tfrac12$ then $x$ is definitely less than $\tfrac12,$ and if $a\gt\tfrac12$ then the chance $x$ is less than $\tfrac12$ is $\tfrac12/a:$

$$ P(x \leq \tfrac{1}{2}\rvert a) = 
\begin{cases} 
1 & \text{if } a \leq \tfrac{1}{2} \\ 
\frac{1}{2a} & \text{if } a > \tfrac{1}{2} 
\end{cases} $$

Now, the integral in the denominator of $P(a\rvert x\leq \tfrac12)$ is

$$ 
	\int_0^{\tfrac12}\text{d}a + \int_{\tfrac12}^1\text{d}a \frac{1}{2a} = \frac12\left(1 + \log 2\right) 
$$

and the expectation integral yields

$$ \langle a\rangle = \frac34 \frac1{1 + \log 2} \approx 0.442962 $$

<br>
