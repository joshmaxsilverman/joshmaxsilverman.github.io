---
layout: post
published: true
title: Wordly Wise
date: 2020/09/20
---

>Question Every night your children change their favorite word and refuse to let you go to bed until you guess which word it is. If you guess wrong, they'll tell you if their word comes before or after yours in a list of all words. If there are 267,751 words that they're knowledgable about, how many guesses will you take, on average, to uncover their word?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-break-a-very-expensive-centrifuge/))

## Solution

First of all, it doesn't matter whether these are words, or pictures, or numbers — so long as they can be ordered it's the same problem. 

### Small cases

Let's think about how things should go if we had $3$ items. If we first asked if the number was $1$ that would be a waste, because in $2/3$ of the cases, it wouldn't be, and we'd have to ask a second question, for an average of $\approx 1.66$ questions. By contrast, if we asked about $2$ first, we would be done — it would either be $2$ or it would be $1$ or $3$ which we'd learn when they said we were too low or too high. 

Similarly, if we had $7$ items, we could ask about $4$ first. $1/7$ of the time we'll learn that we guessed right while $3/7$ of the time we'll have guessed too high and the other $3/7$ of the time we'll have guessed too low. If we guessed too high or too low, then we're back in the $3$-number case. So, on average, we'd need 

$$1\times\frac17 + 2\times\frac67 = 13/7 \approx 1.86$$

The pattern here is that in every layer we double the number of numbers, and that each node is halfway between the nodes that emerge from it. These are called binary trees. 

For trees like this, the number of questions we need to ask is one less than the number of layers. We can make trees like this of size $1, 1+2=3,1+2+4=7,1+2+4+8=15, \ldots$ and so on. The $n^\text{th}$ layer in such a tree contains $2^{n-1}$ numbers.


### Questions for a binary tree 

If the tree has $n$ layers, then it has a total of 

$$2^0 + 2^1 + 2^2 + \cdots + 2^{n-1} + 2^n$$

nodes in it, which comes out to $$2^{n+1} - 1.$$ 

If the kids pick their word at random, then there will be $1$ node that takes $1$ question, $2$ nodes that take $2$ questions, $4$ nodes that take $3$ questions, and so on, until the $(n-1)^\text{st}$ layer. Both the $(n-1)^\text{st}$ and the $n^\text{th}$ layer will require $(n-1)$ questions, making the average number of questions equal to

$$\langle Q\rangle = \dfrac{\sum\limits_{i=0}^{n-2} i 2^{i-1}}{\sum\limits_{i=0}^{n-1} 2^{i-1}} + (n-1)\left(2^{n-1} + 2^n\right) = \frac{2^{n-1}(2n-3) + 1}{2^n-1}$$


### Non-binary trees

For $2^n - 1$ numbers, the question format implicates the binary tree as the natural strategy for extracting the secret word. It's as efficient as possible given the means of interrogation. 

That's great, but $267,751$ is not of the form $2^n - 1$, it's $5608$ greater than $2^{18} - 1.$  What do we do when the number of words is not equal to $1$ less than a power of $2$?

Perhaps we could put $2^{18}-1$ of the numbers into a binary tree, and put the first $5608$ numbers into their own set. Surely, we could sift through the $5608$ numbers in fewer questions than the next biggest binary tree, which can hold $2^{13} - 1$ numbers. However, this gives a guaranteed extra question for all $267,751$ numbers in exchange for getting just under $(2^{13}\times 12 + 1)/(2^{13}-1)$ approx 12$ questions on $5608$ of the numbers.

That doesn't seem worth it. 

In fact, the best strategy is still to use a single binary tree. 

<br>
