---
layout: post
published: false
title: Cool weave curve
date: 2023/09/10
subtitle: What shape is the margin doodle?
tags: geometry lines
---

>Question

<!--more-->

([FiveThirtyEight](https://thefiddler.substack.com/p/can-you-bob-and-weave))

## Solution

to get a picture of where the curve comes from, let's draw the construction with a small number of divisions:

![](/img/2023-09-10-plot-lines-start.png){:width="450 px" class="image-centered"}

for example, the first line has the relationship $y = \frac{(1 - 1/N)}{1/N}(x-1/N).$

in general, the $j^\text{th}$ line is 

$$ y_j = \frac{(1-j/N)}{j/N}(x-j/N) $$

each point on the frontier curve is the intersection of two consecutive lines:

![](/img/2023-09-10-plot-fade.png){:width="450 px" class="image-centered"}

this occurs when $y_j(x) = y_{j+1}(x)$ or

$$ \frac{1-j/N}{j/N}(x-j/N) = \frac{1-(j+1)/N}{(j+1)/N}\left[x-(j+1)/N\right]. $$

solving for $x$ in terms of $j$ gives $x = j(j+1)/N^2.$ taking the limit as $N$ goes to infinity and letting $j/N = t$, we get

$$ x = t^2 $$

we can also use this to get $y$ in terms of $t$ 

$$ y = (1-t)^2, $$

which gives us the frontier in parametric form. plotting this along side the lines, we see that it is the shape of the frontier:

![](/img/2023-09-10-final-plot.png){:width="450 px" class="image-centered"}

### Unmasking the curve

but what kind of shape is it?

<br>




