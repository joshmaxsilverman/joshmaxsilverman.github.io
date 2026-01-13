---
layout: post
published: false
title: A bag of chocolates
date: 2020/10/04
subtitle: What’s the chance you finish on a vegan chocolate?
source: fivethirtyeight
theme: probability
---

>**Question**: Your good friend, the Count, is back from $6$ years on a pirate ship and, as promised, she has brought with her, among other gifts, various and sundry, a bag of chocolates. But not just any bag of a chocolates, a velvet bag of chocolates. And not just any bag of velvet chocolates, but one that contains $d$ dark chocolates, $m$ soymilk chocolates (she is a noble, vegan vampire), and has a built-in game whose rules determine when you can eat them!
>
>The rules are as follows: 1. pick any chocolate from the bag and consume it, 2. pick another chocolate from the bag and eat it if it's the same kind as the one you just consumed, otherwise place it back in the bag and return to step 1. Just as you're about the get started, your well traveled friend says "hey, one more rule, you win this game if the very last chocolate you eat is a soymilk chocolate." 
>
>What is the probability that you win the game?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-eat-all-the-chocolates/))

## Solution

At the bottom of this bag hides a small amplitude pendulum. But first we'll work out the structure of the bag's states and the transitions that happen between them.

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

Because of the rules of the game, there are two ways for us to eat the same kind of chocolate twice in a row, but only one way for us to switch from one chocolate type to another. 

Let's calculate the probability of each trajectory in turn.

### $\mathbf{MDDDM}$

The probability of drawing an $\mathbf{M}$ first is $2/5.$ From there, we switch to $\mathbf{D}$ which means we drew a $\mathbf{D},$ restarting the game, and then drew $\mathbf{D}$ again, which has overall probability $\left(3/4\right)^2.$ The next move is back to $\mathbf{D}$ which can happen either by direct transition (probability $2/3$) or by drawing a soymilk chocolate, restarting the game, and then drawing a dark chocolate again (probability $1/3\times 2/3$), giving the step overall probability $2/3 + 1/3\times 2/3 = 8/9.$ The next step is another draw of $\mathbf{D}$ which has probability $1/2 + \left(1/2\right)^2$ (we can draw dark directly, or draw milk chocolate, restart the game, and draw dark again) and the last step is forced.

In total, $\mathbf{MDDDM}$ has probability $2/5\times \left(3/4\right)^2 \times 8/9 \times 1/2 = 3/20.$

Proceeding by the same rules, the probabilities of the rest are

$$\begin{array}{|c|c|} \hline
\text{move} & P(\text{move}) \\ \hline
\mathbf{MDDDM} & 2/5\times\left(3/4\right)^2\times\left(1/3\times 2/3+2/3\right)\left(1/2\times 1/2+1/2\right)\times 1 = 3/20\\
\mathbf{DMDDM} & 3/5\times\left(2/4\right)^2\left(2/3\right)^2\left(1/2\times 1/2+1/2\right)\times 1 = 1/20 \\
\mathbf{DDMDM} & 3/5\left(2/4\times 2/4+2/4\right)\left(2/3\right)^2\left(1/2\right)^2\times 1 = 1/20 \\
\mathbf{DDDMM} & 3/5\left(2/4\times 2/4+2/4\right)\left(2/3\times 1/3+1/3\right)\times 1\times 1 = 1/4 \\ \hline
\end{array}$$

Adding these up, incredibly, we get $3/20 + 1/20+1/20 + 5/20 = 1/2.$

This matches our expectation that the bag has built-in dynamics that abhor imbalanced states, but $1/2$ seems a little perfect. 

To show that this is true in general, we need to keep track of how $P(m,d)$ relates to $P(m-1,d), P(m,d-1), \ldots, P(m-2,d-1), \ldots.$

We'll show how to do that at the end, but now we'll now switch to an intuitive model of the hidden pendulum that drives the system toward balance so that $P(m,d) = 1/2$ for all $m$ and $d.$

