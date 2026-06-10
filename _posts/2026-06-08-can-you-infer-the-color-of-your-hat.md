---
layout: post
published: false
title: Can you infer the color of your hat?
date: 2026/06/08
subtitle: What hats should be in the bag so that you don't die?
tags: logic game-theory
source: fiddler
kind: puzzle
theme: probability
hide_from_recent : true
---

> **Question**: Three game show contestants are shown a bag containing three red hats and two white hats. They are blindfolded, and each picks a hat at random and places it on their head.
>
> One at a time, their blindfolds are removed. Each contestant can see the hats on the others’ heads but not their own.
>
> - **Contestant 1** looks at the others. If they can identify their own hat color with absolute certainty, they say it and the game ends (everyone wins). If not, they skip.
> - **Contestant 2** then does the same, knowing that Contestant 1 skipped.
> - **Contestant 3** then does the same, knowing that both Contestant 1 and Contestant 2 skipped.
>
> Will the contestants always win the prize? If so, why? If not, why not?
>
> **Extra Credit**: Now there are four contestants. The bag contains $R$ red hats, $W$ white hats, and $B$ blue hats, where $R, W, B \le 4$. The rules are the same: they go in order, and each knows the previous contestants skipped.
>
> For some triples $(R, W, B)$, the contestants can always win. Among these, what is the greatest possible value of $R + W + B$?

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-infer-the-color-of-your-hat))

## Solution

Let's write down the state space for the contestant's hat arrangements.

$$ 
\begin{array}{c|c|c}
	# & h_1 & h_2 & h_3 \\
	1 & \text{R} & \text{R} & \text{R} \\
	2 & \text{R} & \text{R} & \text{W} \\
	3 & \text{R} & \text{W} & \text{R} \\
	4 & \text{W} & \text{R} & \text{R} \\
	5 & \text{W} & \text{W} & \text{R} \\
	6 & \text{W} & \text{R} & \text{W} \\
	7 & \text{R} & \text{W} & \text{W} \\
\end{array} 
$$

Player $h_1$ can be certain of their own hat color if they see $h_2=h_3=\text{W}.$ That's because scenario $7$ is the only one where $h_2$ and $h_3$ are have $\text{W}.$ If, for example, $h_3$ saw $h_2=\text{W}, h_3 = \text{R},$ both scenarios $3$ and $5$ match that and each has a different color for $h_1.$

If $h_1$ doesn't announce their hat color, then $h_2$ can assume we are no in scenario $7,$ otherwise $h_1$ would have announced. With scenario $7$ eliminated, $h_2$ can be certain of their hat color if they see scenarios $2$ or $6$ for similar reasons to $h_1$'s logic above. 

If $h_1$ and $h_2$ did not announce their hat color, then $h_3$ can rule out scenarios $7,$ $2,$ and $6,$ leaving $1,$ $3,$ $4,$ and $5.$ Each one of those has distinct values for $(h_1, h_2)$ so $h_3$ will be certain of their hat color no matter what hats they see.

### Extra credit

The manual analysis above lays out a basic algorithm for making this determination in general:

- find all states that uniquely identify the current contestant's hat
- remove them
- repeat

If, in doing this, the last person has possible scenarios that are indeterminate, then it is not possible to win, otherwise, it is. 

```python
from itertools import permutations
from collections import defaultdict

def can_solve(hats, gnomes):
	states = list(set(permutations(hats, gnomes)))
	for h in range(gnomes):

		state_tracker = defaultdict(lambda : list())
		for s in states:
			stem = tuple(s[i] for i in range(gnomes) if i != h)
			state_tracker[stem] += [s]

		next_states = list()
		for k,v in state_tracker.items():
			if len(v) > 1:
				next_states += v
		
		states = next_states

	if states:
		return False
	return True
```

By playing around with bag compositions, we can find that the most voluminous bag possilbe is  `can_solve(1 * ['W'] + 2 * ['R'] + 4 * ['B'], 4)` or one of its equivalent permutations. 

<!-- Fundamentally, by the last turn, the group has to have eliminated all possibilites in the state space. For the first person to eliminate anything, there has to be one hat color that has $1$ more hat than the sum of the other hat counts. If this were not the case, then they would have no guarantee about their own hat color.  -->






<br>
