---
layout: post
published: true
title: Can You Power Up The Hill?
permalink: /2026-07-16-hhh/
date: 2026/07/16
subtitle: To champion cyclists, each optimized for a different facet of their sport, will tie if you can stretch the hill just so.
tags: optimization calculus
---

> **Question**: This time, we’ll be looking at a model for a cyclist’s speed $v$ as a function of their pedaling power $P$, their mass $m$, and the ground’s angle of inclination $\theta$:
>
> $$v=\frac{P}{m\sin{\theta}+10}$$
>
> In cycling, roads are marked with a gradient $g$, which is a hill’s slope, typically expressed as a percentage. Thus, an incredibly steep 45-degree incline has a gradient of 1, or “100 percent.”
>
> Consider the following two riders:
>
> - A “climber,” who has a power of 300 and a mass of 60
> - A “sprinter,” who has a power of 325 and a mass of 80
>
> At what gradient will the climber and sprinter cycle at the same speed? (You can give your answer as a value between 0 and 1 or as a percentage.)
>
> **Extra credit**: The climber and the sprinter are racing up a perfectly sinusoidal hill. They go from the base, where the gradient is 0 percent, to the peak, where the gradient is again 0 percent. For them to reach the top at the same time, what should the maximum gradient of the hill be? (You can give your answer as a value between 0 and 1 or as a percentage.)
>
> Importantly, note that the formula for $v$ given above is for a rider’s speed *along the ground*. Thus, when the ground is inclined, the same speed will cover less horizontal distance per unit time.

<!--more-->

