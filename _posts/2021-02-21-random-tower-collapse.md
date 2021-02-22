---
layout: post
published: false
title: 
date: 2021/02/21
---

>**Question**:

<!--more-->

([FiveThirtyEight](URL))

## Solution

the basic concept here is that when the center of mass of an "object" is between the edges of the surface it rests on, then it won't topple. if this is true at every level of the tower, then the whole tower will be stable. 

with each new block that's added, there is the potential for a center of mass to move outside the bounds of the surface it rests upon at any level of the tower (above the first block), so we have to keep track of the .

```python
def running_mean(lst):
    L = len(lst)
    return sum((L-i)*lst[i] for i in range(L)) / L

def new_offset():
  return random.uniform(-1/2, +1/2)

def round():
    offsets = [new_offset()]
    (blocks, topple) = (2, False)
    
    while not topple:
        offsets.append(new_offset())
        means = [running_mean(offsets[_:]) for _ in range(len(offsets))]
        blocks += 1
        if any(abs(_) > 0.5 for _ in means):
            topple = True
            
    return blocks
```

<br>
