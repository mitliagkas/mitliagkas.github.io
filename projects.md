---
layout: default
title: Projects
menu: main
permalink: /projects/
---

Projects
=========

Learning, generalization, and domain adaptation
------------------
<div id ="imagelist">
<ul>
      <li>
      <a href="https://www.bradyneal.com/bias-variance-tradeoff-textbooks-update" target="_blank">
      <img src="{{ site.baseurl }}/images/project-bias-variance.png" alt="" title="A Modern Take on the Bias-Variance Tradeoff in Neural Networks">
      <div>
        A Modern Take on the Bias-Variance Tradeoff in Neural Networks
        <em>
	We measure prediction bias and variance in NNs.
	Both bias and variance decrease as the number of parameters
	grows. We decompose variance into
	variance due to sampling and variance due to initialization.
	</em>
	<br>
	Lead: Brady Neal
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/1911.00804"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-adversarial-domain-generalization.png" alt="" title="Adversarial target-invariant representation learning for domain generalization">
      <div>
	Adversarial representation learning for domain generalization
        <em>
	We propose a process that enforces pair-wise domain invariance while training a feature extractor over a diverse set of domains.
	We show that this process ensures invariance to any distribution that can be expressed as a mixture of the training domains.
	</em>
	<br>
	Lead: Isabela Albuquerque, João Monteiro (INRS)
      </div></a>
      </li> 
      <li>
      <a href="https://openreview.net/forum?id=SkeMPEH32N"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-overparametrization-rl.png" alt="" title="In Support of Over-Parametrization in deep RL">
      <div>
	In Support of Over-Parametrization in deep RL
        <em>
	 There is significant recent evidence in supervised learning that, in the over-parametrized setting, wider networks achieve better test error.
	 We experiment on four OpenAI Gym tasks and provide evidence that overparametrization is also beneficial in deep RL.
	</em>
	<br>
	Lead: Brady Neal
      </div></a>
      </li> 
      <li>
      <a href="https://openreview.net/forum?id=SkeMPEH32N"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-mmc-gp.png" alt="" title="Connections between max margin classifiers and gradient penalty">
      <div>
	Connections between max margin classifiers and gradient penalties
        <em>
	 Maximum-margin classifiers can be formulated as Integral Probability Metrics (IPMs) or classifiers with some form of gradient norm penalty.
	 This implies a direct link to a class of Generative adversarial networks (GANs) which penalize a gradient norm.
	</em>
	<br>
	Lead: Alexia Jolicoeur-Martineau, 
	Image source: wikipedia
      </div></a>
      </li> 

</ul>
</div>


Deep learning and applications
------------------

<div id ="imagelist">
<ul>
      <li>
      <a href="https://facebook.com/icml.imls/videos/live-from-icml-2019-in-long-beach-this-session-on-deep-generative-models-include/1269891676506524/"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-state-reification.png" alt="" title="State-Reification Networks">
      <div>
	     State-Reification Networks
        <em>
	     Improving Generalization
	by Modeling the Distribution of Hidden Representations
	</em>
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/1707.02392"  target="_blank">
      <img src="{{ site.baseurl }}/images/shape-analogies.png" alt="" title="Representation and generation">
      <div>
	Representation Learning and Adversarial Generation of 3D Point Clouds
        <em>The first AutoEncoder design suited to 3D point cloud data beats state of the art in reconstruction accuracy. 
		GANs trainined in the AE's latent space generate realistic objects from every-day classes.
		</em>
      </div></a>
      </li> 
</ul>
</div>

Differentiable games
----- 

