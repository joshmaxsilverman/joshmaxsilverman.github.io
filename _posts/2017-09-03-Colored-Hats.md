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

There is a very tempting line of reasoning to the effect that, because every guess has a $1/2$ chance of being correct (which is true), and every victory requires at least one correct guess (also true), it follows that every victory requires at least one event of probability $1/2$ to occur (right again), and so there can't be greater than $1/2$ chance of winning (but this doesn't follow, and is false!). The trick, as we will see, is to ensure that when players guess incorrectly, they do so _together_, and when correctly, alone.

A _distribution_ is an assignment of hat colors to players. For $N$ players, there are $2^N$ distributions.  A _scenario_, representing the information a player has to go on when deciding, is an assignment of hat colors to all but that one player. A _strategy_ tells each player what to do for each scenario they might encounter. It is a function from scenarios to the set of possible actions, $\{White, Black, Pass\}$.

For any guess assigned by a strategy to a scenario there is a loss-distribution, in which the guess is incorrect, and also a distribution in which it is correct (which is a win-distribution if there are no incorrect guesses assigned to other scenarios in that distribution). In order for a strategy to produce more wins than losses in the entire set of $2^N$ distributions, it must be that the loss-distributions for assigned guesses overlap, in that multiple assigned guesses occur in the same loss-distribution. In other words, there must be distributions such that multiple guesses assigned to scenarios in those distributions are incorrect.

For a simple example of this, suppose that every player is assigned the incorrect guess $White$ in the all-black scenario they face in the all-black distribution, and that our strategy assigns $Pass$ to every other scenario.  Then we have just one (all-black) loss-distribution and $N$ win-distributions, namely every one-white-hat distribution (the white-hat player faces the same scenario as in the all-black distribution and hence is assigned $White$, which in this distribution is correct). So a proportion $N/(N+1)$ of distributions in which a guess is made are wins.  Obviously, there are a lot of loss-distributions in this strategy (in which every player passes), so we can certainly do better. But the moral is: stack incorrect guesses into as few loss-distributions as possible; have players be wrong together, and right separately.

The ideal extension of our simple example, in the case of $N=7$, would be to have $16$ instances of that pattern: a "hub" losing distribution with seven "satellite" winning distributions that differ from their hub by one hat-color. Suppose we found sixteen such hubs that together with their satellites cover all $128$ distributions. Then our strategy would be for any player who sees a scenario compatible with a hub distribution to guess the color that he must have if it's actually _not_ a hub distribution, and for players to pass otherwise. Hub distributions themselves, then, produce seven incorrect guesses, and each satellite distribution produces one correct guess (the other six players can see, based on the guesser's hat, that it's not a hub distribution).  This would be optimal in that the incorrect guesses are maximally stacked, and it would give a win ratio of $7/8$.

And in fact this is possible! Initially, I found a set of hubs computationally. Python code is shown below; it uses some randomness and on average it takes only a few seconds to succeed. It is based on the observation that two hubs sharing no satellites is equivalent to their assigning different colors to at least three hats.  Representing black and white with $1$s and $0$s, one set of hub distributions I found that way contains these (different runnings produce different hubs):

```
0000000
0001011
0010110
0011101
0100111
0101100
0110001
0111010
1000101
1001110
1010011
1011000
1100010
1101001
1110100
1111111
```

### Getting Systematic

The computational approach doesn't help for the general case of arbitrary $N$ where $N$ is $2^M-1$ for some $M$. For that we will need to turn to [coding theory](https://en.wikipedia.org/wiki/Forward_error_correction) (where the reason for the curious restriction to such values of $N$ will emerge). 

The problem of finding a complete set of hubs (in the sense that the hubs and their disjoint sets of satellites exhaust the distributions) is the same as the problem of finding a signaling system with a maximally large set of $N$-digit binary numerals as signals, such that the receiver will be able to identify the sent signal even if one bit gets changed along the way. The computationally-found set of hubs for $N=7$ is such a set of sixteen signals. If we receive a satellite, one-digit off from a hub, we know its hub, because each satellite is one-digit off from only its own hub.

