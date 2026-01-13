---
layout: post
published: false
title: Beating the sphinx
date: 2021/04/03
subtitle: What profit can you lock in if three-in-a-row never appears?
subtitle: If the coin can’t land the same way thrice, what payoff can you guarantee?
source: fivethirtyeight
theme: probability
---

>**Question**: an oracular Sphinx gives you a starting capital of a dollar and the opportunity to wager any portion of your stake on a series of $4$ coin flips. The coin flips are completely random, except for the fact that the Sphinx guarantees there aren't any runs of $3$ like outcomes in a row (no $\mathbf{H}\rightarrow\mathbf{H}\rightarrow\mathbf{H}$ or $\mathbf{T}\rightarrow\mathbf{T}\rightarrow\mathbf{T}$).  If you set your wagers right, what is your maximum guaranteed profit for the worst-case outcome? If the Sphinx now offers you $N$ wagers, and guarantees that no $Q$ flips in a row will have the same outcome, what is your maximum guaranteed profit?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-outthink-the-sphinx/))

**Edit**: there is likely an issue with the value for $x.$ Will revisit later.

## Solution

This seems like a hard situation to get a guaranteed advantage. Advantage is information and, on its face, it seems like we only have information in the case where we've already seen $(Q-1)$ repeats.

But it's also information before then. 

Suppose we ask a single question and the answer is $\mathbf{T}.$ This means that, in the $Q=3$ case, it will be at most $(Q-2) = 1$ more questions before we get a $\mathbf{F}.$ This is not something we can say about a coin flip!

### What to do

Say we've just asked our first question and the answer was $\mathbf{T}.$ There are only two things that can happen next. Either, 

- the answer is $\mathbf{F}$, or 
- it's $\mathbf{T}$ and the next answer is guaranteed to be $\mathbf{F}.$

In the second case, we are sure to double whatever amount $x$ we have left on the next turn by betting it all on $\mathbf{F}.$

So, we have two opportunities to bet on $\mathbf{F}.$ If, on the second question, we bet $x$ on $\mathbf{F}$ and it comes out, then we'll have $(1+x)$ going into the third question. If it doesn't, then we'll lose $x,$ bringing us down to $\left(1-x\right).$ But, in this case, the third question is a sure bet, so we can wager the farm and double our total, bringing us up to $2(1-x).$ 

We are trying to maximize the guaranteed worst outcome. If either of these outcomes is worse than the other, it means that we are being too aggressive with $x.$ After all, increasing $x$ will drive the better outcome higher, and the worse outcome lower. This means that to maximize the worst outcome, the two outcomes have to be equal:

$$ 2(1-x) = 1 + x$$

which leads to $x = 4/3,$ a profit of $1/3$

The animating idea is this: we could wait to wager until we have a sure bet, which would make maximize our best case. But this brings our winnings in the other cases to zero. By using our information early early, and balancing our wagers, we can raise our floor at the expense of our ceiling.

![](/img/2021-04-04-basic-payoff.png){:width="400px" class="image-centered"}

### Ask me again, Bob

The requirement to employ this strategy is that a question has already been asked. Once that's happened, then, in either branch, we can increase our stake to $4/3$ in at most $2$ more questions. 

![](/img/2021-04-04-sphinx-payouts-base-case.png){:width="500px" class="image-centered"}

{:.caption}

Full tree for the $N=4, Q=3$ case. Each of the nodes at the bottom of the tree give rise to more sub-trees as $N$ gets bigger. The worst case is obtained by pasting the right most path onto the the $\mathbf{T}$ node of the left-most branch.

Extending the game to $N$ questions, we can find the worst case, which is when we repeatedly miss the first wager, and then make up for it with the sure bet on the second wager. 

Once this has happened, we can start our strategy over again which will require another $(Q-1) = 2$ questions, and will increase our stake by another factor of $4/3.$ If we have $N$ questions, then we can repeat this $\lfloor(N-1)/(Q-1)\rfloor$ times in the worst branch.

So, the best worst-case outcome is just 

$$ W_\text{best worst} = \left(\dfrac43\right)^{\lfloor\frac{N-1}{2}\rfloor}. $$

### Nice to see you again

