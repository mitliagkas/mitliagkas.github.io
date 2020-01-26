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


Differentiable games
----- 

<div id="imagelist">
    <ul>
      <li>
      <a href="https://arxiv.org/abs/2001.00602"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-games-spectral-shapes.png" alt="" title="Accelerating Smooth Games by Manipulating Spectral Shapes ">
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
      <img src="{{ site.baseurl }}/images/project-games-lower-bounds.png" alt="" title="Linear Lower Bounds and Conditioning of Differentiable Games ">
      <div>
            Linear Lower Bounds and Conditioning of Differentiable Games
        <em>
		We approach the question of fundamental iteration complexity for smooth, differentiable games by providing lower bounds to complement the linear
		(i.e. geometric) upper bounds observed in the literature on a wide class of problems.
	</em>
	<br>
	Lead: Adam Ibrahim
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/2001.00602"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-games-tight-analysis.png" alt="" title="A Unified Analysis of Gradient-Based Methods for a Whole Spectrum of Games ">
      <div>
        A Unified Analysis of gradient methods for a Whole Spectrum of Games
        <em>
        We provide new analyses of the extragradient's local and global convergence properties
        and tighter rates for optimistic gradient and consensus optimization.
        Unlike in convex minimization, EG may be much faster than gradient descent.
	</em>
	<br>
	Lead: Waiss Azizian
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/1901.08680"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-multiobjective-gan.png" alt="" title="Multi-objective training of Generative Adversarial Networks with multiple discriminators">
      <div>
        Multi-objective training of GANs with multiple discriminators
        <em>
We study GANs with multiple discriminators by framing them as a multi-objective optimization problem.
Our results indicate that hypervolume maximization presents a better compromise between sample quality and computational cost than previous methods.
	</em>
	<br>
	Lead: Isabela Albuquerque, João Monteiro (INRS)
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


Optimization and numerical analysis
-----
<div id="imagelist">
    <ul>
      <li>
      <a href="http://papers.nips.cc/paper/8779-reducing-the-variance-in-online-optimization-by-transporting-past-gradients"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-igt.png" alt="" title="Reducing the variance in online optimization by transporting past gradients">
      <div>
        Reducing variance in online optimization by transporting past gradients
        <em>
        Implicit gradient transport turns past gradients into gradients evaluated at the current iterate.
        It reduces the variance in online optimization and can be used as a drop-in replacement for the gradient estimate in a number of well-understood methods such as heavy ball or Adam. 
    </em>
    <br>
    Lead: Sebastien Arnold
      </div></a>
      </li> 
      <li>
      <a href="http://dawn.cs.stanford.edu/2017/07/05/yellowfin/"  target="_blank">
      <img src="{{ site.baseurl }}/images/Yellowfin.png" alt="" title="Self-tuning!">
      <div>
	YellowFin: Self-tuning optimization for deep learning
        <em>Simple insights on the momentum update yield an very efficient parameter-free algorithm that performs well across networks and datasets without the need to tune any parameters.</em>
        <br>
        Lead: Jian Zhang
      </div></a>
      </li> 
      <li>
      <a href="https://dawn.cs.stanford.edu/2017/08/29/accelerated-pca/" target="_blank">
      <img src="{{ site.baseurl }}/images/project-accelerated-stochastic-power-iteration.png" alt="" title="Accelerated power iteration">
      <div>
	Accelerated stochastic power iteration
        <em>Exciting recent results on how adding a momentum term to the power iteration yields a numerically stabe, accelerated method.</em>
        <br> 
        Lead: Peng Xu
      </div></a>
      </li> 
      <li>
      <a href="{{ site.baseurl}}/asynchrony/" target="_blank">
      <img src="{{ site.baseurl }}/images/theory-prediction.png" alt="Tuning parallel deep learning systems" title="Optimal momentum values for different levels of parallelization">
      <div>
	 Asynchrony begets momentum
        <em>When training large-scale systems asynchronously, you get a momentum surprise.
        We prove that system dynamics "bleed" into the algorithm introducing a momentum term even when the algorithm uses none.
        This theoretical result has very significant implications on large-scale optimization systems.</em>
      </div></a>
      </li>
      <li>
      <a href="https://arxiv.org/abs/1606.07365" target="_blank">
      <img src="{{ site.baseurl }}/images/project-sgd-averaging.png" alt="Averaging reduces variance but.." title="Averaging reduces variance but..">
      <div>
    Parallel SGD: When does averaging help?
        <em>
        Averaging as a variance-reducing mechanism.
         For convex objectives, we show
        the benefit of frequent averaging depends on the gradient variance envelope.
        For non-convex objectives, we illustrate that this benefit depends on the
        presence of multiple optimal points.
        </em>
        <br>
        Lead: Jian Zhang
      </div></a>
      </li>
      <li>
      <a href="http://papers.nips.cc/paper/5035-memory-limited-streaming-pca" target="_blank">
      <img src="{{ site.baseurl }}/images/pca.png" alt="" title="Memory Limited, Streaming PCA">
      <div>
        Memory Limited, Streaming PCA
        <em>
            An algorithm that uses O(kp) memory and is able to compute the k-dimensional spike with quasi-optimal, O(plogp), sample-complexity -- the first algorithm of its kind.
        </em>
      </div></a>
      </li> 
    </ul>