We can design a set of sixteen such signals more systematically, as a [Hamming Code](https://en.wikipedia.org/wiki/Hamming_code).  

We will treat the first four of our seven digits as _data bits_; the real goal of signal transmission is to recover the data bits that were sent, and there will be one signal for each of the $16$ ways of setting those bits. The remaining three digits are _parity bits_, which allow the receiver to do this even if (exactly) one of the seven bits is erroneous. For four given data bits, we assign to each of the parity bits a value based on the data bits it _covers_. The three parity bits cover the following sets of data bits: $\\{1,2,4\\}, \\{1,3,4\\},$ and $\\{2,3,4\\}$. The signal is completed by setting each parity bit to the sum of the data bits it covers, modulo $2$.

![Bit coverage.](/img/HammingCode.jpg)

Suppose we receive a numeral that has a parity mismatch, and that we know that this can only be because it differs from a signal by one bit. We could break out our list of signals and check which one it's a bit off from. But given how we defined the signals, we will also be able to identify that bit by looking at just which parity bits are mismatched.  There are seven different possibilities ($2^3-1$, where the minus-one is because one possibility is that there is no mismatch), and we have set things up so that each possibility corresponds to a different bit being erroneous.  To give two examples: if only the first parity bit is mismatched, then we know that it itself is in error, because an error in data bit $1$, $2$, or $4$ would lead to two or three parity mismatches. And if the second and third parity bits are mismatched, the erroneous bit must be data bit 3, which is the one bit that they and only they cover.

Every seven-digit binary numeral is either itself a signal or a one-digit variant of a signal that we can decode in this way.  Of course we are not ourselves interested in signal transmission; the point is that this method generates sixteen hubs (the signals) each of which is surrounded by a unique group of seven satellites (the one-bit errors). The hubs generated in this way are:

```
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
```

For an arbitrary $N$ which is $2^M-1$ for some $M$, we can pull the same trick using $N-M$ data bits and $M$ parity bits (which can indicate an error in $2^M-1$ ways). The existence of an adequate scheme of assigning parity bit coverage follows from the fact that the number of subsets of size $2$ or larger of $M$ parity bits is $2^M$ (for all subsets) minus $1$ (for the null subset) minus $M$ (for singleton subsets), or $N-M$, which is exactly what we need for each data bit to be covered by a distinct set of parity bits (of size $2$ or larger, leaving the singletons of parity bits to indicate errors in those bits themselves).

And so in general we will win $N/(N+1)$ of the time.

This was a very interesting Riddler. Thank you, Oliver Roeder and Riddle supplier Jared Bronski!

<br>

```python
# For a given N find 2^N/(N+1) binary numerals which difffer
# from one another in at least three digits.

from random import shuffle

# There are N players
N = 7
Reps = 100000000

def BaseNumeral (n,b):
	# Return a string that is the numeral for n in base b
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return ''.join(reversed(nums))

def Pad(b,D):
	# Add zeroes to binary numeral b until its length is D
	while len(b)<D:
		b = "0" + b
	return b

def DifferByAtLeastThreeBits(m,n):
	# Do the binary representations of m and n differ by
	# at least three bits?
	a = Pad(BaseNumeral(m,2),N)
	b = Pad(BaseNumeral(n,2),N)
	DifferentBits = 0
	for i in range(len(a)):
		if not a[i] == b[i]:
			DifferentBits += 1
	return (DifferentBits >= 3)

for rep in range(Reps):
	# Start with all zeros and all ones as initial hubs
	Hubs = []
	Unused = list(range(2**N))
	while len(Hubs) < 2**N/(N+1):
		FoundNewHub = 0
		shuffle(Unused)
		for TryHub in Unused:
			Success = True
			for Hub in Hubs:
				if not DifferByAtLeastThreeBits(Hub,TryHub):
					# print Pad(BaseNumeral(Hub,2),N),Pad(BaseNumeral(TryHub,2),N),DifferByAtLeastThreeBits(Hub,TryHub)
					Success = False
			if Success:
				break
		if Success:
			Hubs.append(TryHub)
			Unused.remove(TryHub)
		else: 
			break
	if len(Hubs) == 2**N/(N+1):
		print "Success at trial",rep
		Hubs.sort()
		for Hub in Hubs:
			s = Pad(BaseNumeral(Hub,2),N)
			print s
		break

```

<br>
