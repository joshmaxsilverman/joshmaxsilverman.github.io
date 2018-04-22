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

I was quite surprised to find that traversing a $20$ by $10$ grid, which means crossing _thirty_ intersections, the expected wait is just $1.5$ times the length of a "NO-GO" period.

### Expectations

 | | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0
 - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - | 
0 | 5.000 | 4.750 | 4.500 | 4.250 | 4.000 | 3.750 | 3.500 | 3.250 | 3.000 | 2.750 | 2.500 | 2.250 | 2.000 | 1.750 | 1.500 | 1.250 | 1.000 | 0.750 | 0.500 | 0.250 | 0.00
1 | 4.401 | 4.161 | 3.921 | 3.671 | 3.431 | 3.191 | 2.951 | 2.711 | 2.481 | 2.241 | 2.011 | 1.781 | 1.551 | 1.331 | 1.111 | 0.901 | 0.701 | 0.521 | 0.361 | 0.251 | 0.25
2 | 3.892 | 3.652 | 3.422 | 3.192 | 2.962 | 2.732 | 2.502 | 2.282 | 2.062 | 1.852 | 1.632 | 1.432 | 1.232 | 1.042 | 0.862 | 0.692 | 0.552 | 0.432 | 0.362 | 0.362 | 0.50
3 | 3.443 | 3.213 | 2.993 | 2.773 | 2.563 | 2.343 | 2.133 | 1.933 | 1.733 | 1.533 | 1.343 | 1.173 | 1.003 | 0.843 | 0.703 | 0.583 | 0.493 | 0.433 | 0.433 | 0.523 | 0.75
4 | 3.044 | 2.834 | 2.624 | 2.414 | 2.214 | 2.024 | 1.824 | 1.644 | 1.464 | 1.294 | 1.124 | 0.974 | 0.834 | 0.714 | 0.614 | 0.534 | 0.494 | 0.494 | 0.554 | 0.704 | 1.00
5 | 2.695 | 2.495 | 2.305 | 2.115 | 1.925 | 1.745 | 1.575 | 1.405 | 1.245 | 1.095 | 0.965 | 0.835 | 0.725 | 0.635 | 0.575 | 0.535 | 0.535 | 0.585 | 0.695 | 0.905 | 1.25
6 | 2.396 | 2.206 | 2.026 | 1.846 | 1.686 | 1.516 | 1.366 | 1.216 | 1.076 | 0.956 | 0.836 | 0.746 | 0.666 | 0.606 | 0.576 | 0.576 | 0.616 | 0.706 | 0.866 | 1.116 | 1.50
7 | 2.127 | 1.957 | 1.787 | 1.627 | 1.477 | 1.327 | 1.197 | 1.067 | 0.947 | 0.847 | 0.757 | 0.687 | 0.637 | 0.607 | 0.607 | 0.637 | 0.717 | 0.847 | 1.047 | 1.337 | 1.75
8 | 1.888 | 1.738 | 1.588 | 1.438 | 1.298 | 1.178 | 1.058 | 0.948 | 0.858 | 0.768 | 0.708 | 0.658 | 0.638 | 0.638 | 0.668 | 0.728 | 0.838 | 1.008 | 1.238 | 1.558 | 2.00
9 | 1.689 | 1.549 | 1.409 | 1.279 | 1.159 | 1.049 | 0.949 | 0.859 | 0.789 | 0.729 | 0.689 | 0.659 | 0.659 | 0.689 | 0.749 | 0.839 | 0.979 | 1.179 | 1.439 | 1.789 | 2.25
10 | 1.5010 | 1.3710 | 1.2510 | 1.1410 | 1.0410 | 0.9410 | 0.8610 | 0.7910 | 0.7410 | 0.7010 | 0.6810 | 0.6810 | 0.7010 | 0.7510 | 0.8310 | 0.9610 | 1.1210 | 1.3410 | 1.6310 | 2.0110 | 2.50

### Strategies

 | | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0
 - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - |  - | 
0 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | -1.00
1 | 0.841 | 0.831 | 0.831 | 0.821 | 0.811 | 0.801 | 0.791 | 0.771 | 0.761 | 0.741 | 0.721 | 0.701 | 0.671 | 0.641 | 0.601 | 0.551 | 0.481 | 0.391 | 0.251 | 0.001 | -1.00
2 | 0.752 | 0.742 | 0.732 | 0.722 | 0.702 | 0.692 | 0.672 | 0.652 | 0.632 | 0.612 | 0.582 | 0.552 | 0.512 | 0.472 | 0.422 | 0.352 | 0.272 | 0.162 | 0.002 | -0.252 | -1.00
3 | 0.683 | 0.663 | 0.653 | 0.633 | 0.623 | 0.603 | 0.583 | 0.553 | 0.533 | 0.503 | 0.473 | 0.433 | 0.393 | 0.343 | 0.283 | 0.213 | 0.123 | 0.003 | -0.163 | -0.393 | -1.00
4 | 0.614 | 0.594 | 0.584 | 0.564 | 0.544 | 0.524 | 0.504 | 0.474 | 0.444 | 0.414 | 0.374 | 0.334 | 0.294 | 0.234 | 0.174 | 0.094 | 0.004 | -0.124 | -0.274 | -0.484 | -1.00
5 | 0.555 | 0.535 | 0.515 | 0.495 | 0.475 | 0.455 | 0.425 | 0.395 | 0.365 | 0.335 | 0.295 | 0.255 | 0.205 | 0.145 | 0.085 | 0.005 | -0.095 | -0.215 | -0.355 | -0.555 | -1.00
6 | 0.496 | 0.476 | 0.456 | 0.436 | 0.416 | 0.386 | 0.366 | 0.336 | 0.306 | 0.266 | 0.226 | 0.176 | 0.126 | 0.076 | 0.006 | -0.086 | -0.176 | -0.286 | -0.426 | -0.606 | -1.00
7 | 0.447 | 0.427 | 0.407 | 0.387 | 0.357 | 0.337 | 0.307 | 0.277 | 0.237 | 0.207 | 0.167 | 0.117 | 0.067 | 0.007 | -0.077 | -0.147 | -0.237 | -0.347 | -0.477 | -0.647 | -1.00
8 | 0.398 | 0.378 | 0.358 | 0.338 | 0.308 | 0.278 | 0.248 | 0.218 | 0.188 | 0.148 | 0.108 | 0.058 | 0.008 | -0.068 | -0.128 | -0.208 | -0.298 | -0.398 | -0.518 | -0.678 | -1.00
9 | 0.359 | 0.339 | 0.309 | 0.289 | 0.259 | 0.239 | 0.209 | 0.169 | 0.139 | 0.099 | 0.059 | 0.009 | -0.059 | -0.119 | -0.179 | -0.259 | -0.339 | -0.439 | -0.559 | -0.709 | -1.00
10 | 0.3110 | 0.2810 | 0.2610 | 0.2410 | 0.2110 | 0.1810 | 0.1510 | 0.1210 | 0.0810 | 0.0410 | 0.0010 | -0.0510 | -0.1010 | -0.1610 | -0.2210 | -0.2910 | -0.3710 | -0.4710 | -0.5810 | -0.7210 | -1.00

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