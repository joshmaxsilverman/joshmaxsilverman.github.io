---
layout: post
published: true
title: Left handed sister
date: 2023/04/06
subtitle: Are you talking to some brother, or the brother?
tags: bayes partition-function evidence
---

>**Question**: Suppose you meet someone who looks like the brother of your friend Mary. You ask if he has a sister named Mary, and he says “Yes I do, but I don’t think I know you.”
>
>You remember that Mary has a sister who is left-handed, but you don’t remember her name. So you ask your new friend if he has another sister who is left-handed.
>
>If he does, how much evidence does that provide that he is the brother of your friend, rather than a random person who coincidentally has a sister named Mary and another sister who is left-handed? In other words, what is the Bayes factor of the left-handed sister?
>
>Let’s assume:
>
>   - Out of 100 families with children, 20 have one child, 30 have two children, 40 have three children, and 10 have four children.
>   - All children are either boys or girls with equal probability, one girl in 10 is left-handed, and one girl in 100 is named Mary.
>   - Name, sex, and handedness are independent, so every child has the same probability of being a girl, left-handed, or named Mary.
>   - If the person you met had more than one sister named Mary, he would have said so, but he could have more than one sister who is left handed.

<!--more-->

([Probably Overthinking It](https://www.allendowney.com/blog/2021/07/23/the-left-handed-sister-problem/))

## Solution

We want to know if the person we saw is some guy, or "the guy". 

The question is, how much should we increase our credence in "the guy" on the basis of hearing about his lefty sister.

### Evidence and updating

Before we hear about his lefty sister, our relative belief in "the guy" vs "some guy" is

$$
  \dfrac{P(\text{the guy}\rvert \text{sister Mary})}{P(\text{some guy}\rvert \text{sister Mary})} =   \dfrac{P(\text{sister Mary}\rvert \text{the guy})}{P(\text{sister Mary}\rvert\text{some guy})} \dfrac{P(\text{the guy})}{P(\text{some guy})}
$$

and after we hear about the lefty sister, it becomes

$$
  \dfrac{P(\text{the guy}\rvert \text{sister Mary, lefty sister})}{P(\text{some guy}\rvert \text{sister Mary, lefty sister})}.
$$

Using Bayes' rule, this is equal to

$$
  \dfrac{P(\text{sister Mary, lefty sister}\rvert\text{the guy})}{P(\text{sister Mary, lefty sister}\rvert\text{some guy})}\dfrac{P(\text{the guy})}{P(\text{some guy})}.
$$

Using Bayes' rule again, this becomes

$$
  \dfrac{P(\text{lefty sister}\rvert\text{sister Mary, the guy})}{P(\text{lefty sister}\rvert\text{sister Mary, some guy})}\overbrace{\left[\dfrac{P(\text{sister Mary}\rvert\text{the guy})}{P(\text{sister Mary}\rvert\text{some guy})}\dfrac{P(\text{the guy})}{P(\text{some guy})}\right]}^\text{relative belief before lefty sister},
$$

which is just $P(\text{lefty sister}\rvert\text{sister Mary, the guy})/P(\text{lefty sister}\rvert\text{sister Mary, some guy})$ times our relative belief before hearing about his lefty sister. This update factor is called the "Bayes factor" associated with his lefty sister.

The numerator is $1$ on account that "the guy" definitely has these two sisters, so we can turn our focus on the denominator:

$$ \boxed{P(\text{lefty sister}\rvert\text{sister Mary, some guy})}. $$

### Family first

To calculate the probability of the lefty sister given that "some guy" has a sister named Mary, we need to know what kind of family "some guy" comes from. As we know, given that he has a sister Mary he could come from a $2$-, $3$-, or $4$-child family, and can have anywhere from $1$ to all of his siblings be sisters. 

In other words, we can sum over the kind of family he comes from. This is convenient, because we know the distribution of family types, and we can calculate the probability to observe family members given the family they come from:

$$
  \begin{align}
    &P(\text{lefty sister}\rvert\text{sister Mary, some guy}) \\
    &=\sum_{n,m} P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ n\ \text{with}\ m\ \text{girls})P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}).
  \end{align}
$$

The first factor in the summand is straightforward, but the second takes some gymnastics.

It may come as a surprise, but we can use Bayes' rule to do it:

$$
  \begin{align}
  &P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}) = \\
  &\dfrac{P(\text{sister Mary, some guy}\rvert \text{family of}\ n\ \text{with}\ m\ \text{girls})P(\ m\ \text{girls}\rvert \text{family of}\ n)P(\text{family of}\ n)}{\sum_{n^\prime m^\prime} P(\text{sister Mary, some guy}\rvert \text{family of}\ n^\prime\ \text{with}\ m^\prime\ \text{girls})P(\ m^\prime\ \text{girls}\rvert \text{family of}\ n^\prime)P(\text{family of}\ n^\prime)}
  \end{align}
$$

Now, the tricky term is re-expressed in terms of simple forward terms and the known distribution of familiy sizes.

### Familial microstates

The terms $P(\text{sister Mary, some guy}\rvert \text{family of}\ n\ \text{with}\ m\ \text{girls})$ represent the probability weight of boys from families of size $n$, with $m$ girls in the population. This is easier to see if we read "sister Mary, some guy" as the equivalent "spoke to some guy who has a sister Mary".

We can calculate these terms one at a time.

For ease of typing, we'll call

$$ 
  P(\text{sister Mary, some guy}\rvert \text{family of}\ n\ \text{with}\ m\ \text{girls})P(\ m\ \text{girls}\rvert \text{family of}\ n)P(\text{family of}\ n) 
