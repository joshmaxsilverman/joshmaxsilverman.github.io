---
layout: post
published: true
title: Andy's Afternoon Amble
date: 2026/08/25
subtitle: How likely are you to realize that you woke up on the floor?
source: jane-street
theme: probability
tags: random-walk recurrence
hide_from_recent: true

---

>**Question**: Andy the ant has moved on from his classic ‘Telstar’ [soccer ball](https://www.janestreet.com/puzzles/andys-morning-stroll-index/) homeland to live on a simpler spherical surface consisting of four white hexagons that are surrounded by alternating black triangles and white hexagons (three of each), and four black triangles surrounded by three white hexagons. To us this land is a truncated tetrahedron blown up into a sphere we see above on the left. Due to Andy’s tiny size and terrible eyesight, he doesn’t notice the curvature of the land and avoids the black triangles because he suspects they may be bottomless pits.
>
>Much like his morning routine, every afternoon he wakes up from his nap on a white hexagon, leaves some pheromones to mark it as his special *home* space, and starts his random amble. Every step on this walk takes him to one of the three neighboring white hexagons with equal probability. He ends his amble as soon as he first returns to his home space, which he recognizes but cannot distinguish the edges of (i.e. he doesn’t know if he returned across the same edge as he left). As an example, on exactly 1/3 of afternoons Andy’s amble is 2 steps long, as he randomly visits one of the three neighbors, and then has a 1/3 probability of returning immediately to the home hexagon.
>
>This afternoon his truncated tetrahedral homeland bounced through the very same kitchen with an infinite regular hexagonal floor tiling consisting of black and white hexagons, shown above on the right. In this tiling every white hexagon is surrounded by alternating black and white hexagons, and black hexagons are surrounded by six white hexagons. Andy fell off the ball and woke up on a white hexagon. He didn’t notice any change in his surroundings, and goes about his normal amble.
>
>Throughout his walk, Andy remembers the turns he’s taken. Let *p* be the probability that by the end of his afternoon amble on this new land he has discovered that he is no longer on the truncated tetrahedral sphere. **Find *p* in exact terms**.

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/andys-afternoon-amble-index/))

## Solution

Based on the length of the solver list, people did quite well on this problem which either means it was very easy, the monthly puzzle got much more popular, or it was dissolved by LLMs.
In the off chance that it was LLMs, I offer my solution argument.

The first issue is figuring out which tiles on the hexagonal lattice floor Andy will consider equivalent to "home". 
On his ball, making three left turns or three right turns will return him to home. 
So, if he makes three lefts or three rights from his starting tile, he will consider them to be "home" but, if he goes there, he won't smell himself and will realize that he's on the floor instead of on the ball. 
Mapping these tiles out, we see that however he initially steps away from "home", he enters a ring that he can't exit from without passing through true "home" or one of the decoys.

Depending on which face he exits from, he goes into one of three rings, but they're all identically arranged.

![](/img/2026-08-27-JS-hexagon-tiles.png){:width="500 px" class="image-centered"}

It might seem odd that he can go in an infinite loop on the floor and not realize he's not on the ball, but indeed if he steps away from home on the ball and then makes three turns in the opposite direction, he will return to the tile he originally stepped to from home. 
So, he can do infinite cycles on the ball and the floor.

As long as he stays in the ring, and does not move onto a decoy "home" before he exits at the real "home", he won't realize that he's off the ball. 
So, the probability he realizes he's not on the ball is the probability that he first exits the ring at the real "home".

For his purposes, the ring has four states: one step from real home, two steps from real home, three steps from real home, and four steps from real home. 
We can model the probability he exits at true home like so

$$
	\begin{align}
		P_1 &= \frac13 + \frac23 P_2 \\
		P_2 &= \frac13 P_1 + \frac13 P_3 \\
		P_3 &= \frac13 P_2 + \frac13 P_4  \\
		P_4 &= \frac23 P_3.
	\end{align}
$$

Solving the system of equations leads to $P_1 = 9/20, P_2=7/40, P_3=3/40,$ and $P_4=1/20$ so the chance he realizes that he's off the ball is $1-P_1 = 55\%.$

### How long, you've been gone

We can use the same sort of equations to model the expected time to come to a conclusion one way or the other. Allowing for him to exit at the decoys as well as the true "home", we get the system of equations.

$$
	\begin{align}
		T_1 &= 1 + \frac13 + \frac23 T_2 \\
		T_2 &= 1 + \frac13 T_1 + \frac13 T_3 + \frac13 \\
		T_3 &= 1 + \frac13 T_2 + \frac13 T_4 + \frac13  \\
		T_4 &= 1 + \frac23 T_3 + \frac13
	\end{align}
$$

which leads to $T_1 = T_2 = T_3 = T_4 = 4.$

### Duration of deception

We can also calculate the expected length of his walk, provided that he ends up at "home." 
Conditioning on arriving at true "home", we have

$$
	\begin{align}
		\langle T_i\rvert \text{survives} \rangle &= 1 + \sum_{j\in\text{neighbors}}P(i\rightarrow j \rvert \text{fooled})T_j \\
		&= 1+\frac{\sum_{j\in\text{neighbors}} P(i\rightarrow j \,\mathbf{AND} \text{ fooled})T_j}{\sum_{j\in\text{neighbors}} P(i\rightarrow j \,\mathbf{AND} \text{ fooled})}\\
		&= 1+\frac{\sum_{j\in\text{neighbors}} P(i\rightarrow j)P(\text{fooled from }j)T_j}{P\left(\text{fooled from }i\right)} \\
		&= 1 + \sum_{j\in\text{neighbors}} \frac{P(i\rightarrow j)P(\text{fooled from }j)}{P\left(\text{fooled from }i\right)}T_j,
	\end{align}
$$

which leads to 

$$
	\begin{align}
		T_1 &= 1 + \frac{20}{27} + \frac{7}{27} T_2 \\
		T_2 &= 1 + \frac67 T_1 + \frac17 T_3\\
		T_3 &= 1 + \frac79 T_2 + \frac29 T_4\\
		T_4 &= 1 + T_3.
	\end{align}
$$

Solving this system of equations gets the expected time for fools, $T_1^\text{fooled} = 57/20 = 2.85$

Working backwards, this means that the expected time conditioned on going to a decoy home is $T_1^\text{witting} = \frac{20}{11}\left(T_1 - T_1^\text{fooled} \frac{9}{20}\right) = 1087/220  \approx 4.94.$ 
So if you're on a long walk, it's some evidence you might be getting duped. 

Plotting the distribution of walk lengths for people who are fooled or witting, we see that the fools can only have even walk lengths and tend to finish more quickly. 
The witting participants wander longer, and can finish at any number of steps greater than $2$, since all tiles on the loop contact a decoy home tile, except for the first step on the loop which only contacts the real home tile.

![](/img/2026_08_28_js_andy_walk_dist.png){:width="600 px" class="image-centered"}