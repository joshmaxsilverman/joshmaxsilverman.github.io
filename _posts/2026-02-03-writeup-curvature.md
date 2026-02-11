---
layout: post
published: false
title: Curvature
date: 2026/02/03
subtitle: Where does it come form, how do we find it?
source: writeup
kind: physics
theme: differential-geometry
tags: general-relativity differential-geometry
---

>This note has a few angles on curvature. The first is to compute the curvature tensor, intuitively defined as the difference of repeated covariant derivatives in either order. The second is computing the tangent vector under parallel transport on an arbitrary line of latitude on the sphere. Third, we calculate the equation of motion from minimizing the action (energy by proper time) for a particle in some given metric $g,$ and see that it's the same as the geodesic we got from parallel transport.

<!--more-->

([Fiddler on the Proof](URL))

## Solution

First, let's compute the curvature tensor.

### Curvature tensor

curvature is captured by the difference

$$ D_bD_a V_r - D_aD_b V_r.$$ 

with a flat metric, we expect this to be zero since partial derivatives commute, but in curved space the effect of moving in two directions in either order is not the same! we anticipate this therefore to come about from the coordinate changing parts of the covariant derivative.

collecting the two results we'll need from earlier, we have the covariant derivative of rank one and two tensors (e.g. vector and matrix):

$$ 
\begin{align}
    D_a V_r &= \frac{\partial V_r}{\partial X^a} - \Gamma^\ell_{ra} V_\ell \\
    D_b W_{ar} &= \frac{\partial W_{ar}}{\partial X^b} - \Gamma ^k_{ba}W_{kr} - \Gamma^k_{rb}W_{ak}. 
\end{align}
$$

we can evaluate $D_bD_aV_r$ and examine its symmetries to see which terms will survive on the swap $a\leftrightarrow b.$

thinking of $D_aV_r$ as a rank two tensor $W_{ar},$ and plugging in, we get

$$
    \begin{align}
        D_bD_aV_r &= \frac{\partial W_{ar}}{\partial X^b} - \Gamma^k_{ba}W_{kr} - \Gamma^k_{rb} W_{ak} \\
        &= \overbrace{\frac{\partial^2 V_r}{\partial X^a\partial X^b}}^{\text{symmetric in $ab$}} - \frac{\partial}{\partial X^b}\left[\Gamma^k_{ra}V_k\right] \\ &\quad - \overbrace{\Gamma^k_{ba}\left(\frac{\partial V_r}{\partial X^k} - \Gamma^\ell_{rk}V_\ell\right)}^\text{symmetric in $ab$} - \Gamma^k_{rb}\left(\frac{\partial V_k}{\partial X^a} - \Gamma^\ell_{ka}V_\ell\right) \\
    \end{align}
$$

anticipating the subtraction of $D_aD_bV_r$ we can ignore the terms symmetric in $a,b$ so

$$
    \begin{align}
        D_bD_aV_r &= -\frac{\partial \Gamma^k_{ra}}{\partial X^b}V_k - \overbrace{\Gamma^k_{ra}\frac{\partial V_k}{\partial X^b} - \Gamma^k_{rb}\frac{\partial V_k}{\partial X^a}}^\text{equal on exchange} + \Gamma^k_{rb}\Gamma^\ell_{ka}V_\ell
    \end{align}
$$

the middle terms are equal on exchange, so we end up with

$$ \left(D_bD_a - D_aD_b\right)V_r = \frac{\partial \Gamma^k_{rb}}{\partial X^a}V_k - \frac{\partial \Gamma^k_{ra}}{\partial X^b}V_k + \Gamma^k_{rb}\Gamma^\ell_{ka}V_\ell - \Gamma^k_{ra}\Gamma^\ell_{kb}V_\ell. $$

swapping the sum labels $\ell$ and $k$ in the double Christoffel terms, we can define the curvature tensor $\mathcal{R}^k_{bar}$ like 

