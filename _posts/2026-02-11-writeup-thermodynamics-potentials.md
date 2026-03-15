---
layout: post
published: false
title: Thermodynamic free energies
date: 2026/02/11
subtitle: How much work can we get out of a system?
source: writeup
kind: physics
theme: thermodynamics
tags: free-energy second-law
---

> This note lays out the various thermodynamic potentials in the most straightforward way I know. 

<!--more-->

## Argument

For an isolated system and a reservoir, the unencumbered change in entropy (no unaccounted-for constraints on the system) has to be positive:

$$ 
    \begin{align}
        0 &\leq \Delta S_\text{total} \\
        &= \Delta S_\text{reservoir} + \Delta S_\text{system}.
    \end{align}
$$

The entropy change of the reservoir is the heat that flows **out** from the system over temperature of the reservoir, $-Q/T,$ so the second law becomes

$$ -\frac{Q}{T} + \Delta S_\text{system} \geq 0. $$

The change in internal energy of the system $\Delta U$ is the heat flow into it $Q$ minus whatever work it does, so $\Delta U = Q - W,$ or $Q = \Delta U + W.$ Work can be mechanical (like an expanding gas in a balloon, $P\Delta V$) or non-mechanical (like a galvanic cell, or a ribosome forming peptide bonds) so we can draw the distinction ${W = W_\text{$PV$} + W_\text{non-$PV$},}$ and, plugging in for $Q$ we get

$$ 
	0 \leq -\frac{\Delta U + W_\text{$PV$} + W_\text{non-$PV$}}{T} + \Delta S_\text{sys} 
$$

multiplying through by $T$ and separating, this becomes 

$$
	W_\text{$PV$} + W_\text{non-$PV$} \leq -(\Delta U - T\Delta S_\text{sys}).
$$

This is a general expression connecting work in its multiple forms, internal energy, and entropy. The thermodynamic potentials come from holding the non $W_\text{$PV$}$ terms constant in various ways.

When we make sure no mechanical work is done, we get

$$ W_\text{non-$PV$} \leq -(\Delta U - T\Delta S_\text{sys}) = -\Delta F, $$

and the term on the right is minus the Helmholtz free energy change of the system. From the equation, the maximum available work is the energy drop of the system, less the loss to entropy (mixing, chemical rearrangement, ...). This is the situation for phase transitions in materials at constant volume, or processes in rigid containers.

When mechanical work is allowed (work against the ambient, constant pressure), we get

$$ W_\text{non-$PV$} \leq -(\Delta U - T\Delta S_\text{sys}) - W_\text{$PV$} = -\Delta G, $$

and the term on the right is minus the Gibbs free energy change. In this scenario, the maximum possible work is the energy drop of the system less the work done inserting things into or expanding the system, and less the loss to entropy. This is useful in chemical and molecular biological contexts when we are at fixed pressure and because composition matters. fueling reactions with other reactions, and want to channel energy toward specific rearrangements.

If we can work it out so that entropy does not change, then we have

$$W_\text{non-$PV$} \leq -\Delta U  - W_\text{$PV$} = -\Delta H,$$

and the right hand side is minus the enthalpy. In this scenario, we have no chemical rearrangement taking place, we just have a physical process like a flow or a phase change at constant pressure.

These are the upper bounds on chemical work given the various experimental constraints.

<br>