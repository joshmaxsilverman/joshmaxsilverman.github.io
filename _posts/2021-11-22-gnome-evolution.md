---
layout: post
published: true
title: Hat Hostage Strategies II
date: 2021/11/22
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

before looking for solutions, we can lay down some basic facts.

each gnome will guess correctly in exactly $h^{n-1} = 27$ of the $h^n = 81$ potential cases, regardless of how they design their policy.

this is because each player makes the same guess for each pair of hat colors they can see, which have no correlation with the hat on their head.

an immediate corollary is that, in all, the players will make $h^{n-1} \times n = 108$ correct guesses. so, at least in number, there are more than enough correct guesses to distribute $1$ to each of the $h^n = 81$ possible cases. if there are more hat colors than people, then full survival is impossible.

the control we can exert is how the correct responses are distributed. 

a simple example helps illustrate this:

>two players with two hat colors. it is either the case that the two players have the same hat color, or they have different hat colors. so, if Player A always guesses the same as their partner's hat and Player B always guesses the opposite of their partner's hat, then at least one of them will be right in every round that's played. 

we are trying to find a similar sort of structure here.

without any structure (i.e. the gnomes use random strategies) they will survive in, on average, $65$ of the $81$ cases. the first gnome makes $27$ correct guesses which is a third of cases. so the second player will make, on average, $18$ of their correct guesses in cases where the first player is wrong. together, $18$ and $27$ make $45$ which is $5/9^\text{th}$s of all cases, so the third player will make correct guesses in $12$ cases where the first two players are wrong. finally, fourth player will be correct in $8$ novel cases. all together, $27+18+12+8 = 65.$

similarly, the gnomes will survive in no fewer than $45$ of the $81$ cases.

finding a nice breakdown did not yield to analysis, so i turned to biology. essentially, the gnomes pick a random strategy (a map from the $3\times3 = 9$ hat pairs they can see to a prediction for their own hat) and the gnomes figure out how many cases they would currently survive in. they then pick a random gnome among them to mutate a random row in their map. if this does not lower the number of cases they survive in, then they accept the change, otherwise they reject it. then the process starts again.

this has the potential to be a quick discovery process because there is no connection between one gnome being correct and another being wrong. progress is progress is progress.

it's always possible that the gnomes pick a bad region of strategy space to start in, so if they go $5000$ mutations without hitting $81$ they all repick a random strategy and start over.

$$
\begin{array}
\text{View} & \text{Player 1} & \text{Player 2} & \text{Player 3} & \text{Player 4} \\
(r, r) & y & y & r & g \\
(r, g) & y & g & g & r \\
(r, y) & r & r & r & y \\
(g, r) & r & g & g & g \\
(g, g) & y & r & y & g \\
(g, y) & g & r & r & r \\
(y, r) & g & y & y & r \\
(y, g) & r & y & y & y \\
(y, y) & g & g & g & y 
\end{array}
$$

![](/img/sss.jpg)

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
