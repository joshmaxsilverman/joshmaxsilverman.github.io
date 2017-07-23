---
layout: post
published: true
title: Castle Spy
date: 2017/07/23
---

>There are two warlords: you and your archenemy, with whom you’re competing to conquer castles and collect the most victory points. Each of the 10 castles has its own strategic value for a would-be conqueror. Specifically, the castles are worth 1, 2, 3, … , 9 and 10 victory points. You and your enemy each have 100 soldiers to distribute between any of the 10 castles. Whoever sends more soldiers to a given castle conquers that castle and wins its victory points. (If you each send the same number of troops, you split the points.) Whoever ends up with the most points wins.
>
>But now, you have a spy! You know how many soldiers your archenemy will send to each castle. The bad news, though, is that you no longer have 100 soldiers — your army suffered some losses in a previous battle.
>
>What is the value of the spy?
<!--more-->
>
>That is, how many soldiers do you need to have in order to win, no matter the distribution of your opponent’s soldiers? Put another way: What k is the minimum number such that, for any distribution of 100 soldiers in the 10 castles by your opponent, you can distribute k soldiers and win the battle?

[(fivethirtyeight.com)](https://fivethirtyeight.com/features/how-much-is-a-spy-worth-in-a-warring-riddler-nation/)

== Solution

As your opponent, knowing you have a spy, how should I allocate my soldiers to make your at-least-28 points costliest? 

An "even-cost" strategy allocates soldiers so that for each castle the cost in soldiers-per-point is the same. In this case, since there are a total of 55 points, and since the cost of your winning at each castle is the number of soldiers I allocate to it plus one, on average over all ten castles the cost is 110/55, or 2 soldiers per point. I can arrange an even-cost situation by sending, to castle number c, 2c-1 soldiers, which uses up all of my soldiers. Your cost of victory will be the 28 points you need times the cost per point of 2 soldiers, for a total of 56 soldiers.

It makes sense that the even-cost strategy is optimal, in the sense of forcing you to spend the greatest number of soldiers, because if I make some castles more expensive than average, other castles have to become bargains, and surely you can then allocate your soldiers to more of the bargain castles than the expensive ones.

But fans of rigorous proofs will recognize that that's not one. Let's try to do better!

Suppose I have a better strategy than the even-cost one. Call "C(n,m,...)" the cost in soldiers for castles n, m, . . . on that strategy. Because we can assume I use all 100 soldiers, the sum of all the costs is 110, and given that this strategy is assumed to be better than the even-cost one, the sum of the costs of any set of castles whose numbers sum to 28 or higher is greater than 56. So in particular, C(1,8,9,10) and C(1,2,3,4,5,6,7) are greater than 56. So we know that, collectively, 1,8,9,10 cost more than average (the average cost remains 2 soldiers per point), and therefore the remaining castles, namely 2,3,4,5,6,7, cost less than average. Similar reasoning establishes that castles 8,9,10 collectively cost less than average, and we can infer that castle 1 costs more than average. In fact castle 1 must cost at least 4 soldiers, because both sets of castles 2,3,4,5,6,7 and 8,9,10 must be short at least one soldier each from the average cost, and those 2 or more extra soldiers must be assigned to castle 1's cost.

C(2,8,9,10) must be greater than 56, and so C(2) must be at least 4 (that is, average or greater) to make up for C(8,9,10)'s soldier shortfall by at least 2 soldiers. So 3,4,5,6,7 must collectively cost less than average.

Since castles 8,9,10 collectively cost less than average, the same must be true of at least one pair of those three castles. 

Suppose first that that pair is 9,10. Then any pair from 2,3,4,5,6,7 that sums to 9 (2,7 or 3,6 or 4,5) must cost at least 2 soldiers more than average. But then 2,3,4,5,6,7 costs at least 6 soldiers more than average. Contradiction! 

Suppose instead that 8,9 costs less than average. Then the pairs 4,7 and 5,6 cost at least two soldiers more than average, meaning that castle 3 costs at least five soldiers less than average---that is, it costs 1 soldier. But then 3,8,9,10 costs less than 56 soldiers, despite summing to 30 points. Contradiction! 

Finally, suppose 8,10 costs less than average.  Then the pairs 3,7 and 6,4 each cost at least two soldiers more than average, and so castle 5 costs at least five soldiers less than average---that is, it costs 5 soldiers or less. For 5,7,8,10 to cost more than 56 soldiers, castle 7 must cost at least 17 soldiers, or 3 more than average, and for 5,6,8,10 to cost more than 56, castle 6 must also cost at least 17 soldiers, or 5 more than average. Since, together, castles 6 and 7 cost at least 8 more than average, 3,4,5 must together cost at least 9 less than average. Then, 3,4,5,8,10, which sums to 30 points, costs at least 10 soldiers less than its average cost of 60, that is, those castles can be won with 50 or fewer soldiers. Contradiction!

Therefore our supposition, that there's a better strategy for me as your opponent than the even-cost one, is false.

<br>
