---
layout: post
published: false
title: Supreme Vacancies
date: 2017/04/14
---

>Imagine that U.S. Supreme Court nominees are only confirmed if the same party holds the presidency and the Senate. What is the expected number of vacancies on the bench in the long run?
<!--more-->
>You can assume the following:
>
> - You start with an empty, nine-person bench.
> - There are two parties, and each has a 50 percent chance of winning the presidency and a 50 percent chance of winning the Senate in each election.
> - The outcomes of Senate elections and presidential elections are independent.
> - The length of time for which a justice serves is uniformly distributed between zero and 40 years.

([fivethirtyeight](https://fivethirtyeight.com/features/how-many-bingo-cards-are-there-in-the-world/))

## Solution:

Here is a broad-strokes "solution" that turns out to be just a pretty good approximation, but contains the essentials of the correct approach.

Every election has probability $1/2$ of giving joint control to one party or the other for the next two years. When that happens, all vacancies are filled immediately, and for those two years, new vacancies are filled instantly.

When a seat goes vacant, then, there's close to (hiding dark difficulties that are not hugely important to the answer but which will be explained below) a $1/2$ chance that it's during a joint-control cycle, and so the duration of the vacancy will be $0$, and $1/2$ chance that it's a divided-control period so that the seat will be vacant for the remainder of the current election cycle (a period of close to (!) $1$ year on average) plus however long it takes for an election to produce joint control. The expected number of elections to reach the first joint-control outcome is the same as the expected number of tosses of a coin to get a heads, which is $2$ (see Appendix 2 to see why). The second election happens $2$ years after the very next election after the seat goes vacant.  
Therefore the expected duration of the vacancy is (close to) $\frac{1}{2}(1+2)$, or $3/2$.  

The probability that a given seat is vacant at any one time is (close to):

$$ \frac{\frac{3}{2}}{20 + \frac{3}{2}} = \frac{3}{43}$$

That value is also (close to) the expected number of vacancies in that seat at any one time. And so the total expected number of vacancies at any one time is (close to) nine times that, or $27/43$, which is is about $.628$.

### Appendix 1: Why Only "Close To"?

There are two simplifications (false assumptions) in the simple reasoning above. First, it's not true that terms are exactly equally likely to end in joint- and divided-control cycles. Second, term-ends are not exactly uniformly distributed as to where they fall within cycles. The second inexactness turns out to be negligible in effect, whereas the first is more significant.

The fact that any given term (after the very first ones, which we can ignore as negligible in the long term) starts in a joint-control cycle---because only then will the Senate confirm a nomination---entails that the probability is a little more than $1/2$ that it will also end in a joint-control cycle, because there is probability $1$ that it ends in joint control if it ends in the same cycle in which it began (of which there is some positive probability up to $1/20$), and $1/2$ if it ends in any later one. 

To cut to the chase, this makes the average duration a vacancy not $3/2$ but about $1.45$ and the expected number of vacancies not $.628$ but about $.608$. Details follow.

Let's forget about years and calculate in time units of (two-year) cycles. Term durations are uniformly distributed between $0$ and $20$ cycles, with an expectation of $10$. Each term (after the starting ones) starts some time $t$, between $0$ and $1$, into a joint-control cycle. If it ends in the same cycle ($(1-t)/20$ chance of that), there is probability $1$ of ending in a joint-control cycle. If not ($1-(1-t)/20$ chance), there is probability $1/2$ of that. So a term starting $t$ into a cycle has the following chance of ending in a joint-control cycle:

$$\frac{1-t}{20} \times 1 + \left(1 - \frac{1-t}{20}\right)\times\frac{1}{2} 
= \frac{21-t}{40}$$ 

And so a term has chance:

$$1 - \frac{21-t}{40} = \frac{19+t}{40}$$

of ending in a divided-control cycle.

The many terms that start at the beginning of joint-control cycles (after some divided-control ones), have end-times uniformly distributed between $0$ and $20$ cycles after the cycle start-times, and so in particular the end times that fall in divided-control cycles are uniformly distributed across them. So such terms that end in divided-control cycles have expected vacancies of exactly $3/2$.

But terms that start some positive time $t$ into a (joint-control) cycle and end in a divided-control cycle have a slightly higher chance of ending before than ending after $t$ into a cycle.  Such terms have end-times uniformly spread over the periods that consist of the $19$ complete cycles within their possible durations, plus the initial $t$ portion of the cycle following those $19$. That means that such a term has probability $20t/(19+t)$ of ending less than $t$ into its end cycle, which is a bit greater than $t$.

Taking that complication explicitly into account would involve finding an expression for the nonuniform distribution of such end-times, which from where I'm sitting looks like task better suited to the talents of others. Less imposing is the task of showing that, to a very close approximation, the distribution is in fact uniform; that is, that we can assume that it is uniform with very little effect on our calculation.

Every term that ends in a divided-control cycle (every "TEDC") has its root in a term that started at the start of a joint-control cycle. The first-generation TEDCs have their ends uniformly distributed within cycles, producing uniformly-distributed starting points for second-generation TEDCs.

To find out how the ends of second-generation TEDCs are distributed within cycles, we calculate the chance that a TEDC with start time $t_1$ into a cycle ends less than $t_2$ into a cycle. If $t_1 \leq t_2$, then that chance is:

$$\frac{19t_2+t_1}{19+t_1}$$

and if $t_1 \geq t_2$, the chance is:

$$\frac{20t_2}{19+t_1}$$

So the chance that second-gen TEDCs with uniformly distributed start times $t_1$ into a cycle end by $t_2$ in a cycle is:

$$\int_{x=0}^y \frac{19y+x}{19+x} dx
 + \int_{x=y}^1 \frac{20y}{19+x} dx$$

$$ = (19y-19)\ln\left(\frac{y+19}{19}\right) + y + 20y \ln\left(\frac{20}{19+y}\right)$$

Here's a graph of this function together with the function $y = t_2$, which characterizes the uniform distribution. 

![Close functions.](/img/CloseFunctions.PNG)

As you can see, this distribution is so extremely close to uniform that to a very good approximation we can assume that second-gen TEDCs too have end times uniformly distributed in cycles, and hence that so do third-gen, and so on. That is, we can assume that to a very good approximation all term end-times are uniformly distributed as to where they occur within cycles.

To calculate the expected length of a vacancy, we'll need to determine the distribution of term start-times. But first we'll calculate the expected length of a vacancy as a function of the time $t$ that the previous term began. We established above the chance ($(19+t)/40$) that a term starting $t$ into a cycle ends in a divided-control cycle. Because we now know that the distribution within that ending cycle is basically uniform, we expect the term, if it does end in divided control, to end halfway though a cycle, and so the expected vacancy is $3/2$ cycles---that is, half a cycle plus the one full cycle needed to produce the two elections that are expected to generate the first joint-control government.

Thus the expected length in cycles of a vacancy after a term starting at $t$ is:

$$\frac{19+t}{40} \times \frac{3}{2} = \frac{3(19+t)}{80}$$

Now to determine how term start-times are distributed. There are two cases. The terms that start some positive time into a joint-control cycle are uniformly distributed within such cycles. And there are terms that start right when joint control newly occurs. We need to know what proportion of all terms are of this latter kind.

The terms that start at the start of a cycle (after the very start, and with exceptions of probability zero) are the successors of terms that end in divided-control cycles, and so there are exactly as many of the former as of the latter. Let $p$ be the probability that a term starts at the start of a cycle, which is also the probability that a term ends in a divided-control cycle. We will find $p$ by relying on both facts about it. 

A proportion $p$ of terms start at the start of a cycle, and each has chance $19/40$ of ending in a divided-control cycle. And the remaining $(1-p)$ of terms have start-times uniformly distributed between $0$ and $1$ cycles into a cycle, with chance of ending in a divided-control cycle being $(19+t)/40$. So the overall probability of a term ending in a divided-control cycle is:

$$p = p \times \frac{19}{40} 
+ (1-p) \int_{t=0}^1 \frac{19+t}{40} dt$$

$$ = \frac{19}{40}p + \frac{39}{80}(1-p)
= \frac{39}{80} - \frac{1}{80}p
$$ 

$$ p = \frac{39}{81} $$

So $39/81$ of terms start at $t=0$. Thus the overall expected vacancy duration is:

$$ \frac{39}{81} \times \frac{57}{80} 
+ \frac{42}{81} \times \int_{t=0}^1\frac{3(19+t)}{80} dt $$

$$ = \frac{2223}{6480} + \frac{91}{240} = \frac{13}{18} = .7\overline{2} $$

That's in cycles, so the average vacancy is $13/9$, or $/1.\overline{4}$ years.

The expected number of vacancies at any random time, then, is:

$$9\times \frac{\frac{13}{9}}{20 + \frac{13}{9}} = \frac{117}{193} \approx .606$$

Verified by simulation (code below).

### Appendix 2: How Many Flips to Get a Heads?

Flipping a fair coin, the expected number $E$ of flips when the first Heads occurs is $1/2$ times $1$ (half the time, it's the first flip) plus $1/2$ times $1+E$ (half the time, you have one Tails and are back where you started). So:

$$ E = \frac{1}{2} + \frac{1}{2}(1+E)$$

$$E = 2$$

### Code (Python):

```python
{% include SupremeVacancies.py %}
```

<br>
