---
layout: post
published: false
title: Antipersistent Basketball
date: 2018/04/21
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

- intuition for the winner
- the moves // reducing to volleys // master equation
- big picture // tail intuition // assumptions // symmetries (P2 <> P-2, P2 <> P4)
- solving the center // symmetry
  - plot theory <> experiment

### Who is going to win?

first, let's figure out which side has the natural advantage — is it the team that goes first or the one that goes second? 

once either team gets a two basket lead, the game is symmetric. but when the game is close, things get interesting.

after one possession, the nicks can be ahead if they score a basket at even odds, followed by the noughts missing their basket at less than even odds. the noughts can be up after one possession if the nicks miss at even odds, followed by the noughts scoring at even odds. advantage noughts: $\frac12r_{-} < \frac12\times\frac12$

this advantage is compounded on the next possession. the if the nicks are up 2, the game returns to a tie if the nicks miss at better than even odds, and then the noughts make at better than even odds (since they're underdogs). on the other hand, the noughts lose their lead if the nicks make at better than even odds, followed by the noughts missing at even odds. advantage noughts: $r_{+}\times r_{+} > \frac12 r_{+}.$

all in all, we should expect the team that goes second to win a great fraction of games.

<br>
