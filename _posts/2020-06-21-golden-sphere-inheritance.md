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

On first sight this might seem like a problem in number theory, and perhaps it is. But I, a mere rube, could not crack it on those grounds. So, then, it is a problem in set construction. 

Here I offer my simple approach, translated from the back of a napkin, that can find the minimum number of spheres for partitioning inheritance between $p \leq 6$ beneficiaries, and recover solution sets for $p \leq 5.$ It might be possible to push on these boundaries by exploiting more of the problem's structure.

### Intuition

The basic idea for this algorithm is to go through the list of cubes, left to right, and accumulate them in $p$ sets (that start out empty). If adding the cube to the first set would not bring its mass above the target amount of gold, the cube gets added to the first set, otherwise we try the next set. 

That's basically it. After the first number is placed, we go to the next number and offer it to each set in turn. 

The one wrinkle is that we can reach a dead end this way. Because there's no planning ahead, we might find ourselves in the situation where we can't place a remaining sphere into any set without putting it over the target weight. 

If this happens, then we'd have to reverse the last placement, and move it into the next set. This is our escape hatch, which can go all the way back to the second number placed if need be.

```python
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
        if which_subset == k:
            return False
        
        # If not, then we try to put a number in one of the subsets. If it 
        # would make the subset sum to more than the target, then just move
        # on to the next subset. But if it would fit, then explore that 
        # possibility, and give the fallback move (which is to move on to 
        # the next subset).
        if sum(tmp_subsets[which_subset]) + numbers_left[0] <= target:
            tmp_subsets[which_subset].append(numbers_left[0])
            return (
                    find_partition(tmp_subsets, 0, numbers_left[1:]) 
                    or 
                    find_partition(subsets, which_subset + 1, numbers_left)
                )
        else:
            return find_partition(subsets, which_subset + 1, numbers_left)
```

<br>
