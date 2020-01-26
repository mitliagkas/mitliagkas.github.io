---
layout: default
title: ML class
menu: main
permalink: /ift6390-ml-class-2020/
---

IFT6390: Fundamentals of machine learning
=========

An introductory but **very intensive** class in machine learning.
The class will be given again in Fall 2020.

Listed as [IFT6390: Fondements de l'apprentissage machine](https://admission.umontreal.ca/cours-et-horaires/cours/ift-6390/)

This is a graduate class that caters to an overwhelmingly international crowd. It is taught in english. 
Assignments, exams will be available in french and english. 
Students are always encouraged to submit their work and ask questions in their language of preference.
For the equivalent class taught entirely in french, please see 
Guillaume Rabusseau's <a href="https://www-labs.iro.umontreal.ca/~grabus/index.php?page=Teaching">
IFT3395</a>.

**IMPORTANT:
Please do not register for this class unless you have read and carefully considered all the class requirements listed
in the following two sections.** 

Requirements and prerequisites
-------------


Machine learning is a very exciting discipline, but requires building upon some important skills.
Before we begin, you should possess good knowlegde of:
1. Python programming is mandatory. You cannot use a different programming language in the class.
2. Linear algebra
3. Probability 

The pace is meant to be intensive and the homework and exam requirements are going to be tough.
As a result, if you have not mastered those three required skills, you should work on them first. 
This class will not teach you the required math or programming, but you will need them to pass the class.

As an indication, students who took the class in 2019 reported that to keep up with the class's needs, they worked on average:
- 12 hours per week, if they had already mastered the 3 prerequisites above 
- 18 hours per week, if they had this knowledge, but needed to refresh it as we went along
- 25+ hours a week if they had serious gaps in some prerequisite

Students who ignored our advice about the prerequisites and were missing some of it ended up having a really hard time. 
A number of students who were not comfortable with those prerequisites, abandoned the class before the middle of the semester.

Finally, if you are an international student, you will likely rely on scholarships in order to cover a big part of your tuition fees. 
Those scholarships (like the bourse C at UdeM) require you to maintain a high GPA. 
If you take this class before you are certain that you have the prerequisite skills, you might be putting your scholarship at risk.


Preparing to take the class
--------------

"It sounds scary so far!" 

The above stats are meant to give you a clear idea of what to expect rather than to scare you.
The good news is that, if you are determined, you can do it! Depending on your level this might require
taking other classes first, or working to refresh your existing knowledge.
This section will give you advice and resources to improve your background before taking the class.

Ideally, you have already taken university level classes in: probability, linear algebra and programming. 
It is hard to make up for those by yourself. Consider taking those classes at your university before you register for IFT6390.
Even if you have taken such classes, you might need to work hard to improve those skills, especially if you took them many years ago, 
or if you didn't perform well in those classes, or if you learned a different language other than Python. 



**Q: How do I make sure that I have all the necessary math prerequisites before I take IFT6390?**

A: Study the book [Mathematics for Machine Learning](https://mml-book.com/).
Go over the following parts of the book, and make sure you already understand the material **before** IFT6390 begins.
- Section 2: Subsections 2.1, to 2.6 (inclusive)
- Section 3: All subsections
- Section 4: Subsections 4.1 to 4.5.1 (inclusive) 
- Section 5: Subsections 5.1, 5.2, 5.3, 5.4, 5.5, 5.7
- Section 6: Subsections 6.1 to 6.5 (inclusive)

You should be able to solve at least half of the questions from those sections. 
If you find that it is impossible to do that by yourself, then there is no way around it:
you need to take one or two math classes before taking IFT6390.


**Q: How do I make sure that I have the programming prerequisites before I take IFT6390?**

A: Consider IFT6390's [lab midterm exam from 2019](ift6390-lab-midterm-A2019.py).
The exam consists of 10 Python questions. 
In each question, you are given a description of the functionality of a Python fuction, along with its header. 
You goal is to implement the body of each function according to the instructions. 
IFT6390 students who took the exam had full access to internet resources during the exam, but only one hour to finish it. 
In the end, their solutions were graded by our system for correctness. 
In each question, the student got the associated points if their implementation passed all of our unit tests.
If their implementation of the function returned the wrong answer in at least one of the tests, they got 0 points in that question.
Since the goal was to assess effective programming, there was no partial credit for ``semi-correct'' implementations.

Try taking the exam at home in one hour. 
Don't worry if you cannot solve all questions in the alotted time. It is very hard. 
However, you should be able to correctly implement at least half of the functions in that time. 
This means that your code should run, and when you call the function with an arbitrary input it should always give the correct answer.

- If you are not able to solve at least half the questions in the alotted time, you need some serious Python practice before IFT6390 starts. 
Otherwise, you will struggle in the class. 
- If you are only able to solve one or two questions correctly in the allotted time, then you should take a semester-long programming class before you register for IFT6390.



People
------

Instructor: [Ioannis Mitliagkas](https://mitliagkas.github.io), 

Teaching assistants: (TBA)

Communication
------------- 
We will use the class's [Studium page]()
(not yet open for students) for communication.
The Studium page contains a forum for all discussions. 
This is a very large class, so the instructor will not be able to respond to individual questions about the class
via email. 
Make sure to use the class forum. 

**Exclusively in the event that you have a question of a sensitive, personal nature:**
Please feel free to email the instructor.
Please make sure to start the subject of your email with "[IFT6390]" to make sure that it is not lost. 


**Class times and rooms**
follow the instructions to use the functionality "TROUVEZ L’HORAIRE D’UN COURS" at the bottom of <a href="https://admission.umontreal.ca/cours-et-horaires/cours/ift-6390/">
this page</a>.


Content and objectives of class
------------------
This course is an introduction to machine learning (ML), a field of research in artificial intelligence. The purpose of ML algorithms is to enable the machine to learn from examples. The focus of the course is classification and regression: we observe a set of pairs (observation, target) where the target is eg. a class and we try to predict the target corresponding to a new observation. The classic applications of these algorithms are in the field of pattern recognition (characters, image, speech, etc.). In recent years, several new fields of application have emerged: data mining, statistical analysis of textual data, quantitative management of financial portfolios, analysis of genetic expressions, etc. The subject of the course can be exploited in many fields of computer science.

The course will cover the following subjects: general notions (basic terminology, generalization, curse of dimensionality, capacity, classifier comparison), supervised algorithms (k-nearest neighbors, linear classifiers, neural networks, support vector machines, decision trees and regression, ensemble methods), unsupervised algorithms (principal component analysis, k-means method), overview of probabilistic graphical models.

Notions covered (indicative titles):
- Introduction and terminology of learning.
- Data Representation (+ Linear Algebra Reminders.)
-  The tasks of supervised learning (classification, regression) and unsupervised (density estimation, clustering, dimensionality reduction, ...)
-  Histogram-based methods. Curse of dimensionality. (+ reminders of probability and statistics)
-  Neighborhood-based methods (nearest neighbors and Parzen windows)
-  Multivariate Gaussian density
-  General framework of learning, performance evaluation, model selection, concept of capacity.
-  Principle of maximum likelihood v.s. Bayesian inference. Bayes classifier.
-  Regression and linear classification (logistic regression, perceptron, linear SVM, ...)
-  Classification and non-linear regression with kernel trick (+ optimization techniques)
-  Classification and non-linear regression: MLP-type neural networks (+ revision of calculation of partial derivatives)
-  More advanced neural network architectures: convolutional, recurrent.
-  Decision trees.
-  Aggregation methods: bagging and boosting
-  Unsupervised learning: dimensionality reduction (PCA, ...). Partitioning (k-means, ...)
-  Overview of probabilistic graphical models
-  Introduction to deep learning
-  Convolutional neural netoworks
-  Recurrent neural networks


<h2>Labs</h2>
- <a href="https://docs.google.com/presentation/d/1DB5-BGoImjcnsd1amnjQ4s4nhjUZhknCd5rra3eFnaU/edit?usp=sharing">Lab 0 Slides: Class tools (Thursday, September 5th, 2019)</a> 
- <a href="https://drive.google.com/file/d/1XizC8QB33mAhG5FaenF5ILo8La4vdX-9/view?usp=sharing">Lab 1 Notebook: Numpy (Thursday, September 12th, 2019)</a> 
- <a href="https://drive.google.com/file/d/1odCUuWRKk6SBIGpQtkSBVdPErTQ_fEzy/view?usp=sharing">Lab 1 Notebook: k-NN (Thursday, September 12th, 2019)</a> 




<h2>Evaluation</h2>

*Please be advised that some details of this evaluation scheme might be adjusted slightly by the beginning of the semester.*


**Homework (33%):**
3 of homework (8% each) including some theoretical exercises, programming and experimentation.
One Kaggle competition (counts for 9%).
Most sets of homework will be submitted in teams of 2 students.
Some will be submitted individually.


**Lab midterm exam (10%):**
This exam will take place in the lab on the 5th week of class (early October). It will be a hard exam testing the programming abilities of the students in a lab environment.

**Midterm exam(15%):**	
This exam will cover all the material seen until then. Date to be announced.

**Team project(20%):**
Application of learning algorithms to a student's field of interest and / or implementation of a new learning algorithm (programming, experimentation, and performance comparison). Several major themes (or areas of application of machine learning) will be proposed and teams will be able to form around these themes.
The project is done in teams.
The project must be approved by the instructor (details TBA).

**Final exam (20%):**
The whole class material. Precise date in December TBA.

**Class participation (2%):**
For actively participating the discussions on the class forums.

Work and exams:
You can submit your work on our Gradescope site of the course (once the semester starts). It is also on Gradescope that you will be able to see your grades for the homework and exams.

**ATTENTION regarding fraud and plagiarism:**
The University of Montreal now has a strict policy in case of fraud or plagiarism.
If an infraction is found, the professor is required to report to the director of the department.
An administrative procedure is then automatically triggered with the following consequences: the offense is noted in your file,
and a sanction is decided (which can be serious and go to dismissal in case of recidivism). It is important that you do the work yourself!


