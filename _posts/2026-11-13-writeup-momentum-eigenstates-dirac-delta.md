---
layout: post
published: true
title: Inner product of momentum eigenstates
date: 2026/11/13
subtitle: Why is the inner product of momentum eigenstates the Dirac delta distribution?
tags: physics quantum-mechanics distributions dirac-delta
source: writeup
kind: physics
theme: quantum-mechanics
hide_from_recent: true
---

>**Question**: Why is the inner product of momentum eigenstates the Dirac delta distribution?

<!--more-->
The momentum eigenstate $\lvert \psi_k\rangle$, has definite momentum $\hbar k$ and completely unknown position. 
In the position basis, it has representation $\langle x\lvert \psi_k\rangle$ proportional to $e^{ikx}.$

With discrete vectors, the dot product of two eigenstates of a hermitian matrix is zero if they're distinct and one if they're the same.
I.e. $\langle \psi_{k^\prime}\rvert\psi_k\rangle = \delta_{k^\prime k}$ which is a distribution over the discrete states given by $k$.

However, the momentum eigenstate describes a free particle so it can have any momentum (and therefore value of $k$) whatsoever.
We can still think of $\lvert\psi_k\rangle$ as a vector, but as one that has an entry for each value in the continuum of $x$, i.e. a function.
This generalizes the dot product sum $ \langle \psi_{k^\prime}\rvert\psi_k\rangle = \sum_j {\psi_{k^\prime}^j}^\star\psi_k^j$ to an integral

$$ 
	\begin{align}
		\langle\psi_{k^\prime}\rvert\psi_k\rangle &= \int\text{d}x\, \langle\psi_{k^\prime}\rvert x\rangle\langle x\rvert \psi_k\rangle \\ 
		&= \int\text{d}x\, e^{i\left(k-k^\prime\right)x}.
	\end{align} 
$$

This multiplies the "component" of each state in each "direction" $\lvert x\rangle$ and adds them all up, just like the ordinary dot product.

On its face, it isn't obvious that this reproduces the orthogonality of eigenstates.
Yet, momentum is a hermitian operator, and the $\lvert\psi_k\rangle$ are its eigenvectors, so oughtn't they be orthogonal?
Let's take a look.

### What is the generalized dot product of momentum eigenstates?

First, let's set the bounds of the space as $-R$ and $+R$.
We will take these to be infinite eventually, but for the purpose of seeing how the inner product gets to its final form, it is very helpful to start with it finite.

With that, we can evaluate the integral

$$ 
	\begin{align}
		\langle\psi_{k^\prime}\rvert\psi_k\rangle &= \int\limits_{-R}^{+R}\text{d}x\, e^{i\left(k-k^\prime\right)x} \\
		&= \frac{e^{i\left(k-k^\prime\right)R} - e^{-i\left(k-k^\prime\right)R}}{i\left(k-k^\prime\right)} \\
		&= \frac{2\sin \left(k-k^\prime\right) R}{\left(k-k^\prime\right)} \\
		&= \frac{2\sin g R}{g}.
	\end{align} 
$$

Where for ease of writing we have given the gap in wavenumber, $k - k^\prime$, the symbol $g$.

What can we say about

$$ \langle\psi_{k^\prime}\rvert\psi_k\rangle = \frac{2\sin g R}{g}? $$

First of all, it oscillates.
And as $R$ gets bigger and bigger, it oscillates faster and faster.
In fact if we averaged any smooth function against this oscillation, it would sample the function at much greater frequency than any change in the function. 
This means that every small neighborhood on the function gets averaged to zero. 

You can play with the distribution below, and check that this happens as $R$ transitions from small to large.

If that were the whole story, then this would be a very boring distribution.
But something interesting happens at the origin.
As $g$ gets small, we can approximate $\sin Rg$ by $Rg$ which makes the fraction equal to $2Rg/g = 2R$ at the origin. 

So, as $R$ gets very big, the whole function oscillates fast enough to average any function to zero everywhere except exactly at the origin where the distribution is $2R.$
In other words, as $R$ goes to $\infty$, the distribution is zero everywhere except for the origin where it is infinite. 

