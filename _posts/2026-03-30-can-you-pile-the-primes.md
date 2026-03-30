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
---

> **Question**: Suppose you want to make two groups with equal sums using the first $N_2$ prime numbers. What is the smallest value of $N_2$ for which you can do this?
#
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
# go one bucket at a time filling with numbers
# if bucket hits the target, move on to the next one and add current bucket to list of buckets
# if bucket goes over the target, take current number out and try next one
# at the end, the final bucket is the numbers left over

from sympy import prime
from random import shuffle

N = 10
UPPER = 51

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

    if k == N-1 and sum(numbers[j] for j in range(UPPER) if not used[j]) == TARGET:
        buckets.append([numbers[j] for j in range(UPPER) if not used[j]])
        return True

    if current_sum == TARGET:

        buckets.append(current_bucket)
        current_bucket = []
        
        if solve(0, k+1, 0):
            return True
        
        current_bucket = buckets.pop()
        return False

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
        print(f"Bucket {j}: {b}")
```