$$ 
    \begin{align}
        \left(D_bD_a - D_aD_b\right)V_r
        &= \left(\frac{\partial \Gamma^k_{rb}}{\partial X^a} - \frac{\partial \Gamma^k_{ra}}{\partial X^b} + \Gamma^\ell_{rb}\Gamma^k_{\ell a} - \Gamma^\ell_{ra}\Gamma^k_{\ell b}\right)V_k \\
        &= \mathcal{R}^k_{bar}V_k
    \end{align}
$$

### Parallel transport on the sphere

we're going to compute the covariant derivative of the tangent vector as we move around a line of latitude, or parallel of the sphere. to do this, we need to know the metric and the Christoffel symbols. 

when we set the covariant derivative $D_m t^n$ equal to zero, we'll get differential equations that tell us how the components of $\mathbf{t}$ change with the angle $\phi$ around the sphere.

the metric on the surface of the sphere is ${ds^2 = r^2 d\theta^2 + r^2 \cos^2\theta d\phi^2}$ or on the parallel of the unit sphere

$$ g(\theta, \phi) = r^2\left(\begin{array}\ 1 & 0 \\ 0 & \cos^2\theta \end{array}\right). $$

now we can find the Christoffel symbols. because $g_{\theta\phi} = 0$ and $g_{\theta\theta} = 1,$ 

$$ \Gamma^\theta_{\theta\theta} = \frac12 g^{\theta\theta}\left(\partial_\phi g_{\theta\theta} + \partial_\theta g_{\theta\phi} - \partial_\theta g_{\theta\phi}\right) + \frac12 g^{\theta\phi}\left(\partial_\theta g_{\phi\theta} + \partial_\theta g_{\phi\theta} - \partial_\phi g_{\theta\theta}\right) = 0. $$

likewise, $\Gamma^\theta_{\phi\theta} = \Gamma^\theta_{\theta\phi} = 0$ as are $\Gamma^\phi_{\phi\phi}$ and $\Gamma^\phi_{\theta\theta}$

the nonzero symbols are

$$
    \begin{align}
        \Gamma^\phi_{\phi\theta} &= \Gamma^\phi_{\theta\phi} = \frac12g^{\phi\phi}\left(\partial_\phi g_{\phi\theta} + \partial_\theta g_{\phi\phi} - \partial_\phi g_{\theta\phi} \right) + \frac12\times \text{zero} \\
        &= -\frac12\frac{1}{\cos^2\theta}\cos\theta\sin\theta \\
        &= -\tan\theta
    \end{align}
$$

and

$$
    \begin{align}
        \Gamma^\theta_{\phi\phi} &= \frac12 g^{\theta\theta}\left(\partial_\phi g_{\theta\phi} + \partial_\phi g_{\theta\phi} - \partial_\theta g_{\phi\phi}\right) \\
        &= -\frac12\partial_\theta \cos^2\theta \\
        &= \sin\theta\cos\theta
    \end{align}
$$

once again, the covariant derivative of a vector is 

$$ D_at^n = \frac{\partial t^n}{\partial X^a} + \Gamma^n_{\ell a}t^\ell $$

on the parallel, $\theta=\theta_0$ so we can forget about $D_\theta t^\phi$ and $D_\theta t^\theta.$

this leaves us with the non-trivial equations $D_\phi t^\theta = 0$ and $D_\phi t^\phi = 0$ giving

$$ 
    \begin{align}
        D_\phi t^\phi &= \frac{\partial t^\phi}{\partial \phi} + \Gamma^\phi_{\theta\phi}t^\theta + \Gamma^\phi_{\phi\phi}t^\phi \\
        \frac{\partial t^\phi}{\partial\phi} &= -\tan\theta_0 t^\theta
    \end{align}
$$

and

$$ 
    \begin{align}
        D_\phi t^\theta &= \frac{\partial t^\theta}{\partial \phi} + \Gamma^\theta_{\theta\phi}t^\theta + \Gamma^\theta_{\phi\phi}t^\phi \\
        \frac{\partial t^\phi}{\partial\phi} &= -\sin\theta_0\cos\theta_0 t^\phi
    \end{align}
$$

now we can decouple these equations by differentiating each one and substituting the original equations back in, yielding