<div style="display: flex; flex-direction: column; align-items: center; margin: 2em 0;">
  <div style="width: 100%; overflow-x: auto;">
    <canvas id="sincPlot" width="700" height="350" style="display: block; margin: 0 auto;"></canvas>
  </div>
  
  <div style="margin-top: 1.5em; text-align: center; width: 100%; max-width: 450px;">
    <label for="rSlider" style="font-family: 'Courier New', Courier, monospace; font-size: 1.1em; margin-bottom: 0.5em; display: inline-block;">
      <strong><em>R</em>: </strong><span id="rValue" style="display: inline-block; width: 5em; text-align: left;">1.00</span>
    </label>
    <div style="display: flex; align-items: center; gap: 0.5em; font-family: 'Courier New', Courier, monospace;">
      <span>10⁻³</span>
      <input type="range" id="rSlider" min="-3" max="3" step="0.01" value="0" style="flex-grow: 1; cursor: pointer;">
      <span>10³</span>
    </div>
  </div>

  <div style="margin-top: 1em; text-align: center; width: 100%; max-width: 450px;">
    <label for="kSlider" style="font-family: 'Courier New', Courier, monospace; font-size: 1.1em; margin-bottom: 0.5em; display: inline-block;">
      <strong><em>g</em>-scale: </strong><span id="kValue" style="display: inline-block; width: 5em; text-align: left;">1000</span>
    </label>
    <div style="display: flex; align-items: center; gap: 0.5em; font-family: 'Courier New', Courier, monospace;">
      <span>10⁻³</span>
      <input type="range" id="kSlider" min="-3" max="3" step="0.01" value="3" style="flex-grow: 1; cursor: pointer;">
      <span>10³</span>
    </div>
  </div>
</div>

