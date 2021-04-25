---
layout: post
published: true
title: Election Comeback
date: 2021/04/24
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

The trick we're interested in is for the loser on election night to go on to be the winner when all is said and done. For the case at hand, this means that, on election night, a candidate has less than $\frac12 n_1$ (half of the votes), but gets enough in the mail-ins to end up with over half of the total votes (more than $\frac12 (n_1 + n_2)$). 

$$ P(\text{less than half on election night, but majority overall}) $$

Each person's vote is independent, so the probability that candidate $A$ gets $A_i$ votes total out of a bundle of $n_i$ votes is

$$ P(A_i, n_i) = \binom{n_i}{A_i} p^{A_i} (1-p)^{n_i - A_i}. $$

The overall probability of a comeback is the sum over all possible vote totals $A_1$ and $A_2$ that satisfy the conditions we laid out above:

$$ P(\text{comeback}) = \sum_{A_1, A_2} P(A_1, n_1) \times P(A_2, n_2) $$

### Respect your limits

The greatest number of votes the election night loser can get, yet still go on to win is one less than half the votes counted on election night, ($\frac12 n_1 - 1$). Similarly, the least number of votes that a comeback candidate can get on election night is $1$ more than half the total number of votes minus all the mail-in votes ($1 + \frac12 (n_1 + n_2) - n_2).$

Given $A_1$ votes on election night, the fewest votes the comeback candidate can get in the mail-ins is $A_1$ fewer than one more than half the total votes, $(1 + \frac12 (n_1 + n_2) - A_1).$ The greatest number of votes they can get is just all of the available mail-in votes, $n_2.$

### Add 'em up

Putting this together, we have an answer for a finite voting population

$$ P(\text{comeback}) = \sum_{A_2 = 1 + \frac12(n_1+n_2) - A_1}^{n_2}\,\sum_{A_1 = 1 + \frac12(n_1 + n_2) - n_2}^{\frac12 n_1 - 1} P(A_1, n_1)\times P(A_2 n_2) $$

If, say, our population has $1000$ people, then $n_1 = 800,$ $n_2 = 200,$ and 

$$ P(\text{comeback}) = \tiny\frac{10228020292915174228292240870224890030544326637340935132521177367214743208473786730401876487660637310175022678918158737505982977287662874925635566677634882938221002014757573954807921054044146789133883130652904002543332844051020248652614686489524222103423778501587446415038605879162658486606490588085}{167423219872854268898191413915625282900219501828989626163085998182867351738271269139562246689952477832436667643367679191435491450889424069312259024604665231311477621481628609147204290704099549091843034096141351171618467832303105743111961624157454108040174944963852221369694216119572256044331338563584} $$

<br>
