---
layout: post
published: true
title: Street Grid
date: 2018/09/21
---

>You’ve just been hired to work in a juicy middle-management role at Riddler HQ — welcome aboard! We relocated you to a tastefully appointed apartment in Riddler City, five blocks west and 10 blocks south of the office. (The streets of Riddler City, of course, are laid out in a perfect grid.) You walk to work each morning and back home each evening. Restless and inquisitive mathematician that you are, you prefer to walk a different path along the streets each time. How long can you stay in that apartment before you are forced to walk the same path twice? (Assume you don’t take paths that are longer than required, and assume beaucoup bonus points for not using your computer.)
>
>Extra credit: What if you instead took a bigger but more distant apartment, M blocks west and N blocks south of the office?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/two-paths-diverged-in-a-city-and-i-i-took-the-block-less-traveled-by/))

## Solution

We'll go straight to the extra credit.  You have to walk $M+N$ blocks in total, and of those $M+N$ blocks you must choose $M$ blocks to travel east-west. There are ${M+N} \choose M$ ways to do this, and so it will take half that many days to walk all of the paths.

If $M$ and $N$ are $5$ and $10$, you'll walk the final path on the morning of day $1502$.

<br>
