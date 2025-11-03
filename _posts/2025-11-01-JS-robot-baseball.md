---
layout: post
published: true
title: Robot Baseball
date: 2025/11/01
subtitle: How common can league office scheming rig full counts to be?
tags: nash-equilibria optimization
---

>**Question**: 

> The Artificial Automaton Athletics Association (Quad-A) is at it again, to compete with postseason baseball they are developing a Robot Baseball competition. Games are composed of a series of independent at-bats in which the batter is trying to maximize expected score and the pitcher is trying to minimize expected score.
>
> An at-bat is a series of pitches with a running count of balls and strikes, both starting at zero. For each pitch, the pitcher decides whether to throw a ball or strike, and the batter decides whether to wait or swing; these decisions are made secretly and simultaneously. The results of these choices are as follows.
>
> - If the pitcher throws a ball and the batter waits, the count of balls is incremented by $1.$
> - If the pitcher throws a strike and the batter waits, the count of strikes is incremented by $1.$
> - If the pitcher throws a ball and the batter swings, the count of strikes is incremented by $1.$
> - If the pitcher throws a strike and the batter swings, with probability $p$ the batter hits a home run and with probability $(1-p)$ the count of strikes is incremented by $1.$
>
> An at-bat ends when either:
>
> - The count of balls reaches $4,$ in which case the batter receives $1$ point.
> - The count of strikes reaches $3,$ in which case the batter receives $0$ points.
> - The batter hits a home run, in which case the batter receives $4$ points.
>
> By varying the size of the strike zone, Quad-A can adjust the value $p,$ the probability a pitched strike that is swung at results in a home run. They have found that viewers are most excited by at-bats that reach a full count, that is, the at-bats that reach the state of three balls and two strikes. Let $q$ be the probability of at-bats reaching full count; $q$ is dependent on $p.$ Assume the batter and pitcher are both using optimal mixed strategies and Quad-A has chosen the $p$ that maximizes $q.$ Find this $q,$ the maximal probability at-bats reach full count, to ten decimal places.

<!--more-->