$$ 

by its Christian name, $Z_{nm}.$

#### Two child families

For a family with $2$-children, we have two people. Accounting for ordering, we get

$$
  Z_{21} = 1\times 2! p_\text{boy} p_\text{girl} p_\text{Mary} \times P(\text{family of 2})
$$

#### Three child families

For a family of $3$-children, we can have $\\{\text{boy}, \text{sister Mary}, \text{sister}\\}$ or $\\{\text{boy}, \text{boy}, \text{sister Mary}\\},$ so

$$
  \begin{align}
    Z_{32} &= 1\times 3! p_\text{boy} p_\text{Mary} (1-p_\text{Mary}) p_\text{girl}^2 \times P(\text{family of 3})\\
    Z_{31} &= 2 \times \dfrac{3!}{2!}p_\text{boy}^2 p_\text{Mary} p_\text{girl}\times P(\text{family of 3}).
  \end{align}
$$

As we noted, the overall weight is proportional to the number of boys that the family contributes to the population of people we can run into.

#### Four child families

For a family of $4$-children, we can have $\\{\text{boy}, \text{sister Mary}, \text{sister}, \text{sister}\\}$ or $\\{\text{boy}, \text{boy}, \text{sister Mary}, \text{sister}\\}$ or $\\{\text{boy}, \text{boy}, \text{boy}, \text{sister}\\},$ so

$$
  \begin{align}
    Z_{43} &= 1\times 4! p_\text{boy} p_\text{Mary}(1-p_\text{Mary})^2 p_\text{girl}^3 \times P(\text{family of 4})\\
    Z_{42} &= 2\times \dfrac{4!}{2!} p_\text{boy}^2 p_\text{Mary}(1-p_\text{Mary}) p_\text{girl}^2 \times P(\text{family of 4})\\
    Z_{41} &= 3\times \dfrac{4!}{3!} p_\text{boy}^3 p_\text{Mary} p_\text{girl}\times P(\text{family of 4})
  \end{align}
$$

With these in hand, we can renormalize them to recover $\widetilde{Z}_{nm} = P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}):$

$$
 \begin{align}
    \widetilde{Z}_{nm} =& P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}) \\
    =& \dfrac{Z_{nm}}{Z_{21} + Z_{31} + Z_{32} + Z_{41} + Z_{42} + Z_{43}}.
 \end{align}
$$

Now we can return to the sum-form of $P(\text{lefty sister}\rvert\text{sister Mary, some guy}):$

$$ \begin{align}
  &P(\text{lefty sister}\rvert\text{sister Mary, some guy}) = \\
  &\sum_{n,m} P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ n\ \text{with}\ m\ \text{girls})P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}).
  \end{align}
$$

The first factor of the summand kills off most terms in the sum, since the lefty sister can't exist if the family only has $1$ girl (who would have to be Mary). 

The surviving terms are just 

$$
  \begin{align}
    &P(\text{lefty sister}\rvert\text{sister Mary, some guy}) = \\
    &P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 3\ \text{with}\ 2\ \text{girls})\widetilde{Z}_{32} \\
    &+ P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 4\ \text{with}\ 2\ \text{girls})\widetilde{Z}_{42} \\
    &+ P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 4\ \text{with}\ 3\ \text{girls})\widetilde{Z}_{43}
  \end{align}
$$

### Left hand probability

If there is a sister besides Mary, then the probability they're lefty is just $p_\text{lefty}:$

$$ P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 3\ \text{with}\ 2\ \text{girls}) = p_\text{lefty}. $$

Likewise,

$$ P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 4\ \text{with}\ 2\ \text{girls}) = p_\text{lefty}. $$

If there are $2$ girls besides Mary, then either one or both of them can be a lefty:

$$ P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ 4\ \text{with}\ 3\ \text{girls}) = 2p_\text{lefty}(1-p_\text{lefty}) + p_\text{lefty}^2 $$

### "The guy", or "some guy"?

Putting it all together, we get 

$$
  \begin{align}
      P(\text{lefty sister}\rvert\text{sister Mary, some guy}) &= p_\text{lefty}\widetilde{Z}_{32} + \left[2p_\text{lefty}(1-p_\text{lefty}) + p_\text{lefty}^2\right]\widetilde{Z}_{43} + p_\text{lefty}\widetilde{Z}_{42} \\
      &= \dfrac{780219}{13920100} \\
      &\approx 1/17.8
   \end{align}
$$

<!--       &= \sum_{n,m} P(\text{lefty sister}\rvert\text{sister Mary, some guy, family of}\ n\ \text{with}\ m\ \text{girls})P(\text{family of}\ n\ \text{with}\ m\ \text{girls}\rvert\text{sister Mary, some guy}) \\ -->
      
So, after we hear about the left handed sister, we should update our relative belief by $1/P(\text{lefty sister}\rvert\text{sister Mary, some guy}) \approx 17.8$ times in favor of the hypothesis that we're talking to "the guy".

### Next steps

If you're facing this problem in your own life, the general form in terms of $p_\text{Lefty}$ and $p_\text{Mary}$ is the tidy expression:

$$ \dfrac{p_\text{Lefty} (8 + p_\text{Lefty} (-1 + p_\text{Mary}) - 2 p_\text{Mary}) (1 - p_\text{Mary})}{
 14 + (-8 + p_\text{Mary}) p_\text{Mary}}. $$
 
I hope it helps.

<br>
