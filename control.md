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

### Lectures

| #  | Date      | Subject	  	  	  	  	  	        | Resources              |
| -- | --------- | -------------------------------------- | ---------------------- |
|    |           | **Main Lectures**              |  |
| 1  | 3/30      | Discrete MDPs        	    	      | [pdf](https://1five9.github.io/slides/control/Lecture_1_MDPs.pdf) / [vid](https://caltech.zoom.us/rec/share/VR3fwwu9QeALQ80dRtIghSqzpnkpAOpF_bwePNoBSnBzRxzgNN3uV4OdzvmBe8VE.ftHclybplbeeU0_s?startTime=1617141230000) |
| 2  | 4/01      | Optimal Control       	              | [pdf](https://1five9.github.io/slides/control/Lecture_2_OCPs.pdf) / [vid](https://caltech.zoom.us/rec/share/v32Tbod7kDVVatTJO9u4LPjtuKYY1ffxIYMx77NvU3LPcjzvJfBMcr06K9vMkg6p.NbAhirdzWsEf9pE6?startTime=1617312887000)|
| 3  | 4/06      | Model Predictive Control               | [pdf](https://1five9.github.io/slides/control/Lecture_3_MPC.pdf) / [vid](https://caltech.zoom.us/rec/share/Q0kDgmvMJ800GMX46lTipBVjw5Z5SkuJ7MVUXKjmx751bmAUCsTS9kx2AHQWZ-g1.JsnICIGB-NeBSJ9u?startTime=1617744869000)|
| 4  | 4/08      | Learning MPC                           | [pdf](https://1five9.github.io/slides/control/Lecture_4_MPC_TC.pdf) / [vid](https://caltech.zoom.us/rec/share/6hy8WYahNjzqyvbw5vh2JX-RIKeq1LJEt-KTKOXye86DQxA9H7I9GM13jF7NXYU9.LMNtHFtXBmQETYfa?startTime=1617917676000) / [supp](https://1five9.github.io/slides/control/Lecture_4_SuppMaterial.pdf) |
| 5  | 4/13      | Model Learning in MPC 				          | [pdf](https://1five9.github.io/slides/control/Lecture_5_MPC_and_Model_Learning.pdf) / [vid](https://caltech.zoom.us/rec/share/EUwZy302kdmZaHZTxdxm4xNI6AE1kBuijoUNg7Ay909A58kJhfd-THQrEFxOUoZQ.HWlG08DHSjJgL1Ts) |
| 6  | 4/15      | Planning Under Uncertainty and Project Ideas    	          | [pdf](https://1five9.github.io/slides/control/Lecture_6.pdf)  / [vid](https://caltech.zoom.us/rec/play/NMspLIgaI2jjVw84424EkfA_kta9AXX8JIxm2WW2OljV36I7NQ9CMEsYkEyBSosgm2ksCMSM-FeZj4jD.kq7ZyqjY2FPskbRR?continueMode=true) |
|    |           | **Guest Lectures**     |  |
| 13 | 5/11      | Joe Marino                             | [pdf](/slides/guest/marino.pdf) / [vid](https://caltech.zoom.us/rec/play/rKK9PNaM7dtfHEHEcJO0wxoB98Kde7vY_Ge63TjIfe_ATBxQwrL0NIs39vdk8bb9RJ-Kg57Ty4KK2Sdg.8RdlP3SKDlyAogR9) |
| 16 | 5/20      | Guanya Shi	            			  | [pdf](/slides/guest/shi.pdf) / [vid](https://caltech.zoom.us/rec/share/TtP43hzMIUdXuMsPrpwQTteMenoXAD1L3A_Rv3uUxklt7lEU_wE89FrKtFpTgtc.XtVMvJKYsXwwl2lK) |
| 17 | 5/25      | Roberto Calandra	            				      | [pdf](https://slides.com/rcalandra/advances-mbrl/) / [vid](https://caltech.zoom.us/rec/share/I2IY3xPfBNE9Opp8WkjmDa6lFyrcWl7oDAb2Y3IzK2ZwmkRG-eD6hMdeJKbiOaKD.cmvXqrfRmoVBC6eP) |


### Reading material

Discrete MDPs:
- [Neuro-dynamic programming](http://athenasc.com/ndpbook.html)
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
- [Sample-based LMPC](https://arxiv.org/abs/1904.06432)

Learning for control:
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

Robust planning in MPC
- [Optimizing over policies is NP-hard](https://ieeexplore.ieee.org/abstract/document/704989)
- [Affine disturbance feedback policies](https://www.sciencedirect.com/science/article/pii/S0005109806000021)
- [Disturbance feedback from a different prospective](https://link.springer.com/article/10.1007/s10107-003-0454-y)
- [The fixed tube approach](https://www.sciencedirect.com/science/article/pii/S0005109804002870)
- [The shrinking tube approach](https://www.sciencedirect.com/science/article/pii/S0005109801000516)
