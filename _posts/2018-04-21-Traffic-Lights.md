---
layout: post
published: true
title: Traffic Lights
date: 2018/04/21
---

>We are to walk on a rectilinear grid $N$ blocks north and $E$ blocks east, making $N$ and $E$ crossings of timed intersections. The intersections are not synchronized with each other, but there is a constant time period $T$ such that, for a given intersection, the north-south and east-west signals alternate $T/2$ intervals of displaying "GO" (we may start across) and "NO-GO" (we may not start across), along with the number of seconds until the next signal change.  What should our strategy be, so as to have the lowest expected total time waiting at intersections?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-to-cross-the-street/))

## Solution

Give the intersections coordinates: we start at $(E,N)$, with $E$ and $N$ more intersections to cross going east and going north, and we finish at $(0,0)$.  A strategy for a given intersection is a decision about what to do, based on what is displayed on the signals.  We choose units of time so that $T$ is two units, and we can represent a strategy as a number $S(e,n)$ between $-1$ and $1$. This number represents the difference between the expected remaining total wait after crossing this intersection going north versus going east. That is, it is the expected advantage of going east.  If, $S(e,n)$ is, say, $.35$, that means that the pedestrian should go east unless east's signal is "NO-GO" and has a time-until-go of more than $.35$ units.  Negative strategy numbers represent an advantage for going north.

