---
layout: post
published: false
title: Hat Hostage Strategies II
date: 2021/11/22
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution



```python
import random
import itertools
import copy

colors = ['r', 'g', 'y']

strategies = [
    {_ : random.choice(colors) 
    for _ in itertools.product(colors, repeat=2)} 
    for _ in range(4)
  ]

# list of all possible combination of hat colors for 4 gnomes
cases = list(itertools.product(colors, repeat = 4))

# list of all possible pairs of viewable hats for two gnomes
player_views = list(itertools.product(colors, repeat = 2))

def evaluate_round(current_case, strategies):
  P1_prediction = strategies[0][(current_case[1], current_case[3])] == current_case[0]
  P2_prediction = strategies[1][(current_case[0], current_case[2])] == current_case[1]
  P3_prediction = strategies[2][(current_case[1], current_case[3])] == current_case[2]
  P4_prediction = strategies[3][(current_case[0], current_case[2])] == current_case[3]

  return (1 if any([P1_prediction, P2_prediction, P3_prediction, P4_prediction]) else 0)

def score_current_strategies(strategies):
  return sum(evaluate_round(case, strategies) for case in cases)
  
scores = []
for round in range(100000):
  # if 5000 rounds have elapsed, reset the search
  if round % 5000 == 4999:
    strategies = [{_ : random.choice(colors) for _ in itertools.product(colors, repeat=2)} for _ in range(4)]

  current_score = score_current_strategies(strategies)

  # pick a player whose strategy we'll mutate
  strategy_to_mutate = random.randint(0,3)
  # pick the specific view we're mutating
  case_to_mutate = random.choice(player_views)

  temp_strategies = copy.deepcopy(strategies)
  temp_strategies[strategy_to_mutate][case_to_mutate] = random.choice(colors)
  temp_score = score_current_strategies(temp_strategies)

  if temp_score >= current_score:
    strategies = temp_strategies
    current_score = temp_score
  
  scores.append(current_score)

  if temp_score == 81:
    break

```

<br>
