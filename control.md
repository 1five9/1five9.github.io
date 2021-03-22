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