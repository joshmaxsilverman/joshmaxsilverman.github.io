---
layout: post
published: true
title: Can you drink the “random-ade”?
date: 2026/05/11
subtitle: How much will you pour using this deranged protocol?
tags: expectation survival-probability
source: fiddler
kind: puzzle
theme: probability
hide_from_recent : true
---

> **Question**: I’m preparing a mixture of “random-ade” using a large, empty pitcher and two 12-ounce glasses.
>
>First, I fill one glass with some amount of lemon juice chosen randomly and uniformly between 0 and 12 ounces. I fill the other glass with some amount of water, also chosen randomly and uniformly between 0 and 12 ounces. Next, I pour an equal amount from each glass into the pitcher until one of the glasses is empty.
>
>At this point, I refill that empty glass with yet another random amount of the same liquid it previously contained. Once again, I pour an equal amount from each glass into the pitcher until one of the glasses is empty.
>
>On average, how much random-ade can I expect to prepare? (Note that all three random amounts in this problem are chosen independently of each other.)
>
>**Extra Credit**: Once again I’m preparing random-ade, but this time I have three 12-ounce glasses.
>
>I fill the first glass with a random amount of lemon juice, the second glass with a random amount of lime juice, and the third glass with a random amount of water. As before, each amount is chosen uniformly between 0 and 12 ounces, and all amounts are independent. Next, I pour an equal amount from each glass into the pitcher until one of the glasses is empty.
>
>At this point, I refill that empty glass with yet another random amount of the same liquid it previously contained. Once again, I pour an equal amount from each glass into the pitcher until one of the glasses is empty.
>
>Then I refill that now-empty glass with yet another random amount of the same liquid it previously contained. Again, I pour an equal amount from each glass into the pitcher until one of the glasses is empty.
>
>On average, how much random-ade can I expect to prepare?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-drink-the-random-ade))

## Solution

Say we draw $N$ random initial volumes $\{a_1, b_1, c_1, \ldots\}$ all between zero and $1.$ The chance that the smallest volume is greater than $v$ is equal to the chance that none of the $N$ volumes occupy the space between $0$ and $v,$ which is $(1-v)^N.$ Using the fact 

$$ \langle v_1\rangle = \int_0^1 \text{d}x\, P(v_1 \geq x) $$ 

we can find that the average minimum of the random volumes, and therefore the volume that each cup contributes on the first pour, is $1/(N+1)$ for a total pour of $NV_\text{cup}/(N+1)$ from all $N$ cups.

Suppose that $a_1$ is the minimum, then after the first pour, the volumes will be $\left(b_1-a_1\right), \left(c_1-a_1\right),$ and so on, and will keep the same relative order.

Now, the chance that $v_2 = \left(b_1-a_1\right)$ is bigger than $v$ is equal to the chance that none of the $N$ volumes entered the space of length $v$ between $a_1$ and $b_1$ times the chance that the new random volume does not fall inside $b_1-a_1,$ or 

$$ P(v_2 > v) = (1-v)^N\times(1-v) = (1-v)^{N+1}. $$ 

Again using the identity above, we get each cup contributing an average volume $\langle v_2\rangle = 1/(N+2).$

It keeps going on like this until we hit pour $\left(N+1\right).$ At this point, there are multiple possibilities. It could be that one of the cups has not yet been emptied. In that case the pattern continues. But it could also be that all $N$ cups have been emptied once. In that case, we descend into casework.  

So, for the $N$ round prep of random-ade, the expected volume is therefore 

$$ NV_\text{cup}\left(\frac{1}{N+1} + \frac{1}{N+2} + \ldots + \frac{1}{2N}\right). $$

In the limit of many pours, we are adding an average of half a cup of volume to the system each round and, so, should remove half a cup of volume each round too. Once the transients die out, we should expect each cup to contribute $V_\text{cup}/2N$ on average.

### Demonstration of the useful fact

The expectation value of a variable $v$ is 

$$\langle v\rangle = \int_0^{v_\text{max}} \text{d}v^\prime\, v^\prime P(v^\prime). $$

The probability that $v$ is greater than $\ell$ is 
$$P(v\geq\ell) = \int_\ell^{v_\text{max}} \text{d}v^\prime\, P(v^\prime). $$

Taking the derivative with regard to $\ell$
$$ \frac{\text{d}}{\text{d}\ell}P(v\geq\ell) = -P(\ell). $$

Replacing,

$$ \langle v\rangle = -\int_0^{v_\text{max}} \text{d}v^\prime\, v^\prime \frac{\text{d}}{\text{d}v^\prime}P(v\geq v^\prime). $$

Integrating by parts, the derivative moves over to kill $v^\prime$ and the boundary terms are zero (the chance to be larger than $v_\text{max}$ is zero) and we get

$$\langle v\rangle = \int_0^{v_\text{max}}\text{d}v^\prime\, P(v\geq v^\prime). $$
