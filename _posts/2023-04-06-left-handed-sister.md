---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

we want to know if the person we saw is some guy, or "the guy". the question is, how much should we increase our credence in "the guy" on the basis of hearing about his second sister.

before we hear, our relative belief is

$$
  \dfrac{P(\text{the guy}\rvert \text{sister Mary})}{P(\text{some guy}\rvert \text{sister Mary})} =   \dfrac{P(\text{sister Mary}\rvert \text{the guy})}{P(\text{sister Mary}\rvert\text{some guy})} \dfrac{P(\text{the guy})}{P(\text{some guy})}
$$
$$

and after we hear about the lefty sister, it becomes

$$
  \dfrac{P(\text{the guy}\rvert \text{sister Mary, lefty sister})}{P(\text{some guy}\rvert \text{sister Mary, lefty sister})}
$$

using bayes rule, this is equal to

$$
  \dfrac{P(\text{sister Mary, lefty sister}\rvert\text{the guy})}{P(\text{sister Mary, lefty sister}\rvert\text{some guy})}\dfrac{P(\text{the guy})}{P(\text{some guy})}
$$

using bayes rule again, this becomes

$$
  \dfrac{P(\text{lefty sister}\rvert\text{sister Mary, the guy})}{P(\text{lefty sister}\rvert\text{sister Mary, some guy})}\dfrac{P(\text{sister Mary}\rvert\text{the guy})}{P(\text{sister Mary}\rvert\text{some guy})}\dfrac{P(\text{the guy})}{P(\text{some guy})}
$$

which is just $P(\text{lefty sister}\rvert\text{sister Mary, the guy})/P(\text{lefty sister}\rvert\text{sister Mary, some guy})$ times our relative belief before hearing about the lefty sister. this update factor is called the "bayes factor" associated with the lefty sister.

the numerator is $1$ on account that "the guy" definitely has these two sisters, so we can turn our focus on the denominator 

$$ P(\text{lefty sister}\rvert\text{sister Mary, some guy}). $$

to calculate the probability of the "lefty sister", we need to know what kind of family "some guy" comes from. as we know, he could come from a 2-, 3-, or 4-child family given that he has a "sister Mary". in other words

$$
  \sum_{n,m} P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ n\ \text{with}\ m\ \text{girls})P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy})
$$

the first factor is straightforward, but not the second.

it may come as a surprise, but we can use bayes rule to find it

$$
  \begin{align}
  &P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}) = \\
  &\dfrac{P(\text{sister Mary, some guy}\rvert \text{family of}\ n\ \text{with}\ m\ \text{girls})P(\ m\ \text{girls}\rvert \text{family of}\ n)P(\text{family of}\ n)}{\sum_{n^\prime m^\prime} P(\text{sister Mary, some guy}\rvert \text{family of}\ n^\prime\ \text{with}\ m^\prime\ \text{girls})P(\ m^\prime\ \text{girls}\rvert \text{family of}\ n^\prime)P(\text{family of}\ n^\prime)}
  \end{align}
$$

we can calculate the $P(\text{sister Mary, some guy}\rvert \text{family of}\ n\ \text{with}\ m\ \text{girls})$ one at a time.

for ease of typing, we'll call 

$$ 
  P(\text{sister Mary, some guy}\rvert \text{family of}\ n\ \text{with}\ m\ \text{girls})P(\ m\ \text{girls}\rvert \text{family of}\ n)P(\text{family of}\ n) 
$$ 

by its Christian name, $Z^{nm}.$

for a family of $2$-children, we have two people. accounting for ordering, we get

$$
  Z^{21} = 2! p_\text{girl} p_\text{Mary} p_\text{boy}
$$

for a family of $3$-children, we can have $\{\text{boy}, \text{sister Mary}, \text{sister}\}$ or $\{\text{boy}, \text{boy}, \text{sister Mary}\},$ so

$$
  \begin{align}
    Z^{32} &= 1\times 3! p_\text{Mary} p_\text{boy}p_\text{girl}^2 \\
    Z^{31} &= 2 \times \dfrac{3!}{2!}p_\text{Mary} p_\text{boy}^2p_\text{girl}
  \end{align}
$$

for a family of $4$-children, we can have $\{\text{boy}, \text{sister Mary}, \text{sister}, \text{sister}\}$ or $\{\text{boy}, \text{boy}, \text{sister Mary}, \text{sister}\}$ or $\{\text{boy}, \text{boy}, \text{boy}, \text{sister}\},$ so

$$
  \begin{align}
    Z^{43} &= 1\times 4! p_\text{Mary} p_\text{boy}p_\text{girl}^3 \\
    Z^{42} &= 2\times \dfrac{4!}{2!}p_\text{Mary} p_\text{boy}^2p_\text{girl}^2 \\
    Z^{41} &= 3\times \dfrac{4!}{3!}p_\text{Mary} p_\text{boy}^3p_\text{girl}
  \end{align}
$$

with these in hand, we can get $P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy})$ by

$$
 \begin{align}
    &P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}) = 
    &\dfrac{Z^{nm}}{Z^{21} + Z^{31} + Z^{32} + Z^{41} + Z^{42} + Z^{43}}
 \end{align}
$$

now we can return to the sum form

$$ \begin{align}
  &P(\text{lefty sister}\rvert\text{sister Mary, some guy}) = \\
  &\sum_{n,m} P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ n\ \text{with}\ m\ \text{girls})P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy})
  \end{align}
$$

the first term kills off most terms in the sum, since there can't be a lefty sister if the family only has $1$ girl. the surviving terms are just 

$$
  \begin{align}
    &P(\text{lefty sister}\rvert\text{sister Mary, some guy}) = \\
    &P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 3\ \text{with}\ 2\ \text{girls})Z^{32} \\
    &+ P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 4\ \text{with}\ 2\ \text{girls})Z^{42} \\
    &+ P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 4\ \text{with}\ 3\ \text{girls})Z^{43}
  \end{align}
$$

<br>
