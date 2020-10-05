---
layout: post
published: true
title: A Bag of Chocolates
date: 2020/10/04
---

>Question

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-eat-all-the-chocolates/))

## Solution

At the bottom of this bag hides a small amplitude pendulum. But first we'll work out the structue of the bag's states and the transitions that happen between them.

### Intuition

When we start the game, we pick a chocolate, any old chocolate. No matter what it is, we'll eat it. 

But the next time we draw a chocolate, we'll eat it only if it's the same kind as the last one we picked. If it's different, then we start the game over with the remaining chocolates. 

Without doing any analysis we can see that if we have a big imbalance, like $100$ dark chocolates and $1$ soymilk chocolate, then we are overwhelmingly likely to draw a dark chocolate. 

It is always possible that, amidst our dark chocolate eating spree, we pick a soymilk chocolate. However, we wouldn't immediately eat it. Since our most recently consumed chocolate would have been dark, we'd have start the game over and draw another. Unless we pick the soymilk chocolate on the second draw as well, then we'll keep on chugging with dark. 

This shows an important property of the system: once we start eating a certain kind of chocolate, it's easier for us to keep eating it. The reason being that we have to "fail" twice to switch to the other one.

### States

When we start the game, we have $m$ soymilk chocolates, $d$ dark chocolates, and no most recently consumed chocolate, so anything can happen. We call this state "blank slate", or $\mathbf{BS}$ and the state of the system is denoted by $\left(m, d\right).$ 

From here we can select a soymilk chocolate with probability $m/\left(m+d\right)$ or a dark chocolate with probability $d/\left(m+d\right).$ Because eating a soymilk chocolate will make our most recently consumed chocolate a soymilk chocolate, we are now in the state $\mathbf{M},$ and if we eat a dark chocolate, we enter the state $\mathbf{D}.$ 

These are the basic states of the system, and once we're in one of them, we're biased to staying there.

### Transitions

We want to know the probability that the last chocolate we eat is a soymilk chocolate assuming that we start with $m$ soymilk chocolates and $d$ dark chocolates. We can call this probability $P\left(m,d\right).$ 

To get started, we can calculate it for a simple case. 

Suppose we have $2$ soymilk chocolates and $3$ dark chocolates, so our system starts in $\left(2,3\right).$

The orders in which we can eat these chocolates while having a soymilk chocolate be our last are these four:

$$\begin{align}
\mathbf{M} \rightarrow \mathbf{D} \rightarrow \mathbf{D} \rightarrow \mathbf{D} \rightarrow \mathbf{M} \\
\mathbf{D} \rightarrow \mathbf{M} \rightarrow \mathbf{D} \rightarrow \mathbf{D} \rightarrow \mathbf{M} \\
\mathbf{D} \rightarrow \mathbf{D} \rightarrow \mathbf{M} \rightarrow \mathbf{D} \rightarrow \mathbf{M} \\
\mathbf{D} \rightarrow \mathbf{D} \rightarrow \mathbf{D} \rightarrow \mathbf{M} \rightarrow \mathbf{M}
\end{align}$$

We can calculate the probability of each trajectory in turn.

Because of the rules of the game, there are two ways for us to eat the same kind of chocolate twice in a row, but only one way for us to switch from one chocolate type to another. Let's calculate.

The probability of drawing an $\mathbf{M}$ first is $2/5.$ From there, we switch to $\mathbf{D}$ which means we drew a $\mathbf{D},$ restarting the game, and then drew $\mathbf{D}$ again, which has overall probability $\left(3/4\right)^2.$ The next move is back to $\mathbf{D}$ which can happen either by direct transition (probability $2/3$) or by drawing a soymilk chocolate, restarting the game, and then drawing a dark chocolate again (probability $1/3\times 2/3$), giving the step overall probability $2/3 + 1/3\times 2/3 = 8/9.$ The next step is another draw of $\mathbf{D}$ which has probability $1/2 + \left(1/2\right)^2$ (we can draw dark directly, or draw milk chocolate, restart the game, and draw dark again) and the last step is forced.

