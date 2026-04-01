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

The state space for this problem is enormous, so we need to be careful about how we search it. Absent any planning, we are contending with $N!$ factorial possible assignments of primes to groups. Due to this, any kind of graph search or dynamic programming approach is going to take a very long time to descend to a leaf, simply because the search tree is so wide. 

If we could bail out of the search tree as soon as it was clear we were in a dead end, we could turn the tree into something more manageable, like a bush. We know that each bin has to sum to the same value, so if we ever go over that value, we know that we're in a dead end. 

The logic of this approach is to fill the bins with numbers, in order, one by one. If at any point the bin we're in is over the target, we know that any solutions that start with that string of numbers can't possibly work. That means we can take out the last number we tried to insert, and replace it with the next untried number, carrying on until we hit another dead end. If we follow this approach systematically, we will find a solution so long as it exists, and our short circuiting sufficiently reduces the depth of the tree.

It is important to realize, that if we tried to do this by finding bins for numbers, instead of finding numbers for bins, we would cut off dead branches much too late to be efficient.

Before we program anything, we can follow the algorithm in a concrete example. Suppose we start with the numbers below, in the given order, and are trying to make three groups with equal sums. 

```
Target is 43.0
Numbers are [23, 5, 17, 2, 11, 7, 13, 19, 29, 3]
```

To start, we fill the first bucket with numbers one at a time. This increases the sum from $23$ to $28.$ We can't add $17$ to this bucket without exceeding the target sum of $43$ so we skip it and add the next workable number, $2.$ We then try $11$ from which we are stuck, so we take it back out and try $7.$ Carrying on like this we eventually find $13,$ completing the bucket.


```
Current bucket: []
Current bucket: [23]
Current bucket: [23, 5]
Current bucket: [23, 5, 2]
Current bucket: [23, 5, 2, 11]
BACKTRACK
Current bucket: [23, 5, 2]
Current bucket: [23, 5, 2, 7]
Current bucket: [23, 5, 2, 7, 3]
BACKTRACK
Current bucket: [23, 5, 2, 7]
BACKTRACK
Current bucket: [23, 5, 2]
Current bucket: [23, 5, 2, 13]
```

Since $23+5+2+13$ equals the target amount $43,$ we start filling the next bucket back at the start of the list, skipping the numbers we've already used.
We add the unused numbers one at a time until we exceed the target sum with `[17, 11, 7, 3]` which sums to $38.$ This is the end of the line so we're forced to backtrack, going all the way back down to $17$ and trying a new second number. 

```
Bucket 0: [23, 5, 2, 13]
Current bucket: []
Bucket 0: [23, 5, 2, 13]
Current bucket: [17]
Bucket 0: [23, 5, 2, 13]
Current bucket: [17, 11]
Bucket 0: [23, 5, 2, 13]
Current bucket: [17, 11, 7]
Bucket 0: [23, 5, 2, 13]
Current bucket: [17, 11, 7, 3]
BACKTRACK
Current bucket: [17, 11, 7]
BACKTRACK
Current bucket: [17, 11]
Bucket 0: [23, 5, 2, 13]
Current bucket: [17, 11, 3]
BACKTRACK
Current bucket: [17, 11]
BACKTRACK
Current bucket: [17]
```

From there we have an easier go of things and, adding the next two unused numbers $7$ and $19$ to the current bucket we complete the target sum. 

```
Bucket 0: [23, 5, 2, 13]
Current bucket: [17, 7]
Bucket 0: [23, 5, 2, 13]
Current bucket: [17, 7, 19]
Bucket 0: [23, 5, 2, 13]
Bucket 1: [17, 7, 19]
Current bucket: []
Bucket 0: [23, 5, 2, 13]
Bucket 1: [17, 7, 19]
Bucket 2: [11, 29, 3]
```

Because the numbers filled in so far are two thirds of the sum of the original list, we're guaranteed that the leftover numbers will hit the target sum. 

To solve the problem, we can just run this algorithm for a given $N_j$ and a trial upper bound on the primes to use. If no solution returns it means that there is no equal partition for the primes at hand. But if there are solutions for the given upper bound, there are likely to be many of them. 

Practically, for larger values of $N,$ I used several minutes as a proxy for "no solution returns" rather than wait for what still amounts to exhaustive search.

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


For a value of $N_6$ to be a candidate, the sum $\sum_{j=1}^{N_6} p_j$ must be divisible by $6.$ The first value for which this is true is $57$ and, as it happens, this is a workable combo. If we run the algorithm above, we get the following (one of many such) solution:

```
Bucket 1: [149, 103, 109, 61, 37, 43, 127, 3, 83, 19, 13, 173, 199, 7, 2, 17]
Bucket 2: [29, 179, 223, 269, 197, 67, 5, 23, 41, 11, 101]
Bucket 3: [241, 251, 151, 131, 211, 113, 47]
Bucket 4: [229, 193, 227, 239, 97, 71, 89]
Bucket 5: [233, 257, 157, 31, 137, 59, 79, 139, 53]
Bucket 6: [73, 107, 263, 191, 163, 167, 181]
```



