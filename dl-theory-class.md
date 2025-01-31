---
layout: default
title: DL Theory class
menu: main
permalink: /ift6085-dl-theory-class/
order: 2
---

IFT 6169: Theoretical principles for deep learning
=========

**THIS CLASS IS NOT OFFERED IN WINTER 2024** 


Description
----- 

Research in deep learning produces state-of-the-art results on a number of machine learning tasks. Most of those advances are driven by intuition and massive exploration through trial and error. As a result, theory is currently lagging behind practice. The ML community does not fully understand why the best methods work. 
-	Why can we reliably optimize non-convex objectives? 
-	How expressive are our architectures, in terms of the hypothesis class they describe? 
-	Why do some of our most complex models generalize to unseen examples when we use datasets orders of magnitude smaller than what the classic statistical learning theory deems sufficient? 

A symptom of this lack of understanding is that deep learning methods largely lack guarantees and interpretability, two necessary properties for mission-critical applications. More importantly, a solid theoretical foundation can aid the design of a new generation of efficient methods—sans the need for blind trial-and-error-based exploration.

In this class we will go over a number of recent publications that attempt to shed light onto these questions. Before discussing the new results in each paper we will first introduce the necessary fundamental tools from optimization, statistics, information theory and statistical mechanics. The purpose of this class is to get students engaged with new research in the area. To that end, the majority of credit will be given for a class project report and presentation on a relevant topic.

**Prerequisites:**
This is a graduate class for students who want to engage in theory-driven deep learning research.
We will introduce some theoretical tools necessary.
- Probability
- Linear algebra
- Machine learning 


People
------

