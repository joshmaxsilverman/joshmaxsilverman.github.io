
the discrete strategy is all-or-nothing, so any departure from it will lose a race with discrete competition. the only hope for a dissenter to win is to put fuel on a race that nobody else bets in. any non-zero amount will do, so the dissenter puts a non-zero amount on every race.

the chance that some lane is empty is 

P(lane 1 \setunion lane 2 \setunion lane 3 \setunion lane 4)

P(1v2v3v4) 
= P(1v2v3) + P(4) - P(1v2v3^4)
= P(1v2v3) + P(4) - P((1^4)v(2^4)v(3^4))
= P(1v2) + P(3) - P(1v2^3) + P(4) - (P((1^4)v(2^4)) + P(3^4) - P((1^4^3)v(2^3^4)))
= P(1) + P(2) - P(1^2) + P(3) - P((1^3)v(2^3)) + P(4) - (P(1^4) + P(2^4) - P(1^2^4)) - P(3^4) - (P(1^4^3) + P(2^3^4) - P(1^2^3^4))
= P(1) + P(2) + P(3) + P(4) - (P(1^4) + P(2^4) + P(3^4) + P(1^3) + P(2^3) + P(1^2)) + P(1^2^4) + P(2^3^4) + P(1^3^4) + P(1^2^3) - P(1^2^3^4)

In other words, we sum the probabilities for all single lanes to be empty, then subtract the probability that any two lanes are empty, then add the probability that any three lanes are empty, and so on, up until the chance that (n-1) lanes are empty.  

This is 

$P(a lane empty) = \sum\limits_{i=0}{N-1}\binom{N}{i}(\frac{n-j}{n})^{3n-j}(-1)^{j+1}$
