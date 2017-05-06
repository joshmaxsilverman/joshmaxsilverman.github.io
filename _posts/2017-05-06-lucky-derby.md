---
layout: post
published: false
title: Lucky Derby
date: 2017/05/06
---

>The bugle sounds, and 20 horses make their way to the starting gate for the first annual Lucky Derby. These horses, all trained at the mysterious Riddler Stables, are special. Each second, every Riddler-trained horse takes one step. Each step is exactly one meter long. But what these horses exhibit in precision, they lack in sense of direction. Most of the time, their steps are forward (toward the finish line) but the rest of the time they are backward (away from the finish line). As an avid fan of the Lucky Derby, you’ve done exhaustive research on these 20 competitors. You know that Horse One goes forward 52 percent of the time, Horse Two 54 percent of the time, Horse Three 56 percent, and so on, up to the favorite filly, Horse Twenty, who steps forward 90 percent of the time. The horses’ steps are taken independently of one another, and the finish line is 200 meters from the starting gate.
>
>Handicap this race and place your bets! In other words, what are the odds (a percentage is fine) that each horse wins?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/who-will-win-the-lucky-derby/))

## Solution

Each horse's path is an asymmetric random walk. There is a large literature on the probabilities and expectations of such walks, and one approach would be to draw on it to find explicit, if approximate, expressions for the various probability distributions involved. But I'm pretty sure that we would have to manipulate these values numerically anyway, so there is no great benefit over simply running a Monte Carlo simulation. So that's what we do, and we find that, in a series of 100,000 races, no horse below \#14 wins even one race, and among the horses that do win, here are the percentages (which sum to greater than 1 because of ties):

14 | 15 | 16 | 17 | 18 | 19 | 20 
---|----|----|----|----|----|---
.001|.008|.125|.934|5.56|23.3|74.5

### Code (Python):
```python
from random import random,shuffle

reps = 100000
HorseProb = [.52 + .02*i for i in range(20)]
Victories = [0]*20

for r in range(reps):
	Position = [0]*20
	NoVictor = True
	while NoVictor:
		for Horse in range(20):
			if random() < HorseProb[Horse]:
				Position[Horse] += 1
				if Position[Horse] == 200:
					Victories[Horse] += 1
					NoVictor = False
			else:
				Position[Horse] -= 1
for Horse in range(20):
	print(Horse+1,",",Victories[Horse]/reps)

```

<br>
 
