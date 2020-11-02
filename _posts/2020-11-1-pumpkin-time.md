---
layout: post
published: true
title: It's Pumpkin Time
date: 2020/11/1
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

_Disclaimer_: Through studious indifference, I have managed to $30$ virtually undisturbed by any known results in number theory. So I am able to document here a voyage of personal discovery, stumbling through basic ideas about how the integer numbers relate to themselves.

### The Pumpkin Shuffle

A round constitutes $N$ people counting themselves off around the circle until the last of them says $``N''$ and is eliminated for getting caught holding the David S. Pumpkin's hot pumpkin, and the next round begins with the person to their left. We're told that the first three people to be eliminated are positioned $18,$ $31,$ and $0$ positions to the left of the person who started their round and that there are $61$ people in the circle at the beginning of the game. 

Evidently, $N$ is bigger than the number of people, since it doesn't skip an equal number of people in the first three rounds. So, that counting $N$ positions ends the first round at position $19$ means that $N$ is equal to $19$ plus some number of multiples of the number of people, $P$. In other words

$$ N = 18 + \text{some integer}\times P. $$

Likewise, the other two facts lead to

$$\begin{align}
N &= 31 + \text{some other integer}\times (P - 1) \\
N &= 0 + \text{yet another integer}\times (P - 2).
\end{align}$$

This tells us a couple of things. The first is that there's a number $N$ that has remainders of $18,$ $31,$ and $0$ when divided by $61,$ $60,$ and $59,$ respectively. The second is that there are three equivalent representations for this number. 

My first instinct was to set them equal to each other to find a relationship between the undetermined integers. 

Before doing this, let's settle on some symbols. We'll call the remainders (like $18,$ $31,$ and $0$) $r_1,$ $r_2,$ and $r_3,$ and the modular bases (like $61,$ $60,$ and $59$) $n_1,$ $n_2,$ and $n_3.$ Also, we'll call the undetermined integers $x_1,$ $x_2,$ and $x_3.$

### Naive solution

The representation $r_1 + n_1\times x_1$ clearly has a remainder of $r_1$ when divided by $n_1$, just as the representation $r_2 + n_2\times x_2$ has remainder $r_2$ when divided by $n_2.$ What we want to find is a value for $x_1$ so that $r_1 + n_1\times x_1$ **also** has remainder $r_2$ when divided by $n_2.$

Setting the first two representations equal, and using the symbols laid out above, we have

$$\begin{align}
r_1 + n_1\times x_1 &= r_2 \mod n_2 \\
n_1\times x_1 &= \left(r_2 - r_1\right) + n_2\times x_2 \mod n_2
\end{align}$$

At this point it might seem like we could divide by $n_1$ and call it a day, but we want a solution in the integers, not in the reals. So we have to find an integer $n_1^{-1}$ such that $n_1 \times n_1^{-1} = 1$ modulo $n_2.$ In other words, $n_1^{-1}$ is the inverse of $n_1,$ modulo $n_2.$ 

So, if we can solve

$$m_1\times m_1^{-1} \equiv 1 \bmod n_2,$$ 

then we'll have

$$x_1 = n_1^{-1}\times\left(r_2 - r_1\right) \mod n_2.$$

Going back out of modulo $n_2$ we can add back $n_2x_2$ and, plugging into the first representation, we have

$$\begin{align}
N &= r_1 + n_1 \times x_1 \\
&= r_1 + n_1\times\left(n_1^{-1}\times\left(r_2 - r_1\right) + n_2\times x_2\right) \\
&= r_1 + n_1^{-1}n_1\left(r_2 - r_1\right) + n_1n_2x_2
\end{align}$$

We can check that this satisfies the first two remainder conditions. Since the second and third terms are proportional to $n_1,$ and so are zero modulo $n_1,$ it clearly has remainder $r_1$ then divided by $n_1.$ Since the last term is proportional to $n_2,$ the $n_1^{-1}n_1$ is $1$ modulo $n_2,$ the first and second terms boil down to $r_1 + \left(r_2 - r_1\right) = r_2$ modulo $n_2,$ as we wanted.

My plan was to then solve the second and third relations for $x_2$ in terms of $x_3$ and use it to generalize, but there's a problem. The inverse $n_1^{-1}$ is computed modulo $n_2.$ If we equate the third representation to the joint one, the inverse we calculate for $n_3$ will be modulo $n_2.$ We can perhaps consciously calculate it modulo $n_1n_3$ but then we realize we need to adjust the modulo for the calculation for $n_1^{-1}$ too. There is probably a way to adjust this approach, but it's not inherently symmetric to the fact that all three modulos are on the same footing.

This sent me back to the drawing board to look for a symmetric approach. 

### Once bitten, twice shy

Going back to the three relations, we have

$$
N = r_1 \bmod n_1 \,\mathbf{AND}\,N = r_2 \bmod n_2 \,\mathbf{AND}\, N = r_3 \bmod n_3.
$$

The problem with our last approach is that it put the constraints onto the same modulo two at a time. Once we put equations in the same modulo, we can do ordinary algebraic things like addition, subtraction, multiplication, and inversion. 

If we have an equation like $7 \bmod 5 = 2,$ then it is automatically the case that $7c \bmod \left(5c\right) = 2.$ Multiplying by the same factor in front of and behind the $\bmod$ leaves the truth of the statement alone. 

We can use this as inspiration to put all three constraints into modulo $n_1n_2n_3.$ Multiplying the first equation by $n_2n_3,$ the second by $n_1n_3,$ and the third by $n_1n_2,$ we get

$$\begin{align}
Nn_2n_3 &= r_1n_2n_3 \bmod n_1n_2n_3 \\
Nn_1n_3 &= r_2n_1n_3 \bmod n_1n_2n_3 \\
Nn_1n_2 &= r_3n_1n_2 \bmod n_1n_2n_3.
\end{align}$$

With like modulo, we can add these equations so that

$$N\left(n_2n_3 + n_1n_3 + n_1n_2\right) = \left(r_1n_2n_3 + r_2n_1n_3 + r_3n_1n_2\right) \bmod n_1n_2n_3.$$

If we solve

$$\left(n_2n_3 + n_1n_3 + n_1n_2\right)\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}\equiv 1 \bmod n_1n_2n_3$$

for $\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}$ and multiply the joint relationship by it, then we can compute $N:$

$$N = \left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1} \left(r_1n_2n_3 + r_2n_1n_3 + r_3n_1n_2\right).$$

A short program can be used to find $\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}$

```python
(n_1, n_2, n_3) = (61, 60, 59)
inverse = 0
while True:
  inverse += 1
  if inverse * (n_1 * n_2 + n_2 * n_3 + n_3 * n_1) % (n_1 * n_2 * n_3) == 1:
    print(inverse)
    break
```

which yields $5399$ and can be plugged into the result for $N$ to find:

$$N = \overbrace{5399}^{\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}}\times\overbrace{\left(18\times60\times59 + 31\times59\times61 + 0\times59\times60\right)}^{\left(r_1n_2n_3 + r_2n_1n_3 + r_3n_1n_2\right)}\bmod 61\times60\times59 = \boxed{136231}$$

This is the minimal value of $N,$ but in general we can add any multiple of $n_1\cdot n_2\cdot n_3$ so that

$$N = 136231 + 215940\cdot z.$$

### Who is the champion, my friend?

The extra credit asks who would actually win the game if we use this minimal value for $N?$



<br>
