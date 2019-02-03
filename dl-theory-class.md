---
layout: default
title: DL Theory class
permalink: /ift6085-dl-theory-class/
---

(Winter 2018) IFT 6085: Theoretical principles for deep learning 
=========


**This is an old version of the class. For the 2019 class check [here](/ift6085-dl-theory-class-2019/).**


[Extensive class bibliography](/ift6085-papers)

**Class discussion group:** please [sign up](https://groups.google.com/forum/#!forum/ift6085-hiver-2019-theoretical-principles-for-deep-learning) to receive announcements and participate in discussion.

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
[[scribed notes](ift6085/ift-6085-lecture-9-notes.pdf)]

Reading: [13]

**February 8th**
Stability and generalization: Part II
[[scribed notes](ift6085/ift-6085-lecture-10-notes.pdf)]

Reading: [13,14]

---
### Seminar part of class


**February 14th**
Applications of stability and PAC Bayes
[[scribed notes](ift6085/ift-6085-lecture-11-notes.pdf)]

Reading: [14,15]

**February 15th**
**NO CLASS** - Instructor is travelling

**February 21st**
Student paper presentations A

- [Understanding deep learning requires rethinking generalization, Zhang C, Bengio S, Hardt M, Recht B, Vinyals O.](ift6085/student_slides/IFT6085_Presentation_Rethinking.pdf)
**Presented by**: Aldo Lamarre, Matthew C. Scicluna
- [Emergence of invariance and disentanglement in Deep Representations,
Alessandro Achille, Stefano Soatto](ift6085/student_slides/IFT6085_Presentation_Emergence.pdf)
**Presented by**: Aristide Baratin, Brady Neal, Nithin Vasisth 
- [High-dimensional dynamics of generalization error in neural networks, Madhu S. Advani, Andrew M. Saxe](ift6085/student_slides/IFT6085_Presentation_High_Dimensional_Dynamics.pdf)
**Presented by**: Reyhane Askari, Arian Hosseini, Mohammad Pezeshki

**February 22nd**
Generative models
[[scribed notes](ift6085/ift-6085-lecture-12-notes.pdf)]

Reading: [16,17]

**February 28th**
Student paper presentations B

- [Optimizing Neural Networks with Kronecker-factored Approximate Curvature, James Martens, Roger Grosse](ift6085/student_slides/IFT6085_Presentation_KFAC.pdf)
**Presented by**: Josh Romoff & Riashat Islam 
- [Opening the black box of Deep Neural Networks via Information, Ravid Shwartz-Ziv, Naftali Tishby](ift6085/student_slides/IFT6085_Presentation_IB.pdf)
**Presented by**: Philip Amortila and Nicolas Gagné
- [Why and When Can Deep -- but Not Shallow -- Networks Avoid the Curse of Dimensionality, Tomaso Poggio, Hrushikesh Mhaskar, Lorenzo Rosasco, Brando Miranda, Qianli Liao](ift6085/student_slides/IFT6085_Presentation_WhyAndWhen.pdf)
**Presented by**: William Fedus, Christos Tsirigotis, Breandan Considine
- [Flow-GAN: Combining Maximum Likelihood and Adversarial Learning in Generative Models, Aditya Grover, Manik Dhar, Stefano Ermon](ift6085/student_slides/IFT6085_Presentation_FlowGAN.pdf)
**Presented by**: Amy Zhang, Kyle Kastner, Lluís Castrejón

**March 1st**
Wasserstein GANs
[[scribed notes](ift6085/ift-6085-lecture-13-notes.pdf)]

Reading: [18,19]

**March 7th**
**BREAK** No class

**March 8th**
**BREAK** No class

**March 14th**
Student paper presentations C

- Compressed Sensing using Generative Models, Ashish Bora, Ajil Jalal, Eric Price, Alexandros G. Dimakis
- Generalization and Equilibrium in Generative Adversarial Nets (GANs), Sanjeev Arora, Rong Ge, Yingyu Liang, Tengyu Ma, Yi Zhang
- Do GANs actually learn the distribution? An empirical study, Sanjeev Arora, Yi Zhang
- Demystifying MMD GANs,
Mikołaj Bińkowski, Dougal J. Sutherland, Michael Arbel, Arthur Gretton

**March 15th**
The Numerics of GANs
[[scribed notes](ift6085/ift-6085-lecture-14-notes.pdf)]

Reading: [20]

**March 21st**
Variance reduction techniques for stochastic optimization
[[scribed notes](ift6085/ift-6085-lecture-15-notes.pdf)]

Reading: [22], Section 5.3 of [21]

**March 22nd**
Weighted Sums of Random Kitchen Sinks: Replacing
minimization with randomization in learning

Reading: [23]


**March 28th**
**NO CLASS** - Instructor is travelling

**March 29th**
PacGAN: The power of two samples in generative adversarial networks

Reading: [24]

**April 4th**
Some results on non-convex optimization

Reading: [25,26]

**April 5th**
Escaping saddle points
[[scribed notes](ift6085/ift-6085-lecture-16-notes.pdf)]
[slides by Yang Yuan](http://www.callowbird.com/uploads/8/6/6/4/8664563/1.pdf)

Reading: [27, 28]

**April 11th**
The theory of spin glasses

Guest lecture by **Alex Fribergh**, UdeM Math.

Reading: [29]


**April 12th**
The Loss Surfaces of Multilayer Networks

Reading: [30]

**April 25th**
**Class project poster presentation**
<details>
16 group posters, pizza, and science. All are welcome!
</details>



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
9. [YellowFin and the Art of Momentum Tuning](https://arxiv.org/abs/1706.03471), preprint J. Zhang, I. Mitliagkas.
10. [Large-scale Machine Learning and Optimization (class)](http://papail.io/901), Dimitris Papailiopoulos, University of Wisconsin.
11. [Advanced Machine Learning Systems (class)](http://www.cs.cornell.edu/courses/cs6787/2017fa/), Chris De Sa, Cornell University.
12. [A PAC-Bayesian Tutorial with A Dropout Bound](https://arxiv.org/abs/1307.2118), David McAllester.
13. [Stability and generalization](http://www.jmlr.org/papers/volume2/bousquet02a/bousquet02a.pdf), O. Bousquet, A. Elisseeff.
14. [Train faster, generalize better: Stability of stochastic gradient descent](https://arxiv.org/pdf/1509.01240.pdf), M. Hardt, B. Recht, Y. Singer.
15. [Computing Nonvacuous Generalization Bounds for Deep (Stochastic) Neural Networks with Many More Parameters than Training Data](https://arxiv.org/abs/1703.11008), Gintare Karolina Dziugaite, Daniel M. Roy
16. [Lecture notes on generative learning algorithms](http://cs229.stanford.edu/notes/cs229-notes2.pdf), Andrew Ng
17. [Generative Adversarial Nets](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf), Ian Goodfellow et al.
18. [Wasserstein GAN](https://arxiv.org/abs/1701.07875), Martin Arjovsky, Soumith Chintala, Léon Bottou 
19. [Read-through: Wasserstein GAN](https://www.alexirpan.com/2017/02/22/wasserstein-gan.html), Alex Irpan
20. [The Numerics of GANs](https://arxiv.org/pdf/1705.10461.pdf), Lars Mescheder, Sebastian Nowozin, Andreas Geiger
21. [Optimization Methods for Large-Scale Machine Learning](https://arxiv.org/pdf/1606.04838v1.pdf), Léon Bottou, Frank E. Curtis, Jorge Nocedal
22. [Accelerating Stochastic Gradient Descent using Predictive Variance Reduction](http://papers.nips.cc/paper/4937-accelerating-stochastic-gradient-descent-using-predictive-variance-reduction.pdf), Rie Johnson, Tong Zhang
23. [Weighted Sums of Random Kitchen Sinks: Replacingminimization with randomization in learning](https://people.eecs.berkeley.edu/~brecht/papers/08.rah.rec.nips.pdf), Ali Rahimi, Ben Recht
24. [PacGAN: The power of two samples in generative adversarial networks](https://arxiv.org/abs/1712.04086), Zinan Lin, Ashish Khetan, Giulia Fanti, Sewoong Oh
25. [Stochastic First- and Zeroth-order Methods for Nonconvex Stochastic Programming](https://arxiv.org/abs/1309.5549), Saeed Ghadimi, Guanghui Lan
26. [Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Łojasiewicz Condition](https://arxiv.org/abs/1608.04636), Hamed Karimi, Julie Nutini, Mark Schmidt
27. [Escaping From Saddle Points --- Online Stochastic Gradient for Tensor Decomposition](https://arxiv.org/abs/1503.02101), Rong Ge, Furong Huang, Chi Jin, Yang Yuan
28. [How to Escape Saddle Points Efficiently](https://arxiv.org/abs/1703.00887), Chi Jin, Rong Ge, Praneeth Netrapalli, Sham M. Kakade, Michael I. Jordan
29. [RANDOM MATRICES AND COMPLEXITY OF SPIN GLASSES](https://arxiv.org/pdf/1003.1129.pdf), ANTONIO AUFFINGER, GERARD BEN AROUS, AND JIRI CERNY 
30. [The Loss Surfaces of Multilayer Networks](https://arxiv.org/abs/1412.0233), Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, Yann LeCun 


