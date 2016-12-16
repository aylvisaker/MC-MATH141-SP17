---
layout: post
title: "Chapter 2 Outline"
categories: [content]
tags: [content]
description: MC-MATH-141
---
* [Section 2.2 - Other Common Functions](#s2)
* [Section 2.3 - Arithmetic Combinations of Functions](#s3)
* [Section 2.4 - Composition of Functions](#s4)
* [Section 2.5 - Inverse Functions](#s5)

<div id='s2'/>
# Section 2.2 - Other Common Functions

* The **absolute value** of a real number $x$ is defined by $\vert x\vert = \begin{cases}x&x\geq0\\-x&x<0\end{cases}$.
	* Domain: $(-\infty,\infty)$
	* Range: $[0,\infty)$
	* End behavior: $|x|\to\infty$ as $x\to\pm\infty$
	* Increasing: $(0,\infty)$
	* Decreasing: $(-\infty,0)$
	* {% include image.html path="2.2.01.png" path-detail="2.2.01.hd.png" alt="Plot of the absolute value function." %}

* The **square root** of a real number $x$ is a positive number whose square is $x$.
	* Domain: $[0,\infty)$
	* Range: $[0,\infty)$
	* End behavior: $\sqrt{x}\to\infty as $x\to\infty$
	* Increasing: $(0,\infty)$
	* Decreasing: never
	* {% include image.html path="2.2.02.png" path-detail="2.2.02.hd.png" alt="Plot of the square root function." %}

* The **greatest integer function**, also called the **floor function** rounds a number down to the nearest whole number.
	* Domain: $(-\infty,\infty)$
	* Range: The integers, $\mathbb{Z}$
	* End behavior: $\lfloor x\rfloor\to\infty$ as $x\to\infty$, and $\lfloor x\rfloor\to-\infty$ as $x\to-\infty$
	* Increasing: never
	* Decreasing: never
	* Caution: The floor function always rounds *down*. So $\lfloor 2.7\rfloor = 2$, but $\lfloor -2.1\rfloor = -3$.
	* The floor function frequently arises when arbitrary real numbers just don't make sense. For instance, I might pay $.30$ dollars per minute for long distance, but if I make a $3.14$ minute phone call the company is not able to charge me $.942$ dollars. They use the floor function to round the amount down (or more likely, add one and round up).
	* {% include image.html path="2.2.03.png" path-detail="2.2.03.hd.png" alt="Plot of the floor function." %}

<div id='s3'/>
# Section 2.3 - Arithmetic Combinatiosn of Functions
* Let $f$ and $g$ be functions. Then $f+g$, $f-g$, $f\cdot g$, and $f/g$ are also functions, defined as follows.
	* $(f+g)(x) = f(x) + g(x)$
	* $(f-g)(x) = f(x) - g(x)$
	* $(f\cdot g)(x) = f(x) \cdot g(x)$
	* $(f/g)(x) = f(x) / g(x)$
* The domain of $f+g$, $f-g$, and $f\cdot g$ are all the same. Specifically, each domain is the intersection of the domain of $f$ and the domain of $g$. If $f(x)$ and $g(x)$ are defined, then so are $f(x)+g(x)$, $f(x)-g(x)$, and $f(x)\cdot g(x)$.
* The domain of $f/g$ is the domain of $f$ intersected with the domain of $g$ *without* the values that make $g(x)=0$. In order for $f(x)/g(x)$ to be defined, it is necessary that $f(x)$ and $g(x)$ be defined, *and* that $g(x)\neq 0$.
* **Vertical compression and elongation of graphs.** Let $c>0$ and $f$ be any function.
	* If $c<1$ then
		* the graph of $y=g(x)=c\cdot f(x)$ is a **vertical compression** of the graph of $y=f(x)$.
		* the graph of $y=g(x)=-c\cdot f(x)$ is a **vertical compression and reflection** of the graph of $y=f(x)$.
	* If $c>1$ then
		* the graph of $y=g(x)=c\cdot f(x)$ is a **vertical elongation** of the graph of $y=f(x)$.
		* the graph of $y=g(x)=-c\cdot f(x)$ is a **vertical elongation and reflection** of the graph of $y=f(x)$.
	* The domains of $f$, $c\cdot f$, and $-c\cdot f$ all have the same domain and the same $x$-intercepts. Their general shape is the same as well, except for a change in the vertical scale.
	* {% include image.html path="2.3.01.png" path-detail="2.3.01.hd.png" alt="Examples of vertical reflections, compressions, and elongations." %}
* **Graph of the reciprocal function.** Let $g(x)=\frac{1}{f(x)}$. Note that this is a special case of a quotient of functions.
	* $g(x)$ is undefined when $f(x)=0$
	* $g(x)=f(x)$ when $f(x)=\pm1$
	* $g(x)$ is positive when $f(x)$ is positive and negative when $f(x)$ is negative
	* the magnitude (size in absolute value) of $g(x)$ is large when the magnitude of $f(x)$ is small
	* the magnitude of $g(x)$ is small when the magnitude of $f(x)$ is large
	* {% include image.html path="2.3.02.png" path-detail="2.3.02.hd.png" alt="The graph of a function and its reciprocal." %}

<div id='s4'/>
# Section 2.4 - Composition of Functions

<div id='s5'/>
# Section 2.5 - Inverse Functions

