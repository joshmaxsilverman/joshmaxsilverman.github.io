---
layout: post
published: true
title: Hammer golf
date: 2025/04/21
subtitle: Live by the hammer, die by the hammer.
tags: game-theory recursive-games strategy
---

>Question

<!--more-->

([Fiddler on the Proof](URL))

## Solution

on each turn, we need to decide whether to throw the hammer

if we throw the hammer, our opponent will have a choice between accepting it, or rejecting it. they will pick whichever option gives us the least benefit. that means we should only throw the hammer if the minimum value possible is greater than the value of playing a normal $1$ pt hole.

likewise, our opponent will choose to throw the hammer if the maximum of us rejecting or accepting is less than the value of playing a normal hole.

if neither of these result, i.e. rejecting = accepting, then the players will play a normal hole. 

putting this logic to code, we have

```python
def V(score_A, score_B):
  
  if score_A >= TARGET_SCORE:
    return 1
  
  if score_B >= TARGET_SCORE:
    return 0

  B_rejects = V(score_A + 1, score_B)
  A_rejects = V(score_A, score_B + 1)
  accept = 1/2 * (V(score_A + 2, score_B) + V(score_A, score_B + 2))
  normal = 1/2 * (V(score_A + 1, score_B) + V(score_A, score_B + 1))

  A_throws = min(B_rejects, accept) > normal
  B_throws = max(A_rejects, accept) < normal

  if A_throws and B_throws :
    return accept

  if A_throws:
    return min(B_rejects, accept)
  
  if B_throws:
    return max(A_rejects, accept)
  
  else:
    return normal
```

$$
\begin{array}{|c|c|} \hline
 \text{Target score} & V(1,0) \\ \hline
 1 & 1 \\
 2 & \frac12 \\
 3 & \frac34 \\
 4 & \frac12 \\
 5 & \frac{11}{16} \\
 6 & \frac12 \\
 7 & \frac{21}{32} \\
 8 & \frac12 \\
 9 & \frac{163}{256} \\
 10 & \frac12 \\
 11 & \frac{319}{512} \\
 12 & \frac12 \\
 13 & \frac{1255}{2048} \\
 14 & \frac12 \\
 15 & \frac{2477}{4096} \\ \hline
\end{array}
$$


<br>
