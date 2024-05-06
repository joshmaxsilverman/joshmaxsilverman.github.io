---
layout: post
published: true
title: Can You Beat the Heats?
date: 2024/05/06
subtitle: A good old racetrack whodunit.
tags: information-theory trees
---

>**Question**: There are $25$ sprinters at a meet, and there is a well-defined order from fastest to slowest. That is, the fastest sprinter will always beat the second-fastest, who will in turn always beat the third-fastest, and so on. However, this order is not known to you in advance.
>
>To reveal this order, you can choose any $10$ sprinters at a time to run in a heat. For each heat, you only know the ordinal results, so which runner finishes first, second, third, and so on up to $10^\text{th}.$ You do not know the specific finishing time for any runner, making it somewhat difficult to compare performances across heats.
>
>Your goal is to determine with absolute certainty which of the $25$ sprinters is fastest, which is second-fastest, and which is third-fastest. What is the fewest number of heats needed to guarantee you can identify these three sprinters?
>
>**Extra credit**: At a different meet, suppose there are six sprinters that can race head-to-head. (In other words, there are only two sprinters per heat.) Again, they finish races in a consistent order that is not known to you in advance.
>
>This time, your goal is to determine the _entire_ order, from the fastest to the slowest and everywhere in between. What is the fewest number of head-to-head races needed to guarantee you can identify this ordering?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-beat-the-heats))

## Standard credit

In the $25$ person race, we want to find the three fastest people. 

It isn't possible to find the three fastest people without racing all of the sprinters since we can't rank someone in the absence of information. Since each race takes $10$ people, we can't fit $25$ sprinters into less than $3$ races. So, $3$ is the absolute minimum number of races we can hope to use.

Happily, this threshold can be saturated.

- First, we can race any $10$ of the sprinters, identifying the top three ouf of them.
- Next, pick another $8$ of the un-raced sprinters and race them with the second and third fastest sprinters from the first race.
- Now, take the two fastest from the second race, the winner of the first race, and the $7$ remaining un-raced sprinters and run them in a race.

The top three finishers of the last race are the three fastest sprinters.

## Extra credit

Before we start, it pays to think about the information we seek. 

There are $6! = 720$ possible orderings of the six runners which is $\log_2 6! \approx 9.49$ bits of information.

If each race we ran halved the number of possibilities (a perfect "binary question"), it would yield $\log_2 2 = 1$ bit. So, we should expect $10$ races at the very least.

There are at least two ways to think about this.

The first is by symmetry

### By symmetry

At the outset, the possible orderings are fully symmetric with respect to the runners. So, pick any two runners, say $A$ and $B$ and race them against each other. The result of this race will either have $A$ or $B$ winning. Since, at this stage, the orderings are symmetric with regard to $A$ and $B,$ this will remove half of all possibilities, leaving $360$ orders. $1$ bit down, $\approx 8.49$ to go!

Since we haven't touched runners $C$ and $D,$ or $E$ and $F,$ we can pair them off and remove half of all outstanding possibilities again twice more. This brings us down to $90$ orders. $3$ bits down.

Now, running these three races has destroyed the symmetry between those who won their race and those who lost their race. However, there is still symmetry amongst the winners and losers. For argument's sake, say $A,$ $C,$ and $D$ won their races while $B,$ $D,$ and $F$ lost theirs. If we pair $A$ and $C$ in a race, we can eliminate another half of all orders, leaving $45$ orders.

After this question, we will be left with a situation that looks like

< A faster than C, A faster than B, D faster than B >

We don't know if C or B is faster. If we are lucky, B is faster than C. But if it's reversed, we will need another measurement to fully order $\{A,B,C,D\}.$

Now, we have to place $E$ and $F$ in this ordering. We have no information about where $E$ is relative to the others, so we can go position by position (there are $5$ positions). Call the number of races it takes to place $E$ $x.$ That means there will be $(5-x)$ positions left for $F$ by the time $E$ is placed. So, the worst case for placing $E$ and $F$ is $5$ additional races. 

Put together with the $6$ from earlier, we get $11$ races to fully order the sprinters, one more than the lower bound.

### Sorting

The other way to approach this is as a sorting problem. 

Suppose there is a fastest way to sort $N$ sprinters. Whatever it is, it must be faster to sort fewer sprinters. 

So, let's split them into two groups of $3$ and $3$. To order one of these groups, in the worst case, we need races between all three. So, it will take $3+3=6$ races to sort these two sub-groups.

Now, with two ordered lists say $\{A,B,C\}$ and $\{D,E,F\}$, we can merge them.

Call the final list $L.$ Now, race the sprinters at the top of either list and put the winner into $L.$ Now, keep doing that until one of the lists is empty. The worst case is when lists flip flop winners. The most this can happen is $6-1=5$ times.

So, the number of races in the worst case scenario is $6 + 5 = 11.$

**Note**: following this logic, it seems like we ought to split the groups of three into a group of two and a group of one. However, once we do the housekeeping to merge them, it would be the same number of races either way. So, we don't further subdivide once lists have three or fewer sprinters.





<br>