([Fiddler on the Proof](https://thefiddler.substack.com/p/can-you-power-up-the-hill))

## Solution

Due to the relationship between the angle $\theta$ of the hill, the mass $m$, and power $P$ of the rider, small angles favor the sprinter while larger angles favor the climber. We'd expect the sprinter to win a very shallow rise while the climber should win a steep rise.

The hill is a sinusoid that starts out flat at the origin and goes up to the flat peak. We are able to control the maximum gradient of the hill, which means we can stretch it horizontally. Putting these factors together, the hill has an equation proportional to

$$ y(x) = 1 - \cos(G x). $$

You can experiment with the effect of $G$ on the gradient of the hill.

<div style="display: flex; flex-direction: column; align-items: center; margin: 2em 0;">
  <div style="width: 100%; overflow-x: auto;">
    <canvas id="hillPlot" height="350" style="display: block; margin: 0 auto;"></canvas>
  </div>
  <div style="margin-top: 1.5em; text-align: center; width: 100%; max-width: 400px;">
    <label for="gSlider" style="font-family: 'Courier New', Courier, monospace; font-size: 1.1em; margin-bottom: 0.5em; display: inline-block;">
      <strong>G: </strong><span id="gValue" style="display: inline-block; width: 3em; text-align: left;">1.00</span>
    </label>
    <div style="display: flex; align-items: center; gap: 0.5em; font-family: 'Courier New', Courier, monospace;">
      <span>1/4</span>
      <input type="range" id="gSlider" min="0.25" max="1" step="0.01" value="1.0" style="flex-grow: 1; cursor: pointer;">
      <span>1</span>
    </div>
  </div>
</div>

<script>
  function createHillAnimation(options) {
    const canvas = document.getElementById(options.canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const slider = options.sliderId ? document.getElementById(options.sliderId) : null;
    const gValueLabel = options.gValueId ? document.getElementById(options.gValueId) : null;

    let x1 = 0; // Climber
    let x2 = 0; // Sprinter
    let t1 = 0;
    let t2 = 0;
    let lastTimestamp = null;
    let resetTimeout = null;

    function getDxDt(x, P, m, G) {
        const sinGx = Math.sin(G * x);
        const denom = m * G * sinGx + 10 * Math.sqrt(1 + G * G * sinGx * sinGx);
        return P / denom;
    }

    function getG() {
        if (slider) return Math.max(parseFloat(slider.value), 0.01);
        return options.fixedG || 0.087433;
    }

    function drawPlot(G) {
      const marginL = 100; // Left margin for y-axis labels
      const marginB = 70; // Bottom margin for x-axis labels
      const marginR = 50; // Right margin
      const marginT = 20; // Top margin
      
      const basePlotWidth = options.basePlotWidth || 150;
      const plotWidth = basePlotWidth / G;
      canvas.width = marginL + plotWidth + marginR;
      
      ctx.fillStyle = '#f4f4f4';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      const width = canvas.width - marginL - marginR;
      const height = canvas.height - marginT - marginB;
      
      const xMin = 0;
      const xMaxScale = Math.PI / G; 
      const yMin = 0;
      const yMax = 2.2;
      
      function mapX(x) {
        return marginL + ((x - xMin) / (xMaxScale - xMin)) * width;
      }
      
      function mapY(y) {
        return canvas.height - marginB - ((y - yMin) / (yMax - yMin)) * height;
      }
      
      // Draw axes
      ctx.beginPath();
      ctx.strokeStyle = '#000';
      ctx.lineWidth = 5;
      
      ctx.moveTo(marginL, marginT);
      ctx.lineTo(marginL, canvas.height - marginB);
      
      ctx.moveTo(marginL, canvas.height - marginB);
      ctx.lineTo(canvas.width - marginR, canvas.height - marginB);
      ctx.stroke();

      // Tick marks and labels
      ctx.fillStyle = '#000';
      ctx.strokeStyle = '#000';
      ctx.lineWidth = 5;
      ctx.font = '24px "Courier New"';
      ctx.textBaseline = 'middle';
      ctx.textAlign = 'right';

      // Y-axis ticks
      for (let yTick of [0, 0.5, 1, 1.5, 2]) {
          const py = mapY(yTick);
          ctx.beginPath();
          ctx.moveTo(marginL, py);
          ctx.lineTo(marginL - 8, py);
          ctx.stroke();
          ctx.fillText(yTick.toString(), marginL - 15, py);
      }
      
      // Y-axis title
      ctx.save();
      ctx.font = 'italic 28px "Courier New"';
      ctx.translate(marginL - 75, mapY(1.1));
      ctx.rotate(-Math.PI / 2);
      ctx.textAlign = 'center';
      ctx.fillText('y(x)', 0, 0);
      ctx.restore();

      // X-axis ticks
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';
      const midTick = xMaxScale / 2;
      for (let xTick of [0, midTick, xMaxScale]) {
          const px = mapX(xTick);
          ctx.beginPath();
          ctx.moveTo(px, canvas.height - marginB);
          ctx.lineTo(px, canvas.height - marginB + 8);
          ctx.stroke();
          
          let label = '0';
          if (xTick > 0) {
              let coef = xTick / Math.PI;
              if (Math.abs(coef - 1) < 0.001) {
                  label = '𝜋';
              } else {
                  label = parseFloat(coef.toFixed(2)) + '𝜋';
              }
          }
          ctx.fillText(label, px, canvas.height - marginB + 15);
      }
      
      // X-axis title
      ctx.font = 'italic 28px "Courier New"';
      ctx.fillText('x', mapX(midTick), canvas.height - marginB + 45);

      // Draw the curve
      ctx.beginPath();
      ctx.strokeStyle = '#FFD700'; // thick gold/yellow line
      ctx.lineWidth = 8;
      
      let first = true;
      const xStep = xMaxScale / 100;
      for(let x = xMin; x <= xMaxScale + xStep/2; x += xStep) {
        const y = 1 - Math.cos(G * x);
        const px = mapX(x);
        const py = mapY(y);
        if(first) {
          ctx.moveTo(px, py);
          first = false;
        } else {
          ctx.lineTo(px, py);
        }
      }
      ctx.stroke();

      // Draw Cyclists
      const y1 = 1 - Math.cos(G * x1);
      const px1 = mapX(x1);
      const py1 = mapY(y1);

      const y2 = 1 - Math.cos(G * x2);
      const px2 = mapX(x2);
      const py2 = mapY(y2);

      // Climber (Blue)
      ctx.beginPath();
      ctx.arc(px1, py1, 8, 0, 2 * Math.PI);
      ctx.fillStyle = '#007bff';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Sprinter (Red)
      ctx.beginPath();
      ctx.arc(px2, py2, 8, 0, 2 * Math.PI);
      ctx.fillStyle = '#dc3545';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();
      
      // Legend
      ctx.font = '16px "Courier New"';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = '#007bff';
      ctx.fillText(`Climber:  ${t1.toFixed(2)}`, marginL + 20, marginT + 10);
      ctx.fillStyle = '#dc3545';
      ctx.fillText(`Sprinter: ${t2.toFixed(2)}`, marginL + 20, marginT + 30);
    }

    function animate(timestamp) {
      if (!lastTimestamp) lastTimestamp = timestamp;
      const dt = (timestamp - lastTimestamp) / 1000;
      lastTimestamp = timestamp;

      const G = getG();
      if (gValueLabel && slider) {
          gValueLabel.textContent = parseFloat(slider.value).toFixed(2);
      }

      // Scale simulation time so the race visually takes exactly 5 seconds for the Climber.
      const T_approx = (1/300) * (120 + 10 * Math.PI / G + 5 * Math.PI * G / 2);
      const timeScale = T_approx / 5;
      const dt_sim = dt * timeScale;

      const xMaxScale = Math.PI / G;
      
      if (x1 < xMaxScale) {
          const dx = getDxDt(x1, 300, 60, G) * dt_sim;
          if (x1 + dx >= xMaxScale) {
              const fraction = (xMaxScale - x1) / dx;
              t1 += dt_sim * fraction;
              x1 = xMaxScale;
          } else {
              x1 += dx;
              t1 += dt_sim;
          }
      }
      
      if (x2 < xMaxScale) {
          const dx = getDxDt(x2, 325, 80, G) * dt_sim;
          if (x2 + dx >= xMaxScale) {
              const fraction = (xMaxScale - x2) / dx;
              t2 += dt_sim * fraction;
              x2 = xMaxScale;
          } else {
              x2 += dx;
              t2 += dt_sim;
          }
      }

      if (options.autoLoop && x1 >= xMaxScale && x2 >= xMaxScale) {
          if (!resetTimeout) {
              resetTimeout = setTimeout(() => {
                  x1 = 0;
                  x2 = 0;
                  t1 = 0;
                  t2 = 0;
                  lastTimestamp = null;
                  resetTimeout = null;
              }, 1500);
          }
      }

      drawPlot(G);
      requestAnimationFrame(animate);
    }

    if (slider) {
      slider.addEventListener('input', () => {
          x1 = 0;
          x2 = 0;
          t1 = 0;
          t2 = 0;
          lastTimestamp = null;
          if (resetTimeout) {
              clearTimeout(resetTimeout);
              resetTimeout = null;
          }
      });
    }
    
    requestAnimationFrame(animate);
  }

  // Initialize the top animation
  createHillAnimation({ canvasId: 'hillPlot', sliderId: 'gSlider', gValueId: 'gValue', autoLoop: true });
  
  // Expose to window for the bottom block
  window.createHillAnimation = createHillAnimation;
</script>

At some intermediate value of $G$, we expect the two riders to end up in a tie. 

The amount of time it takes a rider to make it up the hill is the integral of $dt$ along the hill

$$ T = \int_\text{hill} \text{d}t. $$

The small increment $\text{d}t$ is the time it takes to traverse the small increment of distance $\text{d}s,$ i.e.

$$ \text{d}t = \frac{\text{d}s}{v}. $$

Furthermore, the increment $\text{d}s^2 = \text{d}x^2 + \text{d}y^2$ or  

$$ 
	\begin{align}
		\text{d}s &= \sqrt{1 + \left(\text{d}y/\text{d}x\right)^2} \text{d}x \\
		&= \sqrt{1+G^2\sin^2 Gx}\text{d}x. 
	\end{align}
$$

We are given $v$ as a function of $\theta$ but we need it in terms of $x.$ Happily, at any point along the hill, the local gradient $\text{d}y/\text{d}x$ is equal to $\tan\theta$ and, so

$$
	\begin{align}
		G \sin Gx &= \tan\theta \\
		&= \frac{\sin\theta}{\sqrt{1-\sin^2\theta}}
	\end{align}
$$

Solving for $\sin\theta$, we get 

$$ 
	\sin\theta = \frac{G\sin Gx}{\sqrt{1 + G^2\sin^2 Gx}}.
$$

Putting these pieces together gives us

$$ 
	\begin{align}
		T &= \int_0^{\pi/G}\text{d}x\, \frac{\sqrt{1 + G^2\sin^2 Gx}}{v(\theta(x))} \\
		&= \int_0^{\pi/G}\text{d}x\, \frac{m\sin\theta + 10}{P} \sqrt{1 + G^2\sin^2 Gx} \\
		&= \frac1P \int_0^{\pi/G} \text{d}x\, \left(mG\sin Gx + 10\sqrt{1+G^2\sin^2 Gx}\right)
	\end{align}
$$

We can either integrate this numerically, or we can approximate the square root. Because $G$ has to be on the order of $5\%,$ $G^2$ will be a small quantity. So, the integral becomes 

$$ 
	\begin{align}
		T &= \frac1P \int_0^{\pi/G} \text{d}x\, \left(mG\sin Gx + 10\left[1+\frac12 G^2\sin^2 Gx\right]\right) \\
		&= \frac{1}{P} \left( 2m + \frac{10\pi}{G} + \frac{5\pi G}{2} \right) 
	\end{align}
$$

The sprinter and the climber reach the top of the hill at the same time when these expressions, evaluated for each rider's mass and power, are equal. Plugging in the values and solving for $G$, we get

$$
	\begin{align} 
		G &= \frac{2(36 - \sqrt{1296 - \pi^2})}{\pi} \\
	 	&= 0.087479\ldots
	\end{align}
$$

Because the maximum value of $\sin$ is $1,$ the maximum gradient is $G$ itself.

If we perform the exact integral instead of approximating, we end up with $\int_0^\pi\text{d}t\sqrt{1 + G^2\sin^2 t} = 36 G $ which yields the exact answer $0.0874330020767798\ldots$ which is less than $0.1\%$ off the approximation.

<br>

<div style="display: flex; flex-direction: column; align-items: center; margin: 2em 0;">
  <div style="font-family: 'Courier New', Courier, monospace; font-size: 1.1em; margin-bottom: 0.5em;">
    <strong>The Tie (G ≈ 0.0874)</strong>
  </div>
  <div style="width: 100%; overflow-x: auto;">
    <canvas id="hillPlotTie" height="350" style="display: block; margin: 0 auto;"></canvas>
  </div>
</div>

<script>
  if (window.createHillAnimation) {
      window.createHillAnimation({ 
          canvasId: 'hillPlotTie', 
          fixedG: 0.087433,
          basePlotWidth: 50,
          autoLoop: true 
      });
  }
</script>