We can start by noticing that, for every $e$, $S(e,0)$ is $1$: we wait to go east no matter what. (Another simple case is an intersection of the form $(i,i)$; by symmetry, neither direction is preferable, and so it is always best to cross in whichever direction is open.  That is, $S(i,i)$ is $0$. While we won't need to rely on this observation, it will help us understand our results.)

As we will see, for every other, "non-trivial," intersection $(e,n)$, best-strategy depends on the expected total waits, given optimal strategy, from intersections $(e-1,n)$ and $(e,n-1)$.

The expected wait time _at_ a given intersection, $W(e,n)$ is a function of its strategy.  At an intersection with strategy $s$, the only situations in which we wait are those $\|s\|/2$ of cases in which we find the preferred-direction signal with less than $\|s\|$ units to "GO."  Our average wait in those cases is also $\|s\|/2$, and so:

$$W(e,n) = S(e,n)^2/4$$

Call $E(e,n)$ the expected total wait time remaining, given optimal strategy, on arrival at intersection $(e,n)$.  Start with intersections of the form $(e,0)$.  $E(e,0)$ is $e$ times the expected wait for an intersection's east signal to display "GO."  Half of the time, the signal already displays "GO," and the other half of the time, it averages $.5$ units until "GO," so the expected wait is $.25$, and so $S(e,0)$ is $e/4$. Similarly, for every $n$, $E(0,n)$ is $n/4$. 

For non-trivial intersections, $E(e,n)$ is calculated from $W(e,n)$, which is the expected wait time at that intersection itself, plus a weighted sum of $E(e-1,n)$ and $E(e,n-1)$, weighted by how likely it is that we'll cross to the east and to the north:

$$E(e,n) = W(e,n) + \frac{1 + S(e,n)}{2}E(e-1,n) + \frac{1 - S(e,n)}{2}E(e,n-1)$$

And we calculate strategies for such intersections as follows. So long as the expected total remaining waits at the two possible next intersections are within $1$ of each other:

$$S(e,n) = E(e,n-1) - E(e-1,n)$$

But if that value is less than $-1$ or greater than $1$, then $S(e,n)$ is $-1$ or $1$.

It's a little complicated, but the upshot is that for non-trivial intersections we can calculate $E(e,n)$ from just $E(e-1,n)$ and $E(e,n-1)$.  This gives us a recurrence that lets us find, starting with the trivial expectations, $E(e,n)$ for any $(e,n)$.

The Python code below implements this.  The resulting strategy always favors heading in a direction, if there is one, that brings the coordinates closer together; that is, towards the $e = n$ "centerline." That's because it's always zero-wait at centerline intersections.


 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0
 - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - | 
10 | 5.0010 | 4.7510 | 4.5010 | 4.2510 | 4.0010 | 3.7510 | 3.5010 | 3.2510 | 3.0010 | 2.7510 | 2.5010 | 2.2510 | 2.0010 | 1.7510 | 1.5010 | 1.2510 | 1.0010 | 0.7510 | 0.5010 | 0.2510 | 0.00
9 | 4.409 | 4.169 | 3.929 | 3.679 | 3.439 | 3.199 | 2.959 | 2.719 | 2.489 | 2.249 | 2.019 | 1.789 | 1.559 | 1.339 | 1.119 | 0.909 | 0.709 | 0.529 | 0.369 | 0.259 | 0.25
8 | 3.898 | 3.658 | 3.428 | 3.198 | 2.968 | 2.738 | 2.508 | 2.288 | 2.068 | 1.858 | 1.638 | 1.438 | 1.238 | 1.048 | 0.868 | 0.698 | 0.558 | 0.438 | 0.368 | 0.368 | 0.50
7 | 3.447 | 3.217 | 2.997 | 2.777 | 2.567 | 2.347 | 2.137 | 1.937 | 1.737 | 1.537 | 1.347 | 1.177 | 1.007 | 0.847 | 0.707 | 0.587 | 0.497 | 0.437 | 0.437 | 0.527 | 0.75
6 | 3.046 | 2.836 | 2.626 | 2.416 | 2.216 | 2.026 | 1.826 | 1.646 | 1.466 | 1.296 | 1.126 | 0.976 | 0.836 | 0.716 | 0.616 | 0.536 | 0.496 | 0.496 | 0.556 | 0.706 | 1.00
5 | 2.695 | 2.495 | 2.305 | 2.115 | 1.925 | 1.745 | 1.575 | 1.405 | 1.245 | 1.095 | 0.965 | 0.835 | 0.725 | 0.635 | 0.575 | 0.535 | 0.535 | 0.585 | 0.695 | 0.905 | 1.25
4 | 2.394 | 2.204 | 2.024 | 1.844 | 1.684 | 1.514 | 1.364 | 1.214 | 1.074 | 0.954 | 0.834 | 0.744 | 0.664 | 0.604 | 0.574 | 0.574 | 0.614 | 0.704 | 0.864 | 1.114 | 1.50
3 | 2.123 | 1.953 | 1.783 | 1.623 | 1.473 | 1.323 | 1.193 | 1.063 | 0.943 | 0.843 | 0.753 | 0.683 | 0.633 | 0.603 | 0.603 | 0.633 | 0.713 | 0.843 | 1.043 | 1.333 | 1.75
2 | 1.882 | 1.732 | 1.582 | 1.432 | 1.292 | 1.172 | 1.052 | 0.942 | 0.852 | 0.762 | 0.702 | 0.652 | 0.632 | 0.632 | 0.662 | 0.722 | 0.832 | 1.002 | 1.232 | 1.552 | 2.00
1 | 1.681 | 1.541 | 1.401 | 1.271 | 1.151 | 1.041 | 0.941 | 0.851 | 0.781 | 0.721 | 0.681 | 0.651 | 0.651 | 0.681 | 0.741 | 0.831 | 0.971 | 1.171 | 1.431 | 1.781 | 2.25
0 | 1.500 | 1.370 | 1.250 | 1.140 | 1.040 | 0.940 | 0.860 | 0.790 | 0.740 | 0.700 | 0.680 | 0.680 | 0.700 | 0.750 | 0.830 | 0.960 | 1.120 | 1.340 | 1.630 | 2.010 | 2.50

```python
E = 20
N = 10

# Populate trivial expecations

Exp = {}
for e in range(E):
    Exp[(e,0)] = e/4.0
for n in range(N):
    Exp[(0,n)] = n/4.0

for e in range(1,E):
    for n in range(1,N):
        EE = Exp[(e-1,n)]
        EN = Exp[(e,n-1)]
        Strategy = EN - EE
        if Strategy < -1:
            Strategy = -1
        if Strategy > 1:
            Strategy = 1
        WaitTimeHere = Strategy**2/4
        Exp[(e,n)] = WaitTimeHere + EE*(1+Strategy)/2 + EN*(1-Strategy)/2
```

<br>