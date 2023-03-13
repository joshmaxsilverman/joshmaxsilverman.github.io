---
layout: post
published: false
title: 
date: 2018/04/21
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

we want to find the trajectory that makes the time from start to finish as small as possible.

the logic will be to express the total time $T$ in terms of the shape of the trajectory and the two endpoints, and then use functional calculus to find the minimal shape.

in the big picture, that problem is analytic without the constraint. the shortest path between two points is a cycloid.

given two points and the imperative to minimize time, the cycloid will do whatever it needs to minimize time. however, we aren't allowed to build the track below $\Delta h.$ still, the cycloid is the fastest trajectory between points. this means that the fastest path is to follow a cycloid down to the lowest allowable height, hit the bottom at $\Delta x,$ follow the floor for a while, then follow the same curve back up to the opposite side. 

this makes good physical sense -- energy is conserved, and dipping down the full $\Delta y$ means we achieve the maximum velocity for the majority of the trajectory.

### calculation

with the logic behind us, what remains is deriving the shape of the curve (a cycloid), use it to determine the value of $\Delta x,$ and then plug the trajectory back into the expression for $T.$

the total time $T$ is the sum of all the little time intervals that make up the trajectory:

$$ T = \int dt. $$

the tiny distance traveled by the marble along the trajectory in time $dt$ is equal to $ds$ divided by the instaneous velocity:

$$ dt = \frac{ds}{v(y)} $$

breaking the linear segment into its horizontal and vertical components, we get $ds = \sqrt{dx^2 + dy^2}$ and so

$$
  \begin{align}
T &= \int \dfrac{\sqrt{dx^2 + dy^2}}{v(y)} \\
  &= \int dx\,\dfrac{\sqrt{1 + \left(\frac{dy}{dx}\right)^2} }{v(y)}.
  \end{align}
$$

conserving energy, the marble's velocity at height $y$ below its starting point is $v(y) = \sqrt{2gy}.$ 

with this, we can identify $\mathcal{T}(y(x),y^\prime(x)),$ the contribution to the total time along the trajectory.

$$ \begin{align}
T &= \int dx\,\sqrt{\dfrac{1 + {y^\prime}^2}{2gy}} \\
&= \int dx\, \mathcal{T}(y,y^\prime). 
\end{align}$$

so, $T(y,y^\prime)$ depends on $y$ and its derivative $y^\prime$ and we want to find the curve $y(x)$ that minimizes it. 

if we had that curve (let's call it $y^*(x)$), and it really is a minimum, then any small change we make to it should keep $T$ very close to the minimum value. in a sense, taking the derivative of $T$ with respect to the function $y(x)$ should be $0.$

add an arbitrary, but small amplitude function $\delta(x)$ to $y^*(x).$ this means that $y(x) = y^*(x) + \delta(x)$ and $y^\prime(x) = {y^*}^\prime(x) + \frac{d}{dx}\delta(x).$

$$ T(y,y^\prime) = \int dx\, \mathcal{T}(y,y^\prime) $$

expand around the optimum and get

$$
  \delta T(y,y^\prime) \approx \int dx\, \left[\dfrac{\partial \mathcal{T}}{\partial y}\delta(x) + \dfrac{\partial \mathcal{T}}{\partial y^\prime}\frac{d}{dx}\delta(x)\right].
$$

the disturbance $\delta(x)$ is arbitrary, so there isn't much that we can say about its derivative. however, we can move the derivative off it if we integrate by parts. doing that, we get 

$$
  \delta T(y,y^\prime) \approx \int dx\, \left[\dfrac{\partial \mathcal{T}}{\partial y} - \frac{d}{dx}\dfrac{\partial \mathcal{T}}{\partial y^\prime}\right]\delta(x).
$$

for the optimal trajectory, this variation is equal to zero. looking at the integral, $\delta(x)$ is, apart from having small magnitude, a totally arbitrary function. for example, we could define it to be positive wherever the bracketed expression is positive, and negative wherever it's negative, making the integral a positive number. the only way for the variation to be zero, regardless of $\delta(x)$ is for the bracketed expression itself to be everywhere zero. this means that the optimal trajectory obeys 

$$ \frac{\partial\mathcal{T}}{\partial y} = \frac{d}{dx}\frac{\partial\mathcal{T}}{\partial y^\prime}, $$

which is the the euler-lagrange equation. 

to take these derivatives, we can use the explicit form for $\mathcal{T}$ above, which yields an unholy mess but boils down nicely to

$$\begin{align}
  0 &= \dfrac{y^{\prime\prime}}{1+{y^\prime}^2} + \dfrac{1}{2y} \\
  &= 2y^{\prime\prime}y + 1 + {y^\prime}^2
\end{align}$$

if we can solve this differential equation, the ideal shape will be revealed. 

the equation has a mixed $y^{\prime\prime}y$ term, indicating coupling between the linear and first order terms. however, the coupled term can't simply be $y^\prime y$, or else there wouldn't be a $2.$ the $2$ could arise if the term were $y{y^prime}^2.$ following this thread, if we multiply through by another factor of $y^\prime,$ we get

$$ 2y^{\prime\prime}y^\prime y + y^\prime + {y^\prime}^3 = 0$$

which is the derivative of 

$$ y\left(1+{y^\prime}^2\right) ,$$

leading us to 

$$ y\left(1+{y^\prime}^2\right) = \text{const.}$$

or

$$ \frac{dy}{dx} = \sqrt{\frac{\text{const.} - y}{y}}. $$

since the curve should meet the floor at zero slope, we know that $dy/dx$ is zero when $y=h,$ which tells us that $\text{const.} = h.$

we can actually solve this without doing an integral. drawing a diagram, we can equate $dy/dx$ with the tangent of the angle with the horizontal (like we did in a [recent problem](https://joshmaxsilverman.github.io/2023-02-11-improbable-sky/)) and solve for $y$ algebraically

$$\begin{align}
\left(\dfrac{dy}{dx}\right)^2 &= \frac{h - y}{y} \\
\dfrac{\sin^2\theta}{\cos^2\theta} &= \\
y\sin^2\theta &= h\cos^2\theta - y\cos^2\theta \\
y &= h\cos^2\theta.
\end{align}$$

this gives the expected limits, with $y=0$ at the beginning ($\theta = 0$) and $h$ at the end ($\theta = \pi/2$).

with this in hand, we can find $x$

$$ 
\begin{align}
  \frac{\sin\theta}{\cos\theta} &= \frac{dx}{dy} \\
    &= \frac{dx}{d\theta}\frac{d\theta}{dy} \\
    &= -\frac{dx}{d\theta}\frac{1}{2\cos\theta\sin\theta}
\end{align}
$$

or 

$$ \frac{dx}{d\theta} = -2\sin^2\theta. $$



<br>
