---
layout: post
published: true
title: Infinite March madness
date: 2025/03/24
subtitle: How often will the $1$-seed make the final four when there are $2^k$ teams in their region?
tags: recursion trees
---

>**Question**: March Madness—the NCAA basketball tournament—is here!
>
>The single-elimination tournament consists of $64$ teams spread across four regions, each with teams seeded $1$ through $16.$ (In recent years, additional teams beyond the $64$ have been added, but you needn’t worry about these teams for this week’s puzzle.)
>
>Suppose in any matchup between teams with seeds $M$ and $N,$ the $M$-seed wins with probability $N/(M+N),$ while the $N$-seed wins with probability $M/(M+N).$ For example, if a $3$-seed plays a $5$-seed, then the $3$-seed wins with probability $5/8,$ while the $5$-seed wins with probability $3/8.$
>
>In one of the brackets, the top four seeds remain (i.e., the $1$-seed, the $2$-seed, the $3$-seed, and the $4$-seed). If case you’re not familiar with how such brackets work, at this point the $1$-seed and $4$-seed face off, as do the $2$-seed and $3$-seed. The winners then play each other.
>
>Instead of $16$ teams in a region, now suppose there are $2^k$ teams, where $k$ is a very large integer.
>
>The teams are seeded $1$ through $2^k$, and play in a traditional seeded tournament format. That is, in the first round, the sum of opponents’ seeds is $2^k+1.$ If the stronger team always advances, then the sum of opponents’ seeds in the second round is $2^{k−1}+1$, and so on. Of course, stronger teams may not always advance, but this convention tells you which seeds can play which other seeds in each round.
>
>For any such region with $2^k$ teams, what is the probability that the $1$-seed emerges victorious from the region?

<!--more-->

([Fiddler on the Proof](URL))

## Solution

This puzzle brings up a practical question for any Duke fan — what is the probability we make the final four when there are $2^k$ worse teams in the way?

The main insight we need to answer this question is that the probability a team makes it to round $(k+1)$ is equal to the probability they beat their opponent in round $k$ times the probability that they and their opponent make it to round $k$, summed over all of their potential round-$k$ opponents.

Looking at the tree structure of the tournament, the potential opponents in round $k$ are all the teams in the opposing subtree at level $k$. If our team of interest is team $j$, and their opponents are indexed by $i$ then this gives us

$$ P(j\,\text{makes level}\, k+1) = P(j\,\text{makes level}\,k)\sum_{i\in\text{opp subtree}} P(i\,\text{makes level}\, k)P(j\,\text{beats}\, i). $$

with the chance any given team makes it to the first level being $1$.

All we have to do is to implement and evaluate this relationship.

## Making the bracket

First, we need to build the playoff bracket which we can do by following the prescription of the problem. Starting at the top, we descend the tree, and assume the best possible teams are facing off at each level. 

Taking a $4$-team bracket for example, at the zeroth level we assume team $1$ has won the tournament. At the first level, we assume team $1$ is playing team $2^1 + 1 - 1 = 2.$ At the second level, on the left side of the tree, we assume team $1$ is playing team $2^2+1-1 = 4$ and that, on the right, team $2$ is playing team $2^2 - 2 = 3.$ 

Implementing this, we get:

```python
def bracket(j, k, d):
    if k == d:
        return ((j,), (2 ** d + 1 - j,))
    else:
        return (bracket(j, k + 1, d) , bracket(2 ** k + 1 - j, k + 1, d))
```

To check, we run it for a $16$-team bracket and get the expected result:

```
(((((1,), (16,)), ((8,), (9,))), (((4,), (13,)), ((5,), (12,)))),
 ((((2,), (15,)), ((7,), (10,))), (((3,), (14,)), ((6,), (11,)))))
```

The probability that team $j$ beats team $i$ is 

```python
def Pbeat(j, i):
  return i / (j + i)
```

Now, we have to implement the recursion from above. Starting at the bottom of the tree, we set the probability of a team making it to the first level to $1$

```python
P = defaultdict(lambda: 0.0)
for j in range(1, 2 ** d+1):
  P[(j, d)] = 1.0
```

Next, we implement the main relationship. We find the probability that team $j$ makes it to level $k$ by adding over all ways they can get there and store the result in a dictionary $P\left[j, k\right]$.

If we are at the leaves of the tree, then we tabulate the probability of each team making it to the next level of the tree (by looping over all possible matchups), and return the concatenation of the two subtrees. Otherwise we descend the tree:

```python
def calc(b, k):
  if type(b[0][0]) is int:
    left, right = b

    for j in left:
      for i in right:
        P[(j,k-1)] += Pbeat(j, i) * P[(i, k)] * P[(j, k)]
        P[(i,k-1)] += Pbeat(i, j) * P[(j, k)] * P[(i, k)]
    
    return left + right
  
  else:
    return (calc(b[0], k+1), calc(b[1], k+1))
```

Finally we loop over the rounds of the tournament

```python
b = bracket(1, 1, d)

for r in range(d):
  b = calc(b, 1)
```

and check inspect the value of $P\left[1,0\right].$ We get

$$
\begin{array}{|c|c|} \hline
d & P\left[1,0\right] \\ \hline
1  & 2/3  \\
2  & 14/25 \\
3  & 0.5279401592158792 \\
4  & 0.5192183551301611 \\
5  & 0.5166943992619705 \\
6  & 0.5158337457249849 \\
7  & 0.5155445666341771 \\
8  & 0.5154592300379053 \\
9  & 0.5154372191498046 \\
10 & 0.5154322958839155 \\
11 & 0.5154314095552358 \\
12 & 0.5154313229728604 \\
13 & 0.5154313454474818 \\
14 & 0.5154313637871086 \\
15 & 0.5154313716456237 \\ \hline
\end{array}
$$

This suggests that the probability of the top-seed winning their region stabilizes somewhere around $\approx 0.515431.$

<br>
