---
layout: post
published: true
title: Uniform Dice
date: 2021/08/22
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

The unusual goal before us is to make the odds of each sum as uniform as we can. We want the odds to roll $1+1=2$ as close to the odds of $1+6=2+5=3+4=7$ as possible. 

So we are interested in the variance of the probability of a pair of dice appearing which, as a subtask, entails finding the expectation value of the probability of a pair of dice appearing!

The second part is easy. Since $\sum_i p_i = 1,$ and there are $11$ possible outcomes for two dice, we get $\langle p\rangle = \frac{1}{11}.$ 

### Add it up

The first part is a little spicy. 

We are looking at the sum 

$$
\sigma^2(p) = \frac{1}{11} \sum_s \left(\sum_{i+j = s} p_i p_i - \langle p\rangle\right)^2
$$

They start out simple — consider the $\left(1,1\right)$ outcome, which has probability $p_1^2.$ But by the $6$, which can come out one of five ways ($P(\text{dice sum}\ = 6) = 2p_1p_5 + 2p_2p_4 + p_3^2$), we have a mess on our hands.

### Slim it down

Adding it up, this generates a big polynomial that we have to minimize. 

On its face this has six variables ($\{p_i\}_{i=1}^6$) but, happily, a moment's thought can reduce it to three. The variables describing sides $1, 2,$ and $3$ are symmetric with the variables describing sides $4, 5,$ and $6,$ respectively. This means we can replace $p_4\rightarrow p_1, p_5\rightarrow p_2,$ and $p_6\rightarrow p_3.$ 

Putting it all together, we have the code below

```mathematica
ps = {p1, p2, p3, p4, p5, p6};

Z =
 Sum[
   ps[[i]] ps[[j]] z^(i + j)
   , {i, 1, 6}
   , {j, 1, 6}
   ] /. {p6 -> p1, p5 -> p2, p4 -> p3}

coeffSymb = CoefficientList[Z, z][[3 ;; -1]]

mean = 1/11
variance =
 1/11 Sum[(coeffSymb[[i]] - mean)^2, {i, 1, Length@coeffSymb}]

sol = NMinimize[
  {variance,
   { 0 <= p4 <= 1/2
   , 0 <= p5 <= 1/2
   , 0 <= p6 <= 1/2
   , p4 + p5 + p6 == 1/2
   }
  }
  , {p1, p2, p3}
 ]
```

which shows that the minimum variance is $\sigma^2_\text{min}\approx 0.00121758$ which is realized by assigning $p_1=p_4\approx 0.118638,$ $p_2=p_5\approx 0.137479,$ and $p_3=p_6=0.243883.$

and produces the following distribution for the dice sum probabilities

![](/img/2021-08-22-uniform-dice-distribution.JPG){:width=450px" class="image-centered"}

For posterity, the approximate numerical values are

$$
\begin{array}{c|c}
\text{Dice sum} & \text{probability} \hline
2	& 0.0594787 \\
3	& 0.0670576 \\
4	& 0.0767681 \\
5	& 0.0904881 \\
6	& 0.113753 \\
7	& 0.184909 \\ 
8	& 0.113753 \\
9	& 0.0904881 \\
10	& 0.0767681 \\ 
11	& 0.0670576 \\
12	& 0.0594787
\end{array}
$$

<br>
