---
layout: page
permalink: /learning/
title: Learning
---

<center><img src="../images/brain.png" style="height:200px"></center>

## Neural network theory: learning & generalisation

Neural networks are a powerful tool in modern machine learning, driving progress in areas ranging from [protein folding](https://www.nature.com/articles/s41586-019-1923-7) to [natural language processing](https://arxiv.org/abs/2005.14165). This half of the course will cover theoretical results with a direct bearing on machine learning practice. The course will tackle questions such as:

- How should I wire up my neural network?
- What class of functions does my network realise?
- If my wide 2-layer network can fit any dataset, why try anything else?
- How far is it safe to perturb my neural network during learning?
- Why does my network with more parameters than training data still generalise?
- Why is VC dimension not a relevant complexity measure for my network?
- How much information did my neural network extract from the training data?

*Health warning: these questions are still the subject of active research. This course will present the instructor's best understanding of the issues and their resolutions.*

### Instructor

This part of the course will be taught by [Jeremy Bernstein](https://jeremybernste.in) ([bernstein@caltech.edu](mailto:bernstein@caltech.edu)).

### Lectures

| #  | Date      | Subject	  	  	  	  	  	        | Resources              |
| -- | --------- | -------------------------------------- | ---------------------- |
|    |           | **Main Lectures**     |  |
| 7  | 4/20      | Neural Architecture Design	          | [pdf](/slides/learning/07.pdf) / [vid](https://caltech.zoom.us/rec/play/rBy3iYhn18vVQZ51EcnqjEfFfCBtsNO19b-vu4md5WI8sNh4rACX0MbIki6-ZMwVXT2zTqHJWEOzd6DN.TvAzOTJK7yLBgABn) |
| 8  | 4/22      | Network Function Spaces	              | [pdf](/slides/learning/08.pdf) / [vid](https://caltech.zoom.us/rec/play/bGLQRSJmHAQApPegayj75CteOeBcwFej4CAy9HzmVptMIkRYXnkhj-jLZHKWnw-y1FnUj_vdyAla9dYL.IcLdrTbDGHHyFxC-) / [ipynb](https://github.com/1five9/1five9.github.io/blob/master/slides/learning/08.ipynb)|
| 9  | 4/27      | Network Optimisation	                  | [pdf](/slides/learning/09.pdf) / [vid](https://caltech.zoom.us/rec/play/rU1nt-YjeJRe6W4nacFoOb-2PZlZJPCZR51HdMM7KXuZ9QEJmSY_qs7HBppFRLVPY_kciq0-zfUunMro.nE0keoLWfmIj-vhd) |
| 10 | 4/29      | Statistical Learning Theory	          | [pdf](/slides/learning/10.pdf) / [vid](https://caltech.zoom.us/rec/play/ywPwbkJuyGT3gAOTOAd_0DPvwlQHk2Ln7YumVRE72eeG3d9E9tqjECDe84tlZsCMW3euLlLrIm_j6nky.-ogkAxzEAEn6tIwH) |
| 11 | 5/04      | PAC-Bayesian Theory                    | [pdf](/slides/learning/11.pdf) / [vid](https://caltech.zoom.us/rec/play/kVxll8Ej94RkPNVb0qlm6DPBlhNY2A3GmheVLW-o5T2u08JvffmsbqJzp9gkciU1XkkkNPq5u5mz3rz8.wC-OPN9SqRq3okfc) |
| 12 | 5/06      | Project Ideas                          | [pdf](/slides/learning/12.pdf) / [vid](https://caltech.zoom.us/rec/play/WbMd0RukBwxyeZHM3slmTrnHiK0R7862SqA70eJl7WrlizTjj2cW_XLpdeEEMEJIbzg4m6_T_O1BZo3f.JI2a3eRUt3g5mB0u) |
|    |           | **Guest Lectures**     |  |
| 14 | 5/13      | Yasaman Bahri       				      | [pdf](/slides/guest/bahri.pdf) / [vid](https://caltech.zoom.us/rec/share/D354UiOLtu9TEWY1anPyhT60Hx8uWrQad0qY9aT02B64rMrunvgw6lnyJLXTcQ.CrFXOmjkOuNjLTrF) |
| 18 | 5/27      | Guillermo Valle-P??rez & Ard Louis	  | [pdf](/slides/guest/louis_valle-perez.pdf) / [vid](https://caltech.zoom.us/rec/share/dsE0BfjFVx4rihOIgOMCq6E4FzUwwT_x1slONNUwprfqkRvlfxExX4BG5aDhaa3T.PFVs_xEuheTNkSaE) |
| 19 | 6/01      | SueYeon Chung	                      | [pdf](/slides/guest/chung.pdf) / [vid](https://caltech.zoom.us/rec/share/rV7vw-jukUtgv-XWAgUV61ywVnlJiCVt6ak4yrmGrcX6B7A3qm5fDpjmDd4XIZgX.nUi_HjxFOZ7WKgiA) |

### Lecture 7 references

Network topologies:
- [Backpropagation applied to handwritten zip code recognition](https://ieeexplore.ieee.org/document/6795724)???CNNs;
- [Attention is all you need](https://arxiv.org/abs/1706.03762)???transformers.

Neural architecture search:
- [DARTS: differentiable architecture search](https://arxiv.org/abs/1806.09055);
- [Neural architecture search with reinforcement learning](https://arxiv.org/abs/1611.01578).

Local network design:
- [Centered weight normalization](https://ieeexplore.ieee.org/document/8237567)???weight constraints;
- [Deep hyperspherical learning](https://arxiv.org/abs/1711.03189);
- [Batch normalization](https://arxiv.org/abs/1502.03167);
- [Normalization propagation](https://arxiv.org/abs/1603.01431)???nonlinearity design.

Perturbation theory:
- [Perturbation theory for the singular value decomposition](https://users.math.msu.edu/users/iwenmark/Teaching/MTH995/Papers/SVD_Stewart.pdf);
- [Perturbation theory for multilayer perceptrons](https://arxiv.org/abs/2002.03432).

### Lecture 8 references

Universal function approximation:
- [Approximation by superpositions of a sigmoidal function](https://link.springer.com/article/10.1007/BF02551274);
- [Approximation capabilities of multilayer feedforward networks](https://www.sciencedirect.com/science/article/abs/pii/089360809190009T).

NNGP correspondence:
- [Radford Neal's PhD thesis](http://www.cs.toronto.edu/~radford/ftp/thesis.pdf)???introduces NNGP;
- [Kernel methods for deep learning](https://papers.nips.cc/paper/2009/hash/5751ec3e9a4feab575962e78e006250d-Abstract.html)???works out the relu kernel;
- [Deep neural networks as Gaussian processes](https://arxiv.org/abs/1711.00165)???NNGP for many layers.

### Lecture 9 references

"Classic" deep learning optimisers:
- [Rprop](https://ieeexplore.ieee.org/document/298623);
- [RMSprop](http://www.cs.toronto.edu/~hinton/coursera/lecture6/lec6.pdf);
- [Adam](https://arxiv.org/abs/1412.6980).

Optimisation models:
- [Lipschitz smoothness](http://www.seas.ucla.edu/~vandenbe/236C/lectures/gradient.pdf);
- [Cubic regularisation](https://link.springer.com/article/10.1007/s10107-006-0706-8);
- [Mirror descent](http://www.princeton.edu/~yc5/ele522_optimization/lectures/mirror_descent.pdf).

Relative optimisers:
- [LARS](https://arxiv.org/abs/1708.03888), [LAMB](https://arxiv.org/abs/1904.00962) and [Fromage](https://arxiv.org/abs/2002.03432)???per layer relative updates;
- [Madam](https://arxiv.org/abs/2006.14560)???per synapse relative updates;
- [Nero](https://arxiv.org/abs/2102.07227) and [NFnets](https://arxiv.org/abs/2102.06171)???per neuron relative updates with weight constraints.

### Lecture 10 references

Function counting and generalisation:
- [Cover's function-counting theorem](https://isl.stanford.edu/~cover/papers/paper2.pdf);
- [Vapnik and Chervonenkis's 1971 paper](https://epubs.siam.org/doi/10.1137/1116025);
- [A textbook chapter on VC theory](http://agbs.kyb.tuebingen.mpg.de/lwk/sections/) (chapter 5).

VC theory and neural networks:
- [Probable networks and plausible predictions](http://www.inference.org.uk/mackay/network.pdf) (section 10.4);
- [Understanding deep learning requires rethinking generalization](https://arxiv.org/abs/1611.03530).

### Lecture 11 references

Bayesian data analysis and model comparison:
- [David MacKay's book](https://www.inference.org.uk/itila/book.html) (chapter 28).

PAC-Bayes derivation:
- [Bounds for averaging classifiers](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.26.4424).

PAC-Bayes for NNs:
- [Sharpness & flatness of minimisers](https://arxiv.org/abs/1905.12213);
- [Taking the prior "local" to the initialisation](https://arxiv.org/abs/1703.11008);
- [Function space at infinite width](https://arxiv.org/abs/1805.08522).

### Lecture 12 references

Understanding the distribution of solutions that SGD samples from:
- [Neural tangent kernel](https://arxiv.org/abs/1806.07572);
- [Is SGD a Bayesian sampler? Well, almost](https://arxiv.org/abs/2006.15191).

Using PAC-Bayes for architecture design:
- [Comparing bounds for different architectures](https://arxiv.org/abs/2012.04115);
- [Analytic lower bound on the NN evidence](https://arxiv.org/abs/2103.01045);
- [Learning GP invariances using the marginal likelihood](https://arxiv.org/abs/1808.05563) (a.k.a. evidence).

Adversarial examples:
- [Intriguing properties of neural networks](https://arxiv.org/abs/1312.6199).

Combining NN architectural properties with control:
- [Neural lander](https://arxiv.org/abs/1811.08027)???NNs with a Lipschitz constraint.
