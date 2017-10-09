---
layout: post
published: true
title: Name Boxes
date: 2017-10-06
---

>You and three of your friends are on a game show. On stage is a sealed room, and in that room are four sealed, numbered boxes. Each box contains one of your names, and each name is in one box. You and your friends take turns entering the room alone and opening up to two boxes, with the aim of finding the box containing your name. Everyone enters exactly once. Your team can confer on a strategy before stepping on stage, but there is no communication allowed during the show — no player knows the outcome of another player’s trip into the room.
>
>Your team wins if it’s ultimately revealed that everyone found the box containing his or her name and loses if any player failed to do so. Obviously, the odds of winning are no better than 50 percent because any single player has a 50 percent chance of finding his or her own name. If each person opens two boxes at random, the chance of winning is (1/2)4=1/16=6.25(1/2)4=1/16=6.25 percent. Or to put it in technical terms: The chance of winning is not so great. Call this the naive strategy.
>
>Your goal: Concoct a strategy that beats the naive strategy — one that gives the team a better chance of winning than 1/16.
>
>Extra credit: Suppose there are 100 contestants and 100 boxes. Each player may open 50 boxes. The chance of winning by using the naive strategy is 1 in 21002100, or about 1 in 1.2×10301.2×1030. How much can you improve the team’s chances?

<!--more-->

Let's go straight to the general case of $n$ players, for some even number $n$.  A strategy is a function from players to sets of $n/2$ numbers from $1$ to $n$. An arrangement is a function from numbers from $1$ to $n$ (numbering the players) to numbers from $1$ to $n$ (numbering the boxes). A strategy wins at an arrangement just in case the arrangement assigns to each player a number that is among those assigned to the player in the strategy.  

Suppose we try the strategy that assigns to each number up to $n/2$ the set of all numbers up to $n/2$ and to each number above $n/2$ the set of all the numbers above $n/2$. Then there will be a winning arrangement for each way of ordering those two sets, for a total of $(n/2)!^2$ arrangements.  For $n=100$, that gives a winning probability that is $12.56$ times that of the naive strategy.

```python
NumberOfPlayers = 4

# An arrangement is an assignment of players to boxes
Arrangements = []
def ExploreArrangements (Arrangement):
	if len(Arrangement) == NumberOfPlayers:
		Arrangements.append(Arrangement)
		return
	for Player in range(NumberOfPlayers):
		if Player in Arrangement:
			continue
		NewArrangement = list(Arrangement)
		NewArrangement.append(Player)
		ExploreArrangements(NewArrangement)
ExploreArrangements([])

# A strategy is an assignment of NumberOfPlayers/2 boxes to each player
PlayerStrategies = []
def ExploreStrategies (Strategy):
	if len(Strategy) == NumberOfPlayers/2:
		PlayerStrategies.append(Strategy)
		return
	Last = -1
	if len(Strategy):
		Last = Strategy[-1]
	for i in range(Last + 1, NumberOfPlayers - (NumberOfPlayers/2 - len(Strategy)) + 1):
		NewStrategy = list(Strategy)
		NewStrategy.append(i)
		ExploreStrategies(NewStrategy)
ExploreStrategies([])

StrategiesPerPlayer = len(PlayerStrategies)

Strategies = (StrategiesPerPlayer)**NumberOfPlayers
# Strategies is the number of team strategies. 
# The numbers from zero to Strategies-1 can be thought of as 
# NumberOfPlayers-digit numerals in base StrategiesPerPlayer,
# where each digit represents a player's strategy. Thus,
# each numeral encodes a team strategy.

print "For",NumberOfPlayers,"players there are", len(PlayerStrategies),"player strategies and",Strategies,"team strategies."

def Win (Strategy,Arrangement):
	global NumberOfPlayers
	for Player in range(NumberOfPlayers):
		PlayerStrategy = (Strategy/(StrategiesPerPlayer**Player))%StrategiesPerPlayer
		if not Arrangement[Player] in PlayerStrategies[PlayerStrategy]:
			return False
	return True

def PrintStrategy(Strategy):
	for Player in range(NumberOfPlayers):
		PlayerStrategy = (Strategy/(StrategiesPerPlayer**Player))%StrategiesPerPlayer
		print PlayerStrategies[PlayerStrategy]

BestStrategy = 0
BestWinTally = 0
for Strategy in range(Strategies):
	WinTally = 0
	for Arrangement in Arrangements:
		if Win(Strategy,Arrangement):
			WinTally += 1
	if WinTally > BestWinTally:
		BestWinTally = WinTally
		BestStrategy = Strategy

print "Best strategy yields",BestWinTally,"wins in",len(Arrangements),"arrangements, and is:"
PrintStrategy(BestStrategy)
```

### Dynamic Strategy 

But it turns out that we can vastly improve upon that if we allow a "strategy" to vary depending on what the players find when they open boxes.

In particular, we instruct each player to open the box with their own number on it and from then on to open the box whose number they just found. Then, either the player will "loop" back to their own number within $n/2$ boxes or not.

This strategy creates, from a given arrangement, a set of loops of size between $1$ and $n$, where the box after a given box in a loop is the box whose number it contains; it is easy to see that there is a one-to-one correspondence between arrangements and ways of forming such loops of boxes. 

The strategy succeeds whenever there is no loop greater than $n/2$ in length. For how many assignments is that true? We'll start by counting the assignments that create a loop of some size $s$ greater than $n/2$. There are $n \choose s$ ways to select boxes in the loop, $(s-1)!$ ways of ordering them, and $(n-s)!$ ways of assigning the remaining boxes. So the number of assignments with $s$-sized loops is:

$${n \choose s} (s-1)!(n-s)! = \frac{n!}{s}$$

And the total number of losing assignments is:

$$\sum_{s=\frac{n}{2}+1}^{n} \frac{n!}{s}$$

And the probability of winning is:

$$1 - \sum_{s=\frac{n}{2}+1}^{n} \frac{1}{s}$$

For $n=100$, that's about $31.18%$.

<br>
