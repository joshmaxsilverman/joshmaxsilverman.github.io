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

We want to calculate the derivative of a vector $\mathbf{V}$ attached to a point that moves along the surface, in the coordinates of the surface, along some particular direction, at that point.

Take a vector $\mathbf{V}(X) = V^i(X) e_i(X)$ where $e_i(X)$ is the $i^\text{th}$ basis vector. The components of $\mathbf{V}$ can change because the $V^i$ change, due to some physical process, or because the basis vectors have changed due to variation of the surface. 

The basis vectors at each point come from the map from surface coordinates to position in the embedding space: ${\mathbf{r}(X) = \boldsymbol{\gamma}(X)= \langle \gamma_1(X), \gamma_2(X), \ldots, \gamma_d(X)\rangle,}$ so that $e_j = \partial \boldsymbol{\gamma}(X) / \partial X^j.$ This means that the basis vectors are tangent to the surface. It also means that we can freely flip flop derivatives of the basis vectors with respect to surface coordinates like $\partial e_i/\partial X^j \leftrightarrow \partial e_j/\partial X^i.$

If we advance along the path, resulting in a shift of $\Delta X^j$ in the coordinates of the surface, the new vector is $$V^i(X+\Delta X)e_i(X+ \Delta X).$$ Expanding this, subtracting $\mathbf{V}(X),$ and dropping second order terms we get (Einstein convention implied)

$$ \left(\frac{\partial V^i(X)}{\partial X^j} e_i(X) + V^i(X) \frac{\partial e_i(X)}{\partial X^j}\right) \Delta X^j. $$

The first term corresponds to the ordinary Jacobian while the second term is the new stuff corresponding to the variation of the basis vectors. The derivative of the basis vector $e_i(X)$ with respect to the coordinate $X^j$ can be expressed in terms of the basis vectors at $X,$ e.g. some superposition $\Gamma^k_{ij} e_k(X)$ plus some normal component.

Focusing on this, we have, so far

$$ \frac{\partial e_i}{\partial X^j} = \Gamma^k_{ij} e_k + \text{normal}. $$

Now we need to get $\Gamma^k_{ij}$ alone. We can dot both sides by $e_m,$ getting the metric tensor on the right side and killing the normal component

$$
  \begin{align}
    \Gamma^k_{ij} e_m\cdot e_k  &= e_m\cdot \frac{\partial e_i}{\partial X^j} + e_m\cdot \text{normal} \\
       \Gamma^k_{ij}g_{mk} &=e_m\cdot \frac12\left[\frac{\partial e_i}{\partial X^j} + \frac{\partial e_j}{\partial X^i}\right] \\
                           &= \frac12\left[\frac{\partial e_m\cdot e_i}{\partial X^j} + \frac{\partial e_m\cdot e_j}{\partial X^i} - e_i\cdot \frac{\partial e_m}{\partial X^j} - e_j\cdot \frac{\partial e_m}{\partial X^i}\right] \\
     &= \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - e_i\cdot\frac{\partial e_j}{\partial X^m} - e_j\cdot \frac{\partial e_i}{\partial X^m}\right] \\
     &= \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial e_i\cdot e_j}{\partial X^m}\right] \\
     &= \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial g_{ij}}{\partial X^m}\right] \\
     \Gamma^k_{ij} g^{\ell m}g_{mk} &= g^{\ell m} \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial g_{ij}}{\partial X^m}\right] \\
     \Gamma^{\ell}_{ij} &= g^{\ell m} \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial g_{ij}}{\partial X^m}\right]
   \end{align}
$$

Now, switching labels $k\leftrightarrow i,$ we can write the covariant derivative $D_{\Delta X}$ of $\mathbf{V}$ at $X$ in the direction of $\Delta X$ like 

$$ 
  \begin{align}
    D_{\Delta X} \mathbf{V} &= \left(\frac{\partial V^i(X)}{\partial X^j} e_i(X) + V^k(X) \Gamma^i_{kj}e_i(X)\right)\frac{\Delta X^j}{\lvert\Delta X\rvert} \\
                   &= \left(\frac{\partial V^i(X)}{\partial X^j} + V^k(X)\Gamma^i_{kj}\right)e_i(X)\frac{\Delta X^j}{\lvert\Delta X\rvert}.
  \end{align} 
$$

<br>
