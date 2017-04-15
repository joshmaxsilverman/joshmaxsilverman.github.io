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

Every election has probability $1/2$ of giving joint control to one party or the other. When a seat goes vacant, then, there's $1/2$ chance that the duration of the vacancy will be $0$, and $1/2$ that the seat will be vacant for the remainder of the current election cycle (a period of $1$ year on average) plus however long it takes for an election to produce joint control. The expected number of elections to reach the first joint-control outcome is the same as the expected number of tosses of a coin to get a heads, that is, $2$. The second election happens $2$ years after the very next election after the seat goes vacant.  Therefore the expected duration of the vacancy is $\frac{1}{2}(1+2)$, or $3/2$.  

The probability that a given seat is vacant at any one time is:

$$ \frac{\frac{3}{2}}{20 + \frac{3}{2}} = \frac{3}{43}$$

That value is also the expected number of vacancies _in that seat_ at any one time. And so the total expected number of vacancies at any one time is nine times that, or $27/43$, which is is about $.628$

### Code (Python):

```python
{% include SupremeVacancies.py %}
```

<br>
