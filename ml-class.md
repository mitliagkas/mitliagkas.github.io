---
layout: default
title: ML class
menu: main
permalink: /ift6390-ml-class/
order: 3
---

IFT6390: Fundamentals of machine learning
=========

An introductory but **very intensive** class in machine learning.
It is taught in Fall 2020 and will be taught again in Winter 2021.

Listed as [IFT6390: Fondements de l'apprentissage machine](https://admission.umontreal.ca/cours-et-horaires/cours/ift-6390/)

This is a graduate class that caters to an overwhelmingly international crowd. It is taught in english. 
Assignments, exams will be available in french and english. 
Students are always encouraged to submit their work and ask questions in their language of preference.
For the equivalent class taught entirely in french, please see 
Guillaume Rabusseau's <a href="https://www-labs.iro.umontreal.ca/~grabus/index.php?page=Teaching">
IFT3395</a>.

**IMPORTANT:
Please do not register for this class unless you have read and carefully considered all the class requirements listed
in the 
[prerequisites](/ift6390-ml-class-prerequisites) page.**

Quick links
--------- 
As of Tuesday, September 1st, all officially registered students have been added to Piazza and Gradescope.
We sent you invitations and announcements to your email address associated with your registration. 
For the majority of you this is an email address that ends in @umontreal.ca. 
You should be able to access it [here](https://outlook.umontreal.ca/) with your UdeM/Synchro credentials. 
If you do not have UdeM credentials, please contact UdeM's IT support.

**IMPORTANT: Make sure you learn how to use that email inbox and check it often. We will not be able to add you using alternative email addresses.**

<span style="color:red">
If you registered late (i.e. did not have access to Studium on September 1st), then please complete [this form](https://forms.gle/gEaECs6kYb1k2JLbA) to be added to class resources.
</span>

- [Piazza](https://piazza.com/umontreal.ca/fall2020/ift6390) for all our communications.
- [Gradescope](https://www.gradescope.com/courses/155310) for submitting your work and seeing your grades.
- [Overleaf](https://www.overleaf.com/read/tbzhcsjtfjfy) for downloading homework announcements and working on your solutions .


People
------

Instructor: [Ioannis Mitliagkas](https://mitliagkas.github.io), 

Teaching assistants: (TBA)


Registering and auditing
--------
The class might be full. It will be taught again in Winter 2021 (January 2021). 
If you want to audit the class, please fill this [form](https://forms.gle/hnfwVpf67WncVYWz9). 


Communication
------------- 

All of our communication will happen through the class Piazza page. 
Registered students will be added to the Piazza page automatically on the day before the first class. 

All lectures, labs and office hours will happen on Zoom. You will find all the links on Piazza.

Homework submission and evaluation will happen on Gradescope. You will be invited to the class's Gradescope page automatically the day before classes start. If you are auditing, you will not be added to Gradescope and you will not be able to submit homeworks.

**Important:** Make sure that you learn how to use and are checking your @umontreal.ca email inbox. That is were you will receive announcements and invitations to class online services.

The class's [studium page](https://studium.umontreal.ca/course/view.php?id=176757) will only be used for initial coordination with registered students until they get access to Piazza. There will be no discussions on Studium. 

**Important notice on email communication:**
This is a very large class, so the instructor will not be able to respond to individual questions about the class via email.  **Exclusively in the event that you have a question of a sensitive, personal nature:** Please feel free to email the instructor.  Please start the subject of your email with "[IFT6390]"; otherwise your email might be lost.


Class and lab times
-----
The instructor's lectures are on
- Wednesday at 9:30am-11:10am ET
- Thursday at 9:30am-10:20am ET

For both lectures we will use the same link that you will find on Piazza (see section above). 

Weekly labs led by a TA on
- Thursday at 10:30am-12:30am ET

You will also find the link to a week's lab on Piazza.

Updated information can always be found by following the instructions below "TROUVEZ L’HORAIRE D’UN COURS" at the bottom of <a href="https://admission.umontreal.ca/cours-et-horaires/cours/ift-6390/">
this page</a>.


Video recordings 
-------------
Lectures and labs will be delivered live, but a video recording will be made available to the class soon after the class is over. Links to all past lectures and lab video recordings will be available on Piazza.


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
This is a sample of the first three labs from last year to get you started until you get access to this year's material.

- <a href="https://docs.google.com/presentation/d/1DB5-BGoImjcnsd1amnjQ4s4nhjUZhknCd5rra3eFnaU/edit?usp=sharing">Lab 0 Slides: Class tools (Thursday, September 5th, 2019)</a> 
- <a href="https://drive.google.com/file/d/1XizC8QB33mAhG5FaenF5ILo8La4vdX-9/view?usp=sharing">Lab 1 Notebook: Numpy (Thursday, September 12th, 2019)</a> 
- <a href="https://drive.google.com/file/d/1odCUuWRKk6SBIGpQtkSBVdPErTQ_fEzy/view?usp=sharing">Lab 1 Notebook: k-NN (Thursday, September 12th, 2019)</a> 




<h2>Evaluation</h2>

*Please be advised that some details of this evaluation scheme might be adjusted slightly by the beginning of the semester.*

**Weekly quizzes (10%):**
We will have a weekly online quiz at the beginning of class every Wednesday of the semester. 
It will consist of short questions about last week's lecture and it will be administered on Gradescope. 
To accommodate students from different timezones, the quiz will be open a few hours before the class start time. 
Once you start the quiz, you will have 15 minutes to finish it. 
We will have at least 12 quizes during the semester; your best 6 quiz scores will be used to compute your semester quiz score (10% of your final grade).



**Homework (30%):**
3 sets of homework (10% each) including some theoretical exercises, programming and experimentation.
Most sets of homework will be submitted individually (each student working on their own) and some in teams of two.

**Data competitions (30%):**
Two Kaggle competitions.
The first one will span the first half of the class and count towards 10% of your grade
 and the second one will span the second half of the class and count towards 20% of your grade.

**Lab midterm exam (10%):**
This timed exam will take place at a specific time and will test your knowledge of the lab material. You will be asked to program specific functions in Python and submit to Gradescope of autograging. 
For some more information and an example of last year's lab midterm, please check 
the [prerequisites](/ift6390-ml-class-prerequisites) page.
We will have this exam in early October (exact date TBA). 

**Final exam (20%):**
Exam on the whole class material at the end of the semester. 
Exact date and format to be announced.

*For most of these evaluations you be able to submit your work and see your grades on Gradescope. 
 See 'Communication' section for some info on access. *

Academic fraud and plagiarism
---------------- 

**ATTENTION:**
The University of Montreal now has a strict policy in case of fraud or plagiarism.
If an infraction is found, the professor is required to report to the director of the department.
An administrative procedure is then automatically triggered with the following consequences: the offense is noted in your file,
and a sanction is decided (which can be serious and go to dismissal in case of recidivism). It is important that you do the work yourself!