### Bag dynamics

The striking thing about this bag is how it can restore balance. To get a handle on this, I focus on how the system switches back and forth between the $\mathbf{M}$ and $\mathbf{D}$ states and, in particular, how it behaves when it's very imbalanced. 

To do this, we'll abandon analyzing individual systems and look at the average system as it settles down to $\left(0,0\right).$

**Note**: because the $\mathbf{BS}$ (blank slate) state is just a stopover, a temporary state we reside in while we restart the game, we will immediately determine the system's next state rather than keeping track of a bunch of $\mathbf{BS}$ states.

Suppose we find ourselves having just eaten a soymilk chocolate, with the bag in the state $\left(m,d\right).$ What is the relative likelihood of our next moves? 

One thing we could do is to eat another soymilk chocolate, which can be achieved either by picking a soymilk chocolate on our next draw, or by picking a dark chocolate, starting the game over, and then picking a milk chocolate. 

The probability of the first event is $m/\left(m+d\right)$ and the second has probability $md/\left(m+d\right)^2.$

The other thing we could do is to eat a dark chocolate, which can be achieved if we draw a dark chocolate, start the game over, and then pick another dark chocolate, which has probability $d^2/\left(m+d\right)^2.$

![](/img/2020-10-04-MD-state-transition.png){:width="450px" class="image-centered"}

So, starting in the $\mathbf{M}$ state, the probability that we eat another soymilk chocolate is

$$p_{m\downarrow} = \dfrac{m^2 + 2md}{\left(m+d\right)^2} = \dfrac{\left(m+d\right)^2 - d^2}{\left(m+d\right)^2}$$

and the probability that we eat a dark chocolate is

$$p_{d\downarrow} = \dfrac{d^2}{\left(m+d\right)^2.}$$

Dividing these two transition probabilities, we get

$$\begin{align}
\dfrac{p_{m\downarrow}}{p_{d\downarrow}} &= \dfrac{\left(m+d\right)^2 - d^2}{d^2} \\
&= \dfrac{\left(m+d\right)^2}{d^2} - 1
\end{align}$$

or, writing $d/\left(m+d\right)$ as $f_d$ (the fraction of chocolates that are dark), we have

$$p_{m\downarrow} = \left(\frac{1}{f_d^2} - 1\right)p_{d\downarrow}.$$

What this says is that when $f_d$ is small, the bag will force us to each soymilk chocolates significantly faster than we eat dark chocolates. In fact, it will drive the system in this direction until the term in parenthesis is equal to $1$ (which makes the rates equal), but this doesn't happen until $f_d = 1/\sqrt{2} \approx 0.7071.$ 

Let's put this into plain English: 

- when we've just eaten a soymilk chocolate, and soymilk chocolates outnumber dark chocolates, the probability that we continue to eat milk chocolate is **much** greater than the probability we switch to dark chocolate. 
- due to the intrinsic inertia of the states, we will be favored to do this until $f_d$ swings up to $0.7071,$ past the balance point $f_d = f_m = 1/2.$ 

The analysis we just performed was for when we've just eaten a soymilk chocolate. If we did the same analysis for when we've just eaten a dark chocolate, we get the similar result

$$p_{d\downarrow} = \left(\frac{1}{f_m^2} -1\right)p_{m\downarrow},$$

which has the same qualitative behavior.

![](/img/2020-10-04-rate-graph.png){:width="450px" class="image-centered"}

### Ensemble mean

We can think of the average behavior as a point in $\left(m,d\right)$ space that approaches the origin as we eat the chocolates in the bag:

![](/img/2020-10-04-graph-scheme.png){:width="450px" class="image-centered"}

Our analysis above suggests that points under the $m=d$ (with more $m$ than $d$) line will race horizontally toward the line, overshoot so that $f_d \approx 1/\sqrt{2}$ and then dive vertically, oscillating in this way down to the origin, hugging the line $m=d.$ Likewise, points above the $m=d$ line (with more $d$ than $m$) will dive vertically down to the line overshoot a bit, then race horizontally back to the line, oscillating down to the origin. 

