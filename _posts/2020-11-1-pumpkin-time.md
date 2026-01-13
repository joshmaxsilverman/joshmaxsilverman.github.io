---
layout: post
published: true
title: It's pumpkin time
date: 2020/11/1
subtitle: When does David S. Pumpkins boot you from the circle?
source: fivethirtyeight
theme: combinatorics
---

>**Question**: It's Halloween Eve and famous ambassador (ambassador of pumpkins) David S. Pumpkins has appeared out of the clear blue sky to invade your apartment complex's elevator. "Join me", he entices, for a few rounds of "Damn That's a Hot Pumpkin" his crazy new game that's been sweeping the nation. Altogether, there are $61$ people, including David S. Pumpkins himself.
>
> The rules are simple, everyone gets in a circle, including David S. Pumpkins, and starts counting from $1$ to a number $N$ that's specified by David S. Pumpkins himself. When his watch strikes "pumpkin time" the players start passing the pumpkin to the left, counting the numbers one by one, until they get to $N.$ When this happens, the person who said $N$ is eliminated, and the next round begins, starting with the person to their left.
>
> Distrusting of his pumpkin ways, you hang back and watch a few rounds from the wall. You see that the first person to be eliminated was $18$ positions to the left of David S. Pumpkins, the second person was $31$ positions to the left of whoever started their round, and the third person eliminated was the very person who began round three! What is the smallest value of $N$ for which this would be possible?
>
> After solving that, David S. Pumpkins proffers another: who will win this game?
>
> After solving that, David S. Pumpkins has had it up to here with other people winning his hot pumpkin games, and says "I'll show you how to do it!!1" Putting aside the constraints from the first two problems, what value of $N$ should David S. Pumpkins pick so that he himself is the person to win the game Damn That's a Hot Pumpkin?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/beware-the-hot-pumpkin/))

## Solution

_Disclaimer_: Through studious indifference, I have managed $\sim 3$ decades on Earth virtually undisturbed by any known results in number theory. So I am able to document here a voyage of personal discovery, stumbling through basic ideas about how the integer numbers relate to themselves.

