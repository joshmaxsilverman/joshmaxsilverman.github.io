---
layout: post
published: true
title: Infinite March madness
date: 2025/03/24
subtitle: How often will Duke get to the final four when there are $2^k$ teams?
tags: recursion trees
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

the chance player j makes it to level k+1 is the chance they make it to level k times the sum of the chance player i makes it to level k, times the chance they beat player i, over all players i in the other subtree:

$$ P(j\,\text{makes it to level}\, k+1) = P(j\,\text{makes it to level}\,k)\sum_{i\in\text{opp leaf}} P(i\,\text{makes it to level}\, k)P(j\,\text{beats}\, i). $$

with the chance anyone makes it to the first level being $1$.

## Making the bracket

first, we need to build the playoff bracket. to do this, we can follow the prescription in the problem. as we descend the tree, we always assume the best possible teams are facing off. 

taking a $4$-team bracket for example, at the zeroth level we assume team $1$ has won the tournament. at the first level, we assume team $1$ is playing team $2^1 + 1 - 1 = 2.$ at the second level, on the left side of the tree, we assume team $1$ is playing team $2^2+1-1 = 4$, and on the right, team $2$ is playing team $2^2 - 2 = 3.$ 

we can implement this algorithm in Python:

```python
def bracket(j, k, d):
    if k == d:
        return ((j,), (2 ** d + 1 - j,))
    else:
        return (bracket(j, k + 1, d) , bracket(2 ** k + 1 - j, k + 1, d))
```

running it for a $16$-team bracket, we get the expected result

```
(((((1,), (16,)), ((8,), (9,))), (((4,), (13,)), ((5,), (12,)))),
 ((((2,), (15,)), ((7,), (10,))), (((3,), (14,)), ((6,), (11,)))))
```

likewise, the probability that team $j$ beats team $i$ is 

```python
def Pbeat(j, i):
  return i / (j + i)
```

now, we have to implement the definition of probability from above. starting at the bottom of the tree, we set the probability of any team making it to the first level to $1$

```python
P = defaultdict(lambda: 0.0)
for j in range(1, 2 ** d+1):
  P[(j, d)] = 1.0
```

next, we implement the main recursion. we have to find the probability that team $j$ makes it to level $k$ by adding over all ways team $j$ can get to level $k$, and store the result in a dictionary $P\left[j, k\right]$.

in the same pass, we join adjacent leaves of the tree so that we can calculate the next level of ascent. 

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

finally we loop over the rounds of the tournament

```python
b = bracket(1, 1, d)

for r in range(d):
  b = calc(b, 1)
```

which results in

$$
\begin{array}{c|c}
d & \text{P(1\,\\text{wins})} \\ \hline
1  & 0.6666666666666666  \\
2  & 0.56 \\
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
15 & 0.5154313716456237
\end{array}
$$

this suggests that the probability of the top-seed winning their region stabilizes somewhere around $\approx 0.515431.$

<br>
