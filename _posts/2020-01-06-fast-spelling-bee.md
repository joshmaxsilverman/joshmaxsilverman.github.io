---
layout: post
published: true
title: Fast spelling bee
date: 2020/01/06
subtitle: Can you build the ultimate Spelling Bee board?
source: fivethirtyeight
theme: algorithms
---

>**Question:** The NYTimes has a new word game called Spelling Bee. The idea of the game is, on a board like the one below, to make words using **only** the letters on the board under the constraint that the central letter must be used. Words are worth their length in letters (with a minimum length of $4$), but words that use all $7$ letters — known as **pangrams** — are awarded $7$ bonus points. The valid word list is Peter Norvig's which contains some 172820 distinct words. The object is to find the game board with the highest possible maximum score.
>
>![](/img/2020-01-06-honeycomb.png){: width="450px" class="image-centered"}


<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/))

## Solution

### The numbers

$$\begin{array}{|c|c|} \hline
\textbf{Quantity} & \textbf{Value} \\ \hline
\text{words} & 172820 \\ \hline
\text{pangrams} & 7\binom{26}{7} = 4604600 \\ \hline
\end{array}$$

On first glance, these numbers are daunting. A naive search would need to generate some $\approx 4.6\times10^6$ pangrams, and compare them against the dictionary of $\approx 1.5\times10^5$ words — a hefty $\approx 10^{12}$ comparisons. Simply looping over a list that long (without any string operations) would take hours in a Colab notebook. Hopefully there is some structure we can exploit.


### Plan

The big idea here is to only ever make linear passes over the word list, and avoid looping the list of possible pangrams entirely. The logic of the two major passes is

1. accumulate the possible pangrams and populate a data structure, `pangram_scores`, that can receive score increments for given $\left(\text{pangram},\text{center letter}\right),$ then
2. loop over the word list and accumulate their scores to the relevant pangrams in `pangram_scores`

### The words

First, we grab the words and accumulate them in the list `words`.

```python
from collections import defaultdict
from itertools import combinations
import time
import requests
from functools import lru_cache

words = requests.get("https://norvig.com/ngrams/enable1.txt")
words = words.text.strip().split('\n')

word_to_pangram = defaultdict(set)
```

Next, we filter the word list for those that are valid ($4$ letters or longer, and don't contain an $\text{S}$) and accumulate them in `valid_words`. `pangrams` is a list of the relevant pangrams found by filtering the word list for all words with exactly $7$ distinct letters. The `word_score()` function takes a word and outputs its score. The `subsets()` function takes a set of characters and returns all of its possible (ordered) subsets.

```python
valid_words = [word for word in words
               if len(word) >= 4
               and 's' not in word
               and len(set(word)) < 8]

pangrams = ["".join(sorted(set(_))) for _ in valid_words if len(set(_)) == 7]

@lru_cache(maxsize=10000)
def subsets(s):
    for size in range(len(s) + 1):
        yield from combinations(list(s), size)
        
@lru_cache(maxsize=10000)
def word_score(word):
    return (1 if len(word) == 4 else len(word)) + (7 if len(set(word)) == 7 else 0)
```

### Speed-enabling data structure

This is the key to the speed of this approach. Instead of testing which pangrams a word is a subset of, we can directly map from the ordered set of letters that a word contains to all pangrams it would be a valid word for. We can think of each of these ordered sets as a **pangram stem**.

In other words, it is a mapping from pangram stems to pangrams though, in effect, it is a mapping from words to pangrams.

Suppose the pangram we're dealing with is $\text{BLOMING}.$ Any word formed from a subset of the its letters would be valid, such as $\text{BOOM},$ $\text{LOOM},$ $\text{BOMBING},$ or $\text{BLOOMING}.$ The letter sets for these words is, respectively, $\\{\text{B},\text{O},\text{M}\\}$, $\\{\text{L},\text{O},\text{M}\\},$ $\\{\text{B},\text{I},\text{G},\text{M},\text{N},\text{O}\\},$ and $\\{\text{B},\text{I},\text{G},\text{L},\text{M},\text{N},\text{O}\\}.$ 

This code creates a dictionary from all pangram stems to their corresponding pangrams. 

```python
for pangram in pangrams:
    keys = [''.join(lst) for lst in subsets(pangram)]
    for key in keys:
        word_to_pangram[key].add(pangram)
```

Next, we need a dicitonary that can track the total score for each pangram. 

So far, we have ignored something we'll have to mind — whether the pangram's center letter is in a candidate word or not. This code initializes a dictionary to keep track of $\left(\text{pangram},\text{center letter}\right)$ pairs.

```python
pangram_scores = defaultdict(lambda: 0)
```

### Accumulate the scores

This code goes through the list of words, and adds the word score to the total score for each of its relevant pangrams. The pangram score dictionary is indexed by a tuple of the pangram string and the given central letter. One loop over the word list accumulates the scores to all relevant $\left(\text{pangram},\text{center letter}\right)$ destinations.

```python
for word in valid_words:
    word_key = "".join(sorted(set(word)))
    for pangram in word_to_pangram[word_key]:
        for letter in word_key:
            pangram_scores[(pangram, letter)] += word_score(word)
```

### Find the max

After this, we simply have to find the maximum score in the dictionary and its associated $\text{pangram}$ and $\text{central letter}.$ This code loops over the two level dictionary to find the max.

```python
max_key = max(pangram_scores, key=pangram_scores.get)
```

On computing, this finds (in $\approx\text{2 s}$) that the highest scoring game board is the pangram stem $\text{AEGINRT}$ with central letter $\text{R}$ which has total score $3898.$



<br>
