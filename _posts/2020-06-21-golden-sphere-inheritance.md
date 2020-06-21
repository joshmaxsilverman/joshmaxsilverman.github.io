---
layout: post
published: true
title: Golden Sphere Inheritance
date: 2020/06/21
---

## Question

>King Auric adored his most prized possession: a set of perfect spheres of solid gold. There was one of each size, with diameters of 1 centimeter, 2 centimeters, 3 centimeters, and so on. Their brilliant beauty brought joy to his heart. After many years, he felt the time had finally come to pass the golden spheres down to the next generation — his three children.
>
>He decided it was best to give each child precisely one-third of the total gold by weight, but he had a difficult time determining just how to do that. After some trial and error, he managed to divide his spheres into three groups of equal weight. He was further amused when he realized that his collection contained the minimum number of spheres needed for this division. How many golden spheres did King Auric have?
>
>Extra credit: How many spheres would the king have needed to be able to divide his collection among other numbers of children: two, four, five, six or even more?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-flip-the-magic-coin/))

## Solution

On first sight it might seem like King Auric has a problem in number theory, and perhaps he does. But I, a mere rube, could not crack it on those grounds. So, then, it is a problem in set construction. 

Here I offer my simple approach, translated from the back of a napkin, that can find the minimum number of spheres for partitioning inheritance between $P \leq 6$ beneficiaries, and recover solution sets for $P \leq 5.$ It might be possible to push on these boundaries by exploiting more of the problem's structure.

### Preliminaries

The weight of each cube is proportional to the cube of its length dimension $M \sim \ell^3,$ so we can just use the cubes of the first $N$ integers $w = \left\\{1^3, 2^3, \ldots, N^3\right\\}$ as a proxy for the set of spheres. If the spheres are divisible into $P$ partitions then their total has to be divisible by $P.$ Also, since each partition sums to $T = \left(\sum w_i\right) / P,$ the heaviest gold sphere has to weigh less than this: $\max\left\\{w_i\right\\} \leq T.$ (if a single sphere is heavier than the target weight for a partition, it won't fit in any partition)

### Intuition

The basic idea for this algorithm is to go through the list of cubes, left to right, and accumulate them in $P$ sets (that start out empty). If adding the cube to the first set would not bring its mass above the target amount of gold, the cube gets added to the first set, otherwise we try the next set. 

That's basically it. After the first number is placed, we go to the next number and offer it to each set in turn. 

`<hand drawing of this strategy>`

The one wrinkle is that we can reach a dead end this way. Because there's no planning ahead, we might find ourselves in the situation where we can't place a remaining sphere into any set without putting it over the target weight. 

If this happens, then we'd have to reverse the last placement, and move it into the next set. This is our escape hatch, which can go all the way back to the second number placed if need be. (By symmetry, it doesn't matter where the first number is placed)

```python
import copy

def find_partition(subsets, which_subset, numbers_left):

    # If all the subsets sum to the target, we're done
    if all([sum(subset) == target for subset in subsets]):
        print(subsets)
        return True

    # If we haven't solved, and there are no numbers left, it means that 
    # this branch won't work
    elif len(numbers_left) == 0:
        return False

    # The first thing here checks if we're beyond the last subset. 
    else:
        if which_subset == P:
            return False
        
        alt_subsets = copy.deepcopy(subsets)
        
        # Try to put a number in one of the subsets. If it would make
        # the subset sum to more than the target, then move on to
        # the next subset. 
        if sum(subsets[which_subset]) + numbers_left[0] > target:
            return find_partition(subsets, which_subset + 1, numbers_left)
            
        # If it would fit, then explore that possibility and give the
        # fallback option of moving on to the next subset.
        else:
            alt_subsets[which_subset].append(numbers_left[0])
            return (find_partition(alt_subsets, 0, numbers_left[1:]) 
                    or 
                    find_partition(subsets, which_subset + 1, numbers_left))
            
```

Run as is, this algorithm will retread old ground. To avoid this, we can store the partial solutions in a dictionary and record when they lead to failure. If we come across that partial solution again we can skip it, avoiding whatever recursion it would have conjured.

Note that reverse sorting the list of cubes promotes early failure, yielding solutions much more quickly.

Running this code for the first few partition sizes produces the minimum collection size for $P$-partition in $\approx 1\text{ s}$ or less for $P < 6$: 

```python
P = 2
[[1728, 729, 512, 64, 8, 1], 
 [1331, 1000, 343, 216, 125, 27]]
To split the inheritance 2 ways, the king needs at least 12 spheres.
Wall time: 1.91 ms
```

```python
P = 3
[[12167, 4913, 3375, 2744, 1331, 729, 125, 8], 
 [10648, 8000, 4096, 1728, 512, 343, 64, 1], 
 [9261, 6859, 5832, 2197, 1000, 216, 27]]
To split the inheritance 3 ways, the king needs at least 23 spheres.
Wall time: 1.09 s
```

```python
P = 4
[[13824, 5832, 2744, 64, 27, 8, 1], 
 [12167, 9261, 729, 343], 
 [10648, 4913, 4096, 1331, 1000, 512], 
 [8000, 6859, 3375, 2197, 1728, 216, 125]]
To split the inheritance 4 ways, the king needs at least 24 spheres.
Wall time: 950 ms
```

```python
P = 5
[[13824, 3375, 729, 64, 8], 
 [12167, 5832, 1], 
 [10648, 4096, 2744, 512], 
 [9261, 6859, 1728, 125, 27], 
 [8000, 4913, 2197, 1331, 1000, 343, 216]]
To split the inheritance 5 ways, the king needs at least 24 spheres.
Wall time: 373 ms
```

For $P = 6$ my laptop ran out of RAM when keeping track of the solution set. By retreating to the mere question solubility, it shows that the minimum for a $6$-way split is $35$ spheres.

Probing below these depths requires more insight and/or RAM than I can provide.

### Uniqueness 

By deleting the `True` return statement, the code will continue printing solutions if there are more. As it turns out, there are multiple $24$-sphere partitions corresponding to the $P=4$ minimum.


<br>
