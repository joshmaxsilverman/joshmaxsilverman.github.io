---
layout: post
published: true
title: Spelling Bee
date: 2020-01-05
---

>The New York Times recently launched some new word puzzles, one of which is Spelling Bee. In this game, seven letters are arranged in a honeycomb lattice, with one letter in the center. The goal is to identify as many words that meet the following criteria: The word must be at least four letters long. The word must include the central letter. The word cannot include any letter beyond the seven given letters.
>Note that letters can be repeated. For example, the words GAME and AMALGAM are both acceptable words. Four-letter words are worth 1 point each, while five-letter words are worth 5 points, six-letter words are worth 6 points, seven-letter words are worth 7 points, etc. Words that use all of the seven letters in the honeycomb are known as “pangrams” and earn 7 bonus points (in addition to the points for the length of the word). 
>
>Which seven-letter honeycomb results in the highest possible game score? To be a valid choice of seven letters, no letter can be repeated, it must not contain the letter S (that would be too easy) and there must be at least one pangram.

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/))

## Solution

This is a computational problem, so I'll let the code mostly speak for itself. A brute-force approach is feasible because there are "only" about 56,000 possible bees. The requirement that there be at least one pangram is what really constrains that number down from the millions that otherwise would be possible. There are about 8,000 sets of seven letters that yield pangrams (call these pangram-sets), and we only need to determine the words that are generable from each of them. Our approach, then, is to find all pangram-sets, and then to assign to each of them a list of all the words that can be formed from its letters. Finally, for each pangram-set we score the seven bees that can be made from it, and we report the over-all winner. 

The code and output is supplied below. The winning bee, which produces 537 words for a score of 3,898, has letters AEGINRT, with R in the center.

Note: there were errors in the originally posted code; see the comments below.

