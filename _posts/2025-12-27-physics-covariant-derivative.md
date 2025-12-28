---
layout: post
published: false
title: Covariant derivative
date: 2025/12/27
subtitle: Where does it come form, how do we find it?
tags:
---

>**Question**: How does the directional derivative generalize when the basis vectors can vary?

<!--more-->

## Argument

Take a vector $$ \mathbf{V}(X) = V^i(X) e_i(X) $$ where $e_i(X)$ is the $i^\text{th}$ basis vector. The components of $\mathbf{V}$ can change because the $V^i$ change due to some physical process, or because the basis vectors have changed. 

If we advance along the path, resulting in a shift of $dX$ in the coordinates of the surface, the new vector is $$V^i(X+dX)e_i(X+ dX).$$ Expanding this and subtracting $\mathbf{V}(X)$ we get (Einstein convention implied)

$$ \frac{\partial V^i(X)}{\partial X^j} e_i(X) + V^i(X) \frac{\partial e_i(X)}{\partial X_j}. $$

The derivative of the basis vector $e_i(X)$ with respect to the coordinate $X_j$ can be expressed in terms of a linear combination of the basis vectors at $X,$ e.g. some superposition $\Gamma^k_{ij} e_k(X).$

<br>
