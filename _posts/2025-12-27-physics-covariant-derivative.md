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

## Derivative of the metric tensor

We can also use the flat coordinates $X$ to learn that the covariant derivative of the metric tensor is zero in all frames $\widetilde{X}.$

From the above, we don't have a direct approach to deal with rank-$2$ tensors. But if we make the assumption that the covariant derivative has to obey a product rule, then we can work it out from the rules on scalars and vectors. One of the ways we'll work out will bootstrap the rule we worked out for the coefficients of vectors, and the other will return to finding the derivatives of basis (and dual basis) vectors.

### As scalar coefficients

One way is to form the quantity $V^2 = g_{mn}V^m V^n.$ Taking the covariant derivative $D_\ell V^2,$ we can evaluate it in two ways. 

The first is to treat the whole thing like a scalar in which case we get a partial derivative

$$ D_\ell V^2 = \frac{\partial V^2}{\partial X^\ell} = \frac{\partial g_{mn}}{\partial X^\ell}V^mV^n + g_{mn}\frac{\partial V^m}{\partial X^\ell}V^n + g_{mn} V^m\frac{\partial V^n}{\partial X^\ell}. $$

The second way is to treat the pieces as tensor objects using the product rule that we assume holds

$$ 
  \begin{align}
    D_\ell V^2 &= \left(D_\ell g_{mn}\right)V^mV^n + g_{mn}\left(D_\ell V^m\right)V^n +  g_{mn}V^m\left(D_\ell V^n\right) \\
    &= \left(D_\ell g_{mn}\right)V^mV^n + g_{mn}\left[\frac{\partial V^m}{\partial X^\ell} + \Gamma^m_{k\ell}V^k\right]V^n + V^m\left[\frac{\partial V^n}{\partial X^\ell} + \Gamma^n_{\ell k}V^k\right]
  \end{align}. 
$$

Equating the two forms, the terms with partial derivatives of the $V$ are present on both sides so we can drop them. We leave the $D_\ell g_{mn}$ unevaluated, since we don't know how to evaluate it. 

$$ \begin{align}
\left(D_\ell g_{mn}\right)V^mV^n + g_{mn}\Gamma^m_{k\ell}V^kV^n + g_{mn}V^m\Gamma^n_{\ell k}V^k &= \frac{\partial g_{mn}}{\partial X^\ell}V^mV^n \\
\left(D_\ell g_{mn}\right)V^m V^n &= \frac{\partial g_{mn}}{\partial X^\ell}V^mV^n - g_{mn}\Gamma^m_{k\ell}V^kV^n - g_{mn}V^m\Gamma^n_{\ell k}V^k
\end{align} $$

Flip-flopping indices $k \leftrightarrow m$ and $k\leftrightarrow n$ in the Christoffel terms on the right, we get the explicit form of the covariant derivative for the metric

$$ \begin{align}
  \left(D_\ell g_{mn}\right)V^m V^n &= \frac{\partial g_{mn}}{\partial X^\ell}V^mV^n - g_{kn}\Gamma^k_{m\ell}V^mV^n - g_{mk}V^m\Gamma^k_{\ell n}V^n \\
    \left(D_\ell g_{mn}\right) &= \frac{\partial g_{mn}}{\partial X^\ell} - g_{kn}\Gamma^k_{m\ell} - g_{mk}\Gamma^k_{\ell n}
    \end{align}
$$

At the point of evaluation, where the flat, orthonormal coordinates $X$ are defined, the metric entries are $\delta_{ij}$ and the Christoffel symbols are zero. So, the covariant derivative of the metric $D_\ell g_{mn}$ is equal to zero. Since the covariant derivative is a tensor, the covariant derivative of the metric tensor is zero in all frames. 

Generalizing, the covariant derivative of a $(0,2)$ tensor $W_{mn}$ is equal to 

$$ \left(D_\ell W_{mn}\right) = \frac{\partial W_{mn}}{\partial X^\ell} - W_{kn}\Gamma^k_{m\ell} - W_{mk}\Gamma^k_{\ell n} $$

### As a tensor field

Another way is to write the metric in its full form with dual basis vectors $\mathbf{g} = g_{mn} e^m\otimes e^n.$ Applying the product rule, we get

$$ D_\ell \mathbf{g} = \left(D_\ell g_{mn}\right)e^m\otimes e^n + g_{mn}\left(D_\ell e^m\right)\otimes e^n + g_{mn}e^m\otimes \left(D_\ell e^n\right). $$

This requires us to figure out the covariant derivative of the dual basis vectors $e^i.$ This is actually straightforward since we know the covariant derivative of the lower basis vector $e_j.$ The product $e^i e_j$ is equal to $\delta^i_j$ so

