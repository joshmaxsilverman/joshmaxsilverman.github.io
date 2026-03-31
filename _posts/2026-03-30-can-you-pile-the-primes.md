---
layout: post
published: true
title: Can you pile the primes?
date: 2026/03/30
subtitle: Can you send your six children home with the same weight of primes in their number bags?
tags: backtracking
source: fiddler
kind: puzzle
theme: algorithms
hide_from_recent : true
---

> **Question**: Suppose you want to make two groups with equal sums using the first $N_2$ prime numbers. What is the smallest value of $N_2$ for which you can do this?
>
>The answer is three! (Clearly, that wasn’t actually the puzzle.)
>
>The first three primes are $2,$ $3,$ and $5,$ and you can split them up into two sets: $\{2, 3\}$ and $\{5\}.$ Sure enough, $2 + 3 = 5.$ 
>
>Your puzzle involves making three groups with equal sums using the first $N_3$ prime numbers. What is the smallest value of $N_3$ for which you can do this?
>
>**Extra Credit**
>Now you want to make six groups with equal sums using the first $N_6$ prime numbers. What is the smallest value of $N_6$ for which you can do this?


<!--more-->

## Solution

the logic of this approach is to try to fill the bins one by one. if a bin goes overweight, we take a number out and try the next one. if we can't get a bin to the target weight, we go back to the last bin and try to hit the target weight with a different combination of numbers, hopefully opening up flexibility for the remaining bins. 

if you try to do this by finding bins for numbers, instead of finding numbers for bins, it takes much longer to prune unworkable branches from the tree.


```python
from sympy import prime
from random import shuffle

# go one bucket at a time filling with numbers
# if bucket hits the target, move on to the next one and add current bucket to list of buckets
# if bucket goes over the target, take current number out and try next one
# at the end, the final bucket is the numbers left over

N, UPPER = 6, 57

numbers = [ prime(j) for j in range(1, UPPER + 1) ]
shuffle(numbers)
TARGET = sum(numbers) / N
used = [ False for j in range(UPPER) ]

buckets = []
current_bucket = []

print(f"Target is {TARGET}")
    
def solve(i, k, current_sum):
    
    global buckets
    global current_bucket

    unused = [ numbers[j] for j in range(UPPER) if not used[j] ]

    # the end
    if k == N - 1 and sum(unused) == TARGET:
        buckets.append(unused)
        return True

    # log a completed bucket
    if current_sum == TARGET:

        buckets.append(current_bucket)
        current_bucket = []
        
        if solve(0, k + 1, 0):
            return True
        
        current_bucket = buckets.pop()
        return False

    # try a number
    for j in range(i, UPPER):
        if not used[j] and current_sum + numbers[j] <= TARGET:
            
            used[j] = True
            current_bucket.append(numbers[j])

            if solve(j + 1, k, current_sum + numbers[j]):
                return True
            
            current_bucket.pop()
            used[j] = False

    return False
    

if solve(0, 0, 0):
    print('Yes.')
    for j, b in enumerate(buckets):
        print(f"Bucket {1 + j}: {b}")
```


for a value of $N_6$ to be a candidate, the sum $\sum_{j=1}^{N_6} p_j$ must be divisible by $6.$ the first value for which this is true is $57.$ as it happens, this is a workable combo and if we run the algorithm below, we get the following (one of many such) solution:

```
Bucket 1: [149, 103, 109, 61, 37, 43, 127, 3, 83, 19, 13, 173, 199, 7, 2, 17]
Bucket 2: [29, 179, 223, 269, 197, 67, 5, 23, 41, 11, 101]
Bucket 3: [241, 251, 151, 131, 211, 113, 47]
Bucket 4: [229, 193, 227, 239, 97, 71, 89]
Bucket 5: [233, 257, 157, 31, 137, 59, 79, 139, 53]
Bucket 6: [73, 107, 263, 191, 163, 167, 181]
```

likewise, for $N_3$ we can run the same algorithm and find a solution, which is first possilbe when $N_3 = 10$:

```
Bucket 1: [2, 13, 23, 5]
Bucket 2: [11, 29, 3]
Bucket 3: [17, 7, 19]
```

let's walk through the algorithm for $N_3=10$ and a target of $43.$ 

