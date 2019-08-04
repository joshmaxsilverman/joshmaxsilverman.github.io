---
layout: post
published: true
title: Ring Train
date: 2019/08/02
---

>You find yourself in a train made up of some unknown number of connected train cars that join to form a circle. It’s the ouroboros of transportation. Don’t think too hard about its practical uses.
>
>From the car you’re in, you can walk to a car on either side — and because the train is a circle, if you walk far enough eventually you’ll wind up back where you started. Each car has a single light that you can turn on and off. Each light in the train is initially set on or off at random.
>
>What is the most efficient method for figuring out how many cars are in the train?
>
>(Assume that you can’t mark or otherwise deface a train car, and that each car’s light is only visible from within that car. The doors automatically close behind you, too. There are only two actions you can take: turning on or off a light and walking between cars.)

<!--more-->


## Solution

Label the cars with positive and negative integers, based on their distance from the start car, which is number $0$. Each car gets labeled by infinitely many numbers, all of which are equal modulo $N$, where $N$ is the number of cars.

Here is our algorithm. Go to car $1$, ensure that its light is on, then travel in the opposite direction to car $-1$, and ensure that its light is off. Now go to car $2$, and ensure that its light is on. Then to car $-2$, ensuring that its light is off. Then to car $4$ (ensuring that cars $3$ and $4$ are on), car $-4$, car $8$, car $-8$ and so on, always ensuring that the positively numbered cars' lights are on, and the negative ones off.  Stop when you find a previously-visited postively-numbered car with its light turned off or a previously-visited negatively-numbered one with its light turned on.  Then you'll know that this car is the last car you ensured was off when you last headed in the negative direction, or the last you ensured was on in the positive direction, which lets you calculate the length of the train by subtracting the negative integer from the positive integer that you know label the car. 

For example, suppose you first come to a changed light in car $-6$, as you head in the negative direction from car $16$ (you had ensured car $-6$'s light was off on your way to car $-8$ previously). This means that car $-6$ is car $16$, and so, subtracting, there are $22$ cars in the train.

How efficient is this? Each back-and-forth circuit ensuring lights are on and off takes $4 \cdot 2^i$, or $2^{i+2}$ steps, for $i$ in $\\{0,1,2,\ldots\\}$. Let $N$ be the length of the train.  The worst-case scenario, in terms of steps per train car, is an $N$ of the form $2^k+1$. For such an $N$, the last completed cycle ($i = k-1$) is of total length $2^{k+1}$, and then the final, partial cycle consists of a back-and-forth trip in the positive direction also of total length $2^{k+1}$ followed by a single step in the negative direction.  So the total number of steps is:

$$4+8+\cdots+ 2^{k+1} + 2^{k+1} + 1 = 6(2^k+1) - 9 = 6N - 9$$

(This relies on the fact that $1+2+4+\cdots+2^n = 2^{n+1}-1$.)

So, the algorithm's complexity is on the order of $N$, which cannot be improved upon for any method that involves visiting every car on the train, which is something that obviously any counting method must involve (this is not, of course, a proof that there is no method that improves on this one at all).  And the number of steps per train car for a worst-case $N = 2^k+1$ approaches $6$ for large $k$.

<br>
