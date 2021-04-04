---
layout: post
published: false
title: 
date: 2021/04/03
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

This seems like a hard situation to get a guaranteed advantage. But advantage is information. 

We know that if we get the same answer $\left(Q-1\right)$ times in a row, then the next answer will be opposite. On its face, this is information in the case we've seen $(Q-1)$ repeats. 

But it's also information before then. 

Say we ask a single question and the answer is $\mathbf{T}.$ This means that it will be at most $(Q-2)$ more questions before we get a $\mathbf{F}$ which is not something we can say about a coin flip!

### What to do

If we find ourselves having seen $(Q-1)$ repeated answers, then we are sure to double whatever money we have left on the next turn by guessing the opposite.

But what about the step before that? 

Say we've just asked our first question and the answer was $\mathbf{T}.$ There are only two things that can happen next. Either, the answer is $\mathbf{F}$ we have no information about the following answer, or it's $\mathbf{T}$ and the next answer is guaranteed to be $\mathbf{F}.$

So, we have two opportunities to bet on $\mathbf{F}.$ On the first guess, we bet $x$ on $\mathbf{F}.$ If it comes out then we have $(1+x)$ on the next turn. If it doesn't, then we lose $x,$ bringing us to $\left(1-x\right).$ In this case, the next question is a sure bet, so we bet the farm, which would double our total, leaving us with $2(1-x).$ 

Now, we are trying to maximize the worst outcome. If one of these outcomes is worse than the other, it means that we're being too aggressive with $x.$ After all, $x$ will drive the better outcome higher, and the lower outcome lower. This means that to maximize the worst outcome, we can just set these equal to each other:

$$ 2(1-x) = 1 + x$$

which leads to $x = 4/3.$





<br>