```python
# Find the highest possible score for the NYT Spelling Bee game, using a supplied
# word list as the dictionary. Runs in 23.3sec in pypy (a fast way to run
# python code) on an older PC.

wordsFile = "538Words.txt"

# Return sorted tuple of distinct letters in the word
def lettersIn(word):
  letters = list(set(word))
  letters.sort()
  return tuple(letters)

# Get list of bee-possible words
wordsList = []
with open(wordsFile,'r') as wordsFile:
  for word in wordsFile:
    word = word[:-1] # pare trainling newline character
    if len(word) >= 4 and len(set(word)) <=7 and not 's' in word:
      wordsList.append(word)

# Find all words with exactly 7 distinct letters; these can be pangrams, and every
# bee uses such a set of letters.
letterClusters = []
used = []
for word in wordsList:
  letters = lettersIn(word)
  if len(letters) == 7 and not letters in used:
      letterClusters.append( \
        { 'letterTuple': letters,\
        'letterSet': set(letters),\
        'wordList': [] } \
        )
      used.append(letters)

# This takes the bulk of run time. Looping over words first saves a bunch of 'set' calls.
for word in wordsList:
  letters = set(word)
  for cluster in letterClusters:
    if letters.issubset(cluster['letterSet']):
      cluster['wordList'].append(word)

# Score a bee: words are worth their length plus 7 for a pangram
def score(cluster,centerLetter):
  s = 0
  for word in cluster['wordList']:
    if centerLetter in word:
      if len(word) == 4:
        s+= 1
      else:
        s += len(word)
      if len(set(word)) == 7:
        s += 7
  return s

# Score all bees, i.e., all pangram 7-tuples and all choices of center letter
highestSoFar = {'score':0}
for cluster in letterClusters:
  for centerLetter in cluster['letterTuple']:
    s = score(cluster,centerLetter) 
    if s > highestSoFar['score']:
      highestSoFar = {'score': s,\
       'letterTuple': cluster['letterTuple'],\
       'centerLetter': centerLetter,\
       'wordList': cluster['wordList']}

# Report results
print 'Maximum score is', highestSoFar['score'], 'for the bee [(letters), center letter]:'
print highestSoFar['letterTuple'], ',', highestSoFar['centerLetter']
words = [ word for word in highestSoFar['wordList'] if highestSoFar['centerLetter'] in word ]
print 'This bee has', len(words), 'words:'
for i in range(len(words)):
  if len(set(words[i])) == 7:
    print words[i].upper(), "",
  else:
    print words[i], "",
  if ((i+1)/7.0).is_integer():
    print ""
print ""

# The output:
# Maximum score is 3898 for the bee [(letters), center letter]:
# [('a', 'e', 'g', 'i', 'n', 'r', 't'), 'r']
# This bee has  537 words:
# aerate  AERATING  aerie  aerier  agar  ager  agger  
# aggregate  AGGREGATING  aginner  agrarian  agree  agreeing  agria  
# aigret  aigrette  airer  airier  airing  airn  airt  
# airting  anear  anearing  anergia  angaria  anger  angering  
# angrier  anteater  antiair  antiar  antiarin  antra  antre  
# area  areae  arena  arenite  arete  argent  ARGENTINE  
# ARGENTITE  arginine  aria  arietta  ariette  arraign  arraigning  
# arrange  arranger  arranging  arrant  arrear  arrearage  artier  
# atria  attainer  attar  attire  attiring  attrite  eager  
# eagerer  eagre  earing  earn  earner  earning  earring  
# eater  eerie  eerier  eger  eggar  egger  egret  
# engager  engineer  engineering  engirt  engrain  engraining  enrage  
# enraging  enter  entera  enterer  entering  entertain  entertainer  
# ENTERTAINING  entire  entrain  entrainer  ENTRAINING  entrant  entreat  
# ENTREATING  entree  ergate  erne  errant  errata  erring  
# etagere  eterne  gager  gagger  gainer  gaiter  ganger  
# gangrene  gangrening  garage  garaging  garget  garner  garnering  
# garnet  garni  GARNIERITE  garret  garring  garter  GARTERING  
# gear  gearing  genera  generate  GENERATING  genre  gerent  
# getter  gettering  ginger  gingering  ginner  ginnier  girn  
# girning  girt  girting  gittern  gnar  gnarr  gnarring  
# GNATTIER  grain  grainer  grainier  graining  gran  grana  
# grange  granger  granita  GRANITE  grannie  grant  grantee  
# granter  granting  grat  grate  grater  gratin  GRATINE  
# GRATINEE  GRATINEEING  grating  great  greaten  GREATENING  greater  
# gree  greegree  greeing  green  greener  greengage  greenie  
# greenier  greening  greet  greeter  greeting  gregarine  greige  
# grig  grigri  grin  grinner  grinning  grit  grittier  
# gritting  igniter  inaner  inerrant  inert  inertia  inertiae  
# ingrain  ingraining  INGRATE  INGRATIATE  ingratiating  inner  integer  
# INTEGRATE  INTEGRATING  intenerate  INTENERATING  inter  INTERAGE  INTERGANG  
# intern  interne  internee  interning  INTERREGNA  interring  intertie  
# intrant  intreat  INTREATING  intrigant  irate  irater  iring  
# irrigate  irrigating  irritant  irritate  irritating  iterant  iterate  
# ITERATING  itinerant  itinerate  ITINERATING  nagger  naggier  naira  
# narine  narrate  narrater  narrating  natter  NATTERING  nattier  
# near  nearer  nearing  neater  negater  netter  nettier  
# nigger  niter  niterie  nitrate  nitrating  nitre  nitrite  
# nittier  raga  rage  ragee  raggee  ragging  ragi  
# raging  ragtag  raia  rain  rainier  raining  ranee  
# rang  range  ranger  rangier  ranging  rani  rant  
# ranter  ranting  rare  rarer  raring  ratan  ratatat  
# rate  rater  ratine  rating  ratite  rattan  ratteen  
# ratten  rattener  RATTENING  ratter  rattier  ratting  reagent  
# reaggregate  REAGGREGATING  reagin  rear  rearer  rearing  rearrange  
# rearranging  reata  reattain  REATTAINING  reearn  reearning  reengage  
# reengaging  reengineer  reengineering  reenter  reentering  reentrant  regain  
# regainer  regaining  regatta  regear  regearing  regenerate  REGENERATING  
# regent  reggae  regina  reginae  regna  regnant  regrant  
# REGRANTING  regrate  REGRATING  regreen  regreening  regreet  regreeting  
# regret  regretter  regretting  reign  reigning  reignite  reigniting  
# rein  reining  reinitiate  REINITIATING  REINTEGRATE  REINTEGRATING  reinter  
# reinterring  reiterate  REITERATING  renege  reneger  reneging  renig  
# renigging  renin  renitent  rennet  rennin  rent  rente  
# renter  rentier  renting  reran  rerig  rerigging  retag  
# RETAGGING  retain  retainer  RETAINING  retarget  RETARGETING  rete  
# retear  RETEARING  retene  retia  retiarii  retie  retina  
# retinae  retine  retinene  retinite  retint  retinting  retirant  
# retire  retiree  retirer  retiring  retrain  RETRAINING  retreat  
# retreatant  retreater  RETREATING  retting  riant  riata  rigger  
# rigging  ring  ringent  ringer  ringgit  ringing  rinning  
# rite  ritter  tagger  tagrag  tanager  TANGERINE  TANGIER  
# tanner  tantara  tantra  tare  targe  target  TARGETING  
# taring  tarn  tarre  tarrier  tarring  tart  tartan  
# tartana  tartar  tarter  tarting  tartrate  tatar  tater  
# tatter  TATTERING  tattier  tear  tearer  tearier  TEARING  
# teenager  teener  teenier  teeter  teetering  tenner  tenter  
# tentering  tentier  terai  terete  terga  tergite  tern  
# ternate  terne  terra  terrae  terrain  terrane  terraria  
# terreen  terrene  terret  terrier  terrine  territ  tertian  
# tetra  tetter  tiara  tier  tiering  tiger  tinier  
# tinner  tinnier  tinter  tire  tiring  titer  titrant  
# titrate  titrating  titre  titter  titterer  tittering  tragi  
# train  trainee  trainer  training  trait  treat  treater  
# TREATING  tree  treeing  treen  tret  triage  triaging  
# triene  triennia  trier  trig  trigger  triggering  trigging  
# trine  trining  trinitarian  trite  triter  
# [Finished in 23.3s]
```

<br>