![](/img/2020-11-1-david-s-pumpkins.JPG){:width=500px" class="image-centered"}

{:.caption}

David S. Pumpkins, the erstwhile host of Damn That's a Hot Pumpkin!

### The Pumpkin Shuffle

A round constitutes $N$ people counting themselves off around the circle until the last of them says $"N"$ and is eliminated for getting caught holding the David S. Pumpkin's hot pumpkin, and the next round begins with the person to their left. We're told that the first three people to be eliminated are positioned $18,$ $31,$ and $0$ positions to the left of the person who started their round and that there are $61$ people in the circle at the beginning of the game. 

**Note**: In this solution, I'm going to work in the zero index convention so that the person at the origin is person zero. The "real" $N$ will be $N^\prime = N + 1.$

Evidently, $N$ is bigger than the number of people, since it doesn't skip an equal number of people in the first three rounds. So, that counting $N$ positions ends the first round at position $18$ means that $N$ is equal to $18$ plus some number of multiples of the number of people, $P$. In other words

$$ N = 18 + \text{some integer}\times P. $$

Likewise, the other two facts lead to

$$\begin{align}
N &= 31 + \text{some other integer}\times (P - 1) \\
N &= 0 + \text{yet another integer}\times (P - 2).
\end{align}$$

This tells us a couple of things. The first is that there's a number $N$ that has remainders of $18,$ $31,$ and $0$ when divided by $61,$ $60,$ and $59,$ respectively. The second is that there are three equivalent representations for this number. 

My first instinct was to set them equal to each other to find a relationship between the undetermined integers. 

Before doing this, let's settle on some symbols. We'll call the remainders (like $18,$ $31,$ and $0$) $r_1,$ $r_2,$ and $r_3,$ and the modular bases (like $61,$ $60,$ and $59$) $n_1,$ $n_2,$ and $n_3.$ Also, we'll call the undetermined integers $x_1,$ $x_2,$ and $x_3.$

### Naive solution

The representation $r_1 + n_1\times x_1$ clearly has a remainder of $r_1$ when divided by $n_1$, just as the representation $r_2 + n_2\times x_2$ has remainder $r_2$ when divided by $n_2.$ What we want to find is a value for $x_1$ so that $r_1 + n_1\times x_1$ **also** has remainder $r_2$ when divided by $n_2.$

Setting the first two representations equal, and using the symbols laid out above, we have

$$\begin{align}
r_1 + n_1\times x_1 &= r_2 \mod n_2 \\
n_1\times x_1 &= \left(r_2 - r_1\right) + n_2\times x_2 \mod n_2
\end{align}$$

At this point it might seem like we could divide by $n_1$ and call it a day, but we want a solution in the integers, not in the reals. So we have to find an integer $n_1^{-1}$ such that $n_1 \times n_1^{-1} = 1$ modulo $n_2.$ In other words, $n_1^{-1}$ is the inverse of $n_1,$ modulo $n_2.$ 

So, if we can solve

$$m_1\times m_1^{-1} \equiv 1 \bmod n_2,$$ 

then we'll have

$$x_1 = n_1^{-1}\times\left(r_2 - r_1\right) \mod n_2.$$

Going back out of modulo $n_2$ we can add back $n_2x_2$ and, plugging into the first representation, we have

$$\begin{align}
N &= r_1 + n_1 \times x_1 \\
&= r_1 + n_1\times\left(n_1^{-1}\times\left(r_2 - r_1\right) + n_2\times x_2\right) \\
&= r_1 + n_1^{-1}n_1\left(r_2 - r_1\right) + n_1n_2x_2
\end{align}$$

We can check that this satisfies the first two remainder conditions. Since the second and third terms are proportional to $n_1,$ and so are zero modulo $n_1,$ it clearly has remainder $r_1$ then divided by $n_1.$ Since the last term is proportional to $n_2,$ the $n_1^{-1}n_1$ is $1$ modulo $n_2,$ the first and second terms boil down to $r_1 + \left(r_2 - r_1\right) = r_2$ modulo $n_2,$ as we wanted.

My plan was to then solve the second and third relations for $x_2$ in terms of $x_3$ and use it to generalize, but there's a problem. The inverse $n_1^{-1}$ is computed modulo $n_2.$ If we equate the third representation to the joint one, the inverse we calculate for $n_3$ will be modulo $n_2.$ We can perhaps consciously calculate it modulo $n_1n_3$ but then we realize we need to adjust the modulo for the calculation for $n_1^{-1}$ too. There is probably a way to adjust this approach, but it's not inherently symmetric to the fact that all three modulos are on the same footing.

This sent me back to the drawing board to look for a symmetric approach. 

### Once bitten, twice shy

Going back to the three relations, we have

$$
N = r_1 \bmod n_1 \,\mathbf{AND}\,N = r_2 \bmod n_2 \,\mathbf{AND}\, N = r_3 \bmod n_3.
$$

The problem with our last approach is that it put the constraints onto the same modulo two at a time. Once we put equations in the same modulo, we can do ordinary algebraic things like addition, subtraction, multiplication, and inversion. 

If we have an equation like $7 \bmod 5 = 2$ then, as long as $c$ is not a divisor of $5$ (or vice versa), it is automatically the case that $7c \bmod \left(5c\right) = 2.$ Multiplying by the same factor in front of and behind the $\bmod$ leaves the truth of the statement alone. 

We can use this as inspiration to put all three constraints into modulo $n_1n_2n_3.$ Multiplying the first equation by $n_2n_3,$ the second by $n_1n_3,$ and the third by $n_1n_2,$ we get

$$\begin{align}
Nn_2n_3 &= r_1n_2n_3 \bmod n_1n_2n_3 \\
Nn_1n_3 &= r_2n_1n_3 \bmod n_1n_2n_3 \\
Nn_1n_2 &= r_3n_1n_2 \bmod n_1n_2n_3.
\end{align}$$

With like modulo, we can add these equations so that

$$N\left(n_2n_3 + n_1n_3 + n_1n_2\right) = \left(r_1n_2n_3 + r_2n_1n_3 + r_3n_1n_2\right) \bmod n_1n_2n_3.$$

If we solve

$$\left(n_2n_3 + n_1n_3 + n_1n_2\right)\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}\equiv 1 \bmod n_1n_2n_3$$

for $\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}$ and multiply the joint relationship by it, then we can compute $N:$

$$N = \left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1} \left(r_1n_2n_3 + r_2n_1n_3 + r_3n_1n_2\right).$$

Note that this breaks if $\left(n_2n_3 + n_1n_3 + n_1n_2\right)$ is proportional to the modulo $n_1n_2n_3$ since $0$ has no inverse.

A short program can be used to find $\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}$

```python
(n_1, n_2, n_3) = (61, 60, 59)
inverse = 0
while True:
  inverse += 1
  if inverse * (n_1 * n_2 + n_2 * n_3 + n_3 * n_1) % (n_1 * n_2 * n_3) == 1:
    print(inverse)
    break
```

which yields $5399$ and can be plugged into the result for $N$ to find:

$$N = \overbrace{5399}^{\left(n_2n_3 + n_1n_3 + n_1n_2\right)^{-1}}\times\overbrace{\left(18\times60\times59 + 31\times59\times61 + 0\times59\times60\right)}^{\left(r_1n_2n_3 + r_2n_1n_3 + r_3n_1n_2\right)}\bmod 61\times60\times59 = 136231$$

making the "real" $N$ equal to $\boxed{N^\prime = N + 1 = 136232}$ adjusting for our convention.

This is the minimal value of $N^\prime,$ but in general we can add any multiple of $n_1\cdot n_2\cdot n_3$ so that

$$N^\prime = 136232 + 215940\cdot x.$$

### Who is the champion, my friend?

