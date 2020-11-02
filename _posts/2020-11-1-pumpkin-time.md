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

Before doing this, let's settle on some symbols. We'll call the remainders (like $18,$ $31,$ and $0$) $r_1,$ $r_2,$ and $r_3,$ and the modular bases (like $61,$ $60,$ and $59$) $m_1,$ $m_2,$ and $m_3.$ Also, we'll call the undetermined integers $x_1,$ $x_2,$ and $x_3.$

### Naive solution

The representation $r_1 + m_1\times x_1$ clearly has a remainder of $r_1$ when divided by $m_1$, just as the representation $r_2 + m_2\times x_2$ has remainder $r_2$ when divided by $m_2.$ What we want to find is a value for $x_1$ so that $r_1 + m_1\times x_1$ **also** has remainder $r_2$ when divided by $m_2.$

Setting the first two representations equal, and using the symbols laid out above, we have

$$\begin{align}
r_1 + m_1\times x_1 &= r_2 \mod m_2 \\
m_1\times x_1 &= \left(r_2 - r_1\right) + m_2\times x_2 \mod m_2
\end{align}$$

At this point it might seem like we could divide by $m_1$ and call it a day, but we want a solution in the integers, not in the reals. So we have to find an integer $m_1^{-1}$ such that $m_1 \times m_1^{-1} = 1$ modulo $m_2.$ In other words, $m_1^{-1}$ is the inverse of $m_1,$ modulo $m_2.$ 

So, if we can solve

$$m_1\times m_1^{-1} \equiv 1 \bmod m_2,$$ 

then we'll have

$$x_1 = m_1^{-1}\times\left(r_2 - r_1\right) \mod m_2.$$

Going back out of modulo $m_2$ we can add back $m_2x_2$ and, plugging into the first representation, we have

$$\begin{align}
N &= r_1 + m_1 \times x_1 \\
&= r_1 + m_1\times\left(m_1^{-1}\times\left(r_2 - r_1\right) + m_2\times x_2\right) \\
&= r_1 + m_1^{-1}m_1\left(r_2 - r_1\right) + m_1m_2x_2
\end{align}$$

We can check that this satisfies the first two remainder conditions. Since the second and third terms are proportional to $m_1,$ and so are zero modulo $m_1,$ it clearly has remainder $r_1$ then divided by $m_1.$ Since the last term is proportional to $m_2,$ the $m_1^{-1}m_1$ is $1$ modulo $m_2,$ the first and second terms boil down to $r_1 + \left(r_2 - r_1\right) = r_2$ modulo $m_2,$ as we wanted.

My plan was to then solve the second and third relations for $x_2$ in terms of $x_3$ and use it to generalize, but there's a problem. The inverse $m_1^{-1}$ is computed modulo $m_2.$ If we equate the third representation to the joint one, the inverse we calculate for $m_3$ will be modulo $m_2.$ We can perhaps consciously calculate it modulo $m_1m_3$ but then we realize we need to adjust the modulo for the calculation for $m_1^{-1}$ too. There is probably a way to adjust this approach, but it's not inherently symmetric to the fact that all three modulos are on the same footing.

This sent me back to the drawing board to look for a symmetric approach. 

### Once bitten, twice shy

Going back to the three relations, we have

$$\begin{align}
N &= r_1 \bmod m_1 \\
N &= r_2 \bmod m_2 \\
N &= r_3 \bmod m_3.
\end{align}$$

The problem with our last approach is that it put the constraints onto the same modulo two at a time. Once we put equations in the same modulo, we can do ordinary algebraic things like addition, subtraction, multiplication, and inversion. 

If we have an equation like $7 \bmod 5 = 2,$ then it is automatically the case that $7c \bmod \left(5c\right) = 2.$ Multiplying by the same factor in front of and behind the $\bmod$ leaves the truth of the statement alone. 

We can use this as inspiration to put all three constraints into modulo $m_1m_2m_3.$ Multiplying the first equation by $m_2m_3,$ the second by $m_1m_3,$ and the third by $m_1m_2,$ we get

$$\begin{align}
Nm_2m_3 &= r_1m_2m_3 \bmod m_1m_2m_3 \\
Nm_1m_3 &= r_2m_1m_3 \bmod m_1m_2m_3 \\
Nm_1m_2 &= r_3m_1m_2 \bmod m_1m_2m_3.
\end{align}$$

With like modulo, we can add these equations so that

$$N\left(m_2m_3 + m_1m_3 + m_1m_2\right) = \left(r_1m_2m_3 + r_2m_1m_3 + r_3m_1m_2\right) \bmod m_1m_2m_3.$$

Solving

$$\left(m_2m_3 + m_1m_3 + m_1m_2\right)\left(m_2m_3 + m_1m_3 + m_1m_2\right)^{-1}\equiv 1 \bmod m_1m_2m_3$$

for $\left(m_2m_3 + m_1m_3 + m_1m_2\right)^{-1}$ and multiplying the joint relationship by it, we can solve for $N:$

$$N = \left(m_2m_3 + m_1m_3 + m_1m_2\right)^{-1} \left(r_1m_2m_3 + r_2m_1m_3 + r_3m_1m_2\right).$$

<br>