<script>
(function() {
  const canvas = document.getElementById('sincPlot');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const rSlider = document.getElementById('rSlider');
  const kSlider = document.getElementById('kSlider');
  const rValueLabel = document.getElementById('rValue');
  const kValueLabel = document.getElementById('kValue');

  function fmt(v) {
    if (Math.abs(v) < 1e-9) return '0';
    const a = Math.abs(v);
    if (a >= 100) return v.toFixed(0);
    if (a >= 10) return v.toFixed(1);
    if (a >= 1) return v.toFixed(2);
    if (a >= 0.01) return v.toFixed(3);
    return v.toExponential(1);
  }

  function draw() {
    const dpr = window.devicePixelRatio || 1;
    if (canvas.width !== 700 * dpr || canvas.height !== 350 * dpr) {
      canvas.width = 700 * dpr;
      canvas.height = 350 * dpr;
      canvas.style.width = '700px';
      canvas.style.height = '350px';
    }
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.scale(dpr, dpr);

    const R = Math.pow(10, parseFloat(rSlider.value));
    const kMax = Math.pow(10, parseFloat(kSlider.value));

    rValueLabel.textContent = fmt(R);
    kValueLabel.textContent = fmt(kMax);

    const yTicks = [0, R, 2 * R];

    // Measure maximum tick label width to dynamically prevent overlap with y-axis title
    ctx.font = '18px "Courier New"';
    let maxTickW = 0;
    for (let yt of yTicks) {
      const w = ctx.measureText(fmt(yt)).width;
      if (w > maxTickW) maxTickW = w;
    }

    const marginL = Math.max(125, Math.ceil(maxTickW + 55));
    const marginB = 65;
    const marginR = 35;
    const marginT = 25;

    ctx.clearRect(0, 0, 700, 350);

    const width = 700 - marginL - marginR;
    const height = 350 - marginT - marginB;

    const xMin = -kMax;
    const xMax = kMax;
    const yMax = 2 * R * 1.15;
    const yMin = -2 * R * 0.3;

    function mapX(x) {
      return marginL + ((x - xMin) / (xMax - xMin)) * width;
    }

    function mapY(y) {
      return 350 - marginB - ((y - yMin) / (yMax - yMin)) * height;
    }

    // Axes
    ctx.beginPath();
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 3;

    // Horizontal axis (y = 0)
    const py0 = mapY(0);
    ctx.moveTo(marginL, py0);
    ctx.lineTo(700 - marginR, py0);

    // Left border / vertical axis
    ctx.moveTo(marginL, marginT);
    ctx.lineTo(marginL, 350 - marginB);
    ctx.stroke();

    // Center vertical line (x = 0)
    const px0 = mapX(0);
    ctx.beginPath();
    ctx.strokeStyle = '#ccc';
    ctx.lineWidth = 1.5;
    ctx.moveTo(px0, marginT);
    ctx.lineTo(px0, 350 - marginB);
    ctx.stroke();

    // Y-axis ticks and labels
    ctx.fillStyle = '#000';
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 3;
    ctx.font = '18px "Courier New"';
    ctx.textBaseline = 'middle';
    ctx.textAlign = 'right';

    for (let yt of yTicks) {
      const py = mapY(yt);
      ctx.beginPath();
      ctx.moveTo(marginL, py);
      ctx.lineTo(marginL - 8, py);
      ctx.stroke();
      ctx.fillText(fmt(yt), marginL - 12, py);
    }

    // Y-axis title: centered in the margin space to the left of the widest tick label
    ctx.save();
    ctx.font = 'italic 20px "Courier New"';
    const yTitleX = Math.max(18, Math.round((marginL - 12 - maxTickW) / 2));
    ctx.translate(yTitleX, mapY(R));
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = 'center';
    ctx.fillText('2 sin(R g) / g', 0, 0);
    ctx.restore();

    // X-axis ticks and labels
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';

    const xTicks = [-kMax, -kMax / 2, 0, kMax / 2, kMax];
    for (let xt of xTicks) {
      const px = mapX(xt);
      ctx.beginPath();
      ctx.moveTo(px, 350 - marginB);
      ctx.lineTo(px, 350 - marginB + 8);
      ctx.stroke();
      ctx.fillText(fmt(xt), px, 350 - marginB + 14);
    }

    // X-axis title
    ctx.font = 'italic 20px "Courier New"';
    ctx.fillText('g', mapX(0), 350 - marginB + 40);

    // Draw the continuous sinc curve without aliasing
    ctx.beginPath();
    ctx.strokeStyle = '#007bff';
    ctx.lineWidth = 3;

    let prevY = null;

    for (let p = 0; p < width; p++) {
      const px = marginL + p;
      const x1 = xMin + (p / width) * (xMax - xMin);
      const x2 = xMin + ((p + 1) / width) * (xMax - xMin);
      const dx = x2 - x1;
      const dTheta = R * dx;

      let yMinP = Infinity, yMaxP = -Infinity;

      if (x1 <= 0 && x2 >= 0) {
        const y0 = 2 * R;
        if (y0 < yMinP) yMinP = y0;
        if (y0 > yMaxP) yMaxP = y0;
      }

      if (dTheta >= 2 * Math.PI && (x1 > 0 || x2 < 0)) {
        const xClose = Math.min(Math.abs(x1), Math.abs(x2));
        const env = Math.min(2 * R, 2 / Math.max(xClose, 1e-12));
        yMaxP = env;
        yMinP = -env;
      } else {
        const samples = Math.min(24, Math.max(4, Math.ceil(dTheta / 0.5)));
        for (let s = 0; s <= samples; s++) {
          const xs = x1 + (s / samples) * dx;
          const ys = Math.abs(xs) < 1e-12 ? 2 * R : (2 * Math.sin(R * xs)) / xs;
          if (ys < yMinP) yMinP = ys;
          if (ys > yMaxP) yMaxP = ys;
        }
      }

      const pyTop = mapY(yMaxP);
      const pyBot = mapY(yMinP);

      if (p === 0) {
        ctx.moveTo(px, (pyTop + pyBot) / 2);
        prevY = (pyTop + pyBot) / 2;
      } else {
        if (Math.abs(pyBot - pyTop) <= 1.5) {
          const py = (pyTop + pyBot) / 2;
          ctx.lineTo(px, py);
          prevY = py;
        } else {
          if (prevY !== null && Math.abs(prevY - pyTop) < Math.abs(prevY - pyBot)) {
            ctx.lineTo(px, pyTop);
            ctx.lineTo(px, pyBot);
            prevY = pyBot;
          } else {
            ctx.lineTo(px, pyBot);
            ctx.lineTo(px, pyTop);
            prevY = pyTop;
          }
        }
      }
    }
    ctx.stroke();
  }

  rSlider.addEventListener('input', draw);
  kSlider.addEventListener('input', draw);
  draw();
})();
</script>

Assuming this can be properly normalized, one corollary is that if we average any function $f(k)$ against this distribution, we will get back $f(0)$.

However, this distribution is not normalized, and may not be normalizable unless it has a non-zero, finite area.

### What's the area?

So, let's go after it.

$$ \text{area} = 2\int\limits_{-\infty}^{+\infty} \text{d}g\, \frac{\sin g R }{g}. $$

First of all, we can change variables to $u = gR$ and $\text{d}u = \text{d}g\, R$ which shows that this integral is, happily, independent of $R$.
Second of all, the integral is even so we can restrict it to $0$ to $\infty$.

