---
layout: post
published: true
title: Candy Bars
date: 2019/11/09
---

>Now that Halloween has come and gone, your chances of getting free candy have similarly disappeared. Desperate for sugar, you wander into the candy store, where three kinds of candy are being sold: Almond Soys (yummy, sounds vegan!), Butterflingers and Candy Kernels.
>
>You’d like to buy at least one candy and at most 100, but you don’t care precisely how many you get of each or how many you get overall. So you might buy one of each, or you might buy 30 Almond Soys, six Butterflingers and 64 Candy Kernels. As long as you have somewhere between one and 100 candies, you’ll leave the store happy.
>
>But as a member of Riddler Nation, you can’t help but wonder: How many distinct ways are there for you to make your candy purchase?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-many-ways-can-you-raid-the-candy-shop/))

## Solution

This is a [stars and bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)) problem, where we're in essence asking, how many sequences of $m$ integers sum to $n$? It might seem that our problem isn't that one, or is really $100$ such problems, because we have to take into account all candy totals from $1$ to $100$. However, if we add into consideration the number of additional candies that would be needed to reach $100$ we find ourselves looking at not three but four numbers, with the same sum every time. 

Call the types of candy $A$, $B$, and $C$. Here's how you'll make your purchasing decision. You have a container with $103$ candy slots in a row, and you have three pennies to use as separators between the different types of candy. Each penny gets its own slot. You will buy as many $A$s as there are slots to the left of the leftmost penny, as many $B$s as slots between the two leftmost pennies, as many $C$s as slots between the two rightmost pennies, and any slots to the right of all three pennies will stay empty. There are $103 \choose 3$ ways of choosing slots for the pennies, one of which we eliminate because it results in purchasing no candy, so our answer is ${103 \choose 3} - 1$, or $176,850$.

<br>
