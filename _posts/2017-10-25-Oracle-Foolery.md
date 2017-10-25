---
layout: post
published: true
title: Oracle Foolery
date: 2017-10-25
---

>You must build a very specific tower out of four differently colored pieces that can be stacked in any order. But when you start building, you don’t know what the correct order is. Upon assembling the pieces in some order, you can consult an architectural oracle (he goes by Frank) who will inform you if zero, one, two or all four pieces of the tower are in the correct position. Your tower doesn’t count as finished until the oracle confirms your solution is correct. How many times should you have to consult the oracle, in the worst case, to assemble the tower correctly?

<!--more-->

[(fivethirtyeight)](https://fivethirtyeight.com/features/can-you-please-the-oracle-can-you-escape-the-prison/)

## Solution

Think of the game like this. The correct order is not determined in advance, but the Oracle delivers messages of how many pieces are misplaced so as to try to extend the game as long as possible. The messages have to be consistent; that is, they must fit at least one possible "correct" order. You succeed the turn after his messages become consistent with just one order.

The tree of possible guesses and messages is not large, so you can calculate the optimal moves for you and for the Oracle in each situation.  It turns out that optimally-played worst-case scenarios are variations on this six-guess scenario:

| Order | Misplaced |
| ----- | --------- |
| ABCD  | 3 |
| CDBA  | 3 |
| DCBA  | 3 |
| BADC  | 3 |
| DBAC  | 3 |
| DACB  | 0 |

### Code (Python)

```python
from itertools import permutations

def DifferAtPlaces(L1,L2,n):
	for i in range(len(L1)):
		if not L1[i] == L2[i]:
			n -= 1
	return (n == 0)

def Explore(Remaining):
	# Given a list of still-possible orderings, find a guess that minimizes 
	# the maximum game length from here. Return that game length and a list
	# of guesses from here onwards in such a game.
	BestWorstCaseLength = 24
	for Guess in Remaining:
		WorstCaseGuessList = []
		WorstCaseLength = 0
		for OracleDifference in (2,3,4):
			NewRemaining = []
			for L in Remaining:
				if DifferAtPlaces(Guess,L,OracleDifference):
					NewRemaining += [L]
			if NewRemaining == []:
				continue
			(Length,GuessList) = Explore(NewRemaining)
			if Length > WorstCaseLength:
				WorstCaseLength = Length
				WorstCaseGuessList = GuessList
		if WorstCaseLength < BestWorstCaseLength:
			BestGuess = Guess
			BestWorstCaseLength = WorstCaseLength
			BestGuessList = WorstCaseGuessList
	return (BestWorstCaseLength+1,BestGuessList + [BestGuess])

print Explore(list(permutations((1,2,3,4))))
```

<br>
