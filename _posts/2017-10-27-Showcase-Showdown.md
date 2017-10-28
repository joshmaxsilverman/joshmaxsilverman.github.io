---
layout: post
published: true
title: Showcase Showdown
date: 2017-10-27
---

>On the brilliant and ageless game show “The Price Is Right,” there is an important segment called the Showcase Showdown. Three players step up, one at a time, to spin an enormous, sparkling wheel. The wheel has 20 segments at which it can stop, labeled from five cents up to one dollar, in increments of five cents. Each player can spin the wheel either one or two times. The goal is for the sum of one’s spins to get closer to one dollar than the other players, without going over. (Any sum over a dollar loses. Ties are broken by a single spin of the wheel, where the highest number triumphs.)
>
>For what amounts should the first spinner stop after just one spin, assuming the other two players will play optimally?

<!--more-->

## Solution

We'll work backwards, first figuring out player $3$'s prospects given what she has witnessed, including her first spin, then the joint prospects of players $2$ and $3$ given player $1$'s score and player $2$'s first spin, and finally player $1$'s prospects given her first spin.

Let $H$ be the highest score so far when player $3$ spins (a player has score zero if they bust), let her first spin have value $C$, and let $t$ be $1/3$ if it's currently a tie, and $1/2$ otherwise. Then, if $C>H$, which has probability $1-H$, she holds and wins with probability $1$. If $C<H$, which has probability $\max(0,H-.05)$, she spins and has a $.05$ probability of a tie (and then probability $t$ of winning the tie-break), and probability $1-H$ of an outright win. And if $C=H$, which has probability $.05$, if $H > 1-t$, she holds and has probability $t$ of winning the tie-break, and if $H\leq 1-t$ she spins and has probability $1-H$ of winning outright.

Thus we can express player $3$'s chance of winning as $P_3(H,t)$, where $t$ is $1/3$ if players $1$ and $2$ have the same score, and $.5$ otherwise.

$$P_3(H,t) = (1-H) + (H-.05)(.05t + 1 - H) + \max(t,1-H)$$

Let $A$ be player 1's score, and let $B_1$ be the value of player $2$'s first spin.  We will calculate the probability $P_{2,3}(A,B_1)$, that one of players $2$ and $3$ will go on to win.

First, suppose $B_1<A$. Then player $2$ must spin; call his new total $B_2$. If $B_2<A$, which happens with probability $\max(0,A-.05-B1)$ , then player $3$ has a $P_3(A,.5)$ chance of winning. If $B_2=A$, and there's a $.05$ chance of that, then there's a $P_3(A,1/3)$ that player $3$ wins, and a $.5 \times (1-P_3(A,1/3))$ chance that player $2$ wins in a tie-break. If $1\geq B_2>A$, and there's a $.05$ chance of that for each of the $(1-A)/.05$ possible values of $B_2$ from $A+.05$ to $1$, then there is a certainty of one of players $2$ and $3$ winning. And if $B_2>1$, and there's a $B_1$ chance of that, then player 3 has a $P_3(A,.5)$ chance of winning. This lets us calculate $P_{2,3}(A,B_1|B_1<A)$.

Second, suppose $B_1>A$. If player 2 holds, he'll have $1-P_3(B_1,.5)$ chance of winning, and player $3$ will have $P_3(B_1,.5)$. If he spins, calling his new total $B_2$, then there's a $.05$ chance of each value of $B_2$ between $B_1+.05$ and $1$, and for each of those he has a $1-P_3(B_2,.5)$ chance of winning, and player $3$ has a $P_3(B_2,.5)$ chance; and if $B_2>1$, and there's a $B_1$ chance of that, then player 3 has a $P_3(A,.5)$ chance of winning. So $P_{2,3}(A,B_1)$ when $B_1>A$ is the hold or spin total that includes the greatest probability of player $2$ winning. This lets us calculate $P_{2,3}(A,B_1|B_1>A)$.

