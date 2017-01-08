---
layout: post
title: "Chapter 2 Outline"
categories: [content]
tags: [content]
description: New Functions from Old
---
* [Section 2.2 - Other Common Functions](#s2)
* [Section 2.3 - Arithmetic Combinations of Functions](#s3)
* [Section 2.4 - Composition of Functions](#s4)
* [Section 2.5 - Inverse Functions](#s5)

<div id='s2'/>
# Section 2.2 - Other Common Functions

* The **absolute value** of a real number $x$ is defined by $\vert x\vert = \begin{cases}x&x\geq0\\\\-x&x<0\end{cases}$.
	* Domain: $(-\infty,\infty)$
	* Range: $[0,\infty)$
	* End behavior: $\vert x\vert\to\infty$ as $x\to\pm\infty$
	* Increasing: $(0,\infty)$
	* Decreasing: $(-\infty,0)$
	* {% include image.html path="2.2.01.png" path-detail="2.2.01.hd.png" alt="Plot of the absolute value function." %}

* The **square root** of a real number $x$ is a positive number whose square is $x$.
	* Domain: $[0,\infty)$
	* Range: $[0,\infty)$
	* End behavior: $\sqrt{x}\to\infty$ as $x\to\infty$
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
	* The floor function frequently arises when arbitrary real numbers just don't make sense. For instance, I might pay $.30$ dollars per minute for long distance, but if I make a $3.14$ minute phone call the company is not able to charge me $.942$ dollars. They use the floor function to round the amount down (or, more likely in the case of the phone company, the ceiling function to round up).
	* {% include image.html path="2.2.03.png" path-detail="2.2.03.hd.png" alt="Plot of the floor function." %}

<div id='s3'/>
# Section 2.3 - Arithmetic Combinations of Functions
* Let $f$ and $g$ be functions. Then $f+g$, $f-g$, $f\cdot g$, and $f/g$ are also functions, defined as follows.
	* $(f+g)(x) = f(x) + g(x)$
	* $(f-g)(x) = f(x) - g(x)$
	* $(f\cdot g)(x) = f(x) \cdot g(x)$
	* $(f/g)(x) = f(x) / g(x)$
* The domain of $f+g$, $f-g$, and $f\cdot g$ are all the same. Specifically, each domain is the intersection of the domain of $f$ and the domain of $g$. If $f(x)$ and $g(x)$ are defined, then so are $f(x)+g(x)$, $f(x)-g(x)$, and $f(x)\cdot g(x)$.
* The domain of $f/g$ is the domain of $f$ intersected with the domain of $g$ *without* the values that make $g(x)=0$. In order for $f(x)/g(x)$ to be defined, it is necessary that $f(x)$ and $g(x)$ be defined, *and* that $g(x)\neq 0$.
* The zeros of $f\cdot g$ are those $x$ values that are zeros of $f$ *or* zeros of $g$.
* The zeros of $f/g$ are those $x$ values that are zeros of $f$ and *not* zeros of $g$.
* Understanding arithmetic combinations is useful for helping us break down complicated functions. Knowing how to work with functions such as $f(x)=x+4$ and $g(x)=x^2-4$ can give us insight when working with functions like $h(x)=\frac{x+4}{x^2-4}$.
* **Vertical compression and elongation of graphs.** Let $c>0$ and $f$ be any function.
	* If $c<1$ then
		* the graph of $y=g(x)=c\cdot f(x)$ is a **vertical compression** of the graph of $y=f(x)$.
		* the graph of $y=g(x)=-c\cdot f(x)$ is a **vertical compression and reflection** of the graph of $y=f(x)$.
	* If $c>1$ then
		* the graph of $y=g(x)=c\cdot f(x)$ is a **vertical elongation** of the graph of $y=f(x)$.
		* the graph of $y=g(x)=-c\cdot f(x)$ is a **vertical elongation and reflection** of the graph of $y=f(x)$.
	* The domains of $f$, $c\cdot f$, and $-c\cdot f$ are all the same, and all three functions have the same $x$-intercepts. The general shape of their graphs is the same as well, except for a change in the vertical scale.
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
* Let $f$ and $g$ be functions. The **composite function**, $f\circ g$ is a new function defined by $(f\circ g)(x) = f(g(x))$.
* The domain of $f\circ g$ consists of those $x$ values for which:
	1. $x$ is in the domain of $g$
	2. $g(x)$ is in the domain of $f$
* Understanding composite functions is useful for helping us break down complicated functions. For instance, consider the function $f(x)=\sqrt{x^2-4\}$. We may not know much about $f$, but we know a good deal about $g(x)=\sqrt{x}$ and $h(x)=x^2-4$. Thus we can gain some understanding of $f$ by recognizing that $f=g\circ h$.
* **Horizontal compression and elongation of graphs.** Let $c>0$ and $f$ be any function.
	* If $c<1$ then
		* the graph of $y=g(x)=f(c\cdot x)$ is a **horizontal elongation** of the graph of $y=f(x)$.
		* the graph of $y=g(x)=f(-c\cdot x)$ is a **horizontal elongation and reflection** of the graph of $y=f(x)$.
	* If $c>1$ then
		* the graph of $y=g(x)=f(c\cdot x)$ is a **horizontal compression** of the graph of $y=f(x)$.
		* the graph of $y=g(x)=f(-c\cdot x)$ is a **horizontal compression and reflection** of the graph of $y=f(x)$.
	* The ranges of $f(x)$, $f(c\cdot x)$, and $f(-c\cdot x)$ are all the same and their graphs have the same $y$-intercept. The general shape of their graphs is the same as well, except for a change in the horizontal scale.
	* Note: This is the opposite of vertical compression/elongation, in that when $c<1$ we get an elongation instead of a compression.
	* {% include image.html path="2.4.01.png" path-detail="2.4.01.hd.png" alt="Examples of horizontal reflections, compressions, and elongations." %}


<div id='s5'/>
# Section 2.5 - Inverse Functions
* A function, $f$, is called **one-to-one** if everything in the range has exactly one element in the domain that maps to it. Formally, we say $f$ is one-to-one when $f(x_1)=f(x_2)$ implies that $x_1=x_2$. Another way to think about this: if $x_1\neq x_2$ then $f(x_1)\neq f(x_2)$.
	* $f(x)=x+5$ is one-to-one because if $f(x_1)=f(x_2)$ then $x_1+5=x_2+5$, and subtracting $5$ from both sides reveals that $x_1=x_2$.
	* $f(x)=x^2$ is not one-to-one because $f(-2)=f(2)$, but $-2\neq 2$. (It's easy to find other examples as well. E.g. $f(-5)=f(5)$, but $-5\neq 5$).
* **Horizontal line test.** A function is one-to-one precisely when every horizontal line crosses its graph at most once.
* **Inverses, generally speaking.** In mathematics, the word inverse gets used a lot. You are already familiar with a few inverses from arithmetic. The additive inverse of a number $x$ is $-x$ because $x+-x=0$ (and $0$ is the *additive identity*). The multiplicative inverse of a non-zero number $x$ is $1/x$ because $x\cdot\frac1x=1$ (and $1$ is the *multiplicative identity*).
* **Inverse functions.** In much the same way that the additive identity satisfies $x+0=x$, and the multiplicative identity satisfies $x\cdot 1=x$, the identity function is $i(x)=x$. If $f$ is a one-to-one function then its **inverse function** is denoted $f^{-1}$ and has the property that $f\circ f^{-1}=f^{-1}\circ f=i$.
	* Note: it is very rarely the case that $f^{-1}(x)=\frac{1}{f(x)}$. Writing such a thing down on an exam will result in a loss of points because it indicates a fundamental misunderstanding of function inverses.
	* For any given one-to-one function $f$, there is only one inverse function.
	* The domain of $f^{-1}$ is the same as the range of $f$.
	* The range of $f^{-1}$ is the same as the domain of $f$.
	* The equation $f(x)=y$ is equivalent to the equation $f^{-1}(y)=x$
	* $f^{-1}(f(x))=x$ and $f(f^{-1}(x))=x$
* **Finding the inverse of a one-to-one function.**
	* Set $y=f(x)$
	* Solve for $x$ in terms of $y$ (now you have $x=f^{-1}(y)$)
	* Interchange the variables $x$ and $y$ (now you have $y=f^{-1}(x)$, as desired)
* The graph of the inverse of the one-to-one function, $f$, is obtained by reflecting the graph of $y=f(x)$ about the line $y=x$. The effect of such a reflection is exactly that of interchanging the $x$ and $y$ coordinates of each point.
* {% include image.html path="2.5.01.png" path-detail="2.5.01.hd.png" alt="Examples of the graph of an inverse function." %}
