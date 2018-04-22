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


### Expectations

 | | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0
 - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - | 
10 | 5.010 | 4.810 | 4.510 | 4.210 | 4.010 | 3.810 | 3.510 | 3.210 | 3.010 | 2.810 | 2.510 | 2.210 | 2.010 | 1.810 | 1.510 | 1.210 | 1.010 | 0.810 | 0.510 | 0.210 | 0.0
9 | 4.49 | 4.29 | 3.99 | 3.79 | 3.49 | 3.29 | 3.09 | 2.79 | 2.59 | 2.29 | 2.09 | 1.89 | 1.69 | 1.39 | 1.19 | 0.99 | 0.79 | 0.59 | 0.49 | 0.29 | 0.2
8 | 3.98 | 3.78 | 3.48 | 3.28 | 3.08 | 2.78 | 2.58 | 2.38 | 2.18 | 1.88 | 1.68 | 1.48 | 1.28 | 1.08 | 0.98 | 0.78 | 0.58 | 0.48 | 0.48 | 0.48 | 0.5
7 | 3.47 | 3.27 | 3.07 | 2.87 | 2.67 | 2.37 | 2.17 | 1.97 | 1.77 | 1.57 | 1.37 | 1.27 | 1.07 | 0.87 | 0.77 | 0.67 | 0.57 | 0.47 | 0.47 | 0.57 | 0.8
6 | 3.06 | 2.86 | 2.66 | 2.46 | 2.26 | 2.06 | 1.86 | 1.66 | 1.56 | 1.36 | 1.16 | 1.06 | 0.86 | 0.76 | 0.66 | 0.56 | 0.56 | 0.56 | 0.56 | 0.76 | 1.0
5 | 2.75 | 2.55 | 2.35 | 2.15 | 1.95 | 1.75 | 1.65 | 1.45 | 1.25 | 1.15 | 1.05 | 0.85 | 0.75 | 0.65 | 0.65 | 0.55 | 0.55 | 0.65 | 0.75 | 0.95 | 1.2
4 | 2.44 | 2.24 | 2.04 | 1.84 | 1.74 | 1.54 | 1.44 | 1.24 | 1.14 | 0.94 | 0.84 | 0.74 | 0.74 | 0.64 | 0.64 | 0.64 | 0.64 | 0.74 | 0.94 | 1.14 | 1.5
3 | 2.13 | 1.93 | 1.83 | 1.63 | 1.53 | 1.33 | 1.23 | 1.13 | 0.93 | 0.83 | 0.83 | 0.73 | 0.63 | 0.63 | 0.63 | 0.63 | 0.73 | 0.83 | 1.03 | 1.33 | 1.8
2 | 1.92 | 1.72 | 1.62 | 1.42 | 1.32 | 1.22 | 1.02 | 0.92 | 0.82 | 0.82 | 0.72 | 0.72 | 0.62 | 0.62 | 0.72 | 0.72 | 0.82 | 1.02 | 1.22 | 1.62 | 2.0
1 | 1.71 | 1.51 | 1.41 | 1.31 | 1.21 | 1.01 | 0.91 | 0.91 | 0.81 | 0.71 | 0.71 | 0.71 | 0.71 | 0.71 | 0.71 | 0.81 | 1.01 | 1.21 | 1.41 | 1.81 | 2.2
0 | 1.50 | 1.40 | 1.30 | 1.10 | 1.00 | 0.90 | 0.90 | 0.80 | 0.70 | 0.70 | 0.70 | 0.70 | 0.70 | 0.80 | 0.80 | 1.00 | 1.10 | 1.30 | 1.60 | 2.00 | 2.5

### Strategies

 | | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0
 - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - | 
10 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | 1.010 | -1.0
9 | 0.89 | 0.89 | 0.89 | 0.89 | 0.89 | 0.89 | 0.89 | 0.89 | 0.89 | 0.79 | 0.79 | 0.79 | 0.79 | 0.69 | 0.69 | 0.69 | 0.59 | 0.49 | 0.29 | 0.09 | -1.0
8 | 0.88 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.78 | 0.68 | 0.68 | 0.68 | 0.58 | 0.58 | 0.58 | 0.48 | 0.48 | 0.38 | 0.28 | 0.08 | -0.28 | -1.0
7 | 0.77 | 0.77 | 0.67 | 0.67 | 0.67 | 0.67 | 0.67 | 0.67 | 0.57 | 0.57 | 0.57 | 0.47 | 0.47 | 0.37 | 0.37 | 0.27 | 0.17 | 0.07 | -0.27 | -0.47 | -1.0
6 | 0.66 | 0.66 | 0.66 | 0.66 | 0.56 | 0.56 | 0.56 | 0.56 | 0.46 | 0.46 | 0.46 | 0.36 | 0.36 | 0.26 | 0.26 | 0.16 | 0.06 | -0.16 | -0.36 | -0.56 | -1.0
5 | 0.55 | 0.55 | 0.55 | 0.55 | 0.55 | 0.45 | 0.45 | 0.45 | 0.45 | 0.35 | 0.35 | 0.25 | 0.25 | 0.15 | 0.15 | 0.05 | -0.15 | -0.25 | -0.45 | -0.65 | -1.0
4 | 0.54 | 0.54 | 0.54 | 0.44 | 0.44 | 0.44 | 0.44 | 0.34 | 0.34 | 0.34 | 0.24 | 0.24 | 0.14 | 0.14 | 0.04 | -0.14 | -0.24 | -0.34 | -0.44 | -0.64 | -1.0
3 | 0.43 | 0.43 | 0.43 | 0.43 | 0.43 | 0.33 | 0.33 | 0.33 | 0.23 | 0.23 | 0.23 | 0.13 | 0.13 | 0.03 | -0.13 | -0.13 | -0.23 | -0.33 | -0.53 | -0.63 | -1.0
2 | 0.42 | 0.42 | 0.32 | 0.32 | 0.32 | 0.32 | 0.22 | 0.22 | 0.22 | 0.12 | 0.12 | 0.12 | 0.02 | -0.12 | -0.12 | -0.22 | -0.32 | -0.42 | -0.52 | -0.72 | -1.0
1 | 0.31 | 0.31 | 0.31 | 0.31 | 0.31 | 0.21 | 0.21 | 0.21 | 0.11 | 0.11 | 0.01 | 0.01 | -0.11 | -0.11 | -0.21 | -0.21 | -0.31 | -0.41 | -0.51 | -0.71 | -1.0
0 | 0.30 | 0.30 | 0.30 | 0.20 | 0.20 | 0.20 | 0.20 | 0.10 | 0.10 | 0.00 | 0.00 | -0.00 | -0.10 | -0.20 | -0.20 | -0.30 | -0.40 | -0.50 | -0.60 | -0.70 | -1.0


### Code (Python)

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