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

### Nice to see you again



- layers -> exponent = $\lfloor\frac{N-1}{Q-1}\rfloor.$
- extend to $Q - 1 > 2$ -> recursive subtrees
- system of equations for profit 


<br>
