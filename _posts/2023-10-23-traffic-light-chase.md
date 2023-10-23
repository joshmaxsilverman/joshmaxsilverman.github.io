---
layout: post
published: false
title: Traffic light chase
date: 2023/10/23
subtitle: How long until you meet your menacing assailant?
tags: counting convolution
---

>**Question**:
>
>You find yourself engaged in a car chase, but it differs from the movies in one key way: Both you and the car that’s chasing you obey all traffic laws, being sure to stop at any and all red lights.
>
>You’re trying to make it to the city limit, but you’re currently one block ahead of your pursuer. Right now you’re both at a red light. The light turns green at the same time for both of you, at which point both cars begin moving east at a speed of one block per minute.
>
>Every time that you come to an intersection, there’s a 50 percent chance the light is green, in which case you coast right on through. But there’s also a 50 percent chance the light is red, in which case it takes exactly one minute for the light to turn green again. These same probabilities govern your pursuer—at each intersection, they have a 50 percent chance of encountering a green light and a 50 percent chance of encountering a red light and having to wait one minute, entirely independent of whatever you might have encountered at that same intersection.
>
>Including the light at which you are now stopped, there are five traffic lights between you and the city limit, as illustrated below. That means there are six lights for your pursuer.
>
>You are displayed as being five stop lights west of the city limit. Your pursuer is six stop lights west of the city limit.
>How likely is it that you’ll make it past the city limit without being caught?

<!--more-->

([Fiddler on the proof](https://thefiddler.substack.com/p/can-you-ride-out-the-slow-car-chase))

## Solution

taken together, the lead and chase car can either move further apart (green light for lead car, red light for chase car), move together (red light for lead car, green light for chase car) or remain the same distance apart (same light color for both cars).

if the two cars are going to meet for the first time at step $N$ then, between the first and last step, the two cars can do anything so long as they don't occupy the same position. we need them to come together for the first time at step $N.$

for simplicity, we're going to change the convention so that the first step happens after the first dual green light, and the last step is just before the cars come together.

here is one such path:

![image of gap over time]()

if we remove the parts where the cars maintain the same relative position, this is just a dyck path -- a path that goes from the bottom left corner to the top right corner of a square lattice without moving under the diagonal. 

in principle, our paths can be anything from a pure dyck path (all up and down moves) to pure staying in place. 

for example, for the case of 3 steps, we can have the cars remain in place the whole time, or we can have them move up, then stay in place, then move back down. 

this has probability 

$$ 1 - \frac14\left[1 + \frac12 + \left(\left(\frac12\right)^2 + \left(\frac14\right)^2\right) + \left(\left(1/2\right)^3 + 3\times\frac12\times\left(\frac14\right)^2\right)\right] = \frac{63}{128}$$

of escape.

## Extra credit

simulating the system, a curious thing happens: increasing the length of the simulation increases the expected number of steps. usually, we'd expect longer runs to bring the estimate closer to its true value. 

what could this mean? it's a tell tale sign that the distribution is fat tailed, and has no true value! as we run the simulation for longer and longer, there is a greater likelihood that the process accesses deeper into the tail, pulling the average up. the longer we sample for, the greater the average, on average.

### Finding the distribution

in general, if the dyck path takes up $2d$ steps of the path, then the sideways steps will take up $(t - 2d)$ steps. the number of such paths would then be the number of dyck paths of length $2d$ plus the number of ways to insert $(t-2d)$ diagonal steps between $2d$ dyck steps. this is just $2d(2d+1)\cdots t/(t-2d)!$ which is $t!/((t-2d)!(2d)!) = \binom{t}{2d}.$

the number of dyck paths of length $2d$ is given by the catalan numbers, $D_{2d} = C_d = \frac{1}{d+1}\binom{2d}{d}$.

now, because sideways and up/down moves distinct probabilities, we need to account for likelihood of each category of path. with $(t-2d)$ sideways moves and $2d$ up/down moves, plus the obligatory final down move, the probability is $\left(\frac14\right)^{1+2d}\left(\frac12\right)^{t-2d}.$

which makes the probability of ending in $t$ steps 

$$ P(\text{ends in}\, t\,\text{steps}) = \sum_{d=0}^{\text{floor}\left(t/2\right)} D_{2d} \binom{t}{2d} \left(\frac14\right)^{2d+1}\left(\frac12\right)^{t-2d}. $$

which comes to 

$$ \frac{\Gamma[\frac32 + t]}{\sqrt{\pi}\Gamma[3+t]}. $$

now, what we are after is the probability of ending the chase by step $N$ or sooner, which is just

$$ P(\text{caught before step}\, N) = \sum_{t=0}^N P(\text{ends in}\, t\,\text{steps}) = 1-2\frac{\Gamma(\frac52 + N}}{\sqrt{\pi}\Gamma[3+N]} $$

which makes the cumulative probability of escape by step $N$

$P(\text{escape in}\,N\text{steps}) = 2\frac{\Gamma(\frac52 + N}}{\sqrt{\pi}\Gamma[3+N]}. $$

evaluations of the gamma function are approximately related by $\Gamma(x + a) \approx \Gamma(x)x^a$ which means the right side of the cumulative distribution scales as $\left(\frac52 + N\right)^{-\frac12}.$ 

integrating the $\text{cdf}$ from $0$ to an upper bound $N$ is proportional to $\sqrt{N}.$ evidently, there is no mean, as the simulation suggested.

<br>
