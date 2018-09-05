<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
</head>
<body>
<div id="header">
<h1 class="title">Homework 1</h1>
</div>
<h1 id="due-september-13-2018-1159-pm-est" class="unnumbered"><strong>Due: September 13, 2018, 11:59 PM EST</strong></h1>
<h1 id="instructions" class="unnumbered"><strong>Instructions</strong></h1>
<p>Your homework submission must cite any references used (including articles, books, code, websites, and personal communications). All solutions must be written in your own words, and you must program the algorithms yourself. If you do work with others, you must list the people you worked with. If you solve any problems by hand just digitize that page and submit it (make sure the problem is labeled).<br /> <br />
Your programs must be written in Python. All code be able to compile and run for full credit. Comment all code following proper coding conventions. Remember, if we can’t read it, we can’t grade it! (For more information on python coding standards, refer to: <a href="https://www.python.org/dev/peps/pep-0008/">Coding Conventions</a>)<br /> <br />
You should submit your assignment via Github. Submit your solutions as a PDF named "hw(hw #).pdf". For example, homework 1 should be submitted as hw01.pdf. If the assignment requires coding, submit your code as a .py file with the same name.<br /> <br />
If you have any questions address them to:</p>
<ul>
<li><p>Connor McCurley (TA) – cmccurley@ufl.edu</p></li>
<li><p>Xiaolei Guo (TA) – suninth@ufl.edu</p></li>
<li><p>Daniel Wells (TA) – dwells@ufl.edu</p></li>
</ul>
<h1 id="question-1---10-points" class="unnumbered">Question 1 - 10 points</h1>
<p>Consider the polynomial curve fitting example discussed in class. As discussed, when the model order is <em>too</em> small, the training data is generally <em>underfit</em> and when the model order is <em>too</em> high, the result can <em>overfit</em> the training data. Write a small script of code that mimics our polynomial curve fitting function. The code should generate simulated data from the true function with added zero-mean Gaussian noise (with the true function assumed to be sinc function). The code should also generate a separate validation test data set generated in the same way. Then, after fitting the polynomial to the training data across a range of model orders and evaluated on both the training and testing data, your code should generate a plot similar to the one shown in Figure 1. Also, provide a discussion based on your plot about which model order, <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=M" alt="M" title="M" />, should be used to avoid over-training.</p>
<p><br /><img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=sinc%28x%29%20%3D%20%5Cleft%5C%7B%0A%5Cbegin%7Barray%7D%7Bll%7D%0A%20%20%20%20%20%201%20%26%20for%20%5C%3A%20x%3D0%20%5C%5C%0A%20%20%20%20%20%20%5Cfrac%7Bsin%28x%29%7D%7Bx%7D%20%26%20otherwise%5C%5C%0A%5Cend%7Barray%7D%20%0A%5Cright." alt="sinc(x) = \left\{
\begin{array}{ll}
      1 &amp; for \: x=0 \\
      \frac{sin(x)}{x} &amp; otherwise\\
\end{array} 
\right." title="sinc(x) = \left\{
\begin{array}{ll}
      1 &amp; for \: x=0 \\
      \frac{sin(x)}{x} &amp; otherwise\\
\end{array} 
\right." /><br /></p>
<div class="figure">
<embed src="/problem1.jpg" height="300" width="400"/>
<p class="caption">Figure 1.5 from the Bishop textbook. The y-axis corresponds to the root-mean-square error between the predicted and the true value (on either the training data or test data sets). The x-axis corresponds to the model order. </p>
</div>
<h1 id="question-2---10-points" class="unnumbered">Question 2 - 10 points</h1>
<h2 id="recall" class="unnumbered">Recall:</h2>
<p>Assuming a univariate Gaussian data likelihood given <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=N" alt="N" title="N" /> i.i.d. data points:</p>
<p><br /><img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=p%28%5Cmathbf%7BX%7D%7C%5Cmu%29%20%3D%20%5Cprod%5E%7BN%7D_%7Bn%3D1%7D%5Cmathcal%7BN%7D%28x_n%7C%5Cmu%2C%5Csigma%5E2%29" alt="p(\mathbf{X}|\mu) = \prod^{N}_{n=1}\mathcal{N}(x_n|\mu,\sigma^2)" title="p(\mathbf{X}|\mu) = \prod^{N}_{n=1}\mathcal{N}(x_n|\mu,\sigma^2)" /><br /></p>
<p>and a Gaussian prior distribution on the mean:</p>
<p><br /><img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=p%28%5Cmu%7C%5Cmu_0%29%20%3D%20%5Cmathcal%7BN%7D%28%5Cmu%7C%5Cmu_0%2C%5Csigma%5E%7B2%7D_%7B0%7D%29" alt="p(\mu|\mu_0) = \mathcal{N}(\mu|\mu_0,\sigma^{2}_{0})" title="p(\mu|\mu_0) = \mathcal{N}(\mu|\mu_0,\sigma^{2}_{0})" /><br /></p>
<p>with fixed variances (<img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Csigma%5E2%2C%20%5Csigma%5E%7B2%7D_%7B0%7D" alt="\sigma^2, \sigma^{2}_{0}" title="\sigma^2, \sigma^{2}_{0}" />, and <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Csigma%5E2%20%5Cneq%20%5Csigma%5E%7B2%7D_%7B0%7D" alt="\sigma^2 \neq \sigma^{2}_{0}" title="\sigma^2 \neq \sigma^{2}_{0}" />), the posterior distribution is given by:</p>
<p><br /><img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=p%28%5Cmu%7C%5Cmathbf%7BX%7D%29%20%3D%20%5Cmathcal%7BN%7D%28%5Cmu%7C%5Cmu_N%2C%5Csigma%5E%7B2%7D_%7BN%7D%29" alt="p(\mu|\mathbf{X}) = \mathcal{N}(\mu|\mu_N,\sigma^{2}_{N})" title="p(\mu|\mathbf{X}) = \mathcal{N}(\mu|\mu_N,\sigma^{2}_{N})" /><br /></p>
<p>where</p>
<p><br /><img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmu_N%20%3D%20%5Cfrac%7B%5Csigma%5E2%7D%7BN%5Csigma%5E%7B2%7D_%7B0%7D%20%2B%20%5Csigma%5E2%7D%5Cmu_0%20%2B%20%5Cfrac%7BN%5Csigma%5E%7B2%7D_%7B0%7D%7D%7BN%5Csigma%5E%7B2%7D_%7B0%7D%20%2B%20%5Csigma%5E2%7D%5Cmu_%7BML%7D" alt="\mu_N = \frac{\sigma^2}{N\sigma^{2}_{0} + \sigma^2}\mu_0 + \frac{N\sigma^{2}_{0}}{N\sigma^{2}_{0} + \sigma^2}\mu_{ML}" title="\mu_N = \frac{\sigma^2}{N\sigma^{2}_{0} + \sigma^2}\mu_0 + \frac{N\sigma^{2}_{0}}{N\sigma^{2}_{0} + \sigma^2}\mu_{ML}" /><br /></p>
<p><br /><img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cfrac%7B1%7D%7B%5Csigma%5E%7B2%7D_%7BN%7D%7D%20%3D%20%5Cfrac%7B1%7D%7B%5Csigma%5E%7B2%7D%7D%20%2B%20%5Cfrac%7BN%7D%7B%5Csigma%5E%7B2%7D%7D" alt="\frac{1}{\sigma^{2}_{N}} = \frac{1}{\sigma^{2}} + \frac{N}{\sigma^{2}}" title="\frac{1}{\sigma^{2}_{N}} = \frac{1}{\sigma^{2}} + \frac{N}{\sigma^{2}}" /><br /></p>
<p>where <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmu_%7BML%7D" alt="\mu_{ML}" title="\mu_{ML}" /> is the maximum likelihood solution for <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmu" alt="\mu" title="\mu" /> given the <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=N" alt="N" title="N" /> data points.</p>
<ul>
<li><p>In or Binomial/Beta example in class, we computed the ML and MAP solutions for the <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmu" alt="\mu" title="\mu" /> parameter of the Binomial distribution iteratively with an increasing number of trials/random draws. Recall, the parameter <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmu" alt="\mu" title="\mu" /> represented the probability of heads.</p></li>
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
<p>Consider <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=f%28%5Cmathbf%7Bx%7D%29%20%3D%203%5Cmathbf%7Bx%7D%5ET%5Cmathbf%7Bx%7D%20%2B%204%5Cmathbf%7By%7D%5ET%5Cmathbf%7Bx%7D%20-%201" alt="f(\mathbf{x}) = 3\mathbf{x}^T\mathbf{x} + 4\mathbf{y}^T\mathbf{x} - 1" title="f(\mathbf{x}) = 3\mathbf{x}^T\mathbf{x} + 4\mathbf{y}^T\mathbf{x} - 1" /> where <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7Bx%7D%2C%20%5Cmathbf%7By%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed" alt="\mathbf{x}, \mathbf{y} \in \mathbb{R}^d" title="\mathbf{x}, \mathbf{y} \in \mathbb{R}^d" />.</p>
<ol>
<li><p>What is <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%5Cmathbf%7Bx%7D%7D" alt="\frac{\partial f}{\partial\mathbf{x}}" title="\frac{\partial f}{\partial\mathbf{x}}" />? Show your work.</p></li>
</ol>
<h1 id="question-4---5-points" class="unnumbered">Question 4 - 5 points</h1>
<p>Consider <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=f%28%5Cmathbf%7Bx%7D%29%20%3D%20-10%5Cmathbf%7Bx%7D%5ET%5Cmathbf%7BQ%7D%5Cmathbf%7Bx%7D%20%2B%204%5Cmathbf%7By%7D%5ET%5Cmathbf%7Bx%7D%20%2B%202" alt="f(\mathbf{x}) = -10\mathbf{x}^T\mathbf{Q}\mathbf{x} + 4\mathbf{y}^T\mathbf{x} + 2" title="f(\mathbf{x}) = -10\mathbf{x}^T\mathbf{Q}\mathbf{x} + 4\mathbf{y}^T\mathbf{x} + 2" /> where <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7Bx%7D%2C%20%5Cmathbf%7By%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed" alt="\mathbf{x}, \mathbf{y} \in \mathbb{R}^d" title="\mathbf{x}, \mathbf{y} \in \mathbb{R}^d" />, <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7BQ%7D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bd%5Ctimes%20d%7D" alt="\mathbf{Q} \in \mathbb{R}^{d\times d}" title="\mathbf{Q} \in \mathbb{R}^{d\times d}" /> and <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7BQ%7D" alt="\mathbf{Q}" title="\mathbf{Q}" /> is symmetric.</p>
<ol>
<li><p>What is <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%5Cmathbf%7Bx%7D%7D" alt="\frac{\partial f}{\partial\mathbf{x}}" title="\frac{\partial f}{\partial\mathbf{x}}" />? Show your work.</p></li>
</ol>
<h1 id="question-5---5-points" class="unnumbered">Question 5 - 5 points</h1>
<p>Consider <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=f%28%5Cmathbf%7Bx%7D%29%20%3D%208%5Cmathbf%7Bx%7D%5ET%5Cmathbf%7BQ%7D%5Cmathbf%7Bx%7D%20-%202%5Cmathbf%7By%7D%5ET%5Cmathbf%7BQ%7D%5ET%5Cmathbf%7Bx%7D%20%2B%206" alt="f(\mathbf{x}) = 8\mathbf{x}^T\mathbf{Q}\mathbf{x} - 2\mathbf{y}^T\mathbf{Q}^T\mathbf{x} + 6" title="f(\mathbf{x}) = 8\mathbf{x}^T\mathbf{Q}\mathbf{x} - 2\mathbf{y}^T\mathbf{Q}^T\mathbf{x} + 6" /> where <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7Bx%7D%2C%20%5Cmathbf%7By%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed" alt="\mathbf{x}, \mathbf{y} \in \mathbb{R}^d" title="\mathbf{x}, \mathbf{y} \in \mathbb{R}^d" />, <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7BQ%7D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bd%5Ctimes%20d%7D" alt="\mathbf{Q} \in \mathbb{R}^{d\times d}" title="\mathbf{Q} \in \mathbb{R}^{d\times d}" /> and <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7BQ%7D" alt="\mathbf{Q}" title="\mathbf{Q}" /> is symmetric.</p>
<ol>
<li><p>What is <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%5Cmathbf%7Bx%7D%5ET%7D" alt="\frac{\partial f}{\partial\mathbf{x}^T}" title="\frac{\partial f}{\partial\mathbf{x}^T}" />? Show your work.</p></li>
<li><p>What is <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%5Cmathbf%7BQ%7D%7D" alt="\frac{\partial f}{\partial\mathbf{Q}}" title="\frac{\partial f}{\partial\mathbf{Q}}" />? Show your work.</p></li>
</ol>
<h1 id="question-6---5-points" class="unnumbered">Question 6 - 5 points</h1>
<p>Consider <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=f%28%5Cmathbf%7Bx%7D%29%20%3D%20%5Cleft%5C%7C%5Cmathbf%7B4x%7D%5Cright%5C%7C_%7B2%7D%5E%7B2%7D" alt="f(\mathbf{x}) = \left\|\mathbf{4x}\right\|_{2}^{2}" title="f(\mathbf{x}) = \left\|\mathbf{4x}\right\|_{2}^{2}" /> where <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cmathbf%7Bx%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed" alt="\mathbf{x} \in \mathbb{R}^d" title="\mathbf{x} \in \mathbb{R}^d" />.</p>
<ol>
<li><p>What is <img style="vertical-align:middle" src="http://chart.apis.google.com/chart?cht=tx&amp;chl=%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%5Cmathbf%7Bx%7D%7D" alt="\frac{\partial f}{\partial\mathbf{x}}" title="\frac{\partial f}{\partial\mathbf{x}}" />? Show your work.</p></li>
</ol>
</body>
</html>