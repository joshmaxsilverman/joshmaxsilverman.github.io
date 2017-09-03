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

For any guess assigned by a strategy to a scenario there is a loss-distribution, and possibly a win-distribution (if there are no incorrect guesses assigned to other scenarios in that distribution). In order for a strategy to produce more wins than losses in the entire set of $2^N$ distributions, it must be that the loss-distributions yielded by assigned guesses overlap, in that multiple assigned guesses yield the same loss-distribution. In other words, there must be distributions such that multiple guesses assigned to scenarios in those distributions are incorrect.

For a simple example of this, suppose every player is assigned the incorrect guess $White$ in the all-black scenario they face in the all-black distribution, and that our strategy assigns $Pass$ to every other scenario.  Then we have just one (all-black) loss-distribution and $N$ win-distributions, namely, every one-white-hat distribution (the white-hat player faces the same scenario as in the all-black distribution and hence is assigned $White$, which in this case is correct). So a proportion $N/(N+1)$ of distributions in which a guess is made are wins.  Obviously, there are a lot of loss-distributions in this strategy in which every player passes, so we can certainly do better. But the first moral is: stack incorrect guesses into as few loss-distributions as possible.

The ideal extension of our simple example would be to have $16$ instances of that pattern: a "hub" losing distribution with seven "satellite" winning distributions that differ from their hub by one hat-color. Suppose we found sixteen such hubs that together with their satellites cover all $128$ distributions. Then our strategy would be for any player who sees a scenario compatible with a hub distribution to guess the color that he must have if it's _not_ a hub distribution, and for players to pass otherwise. Hub distributions themselves, then, produce seven incorrect guesses, and each non-hub distribution produces one correct guess (the other six players can see, based on the guesser's hat, that it's not a hub distribution).

In fact this is possible. Initially, I found a set of hubs computationally (the Python code is shown below; it uses some randomness and on average it takes about 30 repetitions). Representing black and white with $1$s and $0$s, the hub distributions I found that way are:

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

And so we will win $7/8$ of the time. 

The computational approach doesn't help for the general case of $N$ where $N$ is $2^M-1$ for some $M$. For that we will need to turn to coding theory. The problem of finding a complete set of hubs is the same as the problem of finding a signaling system with a set of binary numerals as signals, such that the receiver will be able to identify the sent signal even if one bit gets changed along the way.

The computationally-found set of hubs is such a set of sixteen signals. If we receive a satellite, one-bit off from one of those, we know its hub.

But we can design a set of hubs more systematically, using ideas due to [Richard Hamming](https://en.wikipedia.org/wiki/Hamming_code).  

We will treat the first four of our digits as data bits; the goal of transmission is to recover the data bits that were sent. The remaining three digits are parity bits, which allow us to do this even if (exactly) one bit is erroneous. For four given data bits, we assign to a parity bits the data bits it covers. The three parity bits cover these triples of data bits: $(1,2,4), (1,3,4), (2,3,4)$. However the data bits are set, the signal is completed by setting each parity bit to the sum of the data bits, modulo $2$.

Suppose we receive a numeral with a parity mismatch, owing to being one bit different than a signal. We will be able to identify that bit by looking at just which parity bits are mismatched.  There are seven different possibilities, and we have set things up so that each possibility corresponds to a different bit being erroneous.  For instance, if only the first parity bit is mismatched, then we know that it itself is in error, because an error in data bit $1$, $2$, or $4$ would lead to two or three parity mismatches. And if the second and third parity bits are mismatched, the erroneous bit must be data bit 3.

The hubs produced this way are:

0000000
0001111
0010011
0011100
0100101
0101010
0110110
0111001
1000110
1001001
1010101
1011010
1100011
1101100
1110000
1111111

For an arbitrary $N$ that is $2^M-1$ for some $M$, we can pull the same trick using $(2^M-1)-M$ data bits and $M$ parity bits (which can indicate an error in $2^M-1$ ways). (Find a general algorithm for assigning parity bit coverage [here].) And so in general we will win $N/(N+1)$ of the time.

<br>

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
