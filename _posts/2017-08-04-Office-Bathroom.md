---
layout: post
published: true
title: Office Restroom
date: 2017/08/04
---

>There is a bathroom in your office building that has only one toilet. There is a small sign stuck to the outside of the door that you can slide from “Vacant” to “Occupied” so that no one else will try the door handle (theoretically) when you are inside. Unfortunately, people often forget to slide the sign to “Occupied” when entering, and they often forget to slide it to “Vacant” when exiting.
>
>Assume that 1/3 of bathroom users don’t notice the sign upon entering or exiting. Therefore, whatever the sign reads before their visit, it still reads the same thing during and after their visit. Another 1/3 of the users notice the sign upon entering and make sure that it says “Occupied” as they enter. However, they forget to slide it to “Vacant” when they exit. The remaining 1/3 of the users are very conscientious: They make sure the sign reads “Occupied” when they enter, and then they slide it to “Vacant” when they exit. Finally, assume that the bathroom is occupied exactly half of the time, all day, every day.
>
>Two questions about this workplace situation:
>
>1. If you go to the bathroom and see that the sign on the door reads “Occupied,” what is the probability that the bathroom is actually occupied?
>2. If the sign reads “Vacant,” what is the probability that the bathroom actually is vacant?
<!--more-->

[(fivethirtyeight.com)](https://fivethirtyeight.com/features/is-this-bathroom-occupied/)

## Solution

### Part 1

We are seeking $P(O\|“O")$, which is the conditional probability that the bathroom is occupied given that the sign reads “Occupied." By the definition of conditional probability: 

$$P(O | “O") = \frac{P(O \& “O")}{P(“O")}$$

Start with the numerator. Label the three types of users $A$, $B$, and $C$, letting $O_A$ mean the bathroom is occupied by a type-$A$ user (and so on). Because if the bathroom is now occupied by a type-A user the sign reads whatever it was last set to read by a previous sign-setting user, who is equally likely to be of types $B$ or $C$, the chance it now reads “Occupied" is $1/2$. So:

$$P(O \& “O") = P(O_A \& “O") + P(O_B \& “O") + P(O_C \& “O") $$

$$ = P(“O" | O_A)P(O_A) + P(“O" | O_B)P(O_B) + P(“O" | O_C)P(O_C)

$$= \frac{1}{6} \cdot \frac{1}{2} + \frac{1}{6} \cdot 1 + \frac{1}{6} \cdot 1 = \frac{5}{12}$$

Now $P(“O")$ is $P(“O" \& O)$ plus $P(“O" \& \neg O)$. And $P(“O" \& \neg O)$ is the chance that the bathroom is unoccupied and the previous user left the sign reading “Occupied". The chance that the bathroom is unoccupied and the latest user was of any given type is $1/6$. So, (where $L_A$ means that the bathroom is unoccupied and the latest user was of type $A$, etc.):

$$P(“O" \& \neg O) = P(“O" \& L_A) + P(“O" \& L_B) + P(“O" \& L_C)$$

$$= P(“O" | L_A)P(L_A) + P(“O"|L_B)P(L_B) + P(“O" | L_C)P(L_C)$$

$$ = \frac{1}{2}\cdot \frac{1}{6} + 1\cdot\frac{1}{6} +
0\cdot\frac{1}{6} = \frac{1}{4}$$

So $P(“O")$ is $5/12$ plus $1/4$, or $2/3$. And:

$$P(O|“O") = \frac{P(O \& “O")}{P(“O")}
=  \frac{\frac{5}{12}}{\frac{2}{3}} = \frac{5}{8}$$

### Part 2

Proceeding analogously to Part 1:

$$P(V|“V") = \frac{P(V \& “V")}{P(“V")}$$

Now, $P(“V")$ is $1$ minus $P(“O")$, or $1/3$.

And the chance the bathroom is vacant and the sign reads “Vacant" is based on the chance that the previous user left the sign reading that way. Because the chance a type-$A$ user would do so is again $1/2$:

$$P(V \& “V") = P(V_A \& “V") + P(V_B \& “V") + P(V_C \& “V") $$

$$= \frac{1}{6} \cdot \frac{1}{2} + \frac{1}{6} \cdot 0 + \frac{1}{6} \cdot 1 = \frac{1}{4}$$

And so:

$$P(V|“V") = \frac{\frac{1}{4}}{\frac{1}{3}} = \frac{3}{4}$$


<br>
