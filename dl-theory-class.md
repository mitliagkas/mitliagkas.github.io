---
layout: default
title: New class!
permalink: /ift6085-dl-theory-class/
---

IFT 6085: Theoretical principles for deep learning (new class)
=========

**NEW!**  [Extensive class bibliography](/ift6085-papers)

**Class discussion group:** please [sign up](https://groups.google.com/forum/#!forum/ift6085-h18) to receive announcements and participate in discussion.

Description
----- 

Research in deep learning produces state-of-the-art results on a number of machine learning tasks. Most of those advances are driven by intuition and massive exploration through trial and error. As a result, theory is currently lagging behind practice. The ML community does not fully understand why the best methods work. 
-	Why can we reliably optimize non-convex objectives? 
-	How expressive are our architectures, in terms of the hypothesis class they describe? 
-	Why do some of our most complex models generalize to unseen examples when we use datasets orders of magnitude smaller than what the classic statistical learning theory deems sufficient? 

A symptom of this lack of understanding is that deep learning methods largely lack guarantees and interpretability, two necessary properties for mission-critical applications. More importantly, a solid theoretical foundation can aid the design of a new generation of efficient methods—sans the need for blind trial-and-error-based exploration.

In this class we will go over a number of recent publications that attempt to shed light onto these questions. Before discussing the new results in each paper we will first introduce the necessary fundamental tools from optimization, statistics, information theory and statistical mechanics. The purpose of this class is to get students engaged with new research in the area. To that end, the majority of credit will be given for a class project report and presentation on a relevant topic.

**Prerequisites:**
This is meant to be an advanced graduate class for students who want to engage in theory-driven deep learning research. We will introduce the theoretical tools necessary, but start with the assumption that students are comfortable with basic probability and linear algebra. 

People
------

Lecturer: [Ioannis Mitliagkas](https://mitliagkas.github.io), 
	Office: 3359, André-Aisenstadt

Class info
----------
Winter 2018 semester:
- Wednesday 9h30-11h15  
- Thursday 9h30-11h15

Room: André-Aisestadt 3195

Office hours: 11:15am-12:15pm on Thursday right after class.


Evaluation
----------
Class project: 60%
Paper presentation: 25%
Scribing: 10%
Class participation: 5%

Use this Latex [template](ift6085/scribing_template.zip) for scribing.


Tentative topics--to be updated as we go along
---------

- Generalization: theoretical analysis and practical bounds 
- Information theory and its applications in ML (information bottleneck, lower bounds etc.) 
- Generative models beyond the pretty pictures: a tool for traversing the data manifold, projections, completion, substitutions etc. 
- Taming adversarial objectives: Wasserstein GANs, regularization approaches and controlling the dynamics 
- The expressive power of deep networks (deep information propagation, mean-field analysis of random networks etc.) 

Schedule
-------

**January 10th**
Class introduction
[[slides](ift6085/ift-6085-lecture-1.pdf),
[quiz](ift6085/quiz-first-class.pdf)]


---
### Crash course in optimization


**January 11th**
Basics of convex analysis and gradient descent
[[scribed notes](ift6085/ift-6085-lecture-2-notes.pdf)]

Reading:

Convex analysis basics from 'Convex Optimization' by Boyd, Vandenberge ([5] under references):
- Chapter 2 (required: beginning of chapter to 2.1.4,
recommended: 2.1.5 to end of section)
- Chapter 3 (required: beginning of chapter to 3.1,
recommended: 3.2, 3.3 and 3.4)

Convergence proofs:
from Chapter 3 of [1] ('Convex Optimization...' by S.Bubeck under References)
- Required: Convergence proof of Theorem 3.2 (note that we studied the unconstrained 
case. In this case the projection operator PiX(x) is the identity operator)

**January 17th**
The different rates of gradient descent: from Lipschitz to strongly convex
[[scribed notes](ift6085/ift-6085-lecture-3-notes.pdf)]

Reading:

Convergence proofs from Chapter 3 of [1] ('Convex Optimization...' by S.Bubeck under References)
- Required: Convergence proof of Theorem 3.12 

**January 18th**
Black box models and lower bounds 
[[scribed notes](ift6085/ift-6085-lecture-4-notes.pdf)]

Reading: [1, Theorem 3.15], [6]

**January 24th**
Accelerated methods
[[scribed notes](ift6085/ift-6085-lecture-5-notes.pdf)]

Reading: [6], [7, pages 67-76], [8], [9]

**January 25th**
Nesterov's Accelearted Gradient, Stochastic gradient descent
[[scribed notes](ift6085/ift-6085-lecture-6-notes.pdf)]

Reading: Section 6 until 6.2 of [1], Section 14.3 of [4]

---
### Crash course in statistical learning theory 


**January 31st**
Elements of statistical learning theory
[[scribed notes](ift6085/ift-6085-lecture-7-notes.pdf)]

Reading: Sections 2 (if you need the intro), 3, 4 and 6 of [4].

**February 1st**
PAC-Bayes bounds
[[scribed notes](ift6085/ift-6085-lecture-8-notes.pdf)]

Reading: [12]

Reading (harder): Section 6 of [2]

**February 7th**
Stability and generalization

Reading: [13]

---
### Seminar part of class

**February 8th**
Stability and generalization: Part II
Reading: [13,14]

**February 14th**
Applications of stability and PAC Bayes
Reading: [14,15]

**February 15th**
**NO CLASS** - Instructor is travelling

**February 21st**
Student paper presentations A



Resources
---------
1. [Convex Optimization: Algorithms and Complexity](https://arxiv.org/pdf/1405.4980.pdf), Sebastien Bubeck.
2. [Theory of classification: a survey of some recent advances](https://www.esaim-ps.org/articles/ps/pdf/2005/01/ps0420.pdf) Stephane Boucheron, Olivier Bousquet and Gabor Lugosi
3. iPython [notebook](https://github.com/anadim/ECE901/blob/master/sgd_vs_gd.ipynb) 
	demonstrating basic ideas of gradient descent and stochastic gradient descent,
	simple and complex models as well as generalization.
4. [Understanding Machine Learning: From Theory to Algorithms](http://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/index.html), by Shai Shalev-Shwartz and Shai Ben-David.
5. [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), Stephen Boyd and Lieven Vandenberghe.
6. [Nesterov's Accelerated Gradient Descent for Smooth and Strongly Convex Optimization](https://blogs.princeton.edu/imabandit/2014/03/06/nesterovs-accelerated-gradient-descent-for-smooth-and-strongly-convex-optimization/), blog post by Sebastien Bubeck.
7. [Introductory lectures on convex optimization](https://www.google.ca/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwjhs8Xc4-DYAhVRbK0KHYL4C1wQFgguMAA&url=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fdownload%3Fdoi%3D10.1.1.693.855%26rep%3Drep1%26type%3Dpdf&usg=AOvVaw3mGbk6W45sbV8b1rgS_DRV), Yurii Nesterov.
8. [Why momentum really works](https://distill.pub/2017/momentum/), blog post by Gabriel Goh (this blog post uses a slightly different parametrization of the momentum algorithm. The version we discuss in class, only applies the learning rate on the gradient.)
9. [YellowFin and the Art of Momentum Tuning](papers/yellowfin2017.pdf), preprint J. Zhang, I. Mitliagkas, C. Ré.
10. [Large-scale Machine Learning and Optimization (class)](http://papail.io/901), Dimitris Papailiopoulos, University of Wisconsin.
11. [Advanced Machine Learning Systems (class)](http://www.cs.cornell.edu/courses/cs6787/2017fa/), Chris De Sa, Cornell University.
12. [A PAC-Bayesian Tutorial with A Dropout Bound](https://arxiv.org/abs/1307.2118), David McAllester.
13. [Stability and generalization](http://www.jmlr.org/papers/volume2/bousquet02a/bousquet02a.pdf), O. Bousquet, A. Elisseeff.
14. [Train faster, generalize better: Stability of stochastic gradient descent](https://arxiv.org/pdf/1509.01240.pdf), M. Hardt, B. Recht, Y. Singer.
15. [Computing Nonvacuous Generalization Bounds for Deep (Stochastic) Neural Networks with Many More Parameters than Training Data](https://arxiv.org/abs/1703.11008), Gintare Karolina Dziugaite, Daniel M. Roy





