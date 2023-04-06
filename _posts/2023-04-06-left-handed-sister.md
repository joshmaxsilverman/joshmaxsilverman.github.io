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

the numerator is $1$ on account that "the guy" definitely has these two sisters, so we can turn our focus on the denominator $P(\text{lefty sister}\rvert\text{sister Mary, some guy}).$

to calculate the probability of the "lefty sister", we need to know what kind of family "some guy" comes from. as we know, he could come from a 2-, 3-, or 4-child family given that he has a "sister Mary". in other words

$$
  P(\text{lefty sister}\rvert\text{sister Mary, some guy}) = \sum_n P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ n)P(\text{family of}\ n\rvert\text{sister Mary, some guy})
$$

the first factor is straightforward, but not the second.

it may come as a surprise, but we can use bayes rule to find it

$$
  P(\text{family of}\ n\rvert\text{sister Mary, some guy}) = \dfrac{P(\text{sister Mary, some guy}\rvert \text{family of}\ n)P(\text{family of}\ n)}{\sum_n P(\text{sister Mary, some guy}\rvert \text{family of}\ n)P(\text{family of}\ n)}
$$

we can calculate the $P(\text{sister Mary, some guy}\rvert \text{family of}\ n)$ one at a time.

for a family of $2$-children,

$$
  P(\text{sister Mary, some guy}\rvert \text{family of}\ 2) = 2! p_\text{girl} p_\text{Mary} p_\text{boy}
$$

for a family of $3$-children, we can have $\{\text{boy}, \text{lefty sister}, \text{sister Mary}\}$ or $\{\text{boy}, \text{boy}, \text{sister Mary}\},$ so

$$
  P(\text{sister Mary, some guy}\rvert \text{family of}\ 3) = 3! p_\text{girl} p_\text{Mary} p_\text{boy} + 2\dfrac{3!}{2!}p_\text{boy}^2p_\text{girl}p_\text{Mary}
$$

for a family of $4$-children, we can have $\{\text{boy}, \text{sister Mary}, \text{lefty sister}, \text{lefty sister}\}$ or $\{\text{boy}, \text{boy}, \text{sister Mary}, \text{lefty sister}\}$ or $\{\text{boy}, \text{boy}, \text{boy}, \text{lefty sister}\},$ so

$$
  P(\text{sister Mary, some guy}\rvert \text{family of}\ 4) = 4! p_\text{boy}p_\text{girl}^3 p_\text{Mary} p_\text{lefty} + 2\dfrac{3!}{2!}p_\text{boy}^2p_\text{girl}^2p_\text{Mary}
$$

<br>
