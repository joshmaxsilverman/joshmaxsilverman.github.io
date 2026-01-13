---
layout: post
published: true
title: The price is wrong
date: 2020/10/18
subtitle: How do you bid when no one knows any prices anymore?
source: fivethirtyeight
theme: probability
---

>**Question**: The ghost of Bob Parker takes a break from saving animals to remind you of your invitation to pandemic Price is Right, with Drew Carey. Usually, you're up against some real price wizards, but since nobody has been to a store in $7$ months, everyone is on a level playing field and has no idea about prices. 
>
>With the prices effectively random, you're left to pure strategy to prevail at the game. As a refresher, everyone guesses the price of the product in succession such that the later contestants can hear the guess of the earlier contestants. Whoever guesses the highest without exceeding the true price of the item wins. In the case that everyone guesses too high, the game goes to whoever guessed closest. 
>
>If you are the first to guess, and all the players are perfectly rational, what is the probability that you win the game?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/is-the-price-right/))

## Solution

### Starting from the back

This is basically a territory game. Since the price is random, each player's incentive is to stake out as big a patch of territory as they can without making it unstable. It becomes unstable when it makes more sense for a subsequent player to steal it than to stake out their own territory.

If a player guesses $x \in \left(0, 1\right)$ and nobody else guesses an $x^\prime > x,$ then the player will win if the revealed price is $x$ or greater. In other words, the player would have a probability $1-x$ of winning.

### Protect the throne

Now, if Player 1 chooses $x$ near $0,$ then Player 2 can make a big piece of territory by guessing $x^\prime$ just slightly more than $x.$ This would give Player 1 a chance $\left(x^\prime-x\right)$ of winning, which can be made arbitrarily small. So, they would actually be incentivized to take a smaller piece of territory so that their territory is not appealing to the Player 3, who would have the same opportunity to steal theirs. 

For this reason, Player 1 wants to choose $x$ near $1$. Suppose, for the moment, that Player 1 has chosen $x$ so that it won't be appealing for Player 2 or Player 3 to try and steal it by picking 

$$x^\prime = x + \text{a tiny amount}.$$

Since Player 1's patch is assumed to be unappealing, Player 2 and Player 3 are in a battle for the territory $\left(0,x\right)$ that's up for grabs. Player 2 wants to choose $x^\prime < x$ so that Player 3 is not benefitted by betting $x^{\prime\prime} > x^\prime,$ stealing Player 2's territory. This is so if Player 2 takes exactly half the available territory, i.e. $x^\prime = \frac12 x.$ 

So, both Player 2 and Player 3 have chance $\frac12 x$ to win. 

### A well-balanced throne

Now, we assumed that Player 1 picked their price such that it's not appealing to steal from them. If that's the case, Player 1's chance is at most equal to Player 2 and Player 3's. In other words,

$$1-x = x/2$$

which is solved when $x=2/3,$ giving Player 1 a chance $1-x=1/3$ of winning.

### A note

Because of the tie-breaker condition, which settles the case where everybody guessed higher than the revealed price, Player 3 can actually guess any price between $0$ and $1/3$ without changing their outcome. 


<br>
