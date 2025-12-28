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

Take a vector $$ \mathbf{V}(X) = V^i(X) e_i(X) $$ where $e_i(X)$ is the $i^\text{th}$ basis vector. The components of $\mathbf{V}$ can change because the $V^i$ change, due to some physical process, or because the basis vectors have changed due to variation of the surface. 

If we advance along the path, resulting in a shift of $dX$ in the coordinates of the surface, the new vector is $$V^i(X+\Delta X)e_i(X+ \Delta X).$$ Expanding this, subtracting $\mathbf{V}(X),$ and dropping second order terms we get (Einstein convention implied)

$$ \left(\frac{\partial V^i(X)}{\partial X^j} e_i(X) + V^i(X) \frac{\partial e_i(X)}{\partial X_j}\right) \Delta X. $$

The first term corresponds to the ordinary Jacobian while the second term is the new stuff corresponding to the variation of the basis vectors. The derivative of the basis vector $e_i(X)$ with respect to the coordinate $X_j$ can be expressed in terms of the basis vectors at $X,$ e.g. some superposition $\Gamma^k_{ij} e_k(X).$

Focusing on this, we have, so far

$$ \frac{\partial e_i}{\partial X_j} = \Gamma^k_{ij} e_k. $$

Now we need to get $\Gamma^k_{ij}$ alone. We can multiply both sides by $e_m,$ getting the metric tensor on the right side

$$
  \begin{align}
     e_m \Gamma^k_{ij} e_k  &= e_m\frac{\partial e_i}{\partial X^j} \\
       \Gamma^k_{ij}e_m e_k &=e_m \frac12\left[\frac{\partial e_i}{\partial X^j} + \frac{\partial e_j}{\partial X^i}\right] \\
      \Gamma^k_{ij} g_{mk} &= \frac12\left[\frac{\partial e_me_i}{\partial X^j} + \frac{\partial e_me_j}{\partial X^i} - e_i\frac{\partial e_m}{\partial X^j} - e_j\frac{\partial e_m}{\partial X^i}\right] \\
     &= \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - e_i\frac{\partial e_j}{\partial X^m} - e_j\frac{\partial e_i}{\partial X^m}\right] \\
     &= \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial e_ie_j}{\partial X^m}\right] \\
     &= \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial g_{ij}}{\partial X^m}\right] \\
     \Gamma^k_{ij} g^{\ell m}g_{mk} &= g^{\ell m} \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial g_{ij}}{\partial X^m}\right] \\
     \Gamma^{\ell}_{ij} &= g^{\ell m} \frac12\left[\frac{\partial g_{mi}}{\partial X^j} + \frac{\partial g_{mj}}{\partial X^i} - \frac{\partial g_{ij}}{\partial X^m}\right]
   \end{align}
$$

Now, we can write the derivative 

$$ \left(\frac{\partial V^i(X)}{\partial X^j} e_i(X) + V^i(X) \Gamma^i_{jk}e_i\right) = \left(\frac{\partial V^i(X)}{\partial X^j} + \Gamma^i_{jk}\right)e_i. $$

<br>
