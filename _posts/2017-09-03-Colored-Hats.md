---
layout: post
published: true
title: Colored Hats
date: 2017/09/03
---

>You and six friends are on a hit game show that works as follows: Each of you is randomly given a hat to wear that is either black or white. Each of you can see the colors of the hats that your friends are wearing but cannot see your own hat. Each of you has a decision to make. You can either attempt to guess your own hat color or pass. If at least one of you guesses correctly and none of you guess incorrectly then you win a fabulous, all-expenses-paid trip to see the next eclipse. If anyone guesses incorrectly or everyone passes, you all lose. No communication is possible during the game — you make your guesses or passes in separate soundproof rooms — but you are allowed to confer beforehand to develop a strategy.
>
>What is your best strategy? What are your chances of winning?
>
>Extra credit: What if instead of seven of you there are $2^N−1$?

<!--more-->

[(fivethirtyeight.com)](https://fivethirtyeight.com/features/is-your-friend-full-of-it/)

## Solution

A distribution is an assignment of hat colors to players. For $N$ players, there are $2^N$ distributions.  

A scenario, representing the information a player has to go on when deciding, is an assignment of hat colors to all but one player. 

A strategy instructs each player what to do for each scenario they might encounter. It is a function from scenarios to the set of possible actions, $\{White, Black, Pass\}$.

For any guess assigned by a strategy to a scenario there is a loss-distribution, and possibly a win-distribution (if there are no incorrect guesses assigned to other scenarios in that distribution). In order for a strategy to produce more wins than losses in the entire set of $2^N$ distributions, it must be that the loss-distributions yielded by assigned guesses overlap, in that multiple assigned guesses yield the same loss distribution. In other words, there must be distributions such that multiple guesses assigned to scenarios in those distributions are incorrect.

For a simple example of this, suppose every player is assigned the incorrect guess $White$ in the all-black scenario they face in the all-black distribution, and that our strategy assigns $Pass$ to every other scenario.  Then we have just one (all-black) loss-distribution and $N$ win-distributions, namely, every one-white-hat distribution (the white-hat player faces the same scenario as in the all-black distribution and hence is assigned $White$, which in this case is correct). So a proportion $N/(N+1)$ of distributions in which a guess is made are wins.  Obviously, there are a lot of loss-distributions in this strategy in which every player passes, so we can certainly do better. But the first moral is: stack incorrect guesses into as few loss-distributions as possible.

One way to extend the simple example strategy for $N=7$ is to have players guess $White$ if they see zero or two white hats, $Black$ if they see four or six, and $Pass$ otherwise. This produces wins for every distribution assigning one, three, four, and six white hats, which comprise $7+35+35+7$, or $84$ distributions, which is about $65.6\%$ of the $2^7$ or $128$ total distributions.

But we can do even better! The trick that we began the simple example with was to match a single seven-incorrect-guesses distribution with seven distributions with one correct guess and seven passes. The ideal extension of that would be to have $16$ instances of that pattern: a "hub" losing distribution with seven "satellite" winning distributions that differ from it by one hat-color. Suppose we found sixteen such hubs that together with their satellites cover all $128$ distributions. Then our strategy would be for any player who sees a scenario compatible with a hub distribution to guess the color that he must have if it's not a hub distribution, and for players to pass otherwise. Hub distributions themselves, then, produce seven incorrect guesses, and each non-hub distribution produces one correct guess (the other six players can see, based on the guesser's hat, that it's not a hub distribution).

In fact this is possible. I found 16 such hub distributions computationally (the Python code is below; on average it takes about 30 repetitions). Representing black and white with $1$s and $0$s, the hub distributions are:

```
0000000
1111111
0010110
1000101
0101100
1110100
0001011
1010011
1100010
0111010
0110001
0100111
0011101
1101001
1001110
1011000
```

And so we will $7/8$ of the time. As for the case of larger $N$ (where $N$ is of the form $2^M-1$), I conjecture that the same trick is always possible, and we win $N/(N+1)$ of the time. Given that I found the solution for $N=7$ computationally, though, I don't have a proof of that.

```python
from random import shuffle

# There are N players
N = 7
Reps = 100

def mod (n,b):
	# Return a string that is the numeral for n in base b
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return ''.join(reversed(nums))

def DifferByOneBit(m,n):
	# Do the binary representations of m and n differ by
	# exactly one bit?
	a = mod(min(m,n),2)
	b = mod(max(m,n),2)
	while len(a) < len(b):
		a = "0" + a
	DifferentBits = 0
	for i in range(len(a)):
		if not a[i] == b[i]:
			DifferentBits += 1
	return (DifferentBits == 1)

# A number's neighbors differ from it by one bit
Neighbors = []
for m in range(2**N):
	Neighbors.append([])
	for n in range(2**N):
		if DifferByOneBit(m,n):
			Neighbors[m].append(n)

for rep in range(Reps):
	# Start with all zeros and all ones as initial hubs
	Hubs = [0,2**N-1]
	Unused = list(range(1,2**N-1))
	for dist in Neighbors[0] + Neighbors[2**N-1]:
		Unused.remove(dist)
	while len(Unused) > 0:
		FoundNewHub = 0
		shuffle(Unused)
		for TryHub in Unused:
			Success = True
			for Neighbor in Neighbors[TryHub]:
				if not Neighbor in Unused:
					Success = False
			if Success:
				break
		if Success:
			Hubs.append(TryHub)
			for Neighbor in [TryHub]+Neighbors[TryHub]:
				Unused.remove(Neighbor)
		else: 
			break
	if Unused == []:
		print "Success at trial",rep
		for Hub in Hubs:
			s = mod(Hub,2)
			while len(s) < N:
				s = "0"+s
			print s
		break
```

<br>
