---
layout: post
published: true
title: Covariant derivative
date: 2025/12/27
subtitle: Where does it come form, how do we find it?
tags: general-relativity differential-geometry
---

>**Question**: How does the directional derivative generalize when basis vectors can vary?

<!--more-->

## Argument

We want to calculate the derivative of a vector $\mathbf{V}$ attached to a point that moves along the surface, in the coordinates of the surface, along some particular direction, at that point.

Take a vector 

$$\mathbf{V}(X) = V^i(X) e_i(X)$$ 

where $e_i(X)$ is the $i^\text{th}$ basis vector. The components of $\mathbf{V}$ can change because the $V^i$ change, due to some physical process, or because the basis vectors have changed due to variation of the surface. 

The basis vectors at each point come from the map from surface coordinates to position in the embedding space: ${\mathbf{r}(X) = \boldsymbol{\gamma}(X)= \langle \gamma_1(X), \gamma_2(X), \ldots, \gamma_d(X)\rangle,}$ so that $e_j = \partial \boldsymbol{\gamma}(X) / \partial X^j.$ This means that the basis vectors are tangent to the surface. It also means that we can freely flip flop derivatives of the basis vectors with respect to surface coordinates like $\partial e_i/\partial X^j \leftrightarrow \partial e_j/\partial X^i.$

If we advance along the path, resulting in a shift of $\Delta X^j$ in the coordinates of the surface, the new vector is $$V^i(X+\Delta X)e_i(X+ \Delta X).$$ Expanding this, subtracting $\mathbf{V}(X),$ and dropping second order terms we get (Einstein convention implied)

$$ \left(\frac{\partial V^i(X)}{\partial X^j} e_i(X) + V^i(X) \frac{\partial e_i(X)}{\partial X^j}\right) \Delta X^j. $$

The first term corresponds to the ordinary Jacobian while the second term is the new stuff corresponding to the variation of the basis vectors. The derivative of the basis vector $e_i(X)$ with respect to the coordinate $X^j$ can be expressed in terms of the basis vectors at $X,$ e.g. a superposition $\Gamma^k_{ij} e_k(X)$ plus some normal component.

Focusing on this, we have, so far

$$ \frac{\partial e_i}{\partial X^j} = \Gamma^k_{ij} e_k + \text{some normal component}. $$

Now we need to get $\Gamma^k_{ij}$ alone. We can dot both sides by $e_m,$ getting the metric tensor on the right side and killing the normal component

$$
  \begin{align}
    \Gamma^k_{ij} e_m\cdot e_k  &= e_m\cdot \frac{\partial e_i}{\partial X^j} + e_m\cdot \text{some normal component} \\
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
    D_{\Delta X} \mathbf{V} &= \left(\frac{\partial V^i(X)}{\partial X^j} e_i(X) + V^k(X) \Gamma^i_{kj}e_i(X)\right)\Delta X^j \\
                   &= \left(\frac{\partial V^i(X)}{\partial X^j} + V^k(X)\Gamma^i_{kj}\right)e_i(X)\Delta X^j.
  \end{align} 
$$

Using the embedding let us compare vectors at different points because they are valid members of the ambient embedding space, as well as of their local tangent spaces. This embedding is inessential, and we can cleanse it from the argument to get an intrinsic definition for the covariant derivative.

## Anticipating symmetry

Starting from the definition of the covariant derivative of an amplitude as the partial derivative plus a linear combination of the other amplitudes, we can anticipate the symmetry of the Christoffel components in the lower indices.

Take two coordinate systems, $X$ (Roman indices) where the metric is flat, and $\widetilde{X}$ (Greek indices) where the coordinates are curvilinear. Then the covariant derivative in $\widetilde{X}$ can be gotten from the one in $X$ by the transformation

$$ \begin{align}
    \widetilde{D}_\alpha \widetilde{V}^\beta &= \frac{\partial \widetilde{X}^\beta}{\partial X^b}\frac{\partial X^a}{\partial \widetilde{X}^\alpha} D_a V^b \\
    &= \frac{\partial \widetilde{X}^\beta}{\partial X^b}\frac{\partial X^a}{\partial \widetilde{X}^\alpha} \left[\frac{\partial}{\partial X^a}V^b + \Gamma^b_{\ell a} V^\ell \right]
\end{align}  
$$

In the flat coordinates $X,$ the metric is flat at the point, so the Christoffel symbols are zero. Transforming the partial derivative and the coefficients $V^b$ we get

