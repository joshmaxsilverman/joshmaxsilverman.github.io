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

Let's go straight to the general case of $n$ players, for some even number $n$.  A strategy is a function from players to sets of $n/2$ numbers from $1$ to $n$. An arrangement is a function from numbers from $1$ to $n$ (numbering the players) to numbers from $1$ to $n$ (numbering the boxes). A strategy wins at an arrangement just in case the arrangement assigns to each player a number that is among those assigned to the player in the strategy.  

Suppose we try the strategy that assigns to each number up to $n/2$ the set of all numbers up to $n/2$ and to each number above $n/2$ the set of all the numbers above $n/2$. Then there will be a winning arrangement for each way of ordering those two sets, for a total of $(n/2)!^2$ arrangements.  For $n=100$, that gives a winning probability that is $12.56$ times that of the naive strategy.

I cannot prove that this is optimal, but it's Sunday night, and it's what I have.

<br>
