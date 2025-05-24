---
layout: post
published: true
title: How long is the river?
date: 2025/05/23
subtitle: 
tags:
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

after a long stretch of words, correlations with the beginning disappear and we should be equally likely to hit a space at any position. since half the words are three letters and half are four, this means that two out of every nine characters is a space, and $P(\text{space}) = 2/9.$

since a new word starts each line, we are asking, what is the probability that the 13th character on a new line is a space, and the 14th character on the next line is a space, and ... until the line $j$ at which it ends, where we multiply by the probability that the (12+j)th character on that line is a letter. in other words

$$ 
\begin{align}
  P(\text{river length}=\ell) &= P(12+1)\cdot P(12+2)\cdot \ldots \cdot P(12+\ell-1)\cdot\left(1-P(12+\ell)\right) \\
  &= \left(1-P(12+\ell)\right)\prod\limits_{j=1}^{\ell-1} P(12+j)
\end{align}
$$

because every word begins after a space, and ends on a space, the probability that position $j$ is a space is the probability that position $(j-4)$ ended on a space and the next word had three letters plus the probability $(j-5)$ ended on a space and the next word had four letters. since the probability of a three or four letter word after a space is $\frac12$, this becomes

$$ P(j) = \frac12 P(j-4) +\frac12 P(j-5) $$

at this point, we could code the recursion to find $P(j)$ and then take the weighted sum 

$$ \langle \ell\rangle = \dfrac{\sum\limits_{\ell=1}^\infty \ell P(\text{river length}=\ell)}{\sum\limits_{\ell=1}^\infty  P(\text{river length}=\ell)}. $$

but we can make some more progress analytically, turning to the glory of generating functions. 

the idea is to make a polynomial where the coefficient on $z^\ell$ represents the probability to have a space at position $\ell$. naively, we could make the quantity $(z^4 + z^5)$, raise it to a high enough power (anything bigger than $\ell/4$), expand it, and count how many terms of $z^\ell$ result. 

but with that motivation out of the way, we can accept that such a polynomial would be useful. specifically, the polynomial is 

$$ G(z) = \sum\limits_{\ell=1}^\infty P(\ell)z^\ell. $$

taking the recursive relationship, we get

$$
  \begin{align}
    P(j)z^j  &= \frac12z^jP(j-4) + \frac12z^jP(j-5) \\
    \sum\limits_{j=6}^\infty P(j)z^j  &= \frac12z^4\sum\limits_{j=6} z^{j-4}P(j-4) + \frac12z^5\sum\limits_{j=6} z^{j-5}P(j-5) \\
    G(z) - P(4)z^4 - P(5)z^5 &= z^4 G(z) + z^5 G(z) \\
    G(z) &= \frac{z^4+z^5}{2-z^4-z^5}
  \end{align}
$$

to extract the probabilities, we have to turn this into an unambiguous series in $z$:

$$
  \begin{align}
    G(z) &= \frac12 \dfrac{(z^4+z^5)}{1-\frac{z^4+z^5}{2}} \\
         &= \frac12 (z^4+z^5)\left(1 + \frac{z^4+z^5}{2} + \frac{(z^4+z^5)^2}{2^2} + \ldots \right) \\
         &= \frac12 \sum\limits_{j=1} \frac{1}{2^{j-1}}(z^4+z^5)^j \\
         &= \frac12 \sum\limits_{j=1} \frac{z^{4j}}{2^{j-1}}(1+z)^j
  \end{align}
$$

to get a $z^\ell$ term we need the $4j$ from $z^{4j}$ plus the exponent of a term from the expansion of $(1+z)^j$ to equal $\ell.$ in other words, we have the sum

$$ \begin{align} 
    P(\ell) &= \left[z^\ell\right] \\
      &= \frac12\sum\limits_{j=0} \dfrac{\dbinom{j}{\ell - 4j}}{2^{j-1}} 
    \end{align}
$$

with this in hand, we can evaluate the weighted sum which comes to $\langle \ell\rangle \approx 1.5347081153095188$

```python
def P(l):
  
  return 1/2 * sum(
                math.comb(j, l - 4 * j) / 2 ** (j - 1) 
                for j in range(1, l // 4 + 1)
              )

def P_diag(l):
  
  P_return = 1
  
  for i in range(1, l):
    P_return *= P(12 + i)
  
  return P_return * (1 - P(12 + l))

exp_l = sum(
          j * P_diag(j) 
          for j in range(1, 100)
        ) / sum(
          P_diag(j) 
          for j in range(1, 100)
        )
```



<br>
