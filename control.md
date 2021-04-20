---
layout: page
permalink: /control/
title: Control
---

<center><img src="../images/controller.png" style="height:200px"></center>

## Predictive control & model-based reinforcement learning

Predictive control is ubiquitous in industry, with applications ranging from autonomous driving to large scale interconnected power systems. The first half of the class will explore the connection between model-based reinforcement learning (RL) and predictive control for continuous time problems.

The class will first recall basic ideas from approximate dynamic programming and model-based RL for systems with discrete states. Then, we will discuss optimal control problems for systems with continuous state and action spaces. Finally, for these continuous control problems, we will show how to learn from data the three components that are used in predictive control design: 
1. a model which describes the evolution of the system;
2. a safe set of states (and an associated control policy) from which the control task can be safely executed; and 
3. a value function which represents the cumulative closed-loop cost from a given state from the safe set.

### Instructor

This part of the course will be taught by [Ugo Rosolia](https://urosolia.github.io/) ([urosolia@caltech.edu](mailito:urosolia@caltech.edu)).


### Reading Material

Discrete MPDs:
- [Neuro-Dynamic Programming](http://athenasc.com/ndpbook.html)
- [Markov decision processes: discrete stochastic dynamic programming](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316887)
- [A survey and some new implementations](https://ieeexplore.ieee.org/document/8476633).
- [Aggregation, rollout, and policy improvement for reinforcement learning](https://arxiv.org/abs/1910.02426).
- [The linear programming
approach to approximate dynamic programming](http://www.mit.edu/~pucci/discountedLP.pdf).

Model Predictive Control:
- [Predictive control for linear and hybrid systems](https://drive.google.com/file/d/1zaaZZjoXm73klAWfC62YlrUzujJOXUMt/view)
- [Berkeley ME231A Lecture Notes](http://www.mpc.berkeley.edu/mpc-course-material)

Iterative Learning MPC:
- [The key ideas](https://ieeexplore.ieee.org/abstract/document/8039204)
- [Linear systems](https://www.sciencedirect.com/science/article/pii/S2405896317306523), [optimality guarantees](https://arxiv.org/abs/2010.15153), and [local approximations](https://onlinelibrary.wiley.com/doi/full/10.1002/rnc.5284?casa_token=HmlZ1o4yVTYAAAAA%3AcNSHJUT_0XSaOcPO4fVXi6ErgUs2x1ezIqSjijq_t40F4quz3hauo1rOwMx6bJPj1imQz019yntTcACHbw)
- [System identification for autonomous racing](https://ieeexplore.ieee.org/abstract/document/8896988) and the [python implementation](https://github.com/urosolia/RacingLMPC)
- Iterative LMPC in [python](https://github.com/urosolia/LMPC) and [matlab](https://github.com/urosolia/LMPC_SimpleExample)
- [Sample-based implementation](https://arxiv.org/abs/1904.06432)

Learning for Control:
- [Finite sample properties of system identification methods](https://ieeexplore.ieee.org/abstract/document/1024346)
- [The sample complexity of the linear quadratic regulator](https://link.springer.com/content/pdf/10.1007/s10208-019-09426-y.pdf)
- [Learning multi-step prediction models for receding horizon control](https://ieeexplore.ieee.org/abstract/document/8550494)
- [Data-Enabled Predictive Control (DeePC)](https://ieeexplore.ieee.org/abstract/document/8795639)
- [Provably safe and robust learning-based
model predictive control](https://www.sciencedirect.com/science/article/pii/S0005109813000678)
- [Learning-based model predictive
control: Toward safe learning in control](https://www.annualreviews.org/doi/abs/10.1146/annurev-control-090419-075625)
- [Cautious model predictive control using Gaussian process
regression](https://ieeexplore.ieee.org/abstract/document/8909368)
- [Set membership identification of nonlinear systems](https://www.sciencedirect.com/science/article/pii/S0005109804000470)
- [Adaptive model predictive
control for constrained linear systems](https://ieeexplore.ieee.org/abstract/document/6669544)
- [Adaptive MPC for iterative tasks](https://ieeexplore.ieee.org/abstract/document/8618694)

Deep model-based RL:
- [Deep reinforcement learning in a handful of trials](https://arxiv.org/abs/1805.12114)
- [Neural network dynamics for model-based
deep reinforcement learning](https://ieeexplore.ieee.org/abstract/document/8463189)
- [DeepMPC: Learning deep latent features for model
predictive control](http://www.roboticsproceedings.org/rss11/p12.pdf)
- [Plan online, learn
offline](https://arxiv.org/abs/1811.01848)
- [Safe deep model-based RL for sparse cost robotic tasks](https://ieeexplore.ieee.org/abstract/document/9013084)

Robust Planning in MPC
- [Optimizing over policies is NP-hard](https://ieeexplore.ieee.org/abstract/document/704989)
- [Affine disturbance feedback policies](https://www.sciencedirect.com/science/article/pii/S0005109806000021)
- [Disturbance feedback from a different prospective](https://link.springer.com/article/10.1007/s10107-003-0454-y)
- [The fixed tube approach](https://www.sciencedirect.com/science/article/pii/S0005109804002870)
