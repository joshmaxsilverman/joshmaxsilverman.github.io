---
layout: post
published: false
title: Optimal Coinball
date: 2017/10/13
---

>Coinball is a contest where two players take turns trying to call a fair coin toss. The game lasts for 100 total tosses, 50 tosses for each player. On each toss, the player calling it announces either “heads” or “tails” and either “rush” or “pass.” If he says “rush,” he gets one point if he calls the toss correctly, and his opponent gets one point if the call is incorrect. Saying “pass” means the toss is worth two points to the caller if he calls the toss correctly and two points to his opponent if he does not. At the end, the player with the most points wins. (The margin of victory is irrelevant; in Coinball, league rankings are based only on wins, with a draw counting as half a win.)
>
>- If you know your opponent always calls “rush” and you follow the optimal strategy given that knowledge, what are your chances of winning?
>- What if you know your opponent always calls “pass”?
>- If you and your opponent both play optimally, is it better to go first? Or to go second and therefore get the last call?
>Extra credit: Put your Monte-Carlo simulations away and try to determine the win probabilities to 10 digits of precision.

<!--more-->

[fivethirtyeight](https://fivethirtyeight.com/features/how-much-is-a-perfect-game-of-jeopardy-worth/)

## Solution

We will rely on the computer, but not for random, Monte Carlo simulations. Each of the three problems can be solved exactly by specifying a [recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation), and repeatedly deducing unknown values of a function from known values. While this provides a recipe for an exact calculation, it is much too complicated a procedure for pen and paper, so we will rely on the computer to calculate expectations to high precision.

A _state_ of the game is a triple $(t,m,y)$ where there have been $t$ tosses, I have $m$ and you have $y$ points. All of $t$, $m$, and $y$ are non-negative integers with $t\leq 100$ and $t \leq m+y \leq 200$.  $E(t,m,y)$ is my expected number of wins if it's my turn and the game is now in state $(t,m,y)$. We start with:

$$E(100,m,y) = 1,\ 0,\ \frac{1}{2}\ \mbox{for}\ m > y,\ y>m,\
y=m$$

### Opponent always rushes or always passes

Suppose you always rush and that it's my turn, in state $(t,m,y)$. Suppose also that we have already calculated $E(t+2,m',y')$, for $m',y'\geq m,y$. 

I expect half the time to throw heads and gain either one or two points depending on my choice of rush or pass; in half of those cases you gain one point on the next turn (you throw heads) and in the other half I gain a point (you throw tails). Similarly, half the time I throw tails, so that you gain one or two points; then one of us gains one point on your flip. 

So whichever choice I make there are four cases for the next two turns: I have $1/4$ chance each of ending up in a state $(t+2,m',y')$ such that we've already calculated $E(t+2,m',y')$. This allows us to calculate expectations for my rushing and passing in states where $t=98$ based on the known expectations for $t=100$; $E(98,m,y)$ is then the higher of the two.  And similarly on down to $E(0,0,0)$, which is my expectation, playing optimally, as the first player. If that expectation exceeds $1/2$, it's better to play first. And in fact the expectation for the first player is about $.601766458853$.

The case of your always passing is solved in exactly the same way, and the first player's expected wins per game is about $.558341814467$.

### Opponent plays optimally

If you play optimally, again at each turn I want to maximize my expected number of wins for this game, as do you. So this time we will calculate $E(t,m,y)$ for both odd and even turns, that is, my expectation if playing after turn $t$ with $m$ points to your $y$, even if that means I'm the second player.

If in state $(t,m,y)$ I rush, then with probability $1/2$ each, the game will be in state $(t+1,m+1,y)$ or $(t+1,m,y+1)$, so that I will then expect, respectively, $1-E(t+1,y,m+1)$ or $1-E(t+1,y+1,m)$. That relies on the fact that a given player's expectation is always one minus the other's---it's a [zero-sum game](https://en.wikipedia.org/wiki/Zero-sum_game). So the expectation of rushing is:

$$E_{rush}(t,m,y) = 1 - \frac{1}{2}(E(t+1,y,m+1)+E(t+1,y+1,m))$$

Similarly, the expectation of passing is:

$$E_{pass}(t,m,y) = 1 - \frac{1}{2}(E(t+1,y,m+2)+E(t+1,y+2,m))$$

And so:

$$E(t,m,y) = \max(E_{rush}(t,m,y),E_{pass}(t,m,y))$$

Now it's once again just a matter of working our way from the known expectations for $t=100$ on down to $t=0$. We find that my expected number of wins per game is about $.489818590457$. In this case it's better to go second.

It turns out that the optimal strategy against an optimal opponent can be summed up as follows. If you're losing, pass. If you're winning, rush. If it's tied, then if the number of completed turns is divisible by $4$, pass; otherwise, if it's after turn $92$ and you went first or it's the very last turn, it's a wash; otherwise, rush.

### Code (Python)

```python
N = 100
for Strategy in ("always rush","always pass","optimal"):
	E = {}
	for m in range(2*N+1):
		for y in range(max(0,N-m),2*N-m+1):
			if m>y:
				E[(N,m,y)] = 1
			elif y>m:
				E[(N,m,y)] = 0
			elif m==y:
				E[(N,m,y)] = .5

	for t in range(N-1,-1,-1):
		if t%2 and not Strategy == "optimal":
			continue
		for m in range(2*t+1):
			for y in range(max(0,t-m),2*t-m+1):
				if Strategy == "always rush":
					E_rush = .25*E[(t+2,m+1,y+1)]+.25*E[(t+2,m+2,y)] + .25*E[(t+2,m,y+2)]+.25*E[(t+2,m+1,y+1)]
					E_pass = .25*E[(t+2,m+2,y+1)]+.25*E[(t+2,m+3,y)] + .25*E[(t+2,m,y+3)]+.25*E[(t+2,m+1,y+2)]
				elif Strategy == "always pass":					
					E_rush = .25*E[(t+2,m+1,y+2)]+.25*E[(t+2,m+3,y)] + .25*E[(t+2,m,y+3)]+.25*E[(t+2,m+2,y+1)]
					E_pass = .25*E[(t+2,m+2,y+2)]+.25*E[(t+2,m+4,y)] + .25*E[(t+2,m,y+4)]+.25*E[(t+2,m+2,y+2)]
				elif Strategy == "optimal":
					E_rush = 1 - .5*E[(t+1,y,m+1)] - .5*E[(t+1,y+1,m)]
					E_pass = 1 - .5*E[(t+1,y,m+2)] - .5*E[(t+1,y+2,m)]
				E[(t,m,y)] = max(E_rush,E_pass)
	print "If opponent's strategy is",Strategy,"first player's expectation is", E[(0,0,0)]
```

Output:

```
If opponent's strategy is always rush first player's expectation is 0.601766458853
If opponent's strategy is always pass first player's expectation is 0.558341814467
If opponent's strategy is optimal first player's expectation is 0.489818590457
[Finished in 1.7s]
```

<br>