$$ 
    \begin{align}
        \frac{\partial^2t^\theta}{\partial\phi^2} &= -\sin^2\theta_0 t^\theta \\
        \frac{\partial^2t^\phi}{\partial\phi^2} &= -\sin^2\theta_0 t^\phi
    \end{align}
$$

which is solved by $t^{\theta/\phi} = A \cos \left(\sin^2\theta_0 \phi\right) + B \cos \left(\sin^2\theta_0 \phi\right).$

this shows that when the parallel is the equator, where $\theta_0 = 0,$ then the tangent vector will remain constant as it's transported around the circle. but if say $\theta_0 = \frac14\pi,$ then the vector will rotate by $2\pi\sin\frac{\pi}{4} = 2\pi/\sqrt{2} \approx 254.6\,^\circ$ as the vector is transported around the sphere.

### Geodesic equation from action

the action of a free particle moving in spacetime is the integral of its energy over proper time

$$ \int \mathcal{L} d\tau = -m_0c^2 \int\frac{d\tau}{dt}dt $$

where $d\tau/dt = \sqrt{-g} \equiv \sqrt{g_{tt} - g_{ab}\dot{X}^a\dot{X}^b}. $

we can check the integrand at small $v$ which is $\approx -m_0c^2 + \frac12mv^2.$

the el equation is 

$$ \frac{\partial\mathcal{L}}{\partial{X^\ell}} = \frac{d}{dt}\frac{\partial\mathcal{L}}{\partial\dot{X}^\ell}. $$

the derivatives $\dot{X}^j$ are independent of the $X^j$ so the only term on the left side is 

$$ 
    \begin{align} 
        \frac{\partial\mathcal{L}}{\partial{X^\ell}} &= \frac{1}{2\sqrt{-g}} \frac{\partial g_{ab}}{\partial X^\ell} \dot{X}^a\dot{X}^b\\
        &= \frac{1}{2}\frac{dt}{d\tau} \frac{\partial g_{ab}}{\partial X^\ell}\dot{X}^a\dot{X}^b
    \end{align}. 
$$

the derivative with respect to $\dot{X}^\ell$ gets a pair of terms that can be collapsed to one

$$
    \begin{align}
        \frac{\partial\mathcal{L}}{\partial\dot{X}^\ell} &= \frac12\frac{1}{\sqrt{-g}}\left(g_{a\ell}\dot{X}^a + g_{\ell b}\dot{X}^b\right) \\
        &= \frac{dt}{d\tau} g_{a\ell}\dot{X}^a \\
    \end{align}
$$

taking the time derivative get us

$$
    \begin{align}
        \frac{d}{dt} \frac{\partial\mathcal{L}}{\partial\dot{X}^\ell} &= 0 + \frac{dt}{d\tau}\frac{dg_{a\ell}}{dt}\dot{X}^a + \frac{dt}{d\tau}g_{a\ell}\frac{d \dot{X}^a}{dt} \\
        &= \frac{dt}{d\tau}\frac{\partial g_{a\ell}}{\partial X^m}\dot{X}^m\dot{X}^a + \frac{dt}{d\tau}g_{a\ell}\frac{d^2 X^a}{dt^2}.
    \end{align}
$$

if we multiply both sides by another $dt/d\tau$ we get 

$$ \frac{1}{2}\frac{\partial g_{ab}}{\partial X^\ell}\frac{dX^a}{d\tau}\frac{dX^b}{d\tau} = \frac{\partial g_{a\ell}}{\partial X^m}\frac{dX^m}{d\tau}\frac{dX^a}{d\tau} + g_{a\ell}\frac{d^2 X^a}{d\tau^2}. $$

relabling $m$ to $b$ we get

$$ g_{a\ell}\frac{d^2 X^a}{d\tau^2} = \frac{1}{2}\frac{\partial g_{ab}}{\partial X^\ell}\frac{dX^a}{d\tau}\frac{dX^b}{d\tau} - \frac{\partial g_{a\ell}}{\partial X^b}\frac{dX^b}{d\tau}\frac{dX^a}{d\tau}. $$
<br>