$$
  \begin{align}
    0 &= D_\ell \delta^i_j \\
      &= D_\ell\left(e^i e_j\right) \\
      &= \left(D_\ell e^i\right) e_j + e^i\left(D_\ell e_j\right) \\
      &= \left(D_\ell e^i\right) e_j + e^i \left(\Gamma^c_{\ell j} e_c\right) \\
      -\Gamma^i_{\ell j} &= \left(D_\ell e^i\right) e_j
  \end{align}
$$

The last line shows that $D_\ell e^i$ must be $-\Gamma^i_{\ell j} e^j.$ Plugging this in to $D_\ell\mathbf{g}$ above, we get

$$
  \begin{align}
    D_\ell\mathbf{g} &= \frac{\partial g_{mn}}{\partial X^\ell}e^m\otimes e^n - g_{mn}\Gamma^m_{\ell k}e^k\otimes e^n - g_{mn}e^m\otimes \Gamma^n_{\ell k} e^k \\
    &= \left(\frac{\partial g_{mn}}{\partial X^\ell} - g_{kn}\Gamma^k_{\ell m} - g_{mk}\Gamma^k_{\ell n}\right)e^m\otimes e^n
  \end{align}
$$

Again, due to the flat coordinates $X$, the partials and Christoffel symbols are zero at the point of evaluation, and so the covariant derivative is zero. The piece in parenthesis becomes the definition for the covariant derivative of $g_{mn}$ when we don't want to keep explicit track of basis elements.

## Length preservation under parallel transport

We can also see that the length of a vector is preserved by parallel transport. We can see this two ways, one that requires honest work, and one using our covariant derivative technology. The honest way first.

### By local expansion

After moving from $X$ to $X+dX$ and changing a vector by $dV,$ the squared length goes from $L^2 = g_{mn}(X)V^m V^n$ to

$$ 
  \begin{align}
    {L^\prime}^2 &= g_{mn}(X + dX)(V^m + dV^m)(V^n + dV^n) \\
    &= \left(g_{mn}(X)+\frac{\partial g_{mn}(X)}{\partial X^\ell} dX^\ell\right)\left(V^m + dV^m\right)\left(V^n + dV^n\right)
  \end{align}
$$

where we are expanding using the coordinates of the tangent space at $X.$

The covariant derivative of $V^m$ is $D_{\Delta x} V^m = \left(\frac{\partial V^m}{\partial X^r} + \Gamma^m_{kr}V^k\right)dX^r,$ so if we keep the covariant derivative zero ($D_r V^m dX^r = 0$) a.k.a. parallel transport the vector $V,$ then $dV^m = \frac{\partial V^m}{\partial X^r}dX^r = -\Gamma^m_{kr}V^kdX^r$ and

$$
  \begin{align}
    g_{mn}(X + dX)(V^m + dV^m)(V^n + dV^n) &\approx g_{mn}(X)V^m V^n +\frac{\partial g_{mn}(X)}{\partial X^\ell}dX^\ell V^m V^n - g_{mn}(X) \Gamma^m_{kr}V^k dX^r V^n - g_{mn}(X)V^m\Gamma^n_{jr} V^j dX^r \\
    &= g_{mn}(X)V^mV^n + dX^\ell\left[ \frac{\partial g_{mn}(X)}{\partial X^\ell}V^m V^n - g_{mn}(X)\Gamma^m_{k\ell}V^k V^n - g_{mn}(X)\Gamma^n_{j\ell}V^j V^m\right] \\
    &= g_{mn}(X)V^mV^n + dX^\ell V^mV^n\left[ \frac{\partial g_{mn}(X)}{\partial X^\ell} - g_{kn}(X)\Gamma^k_{m\ell} - g_{mj}(X)\Gamma^j_{n\ell} \right]
  \end{align}
$$

The bracketed term is zero since it's the covariant derivative of the metric tensor, so the new squared length is just $g_{mn}(X)V^mV^n$ which is the old squared length $L^2.$

### By covariant derivative

Starting from the squared length $L^2 = g_{mn}V^mV^n$ and taking the covariant derivative, we get

$$ D_{\Delta X} L^2 = \left(D_{\Delta X} g_{mn}\right)V^mV^n + g_{mn}\left(D_{\Delta X} V^m\right)V^n + g_{mn}V^m\left(D_{\Delta X} V^n\right) $$

which is zero since the covariant derivative of the metric is zero, and $V$ is being parallel transported which makes the $D_{\Delta X}V^m$ zero. Anus.

<br>
