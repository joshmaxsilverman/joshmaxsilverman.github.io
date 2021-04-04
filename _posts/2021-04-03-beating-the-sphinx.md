---
layout: post
published: false
title: Beating the Sphinx
date: 2021/04/03
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

This seems like a hard situation to get a guaranteed advantage. Advantage is information and, on its face, it seems like we have information in the case where we've already seen $(Q-1)$ repeats.

But it's also information before then. 

Say we ask a single question and the answer is $\mathbf{T}.$ This means that, in the $Q=3$ case, it will be at most $(Q-2) = 1$ more questions before we get a $\mathbf{F}.$ This is not something we can say about a coin flip!

### What to do

Say we've just asked our first question and the answer was $\mathbf{T}.$ There are only two things that can happen next. Either, the answer is $\mathbf{F}$ we have no information about the following answer, or it's $\mathbf{T}$ and the next answer is guaranteed to be $\mathbf{F}.$

In the second case, we are sure to double whatever amount $x$ we have left on the next turn by betting it all on $\mathbf{F}.$

So, we have two opportunities to bet on $\mathbf{F}.$ If, on the first question, we bet $x$ on $\mathbf{F}$ and it comes out, then we'll have $(1+x)$ on the next turn. If it doesn't, then we'll lose $x,$ bringing us down to $\left(1-x\right).$ But, in this case, the next question is a sure bet, so we can wager the farm and double our total, bringing us up to $2(1-x).$ 

We are trying to maximize the guaranteed worst outcome. If either of these outcomes is worse than the other, it means that we are being too aggressive with $x.$ After all, increasing $x$ will drive the better outcome higher, and the worse outcome lower. This means that to maximize the worst outcome, we can just set these equal to each other:

$$ 2(1-x) = 1 + x$$

which leads to $x = 4/3.$

The animating idea is this: we could wait to wager until we have a sure bet, which would make maximize our best case. But this brings our winnings in the other cases to zero. By betting early, and balancing our wagers, we can raise our floor at the expense of our ceiling.

### Ask me again, Bob

The requirement to employ this strategy is that a question has already been asked. Once that's happened, then, in either branch, we can increase our stake to $4/3$ in at most $2$ more questions. 

Extending the game to $N$ questions, we can find the worst case, which is when we repeatedly miss the first wager, and then make up for it with the sure bet on the second wager. 

Once this has happened, we can start our strategy over again which will require another $Q-1 = 2$ questions, and increase our stake by another factor of $4/3.$ If we have $N$ question, then we can repeat this $\lfloor(N-1)/(Q-1)\rfloor$ times in the worst branch.

So, best guaranteed worst outcome is just 

$$ W_\text{best worst} = \left(\dfrac43\right)^{\lfloor\frac{N-1}{2}\rfloor}. $$

### Nice to see you again

When $Q > 3,$ we don't get a chance at a sure bet until we've seen $(Q-1)$ of the same answers in a row. We still have information about the outcome once a single answer has come down, but it's less than it was for $Q = 3.$ 

Intuitively, we should bet less on our first guess, and progressively more as we get closer to the sure bet, as in the $Q = 3$ case. 

It will take a tree of at least $N = Q$ questions to get to the sure bet, so we can draw a tree of $(Q + 1)$ questions to see the structure here. 

- If we wager $b_1$ on the first question, we either get lucky and have $(1+b_1)$ or get it wrong and go into the second question with $(1-b_1).$ If we do get lucky, then the process starts over and we can start the strategy again.
- Likewise, if we wager $b_2$ on the second question, we either get lucky and have $(1-b_1 + b_2),$ after which we can restart, or we get it wrong and go into the third question with $(1-b_1-b_2).$
- Finally, if we wager $b_3$ on the third question, we either get lucky and have $(1-b_1 - b_2 + b_3)$ going into a restart, or get it wrong and go into the sure bet question with $(1-b_1-b_2-b_3)$ to wager. 
- If we do get to the last case, then our stake after the sure bet will be $2(1-b_1-b_2-b_3).$

As before, if the worst case outcome is less than the second worst case, it means that $b_3$ was too aggressive. Likewise, if the second to worst outcome is less than the third to worst case, it means that $b_2$ was too aggressive. And if the third to worst outcome is less than the best outcome, it means that $b_1$ was too aggressive. 

Putting it all together, all four outcomes need to be equal to maximize the worst outcome:

$$\begin{align}
1+b_1 &= 1-b_1+b_2 \\
1-b_1+b_2 &= 1-b_2-b_2+b_3 \\
1-b_1-b_2+b_3 &= 2(1-b_1-b_2-b_3)
\end{align}$$

The first relationship gets $b_2 = 2\times b_1,$ while the second gets $b_3 = 2\times b_2 = 2^2\times b_1.$ 

We can rewrite the third relationship as 

$$(1-b_1-b_2-b_3) + 2b_3 = 2(1-b_1-b_2-b_3)$$

or 

$$\begin{align}
b_3 &= \frac12 \left(1-b_1-b_2-b_3\right) \\
&= \frac{1 - b_1\left(1 + 2 + 2^2\right)}{2} \\
&= \frac{1 - b_1(2^3 - 1)}{2}
$$


- extend to $Q - 1 > 2$ -> recursive subtrees
- system of equations for profit 


<br>