In total, $\mathbf{MDDDM}$ has probability $2/5\times \left(3/4\right)^2 \times 8/9 \times 1/2 = 9/40.$

Proceeding by the same rules, the probabilities of the rest are

$$\begin{array}{c|c}
\text{move} & P(\text{move}) \\ \hline
\mathbf{MDDDM} & 2/5\times\left(3/4\right)^2\times\left(1/3\times 2/3+2/3\right)\left(1/2\times 1/2+1/2\right)\times 1 = 3/20\\
\mathbf{DMDDM} & 3/5\times\left(2/4\right)^2\left(2/3\right)^2\left(1/2\times 1/2+1/2\right)\times 1 = 1/20 \\
\mathbf{DDMDM} & 3/5\left(2/4\times 2/4+2/4\right)\left(2/3\right)^2\left(1/2\right)^2\times 1 = 1/20 \\
\mathbf{DDDMM} & 3/5\left(2/4\times 2/4+2/4\right)\left(2/3\times 1/3+1/3\right)\times 1\times 1 = 1/4
\end{array}$$

Adding these up, incredibily, we get $3/20 + 1/20+1/20 + 5/20 = 1/2.$

This matches our expectation that the bag has built-in dynamics that abhor imbalanced states, but $1/2$ seems a little perfect. 

To show that this is true in general, we need to keep track of how $P(m,d)$ relates to $P(m-1,d), P(m,d-1), \ldots, P(m-2,d-1), \ldots.$

### Recursion

$P(m,d)$ refers to the probability that the last chocolate we eat is a soymilk one, given that we start the game in the state $\left(m,d\right).$ However, in the course of the game, we're not always starting new games. In fact, as long as we're amidst a string of $\mathbf{M}$ or $\mathbf{D},$ we won't be in the new game state $\mathbf{BS}.$ 

However, whenever we draw a chocolate different from the last one we've consumed, then we're starting a new game. With this in mind, we can keep track of how we enter the $\mathbf{BS}$ state.

At the beginning of the game, we either enter the $\mathbf{M}$ or $\mathbf{D}$ state. If we enter the $\mathbf{M}$ state and we don't draw a soymilk chocolate on our next attempt, then we'll start a new game in the state $\left(m-1,d\right).$ Likewise, if we do draw another soymilk chocolate, but then draw a dark chocolate, we'll start a new game in the $\left(m-2,d\right)$ state. 

Following the diagram above, we can generate the entire recursion relation. At the base of the left hand chain, we have the state $\left(1,0\right)$ which has $100\%$ probability to end in a soymilk chocolate. Similarly, if we reach the bottom of the right hand chain, we have the state $\left(0,1\right)$ which has $0\%$ chance to end in a soymilk chocolate. Carrying on like this, we get 

![](/img/PNG image.png)



### Lane model

Suppose we enter the $\mathbf{M}$ state. What can happen?

One thing we could do is to eat another soymilk chocolate, which can be achieved either by picking a soymilk chocolate on our next draw, or by picking a dark chocolate, starting the game over, and then picking a milk chocolate. 

The probability of the first event is $m/\left(m+d\right)$ and the second has probability $md/\left(m+d\right)^2.$

The other thing we could do is to eat a dark chocolate, which can be achieved if we draw a dark chocolate, start the game over, and then pick another dark chocolate, which has probability $d^2/\left(m+d\right)^2.$

So, starting in the $\mathbf{M}$ state, the probability that we eat another soymilk chocolate is

$$p_{m\downarrow} = \dfrac{m^2 + 2md}{\left(m+d\right)^2} = \dfrac{\left(m+d\right)^2 - d^2}{\left(m+d\right)^2}$$

and the probability that we eat a dark chocolate is

$$p_{d\downarrow} = \dfrac{d^2}{\left(m+d\right)^2.}$$



<br>