$$
   \begin{align}
      \widetilde{D}_\alpha \widetilde{V}^\beta &= \frac{\partial \widetilde{X}^\beta}{\partial X^b}\frac{\partial X^a}{\partial \widetilde{X}^\alpha}\left[\frac{\partial \widetilde{X}^\delta}{\partial X^a}\frac{\partial}{\partial\widetilde{X}^\delta}\left(\frac{\partial X^b}{\partial\widetilde{X}^\gamma}\widetilde{V}^\gamma\right)\right] \\ 
      &= \frac{\partial \widetilde{X}^\beta}{\partial X^b}\frac{\partial X^a}{\partial \widetilde{X}^\alpha}\frac{\partial \widetilde{X}^\delta}{\partial X^a}\left[\frac{\partial^2 X^b}{\partial\widetilde{X}^\delta\partial\widetilde{X}^\gamma}\widetilde{V}^\gamma + \frac{\partial X^b}{\partial\widetilde{X}^\gamma}\frac{\partial\widetilde{V}^\gamma}{\partial\widetilde{X}^\delta}\right] \\
      &= \frac{\partial\widetilde{X}^\beta}{\partial X^b}\delta^\alpha_\delta\frac{\partial^2 X^b}{\partial\widetilde{X}^\delta\partial\widetilde{X}^\gamma}\widetilde{V}^\gamma + \delta^\beta_\gamma\delta^\delta_\alpha\frac{\partial\widetilde{V}^\gamma}{\partial\widetilde{X}^\delta} \\
      &=  \frac{\partial\widetilde{X}^\beta}{\partial X^b}\frac{\partial^2 X^b}{\partial\widetilde{X}^\alpha\partial\widetilde{X}^\gamma}\widetilde{V}^\gamma + \frac{\partial\widetilde{V}^\beta}{\partial\widetilde{X}^\alpha}
   \end{align}
$$

However, in the curvilinear coordinate system $\widetilde{X},$ this is just 

$$ \widetilde{D}_\alpha\widetilde{V}^\beta = \frac{\partial\widetilde{V}^\beta}{\partial\widetilde{X}^\alpha} + \widetilde{\Gamma}^\beta_{\gamma\alpha}\widetilde{V}^\gamma $$

which shows that the Christoffel symbol can be written as

$$ \widetilde{\Gamma}^\beta_{\gamma\alpha} = \frac{\partial\widetilde{X}^\beta}{\partial X^b}\frac{\partial^2 X^b}{\partial\widetilde{X}^\alpha\partial\widetilde{X}^\gamma} $$

which is symmetric in the lower indices $\gamma$ and $\alpha.$

<!-- ## Derivative of the metric tensor 

We can also use the flat coordinates $X$ to learn that the covariant derivative of the metric tensor is zero in all frames $\widetilde{X}.$

From the above, we don't have a direct approach to deal with rank-$2$ tensors. But if we make the assumption that the covariant derivative has to obey a product rule, then we can work it out from the rules on vectors.

$$ D_\ell g_{mn} = D_\ell \left(e_m\cdot e_n\right). $$

On the left side, we have the covariant derivative of $g$ as a scalar field, so is no variation of basis vectors and we just get the partial derivative in the coordinate $X^\ell.$ On the right side, we can break it up using the product rule and apply the formula we worked out above. Our formula assumes vectors in the coefficient and basis vector form like $V = V^a e_a,$ so we need to re-express the basis vectors like $e_m = \delta^a_m e_a.$ 

$$
  \begin{align}
    D_\ell g_{mn} &= D_\ell \left(e_m\cdot e_n\right) \\
    \frac{\partial g_{mn}}{\partial X^\ell} &= \left(D_\ell e_m\right)\cdot e_n + e_m\cdot \left(D_\ell e_n\right) \\
    &= \left(D_\ell \delta^a_m e_a\right)\cdot e_n + e_m\cdot \left(D_\ell \delta^b_n e_b\right) \\
    &= \left(\frac{\partial \delta^a_m}{\partial X^\ell} e_a + \Gamma^c_{a\ell}e_c\delta^a_m\right)\cdot e_n + e_m\cdot \left(D_\ell \frac{\partial \delta^b_n}{\partial X^\ell} e_b + \Gamma^d_{b\ell}e_d\delta^b_n \right) \\
  \end{align}
$$

The partial derivatives of the $\delta^i_j$ are zero so

$$
  \begin{align}
    \frac{\partial g_{mn}}{\partial X^\ell} &= \Gamma^c_{m\ell}e_c\cdot e_n + e_m\cdot \Gamma^d_{n\ell}e_d \\
    &= \Gamma^c_{m\ell}g_{cn}+ \Gamma^d_{n\ell}g_{md}
  \end{align}
$$

so we end up with

$$ 0 = \frac{\partial g_{mn}}{\partial X^\ell} - \Gamma^c_{m\ell}g_{cn} - \Gamma^d_{n\ell}g_{md}. $$

We evaluated this in $X,$ the coordinates at the point, where the metric is approximately flat. But each quantity is a tensor so it's true in arbitrary coordinates $\widetilde{X}.$ -->

<br>