$$
	\begin{align} \text{area} &= 2\int\limits_{-\infty}^{+\infty} \text{d}u\, \frac{\sin u }{u} \\
	&= 4\int\limits_0^{+\infty} \text{d}u\, \frac{\sin u }{u}.
	\end{align}
$$

There is not an easy way to attack this with substitutions, or integration by parts, but the Feynman trick of differentiating under the integral sign does a wonderful job.
We need to introduce a factor that 1) we can differentiate to cancel the $u$ in the denominator and 2) goes to $0$ at $\infty$, leaving us with something nice that we can integrate by parts.
$e^{-\beta u}$ fits the bill so the integral (dropping the $4$) becomes

$$ \int\limits_0^{\infty} \text{d}u\, e^{-\beta u}\frac{\sin u }{u}. $$

Let's call this integral, for a given value of $\beta$, $a(\beta)$.
The derivative of $a(\beta)$ with respect to $\beta$ is 

$$ \frac{\text{d}a(\beta)}{\text{d}\beta} = -\int\limits_0^{\infty} \text{d}u\, e^{-\beta u}\sin u. $$

To integrate by parts, we can use $\frac{\text{d}}{\text{d}u}\left[e^{-\beta u} \sin u\right] = -\beta e^{-\beta u}\sin u + e^{-\beta u}\cos u$.
Rearranging and inserting this into our integral, we get 

$$ 
	\begin{align}
		\frac{\text{d}a(\beta)}{\text{d}\beta} &= \frac{1}{\beta}\int\limits_0^{\infty} \text{d}u\, \frac{\text{d}}{\text{d}u}\left[e^{-\beta u} \sin u\right] - \frac{1}{\beta}\int\limits_0^{\infty} \text{d}u\, e^{-\beta u} \cos u \\
		&= - \frac{1}{\beta}\int\limits_0^{\infty} \text{d}u\, e^{-\beta u} \cos u.
	\end{align}
$$

The first piece was zero since the bracketed stuff is zero at both endpoints.
It may look like, after another crank of the integration by parts wheel, we will get back the original integral and find ourselves in a futile cycle.
But alas, crank two has a nonzero contribution from the boundary term and will give us a nice differential equation for $a(\beta)$.

We look once again for guidance from the product rule $\frac{\text{d}}{\text{d}u}\left[e^{-\beta u} \cos u\right] = -\beta e^{-\beta u}\cos u - e^{-\beta u}\sin u$ and, making the substitution, we get

$$ 
	\begin{align}
		\frac{\text{d}a(\beta)}{\text{d}\beta} &= \frac{1}{\beta^2}\int\limits_0^{\infty} \text{d}u\, \frac{\text{d}}{\text{d}u}\left[e^{-\beta u} \cos u\right] + \frac{1}{\beta^2}\int\limits_0^{\infty} \text{d}u\, e^{-\beta u} \sin u \\
		&= -\frac{1}{\beta^2} - \frac{1}{\beta^2}\frac{\text{d}a(\beta)}{\text{d}\beta}.
	\end{align} 
$$

Solving for $\text{d}a(\beta)/\text{d}\beta$ gets us

$$ \frac{\text{d}a(\beta)}{\text{d}\beta} = -\frac{1}{1+\beta^2}. $$

Now, $a(\infty) - a(0) = -\int_0^\infty \frac{\text{d}\beta}{1+\beta^2}$ and we know that $a(\infty) = 0$ due to the exponential term, so all we have left is to evaluate the integral on the right. 
The integral of $1/(1+\beta^2)$ is $\arctan \beta$ so we get $a(0) = \arctan \infty - \arctan 0 = \tfrac12\pi.$

### The dust settles

Putting everything back together, this means that the distribution has $\text{area} = 2\pi.$
In turn this means that the normalization constant on momentum eigenstates is $1/\sqrt{2\pi}$ and therefore

$$ \langle x \lvert \psi_k\rangle = \frac{1}{\sqrt{2\pi}}e^{ik\cdot x}. $$

This gives us

$$ \langle \psi_{k^\prime}\rvert\psi_k\rangle = \delta(k-k^\prime) $$

The Dirac delta ~~function~~ distribution.

This shows that the momentum eigenstates are properly orthonormal, and give rise to an amazing distribution that is zero everywhere, except the origin, where it is $\infty.$
Nonetheless, this distribution has a nonzero, and non-infinite area of $1$.
A proper distribution.

This has many fascinating properties, but the point of this writeup is just to show that it arises naturally from momentum eigenstates so we will leave it at that.

<!-- ## Solution -->

<br>
