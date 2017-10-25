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

The tree of possible guesses and messages is small enough so that you can calculate the optimal moves for you and for the Oracle in each situation.  It turns out that optimally-played worst-case scenarios are five-guess games, such as:

| Guess | Misplaced |
| ----- | --------- |
| ADCB  | 2 |
| ACDB  | 3 |
| ACBD  | 2 |
| ABDC  | 2 |
| ABCD  | 0 |

Notice that the third and fourth guesses are informational plays only and are guaranteed to be incorrect; each shares two characters with the second guess, which we know has three incorrect characters.

### Code (Python)

```python
from itertools import permutations

def DifferAtPlaces(L1,L2,n):
	for i in range(len(L1)):
		if not L1[i] == L2[i]:
			n -= 1
	return (n == 0)

def Explore(RemainingPossibilities,PreviousGuesses):
	# Given a list of still-possible orderings, find a guess that minimizes 
	# the maximum game length from here. Return that game length and a list
	# of guesses from here onwards in such a game.
	BestWorstCaseLength = 24
	for Guess in Possibilities:
		WorstCaseGuessList = []
		WorstCaseLength = 0
		for OracleMessage in (2,3,4):
			NewRemainingPossibilities = [L for L in RemainingPossibilities if DifferAtPlaces(Guess,L,OracleMessage)]
			if NewRemainingPossibilities == []:
				continue
			if NewRemainingPossibilities == RemainingPossibilities:
				# Guess is silly; it would gift Oracle an extra turn
				(Length,GuessList) = (25,[])
			else:
				(Length,GuessList) = Explore(NewRemainingPossibilities,PreviousGuesses+[Guess])
			if Length > WorstCaseLength:
				WorstCaseLength = Length
				WorstCaseGuessList = GuessList
		if WorstCaseLength < BestWorstCaseLength:
			BestGuess = Guess
			BestWorstCaseLength = WorstCaseLength
			BestGuessList = WorstCaseGuessList
	return (BestWorstCaseLength+1,BestGuessList + [BestGuess])

Possibilities = list(permutations((1,2,3,4)))
print Explore(Possibilities,[])
```

<br>
