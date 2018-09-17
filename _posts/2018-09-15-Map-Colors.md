---
layout: post
published: true
title: Map Colors
date: 2018/09/15
---

>An eccentric billionaire has a published a devilish math problem that she wants to see solved. Her challenge is to three-color a specific map that she likes — that is, to color its regions with only three colors while ensuring that no bordering regions are the same color. Being an eccentric billionaire, she offers 10 million dollars to anyone who can present her with a solution.
>
>You come up with a solution to this math problem! However, being a poor college student, you cannot come up with the 10,000 dollars needed to travel to the billionaire’s remote island lair. You go to your local bank and ask the manager to lend you the 10,000 dollars. You explain to him that you will soon be winning 10 million dollars, so you will easily be able to pay back the loan. But the manager is skeptical that you actually have a correct solution.
>
>Of course, if you simply hand the manager your solution, there is nothing preventing him from throwing you out of his office and collecting the 10 million for himself. So, the question is: How do you prove to the manager that you have a solution to the problem without giving him the solution (or any part of the solution that makes it easy for him to reproduce it)?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/to-solve-the-eccentric-billionaires-puzzle-you-must-first-defeat-the-banker/))

## Solution

### Producing high confidence

We will show that the banker can reach arbitrarily high confidence that you have a correct solution, without learning anything else about the pattern of your map coloring.

You produce a stack of six colored maps, each one a variation on your solution, with the three colors permuted in the six possible ways. The colored regions, but not the border lines, are then painted with an opaque scratch-off coating.

You bring these to the banker.  He chooses a map and indicates any pair of adjacent regions he likes, and you scratch off the material to reveal the colors of those regions, showing that they are distinct.  You then recoat that map, shuffle the maps, and repeat the same challenge-and-reveal protocol until the banker is sufficiently confident that all adjacent regions on all of the maps in your stack are differently colored.  That makes him sufficiently confident that each of your six colorings is a correct solution, and that in the six colorings, each pair of adjacent regions is differently colored in all six possible ways; but he can conclude nothing more specific about the colorings.

### Producing full confidence

To produce full confidence, we can give the banker a machine that (as he knows) scans a map and determines whether it is three-colored, saving no memory of the colors on the map, but displaying the uncolored skeleton.

![Computer screen displaying an uncolored map and the text, "3-Colored!"](/img/map.png)

### Extra credit

The three-color mapping problem is [NP-complete](https://en.wikipedia.org/wiki/NP-completeness), meaning that every yes/no problem in the [NP complexity class](https://en.wikipedia.org/wiki/NP_(complexity)) can be reduced to it: for any such problem, there is an efficient way of translating it into a map such that the answer to that problem is yes if and only if the map can be three-colored. So for any such problem, you can convince a banker that you have a solution to it by first agreeing with the banker on a translation of the problem to a map, and then convincing him that you have three-colored that map.  A proof that one knows a solution to a given problem, where the proof reveals nothing more about the solution, is called a [zero-knowledge proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof).

<br>
