---
layout: post
published: true
title: Can you meet me at the mall?
date: 2025/07/22
subtitle: What is the greatest number of friends you're likely to meet if everyone fails to coordinate?
tags: maximum approximation
---

>**Question**: You and two friends have arranged to meet at a popular downtown mall between $3$ p.m. and $4$ p.m. one afternoon. However, you neglected to specify a time within that one-hour window. Therefore, the three of you will be arriving at randomly selected times between $3$ p.m. and $4$ p.m. Once each of you arrives at the mall, you will be there for exactly $15$ minutes. When the $15$ minutes are up, you leave.
>
>At some point (or points) during the hour, there will be a maximum number of friends at the mall. This maximum could be one (sad!), two, or three. On average, what would you expect this maximum number of friends to be?
>
>
>**Extra Credit**: Instead of three total friends, now suppose there are four total friends (yourself included). As before, you all arrive at random times during the hour and each stay for 15 minutes.
>
>On average, what would you expect the maximum number of friends meeting up to be?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-meet-me-at-the-mall))

## Solution

## $N=3$ friends

let $t_j$ be the time that friend $j$ arrives and $s$ the fraction of an hour that they stay for (in this case $s=\frac14$). the max can either be $1$, $2$, or $3$. 

if it is $1$ then none of the friends overlap at all, so the probability is equal to

$$ \begin{align} P_3(\text{max}=1) &= \int\limits_0^{1-2s}\text{d}t_1 \int\limits_{t_1+s}^{1-s}\text{d}t_2 \int\limits_{t_2+s}^1\text{d}t_3 \\ &= (1-2s)^3 \end{align}$$

if it is $3$ then they all have to occur within $s$ of friend $1$'s arrival, so

$$ \begin{align} P_3(\text{max}=3) &= \int\limits_0^1\text{d}t_1 \int\limits_{t_1}^{t_1+s}\text{d}t_2 \int\limits_{t_2}^{t_1+s}\text{d}t_3 \\ &= 3s^2 \end{align} $$

because the probabilities sum to $1$, we can figure out $P(\text{max}=2)$ and calculate the expectation.

$$ \langle \text{max}_3 \rangle = \frac{65}{32} \approx 2.03 $$

## $N=4$ friends

with $4$ friends, the cases from above generalize directly, giving $P_4(\text{max}=1)=(1-3s)^4=\frac{1}{256}$ and $P_4(\text{max}=4) = (4-3s)s^3 = \frac{13}{256}$. however, we have to deal with one of the intermediate cases. we'll go for the case of $\text{max}=3.$ 

there are two ways to realize $\text{max}=3$. one is for three of the friends to overlap while the fourth friend overlaps with at most one of the other friends. the other way is for there to be two distinct $3$-friend overlaps, in other words $t_3-t_1 \leq s,$ $t_4-t_2\leq s,$ while $t_4-t_1 \gt s.$ 

$$ \begin{align} P_4(\text{one triple}) &= 2\times 4! \int\limits_0^{1-s}\text{d}t_1\,\hspace{-1em} \int\limits_{t_1}^{\min(t_1+s,1-s)}\hspace{-1em}\text{d}t_2\, \int\limits_{t_2}^{t_1+s}\text{d}t_3\, \hspace{-0.5em}\int\limits_{t_2+s}^1\text{d}t_4\, \\ &= 2s^2(6+s(11s-16)) \\ &= \frac{86}{256} \end{align} $$

$$ \begin{align}P_4(\text{two triples}) &= 2\times 4! \int\limits_0^{1-s}\text{d}t_1\,\int\limits_{t_1}^{t_1+s}\text{d}t_2\, \int\limits_{t_2}^{t_1+s}\text{d}t_3\, \hspace{-0.75em}\int\limits_{\max(t_1+s,t_3)}^{\min(1,t_2+s)}\text{d}t_4\, \\ &= 4s^3-5s^4 \\ &= \frac{11}{246}\end{align}$$

putting these together, we get

$$ \langle \text{max}_4 \rangle = \frac{317}{128} \approx 2.48 $$

## General $N$ case

i now present a calculation which led to that seems to tightly capture the large $N$ behavior. however, it is ultimately unjustified it comes from errantly dropping a pair of terms. i believe it's a glimpse of a deeper calculation i have yet to see how to develop.

the spirit of the calculation is to consider the maximum as the number of friends $k$ above which we wouldn't expect to see such an interval in the typical hour.

the big picture is roughly
- model each of $4$ independent intervals using the poisson process
- find the probability that at any given point in time, a window has $k$ friends
- compute the $k$ at which we would expect one such interval to appear per hour

let's assume there are effectively $1/s = 4$ intervals. the rate at which the people arrive is $\lambda = N\,\text{hr}^{-1}$, so the probability that nobody shows up in time $\Delta t$ is $(1-\lambda \Delta t)$ and the chance nobody shows up for time $t$ is $(1-\lambda \Delta t)^{t/\Delta t}$ which as $\Delta t$ goes to zero becomes $e^{-\lambda t}.$ the probability that someone shows up in time $dt$ is $\lambda dt$ so the chance that $k$ people show up in time $T$ is (making aggressive assumption $\lambda$ stays constant) approximately

