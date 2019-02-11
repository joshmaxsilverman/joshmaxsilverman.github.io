---
layout: post
published: true
title: Nine Cards
date: 2019/02/08
---

>You and I are playing a game. It’s a simple one: Spread out on a table in front of us, face up, are nine index cards with the numbers 1 through 9 on them. We take turns picking up cards and putting them in our hands. There is no discarding.
>
>The game ends in one of two ways. If we run out of cards to pick up, the game is a draw. But if one player has a set of three cards in his or her hand that add up to exactly 15 before we run out of cards, that player wins. (For example, if you had 2, 4, 6 and 7, you would win with the 2, 6 and 7. However, if you had 1, 2, 3, 7 and 8, you haven’t won because no set of three cards adds up to 15.)
>
>Let’s say you go first. With perfect play, who wins and why?
<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/525600-minutes-of-math/))


## Computational Solution

We find the optimal game by recursively calling a function that yields an optimally-played completion of a given partially-played game ("an" optimally-played completion because there can be ties).  It turns out that the best either player can do is to draw.  The particular draw that this code lands on isn't really significant, but the hands are `[[9, 8, 3, 6, 2], [5, 7, 4, 1]]`.  

```python

# Nine-card game played optimally.  Players are 0 and 1, cards are 1 to 9.

def handWins(hand):
	for i in range(len(hand) - 2):
		for j in range(i+1, len(hand) - 1):
			for k in range(j+1,len(hand)):
				if hand[i] + hand[j] + hand[k] == 15:
					return True
	return False

def getOptimalCompletion(hands, nextPlayer):
	# if game's over, return the result and the hands
	if handWins(hands[0]):
		return [0,hands]
	elif handWins(hands[1]):
		return [1,hands]
	elif len(hands[0]) == 5:
		return [2,hands]
	# otherwise, find the best optimal completion available by playing each
	# of the remaining cards, and return that.
	bestOptimalCompletion = []
	for nextCard in range(1,10):
		if nextCard in hands[0] or nextCard in hands[1]:
			continue
		newHands = [list(hands[0]), list(hands[1])]
		newHands[nextPlayer].append(nextCard)
		OptimalCompletion = getOptimalCompletion(newHands, 1 - nextPlayer)
		if OptimalCompletion[0] == nextPlayer:
			return OptimalCompletion
		elif OptimalCompletion[0] == 2 or bestOptimalCompletion == []:
			# a draw, or a loss but the first card tested; best so far either way
			bestOptimalCompletion = OptimalCompletion
	return bestOptimalCompletion

print(getOptimalCompletion ([[],[]],0))

```

<br>