([Jane Street](https://www.janestreet.com/puzzles/robot-baseball-index/))

## Solution

the value of count $(b,s)$ is the average value of the counts it can move to. a strike can be added if the pitcher throws a strike and the batter doesn't swing, or if the pitcher throws a ball and the batter swings, or if the pitcher throws a strike and the batter misses. a ball can be added if the pitcher throws one and the batter doesn't swing. finally, the batter can walk or hit a homerun which have values $1$ and $4$. 

$$ \begin{align} V(b,s) &= P_\text{strike}P_\text{swing}pV_\text{HR} \\ \,& + \left[P_\text{strike}(1-P_\text{swing}) + (1-P_\text{strike})P_\text{swing} + P_\text{strike}P_\text{swing}(1-p) \right]V(b,s+1) \\ &+ (1-P_\text{strike})(1-P_\text{swing})V(b+1,s) \end{align} $$

with any $4$-ball count equal to $1$ and any $3$-strike count equal to zero.

$$
	\begin{align}
		V(4,x) &= 1 \\
		V(x,3) &= 0
	\end{align} 
$$

this is a recursion relating the value of each count to the value of the outcomes it can lead to. but at each step the pitcher and batter can set the probabilities however they like, so they'll change with the count. 

however, we know the batter is trying to maximize the value of the at bat while the pitcher is trying to minimize it. this means the batter will pick $P_\text{swing}$ so that the value is indifferent to a change in $P_\text{strike}$ so they will set according to 

$$ \frac{\partial V(b,s)}{\partial P_\text{strike}} = 0, $$ 

and vice versa for the pitcher 

$$ \frac{\partial V(b,s)}{\partial P_\text{swing}} = 0. $$

somewhat surprisingly, the value function is symmetric with respect to $P_\text{strike}$ and $P_\text{swing},$ so they'll set their probabilities to the same equilibrium value. solving these, we can find this optimal probability in terms of the expected values of the future states. 

this gets us 

$$ P_\text{strike}(b,s) = P_\text{swing}(b,s) = \frac{V(b,s+1) - V(b+1,s)}{pV(b,s+1) - V(b+1,s)-pV_\text{HR}}$$

plugging this back in to the recursion, we get 

$$ V(b,s) = \frac{\left(pV_\text{HR} + (1-p)V(b,s+1)\right)V(b+1,s)-V(b,s+1)^2}{pV_\text{HR}+(1-p)V(b,s+1) + V(b+1,s)]}$$

which lets us compute the expected value of each state. 

```wolfram
Vhomerun = 4;
V[4, _] = 1;
V[_, 3] = 0;
V[b_, s_] :=
  V[b, s] =
   (-V[b, 1 + s]^2 + (p Vhomerun - (-1 + p) V[b, 1 + s]) V[1 + b, s]) /
(p Vhomerun - (1 + p) V[b, 1 + s] + V[1 + b, s]);
```

![](/img/2025-11-03-JS-robot-baseball-V-exp.png){:width="450 px" class="image-centered"}

but what's the probability that we get to a particular state? it's the chance that we get to each predecessor times the chance they transition to the current state. since walks, homeruns, and outs are terminal states that can't transition to the full count, we can ignore them for this purpose.

the transitions are governed by the probabilities we just found, we just need to turn things round and  track the transitions in the forward direction:

$$ \begin{align} W(b,s) &= (1-P_\text{strike}(b-1,s))(1-P_\text{swing}(b-1,s))W(b-1,s) \\ &\, + [P_\text{strike}(b,s-1)P_\text{swing}(b,s-1)(1-p) \\ &\, +P_\text{strike}(b,s-1)(1-P_\text{wing}(b,s-1)) \\ &+(1-P_\text{strike}(b,s-1))P_\text{swing}(b,s-1)]W(b,s-1). \end{align} $$

with

$$ W(-1,x) = W(x,-1) = 0 $$

and 

$$ W(0,0) = 1.$$

```wolfram
pstrike[b_, s_] := (
 V[b, 1 + s] - V[1 + b, s])/(-p Vhomerun + V[b, 1 + s] + p V[b, 1 + s] - V[1 + b, s]
);

pswing[b_, s_] := pstrike[b,s];

W[0, 0] = 1;
W[-1, _] = 0;
W[_, -1] = 0;

W[b_, s_] :=
  W[b, s] =
    ((1 - pstrike[b - 1, s]) (1 - pswing[b - 1, s])) W[b - 1, s] +
     (pstrike[b, s - 1] pswing[b, s - 1] (1 - p) + 
        pstrike[b, 
          s - 1] (1 - pswing[b, s - 1]) + (1 - 
           pstrike[b, s - 1]) pswing[b, s - 1]) W[b, s - 1]
    ;
```

recursing, we can get a nasty expression for $W(3,2).$

$$ W(3,2) = \frac{(4 p+1)^2 (8 p (2 p (p (p (p (p (p (p (p (p (12 p (p (p (3 p (p (p (4 p (p (12 p (p (p (3 p (p (p (4 p (3 p (4 p (p (p (p (12 p (p (4 p (p (24 p (p (p (6 p (8 p (p (3 p (p (2 p (3 p (p (3 p (4 p (4 p (12 p (p (2 p (4 p (3 p (p (48 p (p (3 p (4 p (3 p (6 p (9 p (p (12 p (12 p (6 p (6 p (36 p (24 p (24 p (p (324 p (64 p (9 p (2 p (4 p (8 p (24 p (3 p (36 p (8 p (6 p (6 p (12 p (24 p (72 p (9 p (4 p (1600 p+64637)+5167149)+613042868)+431777383187)+80236770525359)+6146782713427489)+199669739391774505)+5614928041301931607)+185145223430772420915)+24461010513246764022455)+242207067432572830317259)+17398363981613924470167133)+380395087683909098895351233)+3819552508202632836708642701)+17702599331857704223562031625)+342339276046387342068262491251)+43819159162037156350677721723881)+26518938109220808517423135478388809)+46400858593365920446649501605371006)+1830170135662519806732849143778845129)+67964364468156065838967870683649617049)+3572082888685085035062889475767652298197)+29581000427761481289408130383565514335001)+231989824806675104123351102853124985666885)+3451523305281004640923944607417060281401041)+48779342974035631576027326845278126924629941)+54642881007961388192930768389518641051244816)+524622170116150126081124788827006793910808572)+3201208431808859542986631571775478956937080599)+9320238758561880393261447696671038102561059442)+34557799644047715493268034073018901880862952775)+91864850386189633628584564744463545468975880797)+77871250112383311743995080553398405656229502154)+3033080900332764752704379296506529209208915360661)+2357495693216198536019798260952361932850362552649)+5268378739484366524691729487890446638794221425353)+15051888721494985123006536884826101239043058476663)+20625832432433652412813511390954875358998253627113)+13561347917651683804458419090322746733085615126607)+102711451871841902020139184305087954964705805805341)+248988008579896249809387684001663874896241983095277)+579700655354680022901508889792716568139709573190073)+972382865820091642986013199324553008010013871697370)+522345689905116851110650189128987586103027800610990)+808817994067030675519941111817832733585081466212634)+802280830768086089763749740377968338184654663268847)+382340509455384282030481785009835402922770652405808)+525241208937865906486508434363138719323260110682862)+231086720383411298779964474885196727373979738723451)+781368760663232666131406660275829141357776400386545)+1903263317711758842028122965833983019099900275967391)+741986005904837590142953669935632000665829299772501)+277703163776701513235849691371560247811800998151937)+2394008976218790123289728609884902739203827692256995)+824982047940710265738406889187176161403446583824739)+1090484176638366585866134571615680890763223654378053)+345393852252750119925636929661053741933391773789973)+1257554409962357969638404298444656562016202513631111)+365273079701462577371990254017835546326578766070924)+101498362443471353724534756830387769518526619855155)+26959056776437727547250576175953747683183003128344)+27354460717188801397502698312979006994080514409061)+19860941083243820035173571497686926172180118327899)+18323863818321993523753698170507988570879829331903)+4022963684721825446230150586933252459259324198334)+839557362807810119364037789290765301808695785000)+498867216407705970458835833105445460363974690950)+93618628156687425552354405842405613035447635246)+16613768868692541709349598924379380075685179688)+33384473824173623388589608930824808291395558827)+5262219353041913375758628210346626388277607629)+3114452071826688842057533723303979391716738625)+431216400629376009976035269629446721968678878)+55667806118839213056630743016046114930256810)+20018190661193924778036069520437852280985128)+2217271328596814494830398336117443240801986)+225657921317495839547212178051385707983759)+251530334688143981785487775173551072331665)+21153482703966847642395892341345016676676)+1594948061279490484007677878257877048280)+106509672320555452239587146244504498456)+6202468752092323435845468695370375052)+308608697492916479781550526178459085)+12757656134907562676181224583467341)+420732398213955865374635950564785)+10379197397162717141664357817500)+340564308352625826584992058811)+22298719092129794448503164065)}{16 (p+1)^4 (24 p (p (p (p (6 p (24 p (6 p+23)+947)+5779)+3762)+1548)+369)+965)^2 (4 p (2 p (p (3 p (p (p (2 p (p (6 p (p (2 p (p (6 p (p (2 p (p (12 p (p (2 p (3 p (2 p (16 p (3 p (2 p (3 p (2 p (18 p (p (6 p (24 p (6 p (48 p (6 p (24 p (6 p (12 p (6 p (72 p (2 p+33)+19159)+604253)+27962237)+506430601)+29919757891)+370706591755)+31464521482109)+290347458632803)+9434989842902771)+68133132419369485)+73459807060441521)+1285223305099375397)+2263924746006171511)+5443127728802969234)+7965575511587350691)+16006802920066732082)+157361341479016950881)+177638428191495697781)+276562944010385762611)+264028138915564726089)+115905767613333252206)+561150891325969334087)+207818364092931918995)+141041488312119733173)+43746630284589614642)+74177387418982569565)+19021936267518590189)+8807092803058850241)+1828523941044634703)+2025840993785063309)+329108317911216778)+92742521016384959)+11116781488589681)+1103381417140733)+261409380320371)+15410988186168)+1206516102049)+94133971181)^2} $$

![](/img/2025-11-03-JS-robot-baseball-W-grid.png){width="450 px" class="image-centered"}

now, the players will adjust to any value of $p$ and pursue their optimal behavior. it's only the league office that cares about and can set $p$. plotting $W(3,2)$ we see the optimum is around $p \approx 22\%.$ binary searching for the minimum, we find that $q_\text{opt} \approx 0.295967993374272054854169869096$ and $p_\text{opt} \approx 0.226973232538510017721759332456$



<br>
