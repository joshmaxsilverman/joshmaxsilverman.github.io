---
layout: post
published: false
title: Birthday collisions
date: 2022/10/15
subtitle:
tags:
---

>Question

<!--more-->

([FiveThirtyEight](URL))

## Solution

I found three ways to solve this problem: by approximation, counting through recursion, and counting through combinatorics.

The first way is the most insightful and helps reveal what the exact solutions add to the picture, so we'll start there.

## Approximate argument

An exact way to treat the birthday twin case is to multiply the probability that the second person doesn't collide with the first $(1-1/365),$ with the probability that the third person doesn't collide with the first two $(1-2/365)$ and so on up to the $n^\text{th}$ person. The resulting expression is exact and at some point falls below $50%$ giving us the answer for birthday twins.

Each term in the product $(1-j/365)$ is approximately equal to $e^{-j/365}$ and so we can add up all the exponents $\frac{1}{365}\left(1 + 2 + \ldots + n\right) = n(n-1)/2$ and we end up with $P(\text{no collisions in }n\text{ people}) \approx e^{-n^2/(2!\cdot 365)}.$ This is nice but, but the logic doesn't easily extend to triplets and above.

A more audacious way to get the same result is to think about pairs. As long as no pair of people in the room share the same birthday, we keep adding new people. Among $n$ people there are $\binom{n}{2}$ possible pairs and the chance that any given pair has a collision is $\frac{1}{365},$ so the probability of no collisions among $n$ people is approximately

$$\left(1-\frac{1}{365}\right)^\binom{n}{2} \approx e^{-\dbinom{n}{2}/365}$$

The probability of **having** a collision among $n$ (or fewer) people is then $\text{cdf}(n) = 1 - e^{-\dbinom{n}{2}/365}.$

To find the average amount of people at which the collision first appears $n^*$, we can get the $\text{pdf}$ by differentiating the $\text{cdf}$

$$\text{pdf}(n) = \text{cdf}^\prime(n) \approx \dfrac{n}{365}e^{-n^2/(2!\cdot365)}.$$

The expected value of $n^*$ is then $\int\limits_0^{365+1}dn\ n\ \text{pdf}(n),$ or

$$
    \frac{1}{365}\int\limits_0^{365+1}dn\ n^2 e^{-n^2/(2!\cdot 365)}
$$

We can clean this up in a few ways. First of all, the exponential is basically dead by $n=366$ so we can make the upper bound $\infty$ without losing much accuracy. Second, we substitute $\beta = n^2/(2!\cdot 365)$ so that $d\beta = \frac{1}{365}n\ dn.$ With this, the integral becomes

$$
    \sqrt{2\cdot 365} \int\limits_0^\infty d\beta\ \sqrt{\beta}e^{-\beta}
$$

The integral is just the gamma function of $3/2$ so we get $n^* = \sqrt{2\cdot365}\gamma(3/2) = \sqrt{365\pi/2}$ which is approximately $23.94$

The same logic extends to triplets, quadruplets, and so on. For triplets, $n^*$ is 

$$
    \int\limits_0^{2*365+1}dn\ \frac{n^3}{2!\cdot 365^2} e^{-n^3/(3!\cdot 365^2}
$$

which, after a simular substitution, becomes

$$
  n^* \approx \sqrt[3]{3!}365^{2/3}\gamma(4/3) \approx 82.87
$$

As we'll see, the true value for birthday twins is about $24.62$ and for birthday triplets it is $88.74,$ so these aren't perfect, but they aren't too bad either.

## Recursion

We can simplify our thinking about the problem by finding a good way to describe the states. On the way to having doublets, a number has to be a singlet. Likewise, on the way to being a triplet, a number has to be a doublet. 

These are the macroscopic states we care about (how many singlets, doublets, and so on, that there are) not the specific numbers that are chosen. So, we can track the probability of states $(s, d).$ 

Each time we add a number, we can either pick a number that hasn't been chosen before $(s-1,d)\rightarrow(s,d)$ or pick a number that's currently a singlet $(s+1,d-1)\rightarrow(s,d).$

The probability of these events are $(365-(s-1)-d)/365)$ and $d/365,$ respectively.

The recursion is then

