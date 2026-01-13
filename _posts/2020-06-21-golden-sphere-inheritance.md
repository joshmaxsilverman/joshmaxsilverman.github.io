---
layout: post
published: true
title: Golden sphere inheritance
date: 2020/06/21
subtitle: How do you split a solid gold sphere fairly?
source: fivethirtyeight
theme: algorithms
---

>**Question**: King Auric's collection of unique golden spheres of integer radius $\left(1\text{ cm}, 2\text{ cm}, \ldots\right)$ is the object of his covetous children's eyes. To stave off fratri- and regicide, he will divide the gold up evenly by weight and bequeath an equal share unto each. He has the minimum number needed to do this. How many spheres does he have if he has $3$ children? What if he has $C = \\{2,3,4,5,6,\ldots\\}$ children?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-flip-the-magic-coin/))

## Solution

On first sight it might seem like King Auric has a problem in number theory, and perhaps he does. But I, a mere rube, could not crack it on those grounds. So, then, it is a problem in set construction. 

Here I offer my simple approach, translated from the back of a napkin, that can find the minimum number of spheres for partitioning inheritance between $C \leq 6$ beneficiaries, and recover solution sets for $C \leq 5.$ It might be possible to push on these boundaries by exploiting more of the problem's structure.

### Preliminaries

The weight of each cube is proportional to the cube of its length dimension $M \sim \ell^3,$ so we can just use the cubes of the first $N$ integers $w = \left\\{1^3, 2^3, \ldots, N^3\right\\}$ as a proxy for the set of spheres. If the spheres are divisible into $C$ partitions then their total has to be divisible by $C.$ Also, since each partition sums to $T = \left(\sum w_i\right) / C,$ the heaviest gold sphere has to weigh less than this: $\max\left\\{w_i\right\\} \leq T.$ (if a single sphere is heavier than the target weight for a partition, it won't fit in any partition)

### Intuition

The basic idea for this algorithm is to go through the list of spheres, left to right, and accumulate them in $C$ sets (that start out empty). If adding a given sphere to the first set would not bring its mass above the target amount of gold, the sphere gets added to the first set, otherwise we try the next set. 

That's basically it. After the first sphere is placed, we go to the next sphere and offer it to each set in turn. 

![](/img/2020-06-21-gold-sphere-inheritance.jpg){:width="450px" class="image-centered"}

{:.caption}
**Diagram 1** Finding a $3$-partition for the $N=6$ numbers $\\{3,4,1,2,2,3\\}$. Since the sum is $15$, the target sum for each subset is $5$. The algorithm starts by placing $3$ in the first set, then tries to palce $4$ there but can't, so puts it in the second set. $1$ can fit in the first set along with $3$. The first $2$ can't fit in the first or second buckets so it goes in the third. The second $2$ also goes in the third but then the $3$ can't go anywhere. Now the algorithm backtracks, all the way to the last point where it had freedom of action. As everything after the $1$ was a forced placement, it goes back to when that move was made, and tries its second option, to pair with the $4$ in the second set. From here on out, the normal operation of the algorithm finds a $3$-partition with no difficulties.


The one wrinkle is that we can reach a dead end this way. Because there's no planning ahead, we might find ourselves in the situation where we can't place a remaining sphere into any set without putting it over the target weight. 

If this happens, then we'd have to reverse the last free placement, and move it into the next set. This is our escape hatch, which can go all the way back to the second number placed if need be. (By symmetry, it doesn't matter where the first number is placed)

Translating this strategy into Python produces the recursive function `partition` below. It keeps track of the set of subsets it's building (`subsets`), which subset it's currently working on (`which_subset`), and the numbers it has yet to insert (`numbers_left`). The initial call is `partition([[] for _ in range(P)], 0, numbers)`. If there's a partition, it returns `True` and prints the first one it finds. If there isn't, it returns `False`.

```python
import copy

C = 3
N = 23

numbers = [_**3 for _ in range(1, N+1)]
numbers = numbers[::-1]

target = sum(numbers) / C

def partition(subsets, which_subset, numbers_left):

    # If all the subsets sum to the target, we're done.
    if all([sum(subset) == target for subset in subsets]):
        print(subsets)
        return True

    # If we haven't solved, and there are no numbers left, it means that 
    # this branch won't work.
    elif len(numbers_left) == 0:
        return False

    # Check if we're beyond the last subset. 
    else:
        if which_subset == C:
            return False
        
        alt_subsets = copy.deepcopy(subsets)
        
        # Try to put a number in one of the subsets. If it would make
        # the subset sum to more than the target, then move on to
        # the next subset. 
        if sum(subsets[which_subset]) + numbers_left[0] > target:
            return partition(subsets, which_subset + 1, numbers_left)
            
        # If it would fit, then explore that possibility and give the
        # fallback option of moving on to the next subset.
        else:
            alt_subsets[which_subset].append(numbers_left[0])
            return (partition(alt_subsets, 0, numbers_left[1:]) 
                    or 
                    partition(subsets, which_subset + 1, numbers_left))
            
```

Run as is, this algorithm will retread old ground. To avoid this, we can [store the partial solutions in a dictionary](https://colab.research.google.com/drive/1uZMELQpizLXaPSJtp9gDMMNhR9xUBq7T#scrollTo=v1R2b2QpOz-h) and record when they lead to failure. If we come across that partial solution again we can skip it, avoiding whatever recursion it would have conjured.

Note that reverse sorting the list of cubes promotes early failure, yielding solutions much more quickly.

### Results

Running this code for the first few partition sizes produces the minimum collection size for $C$-partition in $\approx 1\text{ s}$ or less for $C < 6$: 

```python
C = 2
[[1728, 729, 512, 64, 8, 1], 
 [1331, 1000, 343, 216, 125, 27]]
To split the inheritance 2 ways, the king needs at least 12 spheres.
Wall time: 1.91 ms
```

```python
C = 3
[[12167, 4913, 3375, 2744, 1331, 729, 125, 8], 
 [10648, 8000, 4096, 1728, 512, 343, 64, 1], 
 [9261, 6859, 5832, 2197, 1000, 216, 27]]
To split the inheritance 3 ways, the king needs at least 23 spheres.
Wall time: 1.09 s
```

```python
C = 4
[[13824, 5832, 2744, 64, 27, 8, 1], 
 [12167, 9261, 729, 343], 
 [10648, 4913, 4096, 1331, 1000, 512], 
 [8000, 6859, 3375, 2197, 1728, 216, 125]]
To split the inheritance 4 ways, the king needs at least 24 spheres.
Wall time: 950 ms
```

```python
C = 5
[[13824, 3375, 729, 64, 8], 
 [12167, 5832, 1], 
 [10648, 4096, 2744, 512], 
 [9261, 6859, 1728, 125, 27], 
 [8000, 4913, 2197, 1331, 1000, 343, 216]]
To split the inheritance 5 ways, the king needs at least 24 spheres.
Wall time: 373 ms
```

For $C = 6$ my laptop ran out of RAM when keeping track of the solution set. By retreating to the mere question of solubility, it shows that the minimum for a $6$-way split is $35$ spheres.

$$\begin{array}{c|c}
C & N_\text{min} \\ \hline
2 & 12 \\
3 & 23 \\
4 & 24 \\
5 & 24 \\
6 & 35 \\
7 & \text{???}
\end{array}$$

Probing below these depths requires more insight and/or RAM than I can provide.

### Uniqueness 

By deleting the `True` return statement, the code will continue printing solutions if there are more. As it turns out, there are multiple $24$-sphere partitions corresponding to the $C=4$ minimum.


<br>