![](/img/2020-10-04-point-dynamics.png){:width="450px" class="image-centered"}

Because the imbalance in transition probabilities gets much stronger (ex. $\sim 1/f_d^2$) when there's a strong imbalance, **all bags**, no matter how "extreme" their imbalance, will be driven strongly toward the line $m=d$ before oscillating down to the origin in unison.

Therefore, we expect the average bag to finish the game in the $\left(1,1\right)$ state, a coin flip between soymilk and dark chocolate.


### Recursion

$P(m,d)$ refers to the probability that the last chocolate we eat is a soymilk one, given that we start the game in the state $\left(m,d\right).$ However, in the course of the game, we're not always starting new games. In fact, as long as we're amidst a string of $\mathbf{M}$ or $\mathbf{D},$ we won't be in the new game state $\mathbf{BS}.$ 

However, whenever we draw a chocolate different from the last one we've consumed, then we're starting a new game. With this in mind, we can keep track of how we enter the $\mathbf{BS}$ state.

At the beginning of the game, we either enter the $\mathbf{M}$ or $\mathbf{D}$ state. If we enter the $\mathbf{M}$ state and we don't draw a soymilk chocolate on our next attempt, then we'll start a new game in the state $\left(m-1,d\right).$ Likewise, if we do draw another soymilk chocolate, but then draw a dark chocolate, we'll start a new game in the $\left(m-2,d\right)$ state. 

![](/img/2020-10-04-recursion-diagram.png){:width="450px" class="image-centered"}

Following the diagram above, we can generate the entire recursion relation. At the base of the left hand chain, we have the state $\left(1,0\right)$ which has $0\%$ probability to end in a soymilk chocolate. Similarly, if we reach the bottom of the right hand chain, we have the state $\left(0,1\right)$ which has $100\%$ chance to end in a soymilk chocolate. 

Carrying on like this, we get 

$$\begin{align}
P(m,d) &= \frac{m}{m+d}\frac{d}{m+d-1}P(m-1,d) \\ &+ \frac{m}{m+d}\frac{m-1}{m+d-1}\frac{d}{m+d-2}P(m-2,d) \\ &+ \frac{m}{m+d}\frac{m-1}{m+d-1}\frac{m-2}{m+d-2}\frac{d}{m+d-3}P(m-3,d) \\ &+ \ldots \\ &+ \frac{d}{m+d}\frac{m}{m+d-1}P(m,d-1) \\ &+ \frac{d}{m+d}\frac{d-1}{m+d-1}\frac{m}{m+d-2}P(m,d-2) \\ &+ \frac{d}{m+d}\frac{d-1}{m+d-1}\frac{d-2}{m+d-2}\frac{m}{m+d-3}P(m,d-3) \\ &+ \ldots \end{align}$$

It seems awfully odd that $P\left(2,3\right)$ is $1/2$ (as are $P(1,1)$ and $P(2,1)$ and $P(1,2).$ To quickly check what's going on, we can simulate with the code below. 

```python
import random
import copy
import numpy as np

N_soymilk, N_dark = (2, 8)
chocolates = ["SOYMILK"] * N_soymilk + ["DARK"] * N_dark

def round():
    last = "NA"
    bag = copy.deepcopy(chocolates)
    while len(bag) > 1:
        candidate = random.sample(bag, 1)[0]
        if last == "NA" or candidate == last:
            bag.remove(candidate)
            last = candidate
        else:
            last = "NA"
    if bag[0] == "SOYMILK":
        return(1)
    else:
        return(0)
        
results = [round() for _ in range(10_000_000)]
np.mean(results)
```

Indeed, we find $1/2$ everywhere we look. If we take this result for granted, we can use induction to show that the recursion equation generates $1/2$ in any higher case we wish to check, though we won't in this slender margin. 

<br>
 
