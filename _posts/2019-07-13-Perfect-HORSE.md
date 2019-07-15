---
layout: post
published: true
title: Perfect HORSE
date: 2019/07/13
---

>Two players have taken to the basketball court for a friendly game of HORSE. The game is played according to its typical playground rules, but here’s how it works, if you’ve never had the pleasure: Alice goes first, taking a shot from wherever she’d like. If the shot goes in, Bob is obligated to try to make the exact same shot. If he misses, he gets the letter H and it’s Alice’s turn to shoot again from wherever she’d like. If he makes the first shot, he doesn’t get a letter but it’s again Alice’s turn to shoot from wherever she’d like. If Alice misses her first shot, she doesn’t get a letter but Bob gets to select any shot he’d like, in an effort to obligate Alice. Every missed obligated shot earns the player another letter in the sequence H-O-R-S-E, and the first player to spell HORSE loses.
>
>Now, Alice and Bob are equally good shooters, and they are both perfectly aware of their skills. That is, they can each select fine-tuned shots such that they have any specific chance they’d like of going in. They could choose to take a 99 percent layup, for example, or a 50 percent midrange jumper, or a 2 percent half-court bomb.
>
>If Alice and Bob are both perfect strategists, what type of shot should Alice take to begin the game?

>What types of shots should each player take at each state of the game — a given set of letters and a given player’s turn?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/i-would-walk-500-miles-and-i-would-riddle-500-more/))

## Solution

It's tempting to think that the optimal strategy when it's her turn is for Ann to maximize the chance that she will make a shot that Bob will miss.  That chance is $p(1-p)$ (where $p$ is the probability of making the shot), which is maximized at $p = 1/2$.  However, this underplays the costly risk of losing her turn. It turns out to be optimal for Ann to be extremely risk-averse, and to rack up more letters for Bob over very long turns than she'd manage over shorter ones.

Whenever it's her turn, what Alice really wants is to maximize the expected number $E$ of letters Bob will gain before it's next his turn. When Ann shoots, there is probability $1-p$ that she misses and Bob gets the next turn, having gained zero letters. There is probability $p$ that she makes the shot, in which case she expects Bob to gain $1-p$ (the chance of his missing) letters with his follow-up shot, after which she is back to expecting Bob to gain $E$ more letters before his next turn. (There's a subtle complication involving game endings here, which I won't go into except to say that we can avoid it by harmlessly assuming that play continues after the winner is determined, until the winner misses a shot.) Therefore:

$$E = (1-p)\times 0 + p \times ((1-p) + E)$$

Solving for $E$ requires dividing by $1-p$, which is fine because we know that $p$ cannot be $1$ (the game would never end). Deploying the mighty Algebra, we find that $E = p$. This means that Ann's best move is always to take a shot that she's nearly certain to make. It also means that there is no truly optimal strategy, since there is no maximal probability less than $1$.

Now let's ask how likely Ann is to win, if both she and Bob adopt shot probability $p$. Let $P(a,b,t)$ be the probability that Ann wins if she currently has $a$ letters, Bob has $b$, and is is player $t$'s turn (let Ann be $A$ and Bob $B$). We know that $P(a,5,t) = 1$ for $0 \leq a \leq 4$ and similarly $P(5,b,t) = 0$ for $0 \leq b \leq 4$. Since the three possible outcomes of a shot are a miss (the turn changes hand), a make followed by the other player's miss (the other player gets a letter), and a make followed by a make (nothing changes), for all other $a$ and $b$:

$$P(a,b,A) = (1-p)P(a,b,B) + p(1-p)P(a,b+1,A) + p^2P(a,b,A)$$

$$P(a,b,B) = (1-p)P(a,b,A) + p(1-p)P(a+1,b,B) + p^2P(a,b,B)$$

And the Algebra Ex Machina gives us:

$$P(a,b,A) = \frac{P(a,b+1,A) + (1+p)P(a+1,b,B)}{2+p}$$

$$P(a,b,B) = \frac{P(a+1,b,B) + (1+p)P(a,b+1,A)}{2+p}$$

These equations allow us to calculate (I used a [spreadsheet](https://docs.google.com/spreadsheets/d/1kGWdQ5Qp9x__X9toe-Qa8vhY1zJXm0qt4A9vs0d7qDM/edit?usp=sharing) all $50$ remaining values of $P(a,b,t)$, including ultimately $P(0,0,A)$, which is Ann's probability of victory. With a value of $p$ very near $1$, this comes out to approximately $.5488$.

<br>