$$
P(s,d) = \dfrac{365-(s-1)-d}{365}P(s-1,d) + \dfrac{d}{365}P(s+1,d-1)
$$

With the base conditions of $P(0,0)=1$ and $P(s,d) = 0$ whenever $s$ or $d$ is less than zero.

As a sanity check, we can look at $P(s,0)$ as $s$ varies. As expected, it crosses $50%$ at $s=23.$

To find the probability that a room with $n$ people has no birthday triplets, we have to add up all the ways that $n$ people could have no triplets. For $n=5$ people, the relevant states are $(s,d) = (5,0),$ $(3,1),$ and $(1,2)$ corresponding to $5$ singlets, $3$ singlets plus $1$ pair of twins, and $1$ singlet plus $2$ pairs of twins.

So, the probability that there are no triplets in a group of $n$ or fewer people is 

$$
  \sum_{d=0}^{n/2} P(n-d, d)
$$

As before this is a cumulative probability ($\text{cdf}$), so the probability that the triplet first appears at $n$ people is $P(n-1) - P(n).$

To  dddd find the average $n^*$ we just sum

$$
  \sum\limits_{n=0}^{2\cdot 365+1} n\left[P(n-1) - P(n)\right]
$$ 

which is 

$$
n^* = \tfrac{188410800397516187399717065559037643830104811782677159115798873065426233643344881488297556659768225376857801014708780098231693129034794219061782328302736745996019262934317072871513609024966990149703977680765646997721439651174737983482772543346613862043047213432404687916815370111920464683273051476731788727278791656986688978131624635636809162183671539275622070083174154780244162282237255688364342656255187162264057523043944266115896563397162573107191448139181814293088129584723003717408509127290384960952228136228359361667292183342928834184420605078666184342989499478510278755755473909375074337802823223612531214656284387560467869873745906416510212353604520401788975806028716441073493463365675804015119323572436939590052364441857513996149806932959911540512374309693946591919660667917383946762549171980557462158154169309657995907945323927099907604222423925577536847578535300897265904177367453992908159846242437147456840105398991801959546186312013325212954955689979477808324812148857819805952861281831587795668738283226806010450597088072854856358582648503445167409058982431455439966032044163463263590998170583531790992966295970532797973472382034157707149489931480317891895521423982713688291133192835491592486992871506266907256368403452510277473471933135457542607783443107537439861184380281782020507915046030887210144588788653401371538489918192601873905853629908428123394376427982863592959412130731477062380606303382827950850832205560156001899527181186888633762899385710341946099772643584412721428603742669611312414064482763731890597804396868043414671308366071388400264334401597408244377102146383757427930847978088334778291999917034503310268841357409124922957868464591233665853422591623936306251148033219550563497627612490079328627}{2123203723752335612386864541924713246245441548614385365874970681741401872669102623700271859014642343953033377466238466087563497942632339799850756007044261204346921261249922297824073822626164035479024054388309466046581219604558694050587413617229131646076169992804402714852356317313123002908526730573063772478607604339880591503326321429373604501364528890410347316414297861320024860246618548558309878305162032453170909455940416698859953123942444918387682220339205377667138322741793224711547844412338703747581228612348462544698183915901866413733452439441910511575217672959294966435294830350005255669696818511354952878861356240172363648141446785018390166382675878779562992066881472626019112836454149177181669280421812042565272856619940480414504689454936035624738667458737403913154314889833755680197599978215743573756515984348932567378332208212345397601358294277702260837583644460588112466576778447149653608610915505764945513814890969928355575362644929355514030552952821007428993332203479947526503146305661614626918240776661469539038670793998904685182176280928327878095214611250992115838903852601036561974912503886432360171354004615228457432729902324111806947686486434399224645654284824891914165886913568219089525886370560507861088803871397808615691959235207246510530309208495202194481240848755268641285280837659934122691961083280550256407249141195622251256297401838643019809582516493847537821715158807686405104747401969813673611392812149077560700943045147394324026376941535654090030604149382984083201751314907094173247232265707260032946186592039798617157710524585827543372330527006334630245663454673797687021352793263405483458372190603650557065400468086190157234317395880863765422493950473133150769200483409804292023181915283203125}
$$
<br>