When $Q > 3,$ we don't get a chance at a sure bet until we've seen $(Q-1)$ of the same answers in a row. We still have information about the outcome once a single answer has come down, but it's less than it was for $Q = 3.$ 

Intuitively, we should wager less on our first guess, and progressively more as we get closer to the sure bet, as in the $Q = 3$ case. 

It will take a tree of at least $N = Q$ questions to get to the sure bet, so we can draw a tree of $(Q + 1)$ questions to see the structure here. Let's try the $Q=5$ case, which takes $(Q-2) = 3$ guesses before we reach a sure bet. Again, assume that the answer to the first question is $\mathbf{T}.$

- If we wager $b_1$ on $\mathbf{F}$ for the first question, we either get lucky and have $(1+b_1)$ or get it wrong and go into the second question with $(1-b_1).$ If we do get lucky, then the process starts over and we can start the strategy again.
- Likewise, if we wager $b_2$ on $\mathbf{F}$ for the second question, we either get lucky and have $(1-b_1 + b_2),$ after which we can restart, or we get it wrong and go into the third question with $(1-b_1-b_2).$
- Finally, if we wager $b_3$ on $\mathbf{F}$ for the third question, we either get lucky and have $(1-b_1 - b_2 + b_3)$ going into a restart, or get it wrong and go into the sure bet question with $(1-b_1-b_2-b_3)$ to wager. 
- If we do get to the last case, then we have a sure bet on $\mathbf{F}$ and our stake becomes $2(1-b_1-b_2-b_3)$ (we wager everything we have left).

As before, if the worst-case outcome is less than the second-to-worst-case outcome, it means that $b_3$ was too aggressive. Likewise, if the second-to-worst-case outcome is less than the third-to-worst-case, it means that $b_2$ was too aggressive. And if the third-to-worst-case-outcome is less than the best-case outcome, it means that $b_1$ was too aggressive. 

![](/img/2021-04-04-sphinx-recursion.png){:width="800px" class="image-centered"}

Putting it all together, all four outcomes need to be equal to maximize the worst-case outcome:

$$\begin{align}
1+b_1 &= 1-b_1+b_2 \\
&= 1-b_2-b_2+b_3 \\
&= 2(1-b_1-b_2-b_3)
\end{align}$$

The first relationship gets $b_2 = 2\times b_1,$ while the second gets $b_3 = 2\times b_2 = 2^2\times b_1.$ 

The third relationshp gets

$$\begin{align}
1+b_1 &= 2\left(1-(b_1+b_2+b_3)\right) \\
&= 2\left(1 - b_1\left(1 + 2 + 2^2\right)\right) \\
&= 2\left(1 - b_1\left(2^3-1\right)\right) \\
&= 2 - 2b_1(2^3 - 1)
\end{align}
$$

or

$$ b_1 = \frac{1}{2^4 - 1}. $$

Since all outcomes are equal, this is the maximum guaranteed profit of the worst-case for $N = Q = 5.$

### Pick a Sphinx, any Sphinx

Now, as before, $N$ can be greater than $Q,$ and if $(N-1)/(Q-1) > 2,$ then the worst-case branch will have a chance to repeat. In general, the worst-case branch will be able to repeat $\lfloor\frac{N-1}{Q-1}\rfloor$ times.

Generalizing the last calculation, the sum $(b_1 + b_2 + \ldots + b_{Q-2})$ becomes $(2^{Q-2} - 1),$ and the guaranteed minimum fold-increase after the first $(Q-1)$ questions becomes $1 + b_1 = 1 + 1/(2^{Q-1} - 1).$

After $N$ questions, our winnings are

$$\begin{align}
W_\text{best worst}(N,Q) &= (1 + b_1)^{\lfloor\frac{N-1}{Q-1}\rfloor} \\
&= \left(1 + \frac{1}{2^{Q-1}-1}\right)^{\lfloor\frac{N-1}{Q-1}\rfloor} 
\end{align}$$

This lines up with expectations: as $Q$ grows, the questions get closer to a random coin flip and we can extract less profit per question. Also, when $Q=2,$ the questions flip-flop deterministically, and can double our money every question after the first.

<br>
