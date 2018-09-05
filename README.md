<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <title>Homework 1</title>
  <style type="text/css">code{white-space: pre;}</style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.1.0/katex.min.js"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.1.0/katex.min.css" /><script type="text/javascript">window.onload = function(){var mathElements = document.getElementsByClassName("math");
  for (var i=0; i < mathElements.length; i++)
  {
   var texText = mathElements[i].firstChild
   katex.render(texText.data, mathElements[i])
  }}
  </script>
</head>
<body>
<div id="header">
<h1 class="title">Homework 1</h1>
</div>
<h1 id="due-september-13-2018-1159-pm-est" class="unnumbered"><strong>Due: September 13, 2018, 11:59 PM EST</strong></h1>
<h1 id="instructions" class="unnumbered"><strong>Instructions</strong></h1>
<p>Your homework submission must cite any references used (including articles, books, code, websites, and personal communications). All solutions must be written in your own words, and you must program the algorithms yourself. If you do work with others, you must list the people you worked with. If you solve any problems by hand just digitize that page and submit it (make sure the problem is labeled).<br />
Your programs must be written in Python. All code be able to compile and run for full credit. Comment all code following proper coding conventions. Remember, if we can’t read it, we can’t grade it! (For more information on python coding standards, refer to: <em>https://www.python.org/dev/peps/pep-0008/</em>)<br />
You should submit your assignment via Github. Submit your solutions as a PDF named ”hw(hw #).pdf”. For example, homework 1 should be submitted as hw01.pdf. If the assignment requires coding, submit your code as a .py file with the same name.<br />
If you have any questions address them to:</p>
<ul>
<li><p>Connor McCurley (TA) – cmccurley@ufl.edu</p></li>
<li><p>Xiaolei Guo (TA) – suninth@ufl.edu</p></li>
<li><p>Daniel Wells (TA) – dwells@ufl.edu</p></li>
</ul>
<h1 id="question-1---10-points" class="unnumbered">Question 1 - 10 points</h1>
<p>Consider the polynomial curve fitting example discussed in class. As discussed, when the model order is <em>too</em> small, the training data is generally <em>underfit</em> and when the model order is <em>too</em> high, the result can <em>overfit</em> the training data. Write a small script of code that mimics our polynomial curve fitting function. The code should generate simulated data from the true function with added zero-mean Gaussian noise (with the true function assumed to be sinc function). The code should also generate a separate validation test data set generated in the same way. Then, after fitting the polynomial to the training data across a range of model orders and evaluated on both the training and testing data, your code should generate a plot similar to the one shown in Figure 1. Also, provide a discussion based on your plot about which model order, <span class="math inline">M</span>, should be used to avoid over-training.</p>
<p><span class="math display">\displaystyle sinc(x) = \left\{
\begin{array}{ll}
      1 &amp; for \: x=0 \\
      \frac{sin(x)}{x} &amp; otherwise\\
\end{array} 
\right.</span></p>
<div class="figure">
<embed src="problem1.pdf" />
<p class="caption">Figure 1.5 from the Bishop textbook. The y-axis corresponds to the root-mean-square error between the predicted and the true value (on either the training data or test data sets). The x-axis corresponds to the model order. </p>
</div>
<h1 id="question-2---10-points" class="unnumbered">Question 2 - 10 points</h1>
<h2 id="recall" class="unnumbered">Recall:</h2>
<p>Assuming a univariate Gaussian data likelihood given <span class="math inline">N</span> i.i.d. data points:</p>
<p><span class="math display">\displaystyle p(\mathbf{X}|\mu) = \prod^{N}_{n=1}\mathcal{N}(x_n|\mu,\sigma^2)</span></p>
<p>and a Gaussian prior distribution on the mean:</p>
<p><span class="math display">\displaystyle p(\mu|\mu_0) = \mathcal{N}(\mu|\mu_0,\sigma^{2}_{0})</span></p>
<p>with fixed variances (<span class="math inline">\sigma^2, \sigma^{2}_{0}</span>, and <span class="math inline">\sigma^2 \neq \sigma^{2}_{0}</span>), the posterior distribution is given by:</p>
<p><span class="math display">\displaystyle p(\mu|\mathbf{X}) = \mathcal{N}(\mu|\mu_N,\sigma^{2}_{N})</span></p>
<p>where</p>
<p><span class="math display">\displaystyle \mu_N = \frac{\sigma^2}{N\sigma^{2}_{0} + \sigma^2}\mu_0 + \frac{N\sigma^{2}_{0}}{N\sigma^{2}_{0} + \sigma^2}\mu_{ML}</span></p>
<p><span class="math display">\displaystyle \frac{1}{\sigma^{2}_{N}} = \frac{1}{\sigma^{2}} + \frac{N}{\sigma^{2}}</span></p>
<p>where <span class="math inline">\mu_{ML}</span> is the maximum likelihood solution for <span class="math inline">\mu</span> given the <span class="math inline">N</span> data points.</p>
<ul>
<li><p>In or Binomial/Beta example in class, we computed the ML and MAP solutions for the <span class="math inline">\mu</span> parameter of the Binomial distribution iteratively with an increasing number of trials/random draws. Recall, the parameter <span class="math inline">\mu</span> represented the probability of heads.</p></li>
<li><p>In this homework question, you will do the same sort of experiment for random draws from a Gaussian distribution (i.e., a Gaussian data likelihood) with a Gaussian prior distribution on the mean parameter (assume a fixed, known variance for both the Gaussian likelihood and Gaussian prior).</p></li>
<li><p>Write a script that iteratively draws one data point from the true Gaussian distribution (with known mean). Each iteration, compute and ML solution and the MAP solution for the Gaussian mean. After each draw, update the prior distribution to be replaced with the posterior distribution from the previous draw (just like the Binomal/Beta example in class).</p></li>
<li><p>In your solution, provide:</p>
<ul>
<li><p>Display multiple sample runs of your code and include a description of what the code shows you about ML vs MAP solutions. Your discussion should illustrate that you understand ML and MAP concepts and their differences. Your discussion should answer, at a minimum, the following questions:</p>
<ul>
<li><p>What happens when the prior mean is initialized to the wrong value? To the correct value?</p></li>
<li><p>What happens as you vary the prior variance from small to large?</p></li>
<li><p>What happens when the likelihood variance is varied from small to large?</p></li>
<li><p>How do the initial values of the prior mean, prior variance, and likelihood variance interact to effect the final estimate of the mean?</p></li>
</ul></li>
</ul></li>
</ul>
<h1 id="question-3---5-points" class="unnumbered">Question 3 - 5 points</h1>
<p>Consider <span class="math inline">f(\mathbf{x}) = 3\mathbf{x}^T\mathbf{x} + 4\mathbf{y}^T\mathbf{x} - 1</span> where <span class="math inline">\mathbf{x}, \mathbf{y} \in \mathbb{R}^d</span>.</p>
<ol>
<li><p>What is <span class="math inline">\frac{\partial f}{\partial\mathbf{x}}</span>? Show your work.</p></li>
</ol>
<h1 id="question-4---5-points" class="unnumbered">Question 4 - 5 points</h1>
<p>Consider <span class="math inline">f(\mathbf{x}) = -10\mathbf{x}^T\mathbf{Q}\mathbf{x} + 4\mathbf{y}^T\mathbf{x} + 2</span> where <span class="math inline">\mathbf{x}, \mathbf{y} \in \mathbb{R}^d</span>, <span class="math inline">\mathbf{Q} \in \mathbb{R}^{d\times d}</span> and <span class="math inline">\mathbf{Q}</span> is symmetric.</p>
<ol>
<li><p>What is <span class="math inline">\frac{\partial f}{\partial\mathbf{x}}</span>? Show your work.</p></li>
</ol>
<h1 id="question-5---5-points" class="unnumbered">Question 5 - 5 points</h1>
<p>Consider <span class="math inline">f(\mathbf{x}) = 8\mathbf{x}^T\mathbf{Q}\mathbf{x} - 2\mathbf{y}^T\mathbf{Q}^T\mathbf{x} + 6</span> where <span class="math inline">\mathbf{x}, \mathbf{y} \in \mathbb{R}^d</span>, <span class="math inline">\mathbf{Q} \in \mathbb{R}^{d\times d}</span> and <span class="math inline">\mathbf{Q}</span> is symmetric.</p>
<ol>
<li><p>What is <span class="math inline">\frac{\partial f}{\partial\mathbf{x}^T}</span>? Show your work.</p></li>
<li><p>What is <span class="math inline">\frac{\partial f}{\partial\mathbf{Q}}</span>? Show your work.</p></li>
</ol>
<h1 id="question-6---5-points" class="unnumbered">Question 6 - 5 points</h1>
<p>Consider <span class="math inline">f(\mathbf{x}) = \left\|\mathbf{4x}\right\|_{2}^{2}</span> where <span class="math inline">\mathbf{x} \in \mathbb{R}^d</span>.</p>
<ol>
<li><p>What is <span class="math inline">\frac{\partial f}{\partial\mathbf{x}}</span>? Show your work.</p></li>
</ol>
</body>
</html>