</div>


Deep learning and applications
------------------

<div id ="imagelist">
<ul>
      <li>
      <a href="https://arxiv.org/abs/1905.11382"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-state-reification.png" alt="" title="State-Reification Networks">
      <div>
	     State-Reification Networks
        <em>
        We model the distribution of hidden states over the training data and then project test hidden states on this distribution.
        This method helps neural nets generalize better, and overcome the challenge of achieving robust generalization with adversarial training
	</em>
	<br>
	Lead: Alex Lamb; oral presentation at ICML 2019
      </div></a>
      </li> 
      <li>
      <a href="http://proceedings.mlr.press/v97/verma19a.html"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-manifold-mixup.png" alt="" title="Manifold Mixup">
      <div>
        Manifold Mixup: Better Representations by Interpolating Hidden States
        <em>
        Simple regularizer that encourages neural networks to predict less confidently on interpolations of hidden representations.
        Manifold mixup improves strong baselines in supervised learning, robustness to single-step adversarial attacks, and test log-likelihood.
	</em>
	<br>
	Lead: Vikas Verma, Alex Lamb
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/1707.02392"  target="_blank">
      <img src="{{ site.baseurl }}/images/shape-analogies.png" alt="" title="Representation and generation">
      <div>
	Deep representations and Adversarial Generation of 3D Point Clouds
        <em>The first AutoEncoder design suited to 3D point cloud data beats state of the art in reconstruction accuracy. 
		GANs trainined in the AE's latent space generate realistic objects from every-day classes.
		</em>
        <br> 
        Lead: Panos Achlioptas
      </div></a>
      </li> 
</ul>
</div>


MCMC methods
----- 

<div id="imagelist">
    <ul>
      <li>
      <a href="https://arxiv.org/pdf/1707.05807.pdf" target="_blank">
      <img src="{{ site.baseurl }}/images/scan-order.png" alt="Gibbs Sampling Scan Order" title="[redacted]">
      <div>
        Dobrushin-optimized Gibbs Sampling
	<em>
    We introduce a method for calculating custom scan orders that lead to very fast inference, targetted at specific variables.
    DoGS can be many orders of magnitude faster than full scans.</em>
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/pdf/1707.05807.pdf" target="_blank">
      <img src="{{ site.baseurl }}/images/graph.png" alt="Gibbs Sampling Scan Order" title="[redacted]">
      <div>
	Gibbs Sampling Scan Order
	<em>Our NIPS 2016 work shows that scan order matters.<br>
	</em>
      </div></a>
      </li> 
</ul>
</div>


Large-scale systems
----- 
<div id="imagelist">
    <ul>
      <li>
      <a href="https://arxiv.org/abs/1904.03257"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-mlsys.png" alt="" title="MLSys: The New Frontier of Machine Learning Systems">
      <div>
        MLSys: The New Frontier of Machine Learning Systems
        <em>
        We propose to foster a new systems machine learning research community at the intersection of the traditional systems and ML communities, focused on topics such as
        </em>
     <br>
     Whitepaper
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/pdf/1708.05256.pdf"  target="_blank">
      <img src="{{ site.baseurl }}/images/project-15pf.png" alt="" title="Deep Learning at 15 Petaflops">
      <div>
        Deep Learning at 15 Petaflops
        <em>15-PetaFLOP Deep Learning system for solving scientific pattern classification problems on contemporary HPC architectures.
        We scale to 10,000 nodes by implementing a hybrid synchronous/asynchronous system and applying careful optimization of hyperparameters.</em>
        <br>
        Collaboration with NERSC at Lawrence Berkeley Labs and Intel.
      </div></a>
      </li> 
      <li>
      <a href="https://arxiv.org/abs/1606.04487">
      <img src="{{ site.baseurl }}/images/project-omnivore.png" alt="" title="Omnivore">
      <div>
        Omnivore: Optimizer for multi-device deep learning 
        <em>
        A high performance system prototype combining a number of much needed algorithmic and software optmimizations. 
        Importantly, we identify the degree of asynchronous parallelization as a key factor affecting both hardware and statistical efficiency.
        </em> 
        <br>
        Lead: Stefan Hadjis
      </div></a>
      </li> 
      <li>
      <a href="{{ site.baseurl}}/frogwild/">
      <img src="{{ site.baseurl }}/images/project-frogwild.png" alt="Picture of cute yet slightly deranged frog." title="Ribbit!">
      <div>
        FrogWild! - Fast PageRank approximations on Graph Engines
        <em>
        Using random walks and a simple modification of the GraphLab egine, we manage to get a 7x improvement compared to the state of the art.
        </em>
      </div></a>
      </li> 
      <li>
      <a href="http://proceedings.mlr.press/v32/papailiopoulos14.pdf">
      <img src="{{ site.baseurl }}/images/project-dks.png" alt="" title="Finding Dense Subgraphs via Low-Rank Bilinear Optimization">
      <div>
        Finding Dense Subgraphs via Low-Rank Bilinear Optimization
        <em>
        Our method searches a low-dimensional space for provably dense subgraphs of graphs with billions of edges.
        We provide data dependent guarantees on the quality of the solution that depend on the graph spectrum.
        </em>
        <br>
        Lead: Dimitris Papailiopoulos
      </div></a>
      </li> 
    </ul>
</div>


