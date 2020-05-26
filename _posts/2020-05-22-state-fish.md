---
layout: post
published: true
title: State Fish
date: 2020-05-22
---

## Question

>Find the longest words that share letters with only 49 of the 50 U.S. states. Extra: find the state with the most such words.

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/somethings-fishy-in-the-state-of-the-riddler/))

## Solution

The straightforward approach to this puzzle is to loop over the list of $200000+$ words and then loop over the list of $50$ states to check if they have any letters in common, which is a loop of order $N_\text{word}N_\text{state}\langle \ell_\text{word}\rangle\langle \ell_\text{state}\rangle.$ 

The only interesting idea here is to make a "typewriter" (the dictionary `letter_state`) that maps directly from *letter* to a $50-$entry vector the encodes which *states* the letter appears in. This cuts out the factor of $N_\text{state}\langle \ell_\text{state}\rangle$ from the main loop. It's simple to build, we just loop over the list of states and record when they contain a letter in the dictionary by adding the $1$-hot vector $\left(0 \ldots j \ldots 0\right)$ where $j$ is the number of the state. 

```python
import string
from collections import defaultdict

alphanum = dict()
alpha = string.ascii_lowercase

for i in range(len(alpha)):
    alphanum[alpha[i]] = i

letter_state = defaultdict(lambda: np.zeros(50))

for i in range(50):
    for ltr in states[i]:
        letter_state[ltr] += np.array([1 if j == i else 0 for j in range(50)])
```

which takes $\approx 6\,\textrm{ms}.$ At the end of this, we're left with a map $f(\textrm{letter})\rightarrow \left{0,1\right}^{\otimes 50}$ of vectors $\mathbf{s}_\textrm{a},\ldots,\mathbf{s}_\textrm{z}.$

With that in hand, we just loop over the words and sum the vectors for each letter:

$$\mathbf{s}_\textrm{tatertot} = \mathbf{s}_\textrm{t} + \mathbf{s}_\textrm{a} + \mathbf{s}_\textrm{e} + \mathbf{s}_\textrm{r} + \mathbf{s}_\textrm{o}.$$

If all but one of the entries in $\mathbf{s}_\text{tatertot}$ are non-zero, then $\mathtt{tatertot}$ is a "mackerel". Accumulating each "mackerel" by the state it is a mackerel for:

```python
mackerel_states = defaultdict(lambda: 0)

for word in word_list:
    word_vec = np.zeros(50)

for ltr in word:
        word_vec += letter_state[ltr]
    zero_idx = np.where(word_vec == 0)[0]
    if len(zero_idx) == 1:
        mackerel_states[zero_idx[0]] += 1
```

and accessing the most flagrant state by how mackerel-full it is, `states[max(mackerel_states, key=mackerel_states.get)]`, we get $\texttt{ohio}$ which has $11342$ mackerel words. The code takes $\approx3.5\, \textrm{s}$ to run.

Reverse-sorting the word list by word length, we can quickly find that the longest mackerels are $\texttt{counterproductivenesses}$ which is mackerel for Alabama, and $\texttt{hydrochlorofluorocarbon}$ which is mackerel for Mississippi, both of which have $23$ letters.

<br>



