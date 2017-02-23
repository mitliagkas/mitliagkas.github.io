---
layout: default
title: YellowFin
---

# YellowFin:
## A fully automated momentum tuner for synchronous and asynchronous systems

>based on ongoing work by **Jian Zhang, Ioannis Mitliagkas** and **Chris Ré**

Stochastic Gradient Descent (SGD) and its variants are the optimization method of choice for many large-scale learning problems including deep learning. A popular approach to running these systems removes locks and synchronization barriers. Such methods are called "asynchronous-parallel methods" or Hogwild! and are used on many systems by companies like Microsoft and Google.

However, the effectiveness of asynchrony has been a bit of a mystery. 
During our recent [work](https://arxiv.org/abs/1606.04487)
we discovered and unexpected 
[theoretical link](http://arxiv.org/pdf/1605.09774.pdf) 
between system and algorithm dynamics.
We showed that asynchrony introduces momentum-like dynamics into your optimization update. The optimal setting for momentum depends on the data and the hardware. So, tuning is critical! 
More details on that in our
[blog post](stanford.edu/~imit/tuneyourmomentum/theory/).

Following up on this line of work we have been working on an fully automated momentum tuner---codenamed *YellowFin*---which uses our theoretical and practical understaning of asynchronous dynamics to tune optimally tune momentum on the fly.


#### Robustness Properties of the momentum operator
<img align="right" src="{{ site.baseurl }}/images/pos-mom-robustness.png" alt="Robustntess"  width="300"/>
We study the robustness properties of the momentum operator; we point out that the rate of convergence for simple objectives is robust to learning rate mis-specification as well as curvature variations.

<br><br><br><br><br>

#### Synchronous momentum tuner

<img align="right" src="{{ site.baseurl }}/images/sync-yellowfin.png" alt="Synchronous tuner"  width="300"/>
We propose a simple momentum tuner that only uses the gradients of a running system to pick a target momentum value. 
Our momentum rule computes a quantiy similar to the condition number, that also encapsulates the stochastic noise present in SGD updates.

Preliminary results suggest that our tuner outperforms the best hand-tuned Momentum SGD update and Adam on ResNets.

<br><br><br>

#### Asynchronous momentum tuner

<img align="right" src="{{ site.baseurl }}/images/async-yellowfin.png" alt="Synchronous tuner"  width="300"/>
We use our [theory](http://arxiv.org/pdf/1605.09774.pdf) to **measure** the total amount of momentum in a running asynchronous system.
Then **we close the loop**:
We do some simple control theory to efficiently tune the total momentum in the system, so that it runs at maximum statistical efficiency.
<br><br><br><br><br>


## What's next?


* We plan to release a comprehensive set of experiments on a number of models, both in the synchronous and asynchronous setting.
* Running our asychronous tuner on very large scale settings (1000s of nodes).
* We plan to release a TensorFlow implementation of our tuner for the community to use.

