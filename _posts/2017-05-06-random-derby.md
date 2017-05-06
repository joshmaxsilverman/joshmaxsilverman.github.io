---
layout: post
published: false
title: Random Derby
date: 2017/05/06
---

>The bugle sounds, and 20 horses make their way to the starting gate for the first annual Lucky Derby. These horses, all trained at the mysterious Riddler Stables, are special. Each second, every Riddler-trained horse takes one step. Each step is exactly one meter long. But what these horses exhibit in precision, they lack in sense of direction. Most of the time, their steps are forward (toward the finish line) but the rest of the time they are backward (away from the finish line). As an avid fan of the Lucky Derby, you’ve done exhaustive research on these 20 competitors. You know that Horse One goes forward 52 percent of the time, Horse Two 54 percent of the time, Horse Three 56 percent, and so on, up to the favorite filly, Horse Twenty, who steps forward 90 percent of the time. The horses’ steps are taken independently of one another, and the finish line is 200 meters from the starting gate.
>
>Handicap this race and place your bets! In other words, what are the odds (a percentage is fine) that each horse wins?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/who-will-win-the-lucky-derby/))

## Solution

Each horse's path is an asymmetric random walk. There is a large literature on the probabilities and expectations of such walks, and one approach would be to draw on it to find explicit, if approximate, expressions for the various probabilities involved. But we would have to manipulate these values numerically anyway, so there is no great benefit over simply running a Monte Carlo simulation. So that's what we do, and we find that, in a series of 100,000 races, no horse below \#14 wins even one race, and among the horses that do win, here are the percentages:

14 | 15 | 16 | 17 | 18 | 19 | 20 
---|----|----|----|----|----|---
.001|.008|.085|.813|5.04|21.8|72.3

### Code (Python):

```python
{% include RandomDerby.py %}
```

<br>
 
