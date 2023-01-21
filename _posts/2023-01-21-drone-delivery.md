---
layout: post
published: false
title: Drone delivery
date: 2023/01/21
subtitle:
tags:
---

>**Question**: A  restaurant at the center of Riddler City is testing an airborne drone delivery service against their existing fleet of scooters. The restaurant is at the center of a large Manhattan-like array of square city blocks, which the scooter must follow.
>
>Both vehicles travel at the same speed, which means drones can make more deliveries per unit time. Assume that (1) Riddler City is circular in shape, as you may recall (2) deliveries are made to random locations throughout the city and (3) the city is much, much larger than its individual blocks.
>
>In a given amount of time, what is the expected ratio between the number of deliveries a drone can make to the number of deliveries a scooter can make?
>
>Extra credit: In addition to traveling parallel to the city blocks, suppose scooters can also move diagonally from one corner of a block to the opposite corner of the block. Now, what is the new expected ratio between the number of deliveries a drone can make and the number of deliveries a scooter can make?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-make-a-speedy-delivery/))

## Solution

Because the drone can fly straight to the target, if a house has coordinates $(x,y)$ on the city grid, the drone has to cover distance $\sqrt{x^2 + y^2}$ whereas the scooter, confined to the blocks of the grid, has to cover distance $\left\lvert x\rvert + \lvert y\rvert\right).$

Summing over the point

<br>