Instructor: [Ioannis Mitliagkas](https://mitliagkas.github.io)

TAs: [Jose Gallego](https://jgalle29.github.io/),
[Motahareh Sohrabi](https://motahareh-sohrabi.github.io/)

Class info
----------
Winter 2023 semester:
- Wednesday 9h30-11h15  
- Thursday 9h30-11h15

Location (Hybrid):
- In person at Mila's Auditorium 2 (located at 6650 Saint-Urbain, first floor. No key card needed to access)
- Online via [Zoom](https://umontreal.zoom.us/j/89831162230?pwd=Skc4YXlCK1ZvQWh3MytDTXVpenQ4dz09)
- Video recordings of lectures will be made available after lectures end.

**First class**: Thursday, January 12th, 2023. 

Office hours: 11:15am-12:00pm on Thursday right after class.


Registering and auditing
--------
If you want to audit the class, please fill this [form](https://forms.gle/w7LkmxWKCo9nX3aK8).
You will get access to the course material, but you will not be able to submit work or be graded. 



Communication
------------- 
We will use the class's [Studium](https://studium.umontreal.ca/course/view.php?id=237083)to make announcements.
We will use a Slack workspace for discussion. Please keep an eye out for an invitation to the Slack. 
We will use Gradescope for quizzes and report submissions.
If you have something personal/sensitive to discuss, feel free to email me or the TA.
Starting your email subject with 'IFT6169:' will ensure that your email is not miscategorized. 

Evaluation
----------
- Class project on a research topic: 35%
- Paper presentations: 25%
- Midterm exam: 15%
- Quizzes: 20%
- Class participation: 5%

Use this Latex [template](ift6085-2019/scribing_template.zip) for scribing.


Tentative topics--to be updated as we go along
---------

- Generalization: theoretical analysis and practical bounds 
- Information theory and its applications in ML (information bottleneck, lower bounds etc.) 
- Generative models beyond the pretty pictures: a tool for traversing the data manifold, projections, completion, substitutions etc. 
- Taming adversarial objectives: Wasserstein GANs, regularization approaches and controlling the dynamics 
- The expressive power of deep networks (deep information propagation, mean-field analysis of random networks etc.) 

Extensive class bibliography
--------

You can find a large number of recent (mostly) research papers related to the class's objectives 
[here](/ift6085-papers-2020).
You can use those for your in-class paper presentations and projects.

Schedule
-------

For the first half of the class we will be closely following the
[previous iteration](/ift6085-dl-theory-class-2021) of the class.


**January 12th**
Class introduction
[[slides](/ift6169-2023/ift-6169-lecture-1.pdf),
[old quiz](ift6085-2019/quiz-first-class.pdf)]



---
<br/>

### Crash course in optimization


**January 18th**
Basics of convex analysis and gradient descent
[[scribed notes](ift6085-2020/ift-6085-lecture-2-notes.pdf)]

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

**January 19th**
[continuation of previous lecture]



**January 25th**
The different rates of gradient descent: from Lipschitz to strongly convex
[[scribed notes](ift6085-2020/ift-6085-lecture-3-notes.pdf)]

Reading:

Convergence proofs from Chapter 3 of [1] ('Convex Optimization...' by S.Bubeck under References)
- Required: Sections 3.1, 3.2, 3.4, with emphasis on the Convergence proof of Theorem 3.12 
- Optional: Section 3.3 and anything related to constrained optimization. Keep in mind that we still discuss in class simplified unconstrained versions of some constrained results from Bubeck. Anything in our scribed notes is also required.



**January 26th**
Black box models and lower bounds 
[[scribed notes](ift6085-2019/ift-6085-lecture-4-notes.pdf)]

Reading:
- Required: [1, Theorem 3.15]
- Recommended: [6]


**February 1st**
Accelerated methods: Polyak's momentum (the heavy ball method)
[[scribed notes](ift6085-2020/ift-6085-lecture-5-notes.pdf)]
[[slides](ift6085-2019/ift-6085-lecture-5-slides.pdf)]

Reading: 
- Required: [8], [9, Sections 1, 2, 3, 4]
- Recommended: [35]


**February 2nd**
Nesterov's Accelerated Gradient, Stochastic gradient descent
[[scribed notes](ift6085-2020/ift-6085-lecture-6-notes.pdf)]

Reading: 
- Required: [6], [7, pages 67-76]
- Required: [1, Section 6 until 6.2], [4, Section 14.3]

---
### Crash course in statistical learning theory 


**February 8th**
Stochastic gradient descent
[[scribed notes](ift6085-2020/ift-6085-lecture-6-notes.pdf)]


**February 9th**
Elements of statistical learning theory
[[scribed notes](ift6085-2020/ift-6085-lecture-7-notes.pdf)]

Recommended reading: Section 2 (if you need the intro) and Section 5 of [4].

Required reading: Sections 3, 4 and 6 of [4].

**February 15th**
Elements of statistical learning theory [continuation of previous lecture]



**February 16th**
PAC-Bayes bounds
[[scribed notes](ift6085-2020/ift-6085-lecture-8-notes.pdf)]

Required reading: [12]

Recommended reading: Section 31 of [4]

Recommended reading (harder): Section 6 of [2]




**February 22nd**
Probably Approximately Correct Constrained Learning

Reading:
- [[paper](https://arxiv.org/abs/2006.05487)]



**February 23rd**
MIDTERM EXAM

---


Winter break
--------------

**March 1st**
**Winter break** No class

**March 2nd**
**Winter break** No class


--------------

<br/>


**March 8th**

Stability and generalization
[[scribed notes](ift6085-2020/ift-6085-lecture-9-notes.pdf)]

Required reading:
- Main body of the papers [13,14] without all the proofs 
- The two sets of scribed notes provided here, including the covered proofs

Optional reading: Proofs that are not covevered in the scribed notes. 

<br/>


### Seminar part of class
**March 9th**
Weighted Sums of Random Kitchen Sinks: Replacing
minimization with randomization in learning
[[scribed notes](ift6085-2020/ift-6085-lecture-11-notes.pdf)]

- Recommended reading: Section 16 (Kernel methods) of [4]
- Required reading: [23]
- Recommended viewing: [video of talk by A. Rahimi](https://www.youtube.com/watch?v=Nqi2iU7kbD0). 
    The discussion pertaining to this paper, starts at 31:10 (though the intro might be necessary) and ends at about 48:10.


**March 15th**
Surprising results on the generalization error of neural networks 

- Recommended reading: [In Search of the Real Inductive Bias: On the Role of Implicit Regularization in Deep Learning](https://arxiv.org/abs/1412.6614)
- Recommended reading: [Understanding deep learning requires rethinking generalization](https://arxiv.org/abs/1611.03530)
- Recommended reading: [On the Bias-Variance Tradeoff: Textbooks Need an Update](https://www.bradyneal.com/bias-variance-tradeoff-textbooks-update), blog post by Brady Neal



**March 16th**
Where is the Bayes risk hiding? 

- Recommended reading (refresher from last week): [Understanding deep learning requires rethinking generalization](https://arxiv.org/abs/1611.03530)
- Recommended reading: [To Understand Deep Learning We Need to Understand Kernel Learning](https://arxiv.org/abs/1802.01396)
- Recommended reading: [Overfitting or perfect fitting? Risk bounds for classification and regression rules that interpolate](https://arxiv.org/abs/1806.05161)



**March 22nd**
Student presentations

**March 23rd**
Student presentations


**March 29th**
Student presentations


**March 30th**
Student presentations

**April 5th**
Student presentations

**April 13th**
Neural Tangent Kernel [new lecture - no scribed notes]
- Recommended reading: [Neural Tangent Kernel: Convergence and Generalization in Neural Networks](https://arxiv.org/abs/1806.07572)
- Recommended reading: [Blog summary of paper](https://rajatvd.github.io/NTK/) 

Recommended reading on reproducing kernel hilbert spaces:
- Guest lecture by Jose Gallego from last year[video](https://www.dropbox.com/s/e1bhq2bbdqhx4z3/lecture-jose-rkhs.mp4?dl=0)
- [15min] Watch [this great video](https://www.youtube.com/watch?v=LyGKycYT2v0) on duality.
- [5min] Get familiar with the *statement* of the [Riesz representation theorem](https://en.wikipedia.org/wiki/Riesz_representation_theorem) and think about the relationship with the video above.
- [40min] Read the Wikipedia entry on [RKHSs](https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space) - Can skip sections 4, 8 and 9.
- [15min] *Optional:* Read sections 1 and 2 of the Wikipedia entry on [Kernel embedding of distributions](https://en.wikipedia.org/wiki/Kernel_embedding_of_distributions)



**April 19th**
1-1 discussions on course projects 

**April 20th**
1-1 discussions on course projects 




**May 3rd **
Final poster presentation for projects


**Extra material (not scheduled)**
Determinantal point processes for ML (guest lecture by Jose Gallego)
- Recommended reading: [Notes from Stefanie Jegelka's class at MIT](http://people.csail.mit.edu/stefje/fall15/notes_lecture21.pdf), written by Swati Gupta.
- Recommended reading: [Determinantal Point Processes in Randomized Numerical Linear Algebra](https://arxiv.org/pdf/2005.03185.pdf), Derezinski and Mahoney.






<!---




**March 14th: Guest lecturer, Guillaume Lajoie**
Intro to dynamical systems with application to neural networks
[[scribed notes](ift6085-2019/ift-6085-lecture-15-notes.pdf)]

Reading: [31, 32, 33]


**April 3rd**
Distributional reinforcement learning
[[scribed notes](ift6085-2019/ift-6085-lecture-18-notes.pdf)]


Bonus lectures
--------
This section contains useful material (older lectures) that have been replaced by new material,
but are still very interesting and useful.
Students will not be examined on this material.


Variance reduction techniques for stochastic optimization
[[scribed notes](ift6085-2019/ift-6085-bonus-lecture-variance-reduction.pdf)]

Reading: [22], Section 5.3 of [21]



Expressivity and universal approximation theorems
[[scribed notes](ift6169-2022/ift-6169-lecture-10-notes.pdf)]


Reading:
- Optional reminder: Subsections 6.1, 6.2, 6.3 from [4]
- Required: [Simple construction for universal approximation theorem: A visual proof that neural nets can compute any function By Michael Nielsen](http://neuralnetworksanddeeplearning.com/chap4.html)
- Required: Beginning of Section 20 until 20.4 (inclusive) in [4]
- Required: All of [40]




PacGAN: The power of two samples in generative adversarial networks

Reading: [24]


**April 4th, 2018**
Some results on non-convex optimization

Reading: [25,26]

**April 5th, 2018**
Escaping saddle points
[[scribed notes](ift6085-2019/ift-6085-bonus-lecture-saddle-points-notes.pdf)]
[slides by Yang Yuan](http://www.callowbird.com/uploads/8/6/6/4/8664563/1.pdf)

Reading: [27, 28]

**April 11th, 2018**
The theory of spin glasses

Guest lecture by **Alex Fribergh**, UdeM Math.

Reading: [29]


**April 12th, 2018**
The Loss Surfaces of Multilayer Networks

Reading: [30]

--->

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
9. [YellowFin and the Art of Momentum Tuning](https://arxiv.org/abs/1706.03471), SysML 2019, J. Zhang, I. Mitliagkas.
10. [Large-scale Machine Learning and Optimization (class)](http://papail.io/901), Dimitris Papailiopoulos, University of Wisconsin.
11. [Advanced Machine Learning Systems (class)](http://www.cs.cornell.edu/courses/cs6787/2017fa/), Chris De Sa, Cornell University.
12. [A PAC-Bayesian Tutorial with A Dropout Bound](https://arxiv.org/abs/1307.2118), David McAllester.
13. [Stability and generalization](http://www.jmlr.org/papers/volume2/bousquet02a/bousquet02a.pdf), O. Bousquet, A. Elisseeff.
14. [Train faster, generalize better: Stability of stochastic gradient descent](https://arxiv.org/pdf/1509.01240.pdf), M. Hardt, B. Recht, Y. Singer.
15. [Computing Nonvacuous Generalization Bounds for Deep (Stochastic) Neural Networks with Many More Parameters than Training Data](https://arxiv.org/abs/1703.11008), Gintare Karolina Dziugaite, Daniel M. Roy
16. [Lecture notes on generative learning algorithms](http://cs229.stanford.edu/notes2021fall/cs229-notes2.pdf), Andrew Ng
17. [Generative Adversarial Nets](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf), Ian Goodfellow et al.
18. [Wasserstein GAN](https://arxiv.org/abs/1701.07875), Martin Arjovsky, Soumith Chintala, Léon Bottou 
19. [Read-through: Wasserstein GAN](https://www.alexirpan.com/2017/02/22/wasserstein-gan.html), Alex Irpan
20. [The Numerics of GANs](https://arxiv.org/pdf/1705.10461.pdf), Lars Mescheder, Sebastian Nowozin, Andreas Geiger
21. [Optimization Methods for Large-Scale Machine Learning](https://arxiv.org/pdf/1606.04838v1.pdf), Léon Bottou, Frank E. Curtis, Jorge Nocedal
22. [Accelerating Stochastic Gradient Descent using Predictive Variance Reduction](http://papers.nips.cc/paper/4937-accelerating-stochastic-gradient-descent-using-predictive-variance-reduction.pdf), Rie Johnson, Tong Zhang
23. [Weighted Sums of Random Kitchen Sinks: Replacing minimization with randomization in learning](https://people.eecs.berkeley.edu/~brecht/papers/08.rah.rec.nips.pdf), Ali Rahimi, Ben Recht
24. [PacGAN: The power of two samples in generative adversarial networks](https://arxiv.org/abs/1712.04086), Zinan Lin, Ashish Khetan, Giulia Fanti, Sewoong Oh
25. [Stochastic First- and Zeroth-order Methods for Nonconvex Stochastic Programming](https://arxiv.org/abs/1309.5549), Saeed Ghadimi, Guanghui Lan
26. [Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Łojasiewicz Condition](https://arxiv.org/abs/1608.04636), Hamed Karimi, Julie Nutini, Mark Schmidt
27. [Escaping From Saddle Points --- Online Stochastic Gradient for Tensor Decomposition](https://arxiv.org/abs/1503.02101), Rong Ge, Furong Huang, Chi Jin, Yang Yuan
28. [How to Escape Saddle Points Efficiently](https://arxiv.org/abs/1703.00887), Chi Jin, Rong Ge, Praneeth Netrapalli, Sham M. Kakade, Michael I. Jordan
29. [RANDOM MATRICES AND COMPLEXITY OF SPIN GLASSES](https://arxiv.org/pdf/1003.1129.pdf), ANTONIO AUFFINGER, GERARD BEN AROUS, AND JIRI CERNY 
30. [The Loss Surfaces of Multilayer Networks](https://arxiv.org/abs/1412.0233), Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, Yann LeCun 
31. [Learning Long-Term Dependencies with Gradient Descent is Difficult](http://www.comp.hkbu.edu.hk/~markus/teaching/comp7650/tnn-94-gradient.pdf), Y Bengio, P Simard, P Frasconi
32. [On the difficulty of training Recurrent Neural Networks](https://arxiv.org/abs/1211.5063), Razvan Pascanu, Tomas Mikolov, Yoshua Bengio
33. [Opening the Black Box: Low-Dimensional Dynamics in High-Dimensional Recurrent Neural Networks](https://www.mitpressjournals.org/doi/full/10.1162/NECO_a_00409), David Sussillo and Omri Barak 
34. [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html), Richard S. Sutton and Andrew G. Barto
35. [Course Notes for EE227C (Spring 2018): Convex Optimization and Approximation](https://ee227c.github.io/notes/ee227c-lecture06.pdf), Moritz Hardt.
36. [Uniform convergence may be unable to explain generalization in deep learning
](https://arxiv.org/abs/1902.04742), Vaishnavh Nagarajan, J. Zico Kolter 
37. [Tutorial on Practical Prediction Theory for Classification](http://www.jmlr.org/papers/volume6/langford05a/langford05a.pdf), John Langford, 2005.
38. [Computing Nonvacuous Generalization Bounds for Deep (Stochastic) Neural Networks with Many More Parameters than Training Data](https://arxiv.org/abs/1703.11008), Gintare Karolina Dziugaite, Daniel M. Roy, 2017.
39. [Non-Vacuous Generalization Bounds at the ImageNet Scale: A PAC-Bayesian Compression Approach
](https://arxiv.org/pdf/1804.05862.pdf), Wenda Zhou, Victor Veitch, Morgane Austern, Ryan P. Adams, Peter Orbanz, 2018.
40. [Representation benefits of deep feedforward](https://arxiv.org/abs/1509.08101), Matus Telgarsky, 2015. 