The extra credit asks who would actually win the game if we use this minimal value for $N?$ Since the constraints are expressed in the form "the person $M$ positions to the left of the starting point was eliminated", we've been able to remain blissfully ignorant of the fact that one index disappears every round. 

In the forward problem, we do indeed have to keep track of indices. For example, if there are $P = 6$ players to begin, and $N=4$ then the pumpkin will start with player $1$, go to player $4$, and take player 4 out of the system:

$$\mathbf{1} 2 3 4 5 6 \rightarrow 1 2 3 \mathbf{4} 5 6 \rightarrow 1 2 3 \mathbf{5} 6$$

In the next round, the pumpkin will start with player 5, move to player 2, and take player 2 out of the system

$$1 2 3 \mathbf{5} 6 \rightarrow 1 \mathbf{2} 3 5 6 \rightarrow 1 3 5 6.$$

The next round will go 

$$1\mathbf{3}56\rightarrow \mathbf{1}356\rightarrow 356.$$

The round after that will go 

$$\mathbf{3}56\rightarrow \mathbf{3}56\rightarrow 56.$$

and the final round will go

$$5\mathbf{6}\rightarrow 5\mathbf{6}\rightarrow 5.$$

The thought of tracking the changing circle, which numbers remain, and which slots they're in is a fright indeed. But why tear down when we can build? Indeed, if we had a movie of the hot pumpkin game, we could play it in reverse and predict where new players would appear. By doing things this way, it's easier to think about.

No matter what, we start with the winner, who we represent by

$$\star$$

We know that in the step before, we had another player $\mathbf{A},$ who we can place to the left (or right) of $\star$ (at this point it doesn't matter since things are rotationally symmetric), so we have

$$\mathbf{A}\star$$

Now, in the step before that, we had a third player $\mathbf{B}.$ To figure out where $\mathbf{B}$ was, we have to figure out where the final round began. If $N\bmod 2 = 0,$ then it started with $\star,$ meaning that player $\mathbf{B}$ was $0$ steps to the left of $\star$ when they were eliminated. On the other hand, if $N\bmod 2 = 1,$ then it started with $\mathbf{A},$ meaning that player $\mathbf{B}$ was $1$ step to the right of $\star$ when they were eliminated.  This brings us to

$$\mathbf{A}\mathbf{B}\star$$

Now, we have to place player $\mathbf{C}$ back into the circle. We take $4$ steps back modulo $P = 3$ (the current number of players) and get $4\bmod3=1,$ meaning they were $1$ step to the left of where we just placed $\mathbf{B}$:

$$\mathbf{A}\mathbf{C}\mathbf{B}\star$$

To place player $\mathbf{D},$ we take $4$ steps back modulo $P=4$ and get $4\bmod4=0$ meaning the were also standing $1$ step to the left of $\star$ when they were eliminated. We have

$$\mathbf{A}\mathbf{C}\mathbf{D}\mathbf{B}\star$$

To place $\mathbf{E},$ we take $4$ steps back modulo $5$ which is $4\bmod5=4,$ which brings us to $\left(1 + 4\right) \bmod 5 = 0$ steps to the left of $\star.$ In other words, $\mathbf{E}$ is directly to the left of $\star,$ bringing us to

$$\mathbf{A}\mathbf{C}\mathbf{D}\mathbf{B}\mathbf{E}\star$$

The last step is to find the absolute position of $\mathbf{E}.$ Since the first step eliminates $\mathbf{E},$ the position of $\mathbf{E}$ is simply $4\bmod 6 = 4$ which means that $\star$ is at position $5$ (since it's directly to the right of $\mathbf{E}$). So, the survivor is player $5,$ as we found above. 

Translating the position bookkeeping from above into modular arithmetic, we found that the position of $\star$ is equal to

$$\left(\left(\left(\left(\left(\left(4 + 0\right)\bmod 1 + 4\right)\bmod 2 + 4\right)\bmod 3 + 4\right)\bmod 4 + 4\right) \bmod 5 + 4\right) \bmod 6$$

Coding this up, we have (using the minimal $N$ from the main problem)

```python
N = 136232
def pumpkin_champ_offset(players):
  if players == 1:
    return 0
   else:
    return (N + pumpkin_champ_offset(players - 1)) % players
```

which gives `57` to the left of player $1,$ i.e. player $\boxed{\text{player }58}.$

### A win for David S. Pumpkins?

The second extra credit asks (abandoning the three constraint equations) what is the smallest value of $N$ that will lead to player $1$, i.e. David S. Pumpkins himself, winning. 

Now we have to vary $N$ so we slightly redefine `pumpkin_champ_offset()`:

```python
def pumpkin_champ_offset(players, N):
    if players == 1:
        return 0
    else:
        return (N + pumpkin_champ_offset(players - 1, N)) % players

N = 1
while True:
    N += 1
    if pumpkin_champ_offset(61, N) == 0:
        print("The minimal N is " + str(N))
        break
```

Which returns $\boxed{N = 140}$ as the minimal $N$ for which player $1$ wins.

<br>
