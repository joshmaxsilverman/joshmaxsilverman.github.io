---
layout: post
published: false
title: Not a Marathon
date: 2020/11/08
---

>**Question**: you're practicing for the forgotten NYC marathon. On the first day you set your treadmill to $9$ minutes per mile. On the second day, you set it to steadily "speed up" over time from $r_0 = 10$ minutes per mile at the beginning down to $r_1 = 8$ minutes per mile at the end (when the run is half over, the treadmill moves at $9$ minutes per mile). Which run took less time?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-make-an-unfair-coin-fair/))

## Solution

What's interesting here is that the treadmill rate $r$ imposes a different kind of "speed" than is usual. Miles per hour is distance per time, but minutes per mile is time per distance. 

Say the run lasts for $T$ minutes total, then the treadmill's rate a time $t$ after the start of the run is 

$$d = r_0 + \left(r_1 - r_0\right)\dfrac{t}{T}.$$

### Inharmonious slog

$r$ is the ratio of the incremental time taken to the incremental distance travelled

$$ r(t) = \dfrac{\Delta t}{\Delta x}. $$

Inverting, this becomes $\Delta x = \Delta t / r$ so that

$$\begin{align} X_\text{total} &= \sum \Delta x \\
&= \sum \dfrac{\Delta t}{r(t)}
\end{align}$$

or, as the time increments become continuous

$$ X_\text{total} = \int\limits_0^{T} \dfrac{dt}{r_0 + \left(r_1 - r_0\right)\dfrac{t}{T}} $$

Changing variables to $r = r_0 + \left(r_1-r_0\right)t/T,$ so $dt =  T\, dr/\left(r_1 - r_0\right)$ and

$$ X_\text{total} = \dfrac{T}{r_1 - r_0}\int\limits_{r_0}^{r_1}\dfrac{dr}{r} = \dfrac{1}{r_1 - r_0}T \log \dfrac{r_1}{r_0}$$

<br>
