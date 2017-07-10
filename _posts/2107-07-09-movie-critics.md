---
layout: post
published: true
title: Movie Critics
date: 2017/07/09
---

>A town of 1,000 households has a strange law intended to prevent wealth-hoarding. On January 1 of every year, each household robs one other household, selected at random, moving all of that house’s money into their own house. The order in which the robberies take place is also random and is determined by a lottery. (Note that if House A robs House B first, and then C robs A, the houses of A and B would each be empty and C would have acquired the resources of both A and B.)
>
>Two questions about this fateful day:
>
>What is the probability that a house is not robbed over the course of the day?
Suppose that every house has the same amount of cash to begin with — say \$100. Which position in the lottery has the most expected cash at the end of the day, and what is that amount?
<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-many-critics-does-it-take-to-rank-all-the-movies/))

## Solution

There is an ambiguity in the statement of the problem. A _static_ interpretation requires us to assign critics to watch a fixed sequence of movies in advance. A _dynamic_ interpretation allows for the critics to base their plans on all the critics' evaluative judgments before every viewing. While I doubt it makes a difference, I am not sure of that, and I will operate on the assumption that the static interpretation is intended.

First, let's establish that for every pair of non-simultaneous movies -- all $30 \times 27 / 2$, or $405$, of them --  at least one of the critics must watch both.  Suppose some pair of movies is not co-watched in that sense. Then if it contains the best and second-best movies, all we will know at the end of the festival is that every critic who has seen either of them rated it higher than every other movie they've seen. That provides no way to rank them with respect to each other. So to guarantee that we'll find the best movie, every pair of movies must be co-watched.

Each movie must be watched by a unique crowd (set of critics), because if two movies are watched by the same crowd, then the earlier of the movies is not co-watched with the two movies shown at the same time as the later.

There have to be at least three critics in each initial crowd to be able to fan out into all the three second-showing movies. Nine critics can form $3\times3\times3$, or $27$ unique crowds of three overlapping each of the initial crowds, which is exactly the number of unique crowds needed for the final $9$ showings. And nine critics end up watching $9 \times 10 \times 9 / 2$, or 405 pairs of movies, which is exactly what we need. However, given the need for any two non-simultaneous crowds to overlap, and given the fact that each critic can see only one movie at a time, it turns out that nine critics can cover at most four showings of three movies each.

In general terms, the problem (which is really a problem in set theory and combinatorics) is to determine, for $c$ critics and $s$ screens, the maximum number of distinct single-showing-assignments (partitions) of the $c$ critics into $s$ crowds (subsets) such that any two crowds in any two (distinct) assignments are distinct but overlap. That sounds like a hard problem to me, and I look forward to seeing if the puzzle author (or anyone else) has a nice way into it.  

What I do have is a relatively simple and effective strategy that uses a lavish staff of 21 critics.

Let's represent a critic's overall assignment of theaters as a ten-character string, such as "ACCBBCAABA".  Then, nine critics could satisfy the desideratum---necessary, but not sufficient to solved the problem---of having movies in consecutive showings co-watched, as follows:

```
    1: AAAAAAAAAA
    2: ABABABABAB
    3: ACACACACAC
    4: BABABABABA
    5: BBBBBBBBBB
    6: BCBCBCBCBC
    7: CACACACACA
    8: CBCBCBCBCB
    9: CCCCCCCCCC
```

These assignments ensure that every pair of movies containing one from an odd- and one from an an even-numbered showing are both watched by a critic.  But all of the pairs of movies from odd-odd and even-even showings are not co-watched.

We can start to repair that with $9$ more critics, using the same assignment chart as above but reading it differently, namely by considering the showings to be represented in the order 1, 3, 5, 7, 9, 2, 4, 6, 8, 10. That will cover pairs movies that are in showings whose numbers are odd and even in this ordering. Reordering, this second set of assignments is:

```
    1: AAAAAAAAAA
    2: ABBAABBAAB
    3: ACCAACCAAC
    4: BAABBAABBA
    5: BBBBBBBBBB
    6: BCCBBCCBBC
    7: CAACCAACCA
    8: CBBCCBBCCB
    9: CCCCCCCCCC
```

To finish up, do the same thing yet again, but scramble the ordering as follows: 1,5,9,3,7,2,6,10,4,8. This yields:

```
    1: AAAAAAAAAA
    2: ABBABAABAB
    3: ACCACAACAC
    4: BAABABBABA
    5: BBBBBBBBBB
    6: BCCBCBBCBC
    7: CAACACCACA
    8: CBBCBCCBCB
    9: CCCCCCCCCC
```

Now every pair of showings has been odd-even, and so all pairs of movies are covered by the $27$ critics we've employed. The six constant-theater assignments in the second and third charts are redundant (we already had those assignments covered among our initial nine critics). So in the words of our President, they are fired, and in total we get by with 21 critics. 

The chart has an obvious pattern, which can be repeated for any  number of showings without a need for additional critics. And a similar chart can be made for any number $s$ of screens, with $s^2$ lines, and again needing to re-use the chart twice, for a total (after eliminating redundancies) of $3s^2-2s$ critics for any number of showings.

I do doubt that this scheme is optimal, as among 21 critics, $21 \times 10 \times 9 /2 $, or 945, movie pairs are covered---more than half redundantly. But it's Sunday night, and it's what I got.

<br>
 
