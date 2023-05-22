---
layout: post
published: true
title: Take a number
date: 2023/05/23
subtitle: When should you start dreaming of a brighter future?
tags: expectation strategy
---

>**Question**: You start with just the number 1 written on a slip of paper in a hat. Initially, there are no other slips of paper in the hat. You will draw from the hat $100$ times, and each time you draw, you have a choice: If the number on the slip of paper you draw is $k,$ then you can either receive k dollars or add $k$ higher numbers to the hat.

For example, if the hat were to contain slips with the numbers $1$ through $6$ and you drew a $4,$ you could either receive $\$4$ or receive no money but add four more slips numbered $7, 8, 9$ and $10$ into the hat. In either case, the slip with the number $4$ would then be returned to the hat.

If you play this game perfectly — that is, to maximize the total amount of money you’ll receive after all $100$ rounds — how much money would you expect to receive on average?
>

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/how-much-money-can-you-pull-out-of-a-hat/))

## Solution

each time we draw a number $k,$ we have to figure out if it's worth more to cash it in, or to hedge so that there are $(h+k)$ numbers in the bowl to start the next round, taking into account how many rounds we have left, $\ell.$

### approximate argument

suppose we're playing the game with current highest number $h.$

crudely, if we decide to cash in for $n$ rounds in a row, the expected value of play is 

$$n\langle k \rangle = \frac12 nh.$$

if we decide to hedge for the first $(n-1)$ turns, and cash in on the last, the expected value of play is 

$$ \frac12 \left(\frac{h+\frac12h}{h}\right)^{n-1} h = \frac12 \left(\frac32\right)^{n-1}h, $$

since we expect to raise the highest number $h$ by $\frac12h$ on each draw, and the expected value of the cash in is half the highest number at the time of the draw.

the hedging strategy wins out at $n=5,$ and we expect the best outcome to scale like $\approx \left(\frac32\right)^\ell.$

in the real game, this $n$ should be lower since the first turn doubles $h$ from $1$ to $2.$

### rigorous argument

let's call the expected value of our remaining turns $\Omega(h, \ell, k)$ where $h$ is the biggest number currently in the bowl, $\ell$ is the number of turns we have left, and $k$ is the number we draw from the bowl. 

if we cash in, then we immediately get $k$ and can expect to add the average value of all the games we can immediately move it, i.e. 

$$ \langle\text{cash in}\rangle_{h,\ell,k} = k + \frac{1}{h}\sum\limits_{j=1}^h \Omega(h, \ell-1, j). $$

if we hedge, then we get nothing immediately, but raise the value of $h$ to $(h+k)$ in the next game:

$$ \langle\text{hedge}\rangle_{h,\ell,k} = \frac{1}{h+k}\sum\limits_{j=1}^{h+k} \Omega(h+k, \ell-1, j). $$

so, 

$$ \Omega(h,\ell,k) = \max\{ \langle\text{cash in}\rangle_{h,\ell,k}, \langle\text{hedge}\rangle_{h,\ell,k} \}. $$

which can be evaluated analytically. 

when $\ell=1,$ we have just onw turn left and there is nothing we can do but take the money on the table

$$ \Omega(h, 1, k) = k. $$

plugging this in to the maximization, we get 

$$ 
\begin{align}
  \Omega(h, 2, k) &= \max\{ \langle\text{cash in}\rangle_{h,2,k}, \langle\text{hedge}\rangle_{h,2,k} \}
  &= \max\{ k + \frac{1}{h}\sum\limits_{j=1}^h \Omega(h, \ell-1, j), \frac{1}{h+k}\sum\limits_{j=1}^{h+k} \Omega(h+k, \ell-1, j)\} \\
  &= \max\{ k + \frac{1}{h}\sum\limits_{j=1}^h j, \frac{1}{h+k}\sum\limits_{j=1}^{h+k} j\} \\
  &= \max\{k + \frac{1}{h}\frac{h(h+1)}{2}, \frac{1}{h+k}\frac12(h+k+1)(h+k)\} \\
  &= \max\{k + \frac12(h+1), \frac12(h+k+1)\} \\
  &= k + \frac12(h+1)
\end{align}
$$

so, with $2$ turns left, we should take the cash out.

going again, the decision is

$$
  \begin{align}
    \Omega(h, 3, k) &= \max\{ \langle\text{cash in}\rangle_{h,3,k}, \langle\text{hedge}\rangle_{h,3,k} \} \\
    &= \max \{k+h+1, \frac12 k + h+1\} \\
    &= k+h+1
  \end{align}
$$

and, with $3$ turns left, we should cash out.

with $4$ turns left, the decision is

$$
  \begin{align}
    \Omega(h, 4, k) &= \max\{ \langle\text{cash in}\rangle_{h,4,k}, \langle\text{hedge}\rangle_{h,4,k} \} \\
    &= \max \{\frac12 k + \frac32(h+1), \frac32(k+h+1)\}
  \end{align}
$$

and we should hedge. 

from here on out, $(k+h+1)$ picks up one factor of $\frac32$ on each iteration, giving 

$$ \Omega(1,\ell,1) = 2\times\left(\frac32\right)^{\ell-2}, $$

for $\ell \geq 2$ and $\Omega(1,1,1) = 2.$

for a $100$ round game, we expect to win $2\times\left(\frac32\right)^{98} \approx \$361,387,713,364,635,766.58$




<br>