Finally, suppose $B_1=A$. Then if player $2$ holds, player $3$ has chance $P_3(A,1/3)$ of winning and player $2$ has chance $(1/2)(1-P_3(A,1/3))$ of winning. And if he spins, calling the new total $B_2$, for each value of $B_2$ between $A+.05$ and $1$, he has chance $.05\times (1-P_3(B_2,.5))$ of winning; and if $B_2>1$, and there's a $B_1$ chance of that, then player 3 has a $P_3(A,.5)$ chance of winning. Again $P_{2,3}(A,B_1)$ is calculated based on whether holding or spinning is best for player $2$. This lets us calculate $P_{2,3}(A,B_1|B_1=A)$.

Because the three cases partition the possibilities,

$$P_{2,3}(A,B_1) = P_{2,3}(A,B_1|B_1<A) + P_{2,3}(A,B_1|B_1>A) + P_{2,3}(A,B_1|B_1=A)$$

Player $1$, with first spin value $A_1$, now has a straightforward calculation. If she holds, then there's an even chance that $B_1$ will be any of the possible values, so her chance of winning is the average of the values of $(1-P_{2,3}(A_1,B_1))$. And if she spins, for each of the values of $A_2$ between $A_1+.05$ and $1$ she has a chance of $.05$ of landing on that value and then having the probability of winning that she'd have if her first spin had that value and she held. 

### Code (Python)

```python
P3 = {}
for i in (2,3):
	t = 1.0/i
	for j in range(21):
		H = j*.05
		P3[(j,i)] = (1-H) + max(0,(H-.05))*(.05*t + (1-H)) + .05*max(t,1-H)

P23 = {}
for i in range(21):
	A = i*.05
	for j in range(1,21):
		B1 = j*.05
		if B1 < A:
			P23[(i,j)] = (max(0,A-.05-B1))*P3[(i,2)] + .05*(P3[(i,3)] + .5*(1-P3[(i,3)])) + (1-A) + B1*P3[(i,2)]
		else:
			if B1 > A:
				Holds = 1-P3[(j,2)]
			elif B1 == A:
				Holds = .5*(1-P3[(i,3)])
			Spins = 0
			for k in range(j+1,21):
				B2 = k*.05
				Spins += .05*(1-P3[(k,2)])
			if Holds > Spins:
				P23[(i,j)] = Holds + P3[(j,2)]
			else:
				P23[(i,j)] = Spins
				for k in range(j+1,21):
					B2 = k*.05
					P23[(i,j)] += .05*P3[(k,2)]
				P23[(i,j)] += B1*P3[(i,2)]
print "First Spin, P(Hold), P(Spin):"
for h in range(1,21):
	Holds = 0
	for j in range(1,21):
		Holds +=  .05*(1-P23[(h,j)])
	Spins = 0
	for i in range(h+1,21):
		for j in range(1,21):
			Spins += .05*.05*(1-P23[(i,j)])
	print h*.05, Holds, Spins
```

Output:

```
First Spin, P(Hold), P(Spin):
0.05 0.00034375 0.2056840625
0.1 0.00121458333333 0.205623333333
0.15 0.00285208333333 0.205480729167
0.2 0.005396875 0.205210885417
0.25 0.00906458333333 0.20475765625
0.3 0.0141458333333 0.204050364583
0.35 0.02100625 0.203000052083
0.4 0.0300864583333 0.201495729167
0.45 0.0419020833333 0.199400625
0.5 0.05704375 0.1965484375
0.55 0.0834583333333 0.192375520833
0.6 0.118289583333 0.186461041667
0.65 0.1631875 0.178301666667
0.7 0.21494375 0.167554479167
0.75 0.28345 0.153381979167
0.8 0.367447916667 0.135009583333
0.85 0.46915 0.111552083333
0.9 0.59091875 0.0820061458333
0.95 0.735266666667 0.0452428125
1.0 0.90485625 0
[Finished in 0.1s]
```

<br>