$$\begin{align} P(k\,\,\text{friends in time}\,\, T) &\approx \int \lambda\, dt_1 \int \lambda\, dt_2 \ldots \int \lambda\, dt_k\, e^{-\lambda(t_1 + t_2 + \ldots + t_k)} \\ &= \lambda^k e^{-\lambda s} \int\, dt_1 \int\, dt_2 \ldots \int\, dt_k \\ &= \frac{(\lambda s)^k}{k!} e^{-\lambda s} \end{align}$$

the expectation of this distribution is $\mu = \lambda s = N s$ and is approximately gaussian for large $\lambda.$ 

$$ P(\text{max}=k) = \frac1{k!} \mu^k e^{-\mu } $$
taking the log...

$$ \begin{align} \log P(\text{max} = k) &= k\log \mu - \mu - \log k! \\ &= k\log\mu - \mu - \left(k\log k - k + \frac12 \log 2\pi k\right)  \end{align} $$

centering about the mean $\mu = k - \delta$ we get

$$ \begin{align}\log P(\text{deviation} = \delta) &= \delta + (\mu + \delta) \log\mu - (\mu + \delta)\log(\mu + \delta) - \frac12\log 2\pi(\mu+\delta) \\ &= \delta - (\mu + \delta) \log\frac{\mu + \delta}{\mu} - \frac12\log 2\pi(\mu+\delta) \\ &= \delta - (\mu + \delta) \log\left(1 + \delta/\mu\right) - \frac12\log 2\pi(\mu+\delta) \\ &= \delta -(\mu+\delta)\left(\delta/\mu - \frac12\delta^2/\mu^2\right) - \frac12\log 2\pi(\mu+\delta) \\ &= \delta - \delta + \frac12 \delta^2/\mu - \delta^2/\mu + \frac12\delta^3/\mu^2 - \frac12\log 2\pi(\mu+\delta) \\ &\approx -\frac12\delta^2/\mu - \frac12\log 2\pi\mu\end{align} $$

so the probability of seeing a deviation of size $\delta$ at a random point in time is approximately

$$ P(\delta) = \frac{1}{\sqrt{2\pi\mu}}\large e^{-\frac12\delta^2/\mu} $$

the probability of a random time being inside an interval of magnitude $\delta$ is the rate at which such intervals spawn times the amount of time they last once they exist. 

$$ P(\delta) = r(\delta)\tau(\delta). $$

we can approximate the maximum magnitude $\delta$ as the interval whose spawn rate is once per hour, so

$$ P(\delta) = \tau(\delta) $$
the default size of an interval is the mean, i.e. $k = \mu$ so we need to find out the lifetime of an excitation of magnitude $\delta.$ if there are $\delta$ friends in the excitation, and they all spawned inside the window size $s,$ then we'd expect the oldest friend to have time $s/\delta$ left before they leave the mall. 

so we have

$$ s/\delta = \frac{1}{\sqrt{2\pi\mu}}e^{-\frac12\delta^2/\mu} $$

this equation can't be solved outright, but we can use it to develop an approximation for $\delta$. 

taking logs we get 

$$ \log\frac1s  = \frac12\delta^2/\mu + \log\sqrt{2\pi\mu} - \log\delta  $$

we are about to see the unjustified step.

the thinking goes roughly: $\log\frac1s$ doesn't grow at all, so the right side mustn't either. however, the second term grows as $\log\sqrt{\mu}$, so the negative term must also grow as $\log\sqrt{\mu},$ since the $\delta^2$ term is positive. therefore, to leading order we have $\log\frac1s \approx \frac12\delta^2/\mu$ and $\delta = \sqrt{2\mu\log\frac1s}$ leading to

$$\begin{align} k &= \mu + \delta \\ &= Ns + \sqrt{2Ns\log\frac1s}\end{align} $$

this is a wonderful formula, that closely matches the data as $N$ scales:

![](/img/2025-07-22-fiddler-meet-at-mall-plot.png){:width="450 px" class="image-centered"}

$$
\begin{array}{ccc}
N & $10^5\,\text{Monte Carlo sim} & \text{formula} \\ \hline
 10 & 4.97447 & 5.13277 \\
 20 & 8.61085 & 8.7233 \\
 30 & 11.9893 & 12.0601 \\
 40 & 15.2142 & 15.2655 \\
 50 & 18.372 & 18.3871 \\
 100 & 33.4214 & 33.3255 \\
 200 & 62.026 & 61.7741 \\
 400 & 117.148 & 116.651 \\
 800 & 224.349 & 223.548 \\
 1600 & 434.588 & 433.302 \\
 3200 & 848.996 & 847.096 \\
 6400 & 1669.43 & 1666.6 \\
\end{array}
$$

however, the formula $\delta = \sqrt{2\mu\log\frac1s}$ is not a close approximation for the numerical solution of the $P(\delta) = \tau(\delta)$ equation. in the first place, we know we are making the aggressive assumption ( that the rate $\lambda$ of the poisson process remains constant as friends come and go, even though we should expect it to rise or fall as we observe windows of low or high friend attendance), so we shouldn't expect the numerical solution to be spot on. however, it is remarkable that effectively ignoring the normalization of the probability distribution, and the $\delta$ from the estimation of the excitation lifetime, leads to a spot-on prediction.

in the time i had, i did not arrive at a more fundamental argument for this result, though it demands a sound explanation.

<br>