<div id="imagelist">
    <ul>
      <li>
      <a href="https://arxiv.org/abs/2001.00602"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-games-spectral-shapes.png" alt="" title="Negative Momentum for Improved Game Dynamics">
      <div>
	Accelerating Smooth Games by Manipulating Spectral Shapes
        <em>
	We use matrix iteration theory to characterize acceleration in smooth games.
	The spectral shape of a family of games is the set containing all eigenvalues of the Jacobians of standard gradient dynamics in the family.
	</em>
	<br>
	Lead: Waiss Azizian
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/1906.07300"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-games-spectral-shapes.png" alt="" title="Negative Momentum for Improved Game Dynamics">
      <div>
	Linear Lower Bounds and Conditioning of Differentiable Games
        <em>
		In this work, we approach the question of fundamental iteration complexity by providing lower bounds to complement the linear
		(i.e. geometric) upper bounds observed in the literature on a wide class of problems.
	</em>
	<br>
	Lead: Adam Ibrahim
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/2001.00602"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-games-spectral-shapes.png" alt="" title="Negative Momentum for Improved Game Dynamics">
      <div>
	Accelerating Smooth Games by Manipulating Spectral Shapes
        <em>
	We use matrix iteration theory to characterize acceleration in smooth games.
	The spectral shape of a family of games is the set containing all eigenvalues of the Jacobians of standard gradient dynamics in the family.
	</em>
	<br>
	Lead: Waiss Azizian
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/pdf/2001.00602.pdf"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-negative-momentum.png" alt="" title="Negative Momentum for Improved Game Dynamics">
      <div>
        Negative Momentum for Improved Game Dynamics
        <em>
	Alternating updates are more stable than
	simultaneous updates on simple games.
	A negative momentum
	term achieves convergence in a difficult toy adversarial problem, but also on the notoriously
	difficult to train saturating GANs
	</em>
	<br>
	Lead: Gauthier Gidel, Reyhane Askari-Hemmat
      </div></a>
      </li> 
    </ul>
</div>

Large-scale optimization systems
----- 
<div id="imagelist">
    <ul>
      <li>
      <a href="https://arxiv.org/pdf/1708.05256.pdf"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-15pf.png" alt="" title="Deep Learning at 15 Petaflops">
      <div>
        Deep Learning at 15 Petaflops
        <em>15-PetaFLOP Deep Learning system for solving scientific pattern classification problems on contemporary HPC architectures</em>
      </div></a>
      </li> 
      <li>
      <a href="{{ site.baseurl}}/frogwild/">
      <img src="{{ site.baseurl }}/images/frog.png" alt="Picture of cute yet slightly deranged frog." title="Ribbit!">
      <div>
        FrogWild!
        <em>Fast PageRank approximations on Graph Engines</em>
      </div></a>
      </li> 
      <li>
      <a href="{{ site.baseurl}}/frogwild/">
      <img src="{{ site.baseurl }}/images/frog.png" alt="Picture of cute yet slightly deranged frog." title="Ribbit!">
      <div>
        FrogWild!
        <em>Fast PageRank approximations on Graph Engines</em>
      </div></a>
      </li> 
    </ul>
</div>


Optimization and numerical analysis
-----
<div id="imagelist">
    <ul>
      <li>
      <li>
      <a href="http://dawn.cs.stanford.edu/2017/07/05/yellowfin/"  target="_blank">
      <img src="{{ site.baseurl }}/images/Yellowfin.png" alt="" title="Self-tuning!">
      <div>
	YellowFin: Self-tuning optimization for deep learning
        <em>Simple insights on the momentum update yield an very efficient parameter-free algorithm that performs well across networks and datasets without the need to tune any parameters.</em>
      </div></a>
      </li> 
      <a href="https://arxiv.org/abs/1707.02670" target="_blank">
      <img src="{{ site.baseurl }}/images/pca.png" alt="" title="Accelerated power iteration">
      <div>
	Accelerated stochastic power iteration
        <em>Exciting recent results on how adding a momentum term to the power iteration yields a numerically stabe, accelerated method.</em>
      </div></a>
      </li> 
      <li>
      <a href="{{ site.baseurl}}/asynchrony/" target="_blank">
      <img src="{{ site.baseurl }}/images/theory-prediction.png" alt="Tuning parallel deep learning systems" title="Optimal momentum values for different levels of parallelization">
      <div>
	 Asynchrony and Momentum
        <em>When training large scale systems asynchronously, you get a momentum surprise.</em>
      </div></a>
      </li>
    </ul>
</div>


Everything else
----- 

<div id="imagelist">
    <ul>
      <li>
      <a href="https://arxiv.org/pdf/1707.05807.pdf" target="_blank">
      <img src="{{ site.baseurl }}/images/graph.png" alt="Gibbs Sampling Scan Order" title="[redacted]">
      <div>
	Gibbs Sampling Scan Order
	<em>Our NIPS 2016 work shows that scan order matters.<br>
	Now we show that it is possible to make Gibbs sampling many orders of magnitude faster by customizing the scan sequence to a specific model and given set of target variables.</em>
      </div></a>
      </li> 
</ul>
</div>



