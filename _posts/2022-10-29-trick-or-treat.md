---
layout: post
published: true
title: Neurotic halloween
date: 2022/10/29
subtitle: How close can you get to perfect candy disbursement?
source: fivethirtyeight
tags: expectation dynamic-programming optimality
theme: probability
theme: probability
---

>**Question**: For Halloween this year, David S. Pumpkins has asked you to purchase $150$ pieces of vegan chocolate to hand out to trick or treaters. You’re not sure how many trick-or-treaters will visit you but, based on previous years, it could be anywhere from $50$ to $150$ (inclusive), with each number being equally likely.
>
> The twist is this: David S. Pumpkins loves Halloween, and he wants the trick or treaters to get as much chocolate as possible. If you're not perfect at planning the chocolate disbursement (running out of chocolate before the last trick or treater, or ending up with leftover chocolate) David S. Pumpkins will appear and quantify your failure. He will determine $X$ (which is either the number of unserved trick or treaters or the number of leftover chocolate) and then he and his skeleton beat boys will dance in your living room for that many days.
>
>As the trick-or-treaters arrive, you can decide to give each of them one, two or three chocolates.
>
>This year, the day before Halloween, you come up with a strategy to minimize the expected value of $X.$ What is this minimum expected value?



<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-hand-out-all-the-candy/))

## Solution

Once again, we are solving puzzles at the behest of David S. Pumpkins and his troupe of skeleton beat boys. How can we minimize the time they spend doing their retributive dance in our living room?

![](/img/2020-11-1-david-s-pumpkins.JPG){:width="450 px" class="image-centered"}

The plan for this solution is

1. illuminate the logic with the worst cases
2. discover the family of potential strategies
3. calculate the expectation and minimize it
4. make sure that physics chutzpah didn't mislead us by re-solving with dynamic programming

### Worst case

If we want to incur the maximum average penalty, we can either always dispense $3$ chocolate or always dispense $1$ chocolate. 

In the first case, we'll run out of chocolate by the $50^\text{th}$ trick or treater (ToT) and so, $X$ (our penalty) will always be $50.$ In the second case, we'll have $100$ candies left by the $50^\text{th}$ ToT and, so, have an average of $50$ candies left over after the last ToT has come to the door. 

Evidently, the optimal approach is something between these two extremes.

<!-- ### Chocolate continuum 

The penalty is symmetric with respect to leftover candy and unserved ToTs, so we should aim to run out of candies precisely at the average number of ToTs, dispensing $150/100 = 1.5$ chocolates each visit until we run out. 

If we plan for e.g. $99$ ToT, then we'll add an average penalty of $1/101$ 

If we aimed slightly beyond $100,$ we'd be 

any candy that's left after the $50^\text{th}$ ToT will contribute to our penalty. 

so we should aim to run out of candy by the $100^\text{th}$ ToT (the average number of ToTs).

On average, there will be $100$ ToTs. So, if we were free to divide the chocolate anyway we like, then we would want to  -->

### Chocoallotment

We can figure out the "shape" of the strategy by thinking about the penalties.

After the $49^\text{th}$ ToT, we're penalized for undisbursed chocolates. So, after that point, we'll only hand out single chocolates. This also means that, before ToT $\\#50,$ it doesn't matter what order we hand out chocolates in, only the total number we dispense by that point.

So, we'll plan for some number $L$ of ToTs, handing out single chocolates to ToTs $50$ through $L,$ and a total of $\left(150-L\right)$ to ToTs $1$ through $49:$

$$
  \overbrace{\{C_1, C_2, \ldots, C_{49}, 1, 1, 1, \ldots, 1\}}^{L\text{ entries}}
$$

### Expectation penalty

If there are more than $L$ ToTs then we'll incur, on average, a penalty of $\frac12(150-L)$ for the unserved ToTs, which happens with probability $\frac{1}{101}(150-L+1).$ 

If there are less than $L$ ToTs, then we'll incur, on average, a penalty of $\frac12(L-50)$ for the leftover chocolates, which happens with probability $\frac{1}{101}(L-50+1).$

Putting it together, the expected penalty is

$$
  \frac12\frac{\left(150-L\right)\left(150-L+1\right)}{101} + \frac12\frac{\left(L-50\right)\left(L-50+1\right)}{101}
$$

which is minimized at $L=100$ which can be seen by symmetry, or expanding it. Temporarily writing $150$ as $U,$ and $50$ as $B,$ and ignoring factors of $101$, the form is

$$
  \begin{align}
    (U-L)(U-L+1) + (L-B)(L-B+1) &= U^2 + B^2 - 2(U+B)L + 2L^2 + U - B \\
    &= \left(U^2 + B^2 + U - B\right) + 2L(L- (U + B))
  \end{align}
$$

The $\left(U^2 + B^2 + U - B\right)$ is just an overall constant that shifts the parabola vertically. The shape and symmetry are determined by the expression $2L(L-U-B),$ which manifestly has roots at $L=0$ and $L = (U + B)$ and opens upward. Parabolas are symmetrical about the average of their roots, so the strategy of minimum penalty is $L_\text{min} = \frac12(U+B) = 100,$ which yields an average penalty of $2550/101\approx 25.248.$

### Optimality check

We should check that our physics chutzpah did not lead us astray. At each step, we have a choice between three decisions:

- hand out $1$ chocolate,
- hand out $2$ chocolates, or
- hand out $3$ chocolates.

We should always make the choice that minimies expectation, so the expected penalty starting from $C$ candies, after seeing $T$ trick or treaters, is

$$
  E(C,T) = \min\limits_c\{\gamma(C-1, T+1), \gamma(C-2,T+1), \gamma(C-3,T+1)\}.
$$

The value of the choice $\gamma(C, T)$ depends on where we find ourselves. 

- if we've seen less than $49$ ToTs so far, then we immediately make our next choice. 
- if we run out of candies, and we've seen $49$ or more ToTs, then there's a $1$ in $(150-T)$ chance that we've just given candy to the final ToT. If that's not the case, then we incur an average penalty of half the potential remaining ToTs.
- if we have candies remaining and have seen $49$ or more ToTs, then we've either seen the last ToT, or we have another choice to make.
- if we reach the end with no candies, we have no penalty. 

Finally, we can't have a negative amount of candies. Putting it all together, we have:

$$
  \displaystyle \gamma(C,T) = 
  \begin{cases}
    E(C,T) & T < 49 \\
    (1-\frac{1}{150-T})\frac{150-T}{2} & C=0, T\geq 49 \\
    \frac{1}{150-T}C + (1-\frac{1}{150-T})E(C,T) & C > 0, T\geq 49 \\
    0 & C=0,T=150 \\
    \infty & C<0.
  \end{cases} 
$$

Running this in Python, we get $E(150,0) = 2550/101$ as expected.

```python
from functools import lru_cache

impossible = 10_000

@lru_cache(maxsize=150)
def gamma(C, T):
  if C < 0:
    return impossible
  if T == 150:
    return C
  if T < 49:
    return E(C, T)
  if C == 0:
    return (1 - 1/(150-T)) * (150-T)/2
  if C > 0:
    return 1/(150-T) * C + (1 - 1/(150-T)) * E(C, T)

def E(C, T):
  return min([gamma(C-1, T+1), gamma(C-2, T+1), gamma(C-3, T+1)])
```

<br>
