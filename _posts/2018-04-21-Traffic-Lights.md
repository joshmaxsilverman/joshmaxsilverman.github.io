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

Give the intersections coordinates: we start at $(E,N)$ and finish at $(0,0)$.  A strategy for a given intersection is a decision about what to do, based on what is displayed on the signals.  We can choose units of time so that $T$ is two units, and we can represent a strategy as a number $S(e,n)$ between $-1$ and $1$. This number represents the difference between the expected remaining total wait after crossing this intersection going east versus going north. That is, it is the expected advantage of going east.  If, $S(e,n)$ is, say, $.35$, that means that the pedestrian should go east unless east's signal is "NO-GO" and has a time-till-go of more than $.355$ units.  Negative strategy numbers represent an advantage for going north.

We can start by noticing that, for every $e$, $S(e,0)$ is $1$: we wait to go east no matter what. (Another simple case is an intersection of the form $(i,i)$; by symmetry, neither direction is preferable, and so it is always best to cross in whichever direction is open.  That is, $S(i,i)$ is $0$. But we won't need to rely on this observation.)

As we will see, for every other, "non-trivial," intersection $(e,n)$, strategy depends on the expected total waits, given optimal strategy, from intersections $(e-1,n)$ and $(e,n-1)$.

The expected wait time at a given intersection, $W(e,n)$ is a function of its strategy.  At an intersection with strategy $s$, the only situations in which we wait are the $|s|/2$ of the cases in which we find the preferred-direction signal with less than $|s|$ units to "GO."  Our average wait in those cases is also $|s|/2$, and so:

$$W(e,n) = S(e,n)^2/4$$

Call $E(e,n)$ the expected total wait time remaining, given optimal strategy, on arrival at intersection $(e,n)$.  Start with intersections of the form $(e,0)$.  $E(e,0)$ is $e$ times the expected wait for an intersection's east signal to display "GO."  Half of the time, the signal already displays "GO," and the other half of the time, it averages $.5$ units until "GO," so the expected wait is $.25$, and so $S(e,0)$ is $e/4$. Similarly, for every $n$, $E(0,n)$ is $n/4$. 

For non-trivial intersections, $E(e,n)$ is calculated from $W(e,n)$, which is the expected wait time at that intersection itself, plus a weighted sum of $E(e-1,n)$ and $E(e,n-1)$, weighted by how likely it is that we'll cross to the east and to the north:

$$E(e,n) = W(e,n) + \frac{1 + S(e,n)}{2}E(e-1,n) + \frac{1 - S(e,n)}{2}E(e,n-1)$$

And we calculate strategies for such intersections as follows. So long as the expected total remaining waits at the two possible next intersections are within $1$ of each other:

$$S(e,n) = E(e,n-1) - E(e-1,n)$$

But if that value is less than $-1$ or greater than $1$, then $S(e,n)$ is $-1$ or $1$.

It's a little complicated, but the upshot is that for non-trivial intersections we can calculate $E(e,n)$ from just $E(e-1,n)$ and $E(e,n-1)$.  This gives us a recurrence that lets us find, starting with the trivial expectations, $E(e,n)$ for any $(e,n)$.

The Python code below implements this.  The resulting strategy always favors heading in a direction, if there is one, that brings the coordinates closer together; that is, towards the $e = n$ "centerline." That's because it's always zero-wait at centerline intersections.

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