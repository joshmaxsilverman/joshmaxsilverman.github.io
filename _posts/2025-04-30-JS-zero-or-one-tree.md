---
layout: post
published: false
title: 
date: 2025/04/30
subtitle:
tags:
---

>**Question**:

<!--more-->

([Fiddler on the Proof](URL))

## Solution

$$ P_\text{zero} = 2p P_\text{zero} - p P^2_\text{zero} $$

$$ P_\text{zero} = 
  \begin{cases} 
    0 & p < \frac12 \\ 
    \frac{2p-1}{p} & p \geq \frac12 
  \end{cases} 
$$

$$ P_\text{either} = 2p P_\text{either} + 2(1-p)P_\text{zero} - p P^2_\text{either} + (1-p)P^2_\text{zero}) $$

$$ P_\text{either} = \dfrac{2 p+\sqrt{\dfrac{4 (p-1)^3}{p}+1}-1}{2 p} $$

$$ 
  \begin{align}
    p_{1/2} &= \dfrac{1}{9} \left(10-\dfrac{4\ 2^{2/3}}{\sqrt[3]{9 \sqrt{57}-67}}+\sqrt[3]{2 \left(9 \sqrt{57}-67\right)}\right) \\ 
                &\approx 0.5306035754 
  \end{align} 
$$

![](/img/2025-04-30-JS-zero-or-one-tree.png){:width="450-px" class="image-centered"}

<br>