```
Target is 43.0
Current bucket: []
Current bucket: [2]
Current bucket: [2, 3]
Current bucket: [2, 3, 5]
Current bucket: [2, 3, 5, 7]
Current bucket: [2, 3, 5, 7, 11]
Current bucket: [2, 3, 5, 7, 11, 13]
BACKTRACK
Current bucket: [2, 3, 5, 7, 11]
BACKTRACK
Current bucket: [2, 3, 5, 7]
Current bucket: [2, 3, 5, 7, 13]
BACKTRACK
Current bucket: [2, 3, 5, 7]
Current bucket: [2, 3, 5, 7, 17]
BACKTRACK
Current bucket: [2, 3, 5, 7]
Current bucket: [2, 3, 5, 7, 19]
BACKTRACK
Current bucket: [2, 3, 5, 7]
Current bucket: [2, 3, 5, 7, 23]
BACKTRACK
Current bucket: [2, 3, 5, 7]
BACKTRACK
Current bucket: [2, 3, 5]
Current bucket: [2, 3, 5, 11]
Current bucket: [2, 3, 5, 11, 13]
BACKTRACK
Current bucket: [2, 3, 5, 11]
Current bucket: [2, 3, 5, 11, 17]
BACKTRACK
Current bucket: [2, 3, 5, 11]
Current bucket: [2, 3, 5, 11, 19]
BACKTRACK
Current bucket: [2, 3, 5, 11]
BACKTRACK
Current bucket: [2, 3, 5]
Current bucket: [2, 3, 5, 13]
Current bucket: [2, 3, 5, 13, 17]
BACKTRACK
Current bucket: [2, 3, 5, 13]
Current bucket: [2, 3, 5, 13, 19]
BACKTRACK
Current bucket: [2, 3, 5, 13]
BACKTRACK
Current bucket: [2, 3, 5]
Current bucket: [2, 3, 5, 17]
BACKTRACK
Current bucket: [2, 3, 5]
Current bucket: [2, 3, 5, 19]
BACKTRACK
Current bucket: [2, 3, 5]
Current bucket: [2, 3, 5, 23]
BACKTRACK
Current bucket: [2, 3, 5]
Current bucket: [2, 3, 5, 29]
BACKTRACK
Current bucket: [2, 3, 5]
BACKTRACK
Current bucket: [2, 3]
Current bucket: [2, 3, 7]
Current bucket: [2, 3, 7, 11]
Current bucket: [2, 3, 7, 11, 13]
BACKTRACK
Current bucket: [2, 3, 7, 11]
Current bucket: [2, 3, 7, 11, 17]
BACKTRACK
Current bucket: [2, 3, 7, 11]
Current bucket: [2, 3, 7, 11, 19]
BACKTRACK
Current bucket: [2, 3, 7, 11]
BACKTRACK
Current bucket: [2, 3, 7]
Current bucket: [2, 3, 7, 13]
Current bucket: [2, 3, 7, 13, 17]
BACKTRACK
Current bucket: [2, 3, 7, 13]
BACKTRACK
Current bucket: [2, 3, 7]
Current bucket: [2, 3, 7, 17]
BACKTRACK
Current bucket: [2, 3, 7]
Current bucket: [2, 3, 7, 19]
BACKTRACK
Current bucket: [2, 3, 7]
Current bucket: [2, 3, 7, 23]
BACKTRACK
Current bucket: [2, 3, 7]
Current bucket: [2, 3, 7, 29]
BACKTRACK
Current bucket: [2, 3, 7]
BACKTRACK
Current bucket: [2, 3]
Current bucket: [2, 3, 11]
Current bucket: [2, 3, 11, 13]
BACKTRACK
Current bucket: [2, 3, 11]
Current bucket: [2, 3, 11, 17]
BACKTRACK
Current bucket: [2, 3, 11]
Current bucket: [2, 3, 11, 19]
BACKTRACK
Current bucket: [2, 3, 11]
Current bucket: [2, 3, 11, 23]
BACKTRACK
Current bucket: [2, 3, 11]
BACKTRACK
Current bucket: [2, 3]
Current bucket: [2, 3, 13]
Current bucket: [2, 3, 13, 17]
BACKTRACK
Current bucket: [2, 3, 13]
Current bucket: [2, 3, 13, 19]
BACKTRACK
Current bucket: [2, 3, 13]
Current bucket: [2, 3, 13, 23]
BACKTRACK
Current bucket: [2, 3, 13]
BACKTRACK
Current bucket: [2, 3]
Current bucket: [2, 3, 17]
Current bucket: [2, 3, 17, 19]
BACKTRACK
Current bucket: [2, 3, 17]
BACKTRACK
Current bucket: [2, 3]
Current bucket: [2, 3, 19]
BACKTRACK
Current bucket: [2, 3]
Current bucket: [2, 3, 23]
BACKTRACK
Current bucket: [2, 3]
Current bucket: [2, 3, 29]
BACKTRACK
Current bucket: [2, 3]
BACKTRACK
Current bucket: [2]
Current bucket: [2, 5]
Current bucket: [2, 5, 7]
Current bucket: [2, 5, 7, 11]
Current bucket: [2, 5, 7, 11, 13]
BACKTRACK
Current bucket: [2, 5, 7, 11]
Current bucket: [2, 5, 7, 11, 17]
BACKTRACK
Current bucket: [2, 5, 7, 11]
BACKTRACK
Current bucket: [2, 5, 7]
Current bucket: [2, 5, 7, 13]
BACKTRACK
Current bucket: [2, 5, 7]
Current bucket: [2, 5, 7, 17]
BACKTRACK
Current bucket: [2, 5, 7]
Current bucket: [2, 5, 7, 19]
BACKTRACK
Current bucket: [2, 5, 7]
Current bucket: [2, 5, 7, 23]
BACKTRACK
Current bucket: [2, 5, 7]
Current bucket: [2, 5, 7, 29]
Bucket 0: [2, 5, 7, 29]
Current bucket: []
Bucket 0: [2, 5, 7, 29]
Current bucket: [3]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 11]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 11, 13]
BACKTRACK
Current bucket: [3, 11]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 11, 17]
BACKTRACK
Current bucket: [3, 11]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 11, 19]
BACKTRACK
Current bucket: [3, 11]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 11, 23]
BACKTRACK
Current bucket: [3, 11]
BACKTRACK
Current bucket: [3]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 13]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 13, 17]
BACKTRACK
Current bucket: [3, 13]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 13, 19]
BACKTRACK
Current bucket: [3, 13]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 13, 23]
BACKTRACK
Current bucket: [3, 13]
BACKTRACK
Current bucket: [3]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 17]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 17, 19]
BACKTRACK
Current bucket: [3, 17]
Bucket 0: [2, 5, 7, 29]
Current bucket: [3, 17, 23]
Bucket 0: [2, 5, 7, 29]
Bucket 1: [3, 17, 23]
Current bucket: []
Yes.
Bucket 0: [2, 5, 7, 29]
Bucket 1: [3, 17, 23]
Bucket 2: [11, 13, 19]
```