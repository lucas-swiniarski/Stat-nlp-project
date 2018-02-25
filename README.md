# Natural Language Processing Project

## Goal

* Is sarcasm easily predictable by current state-of-the-art machine learning techniques ?
* Does it rely heavily on the context?
* Is it transferable from one dataset to another ?

## Data

Starting from the anotated [reddit sarcasm dataset](http://nlp.cs.princeton.edu/SARC/2.0/) we train models and evaluate the generalization capabilities on both the reddit testing set, and a [southpark dataset](https://www.kaggle.com/tovarischsukhov/southparklines/data).

## Deep Models

Trying both a Recurrent Neural Network and a network with [positionnal attention](https://arxiv.org/abs/1706.03762), we achieved our best results with the following architecture :
![Image not found](images/full-network.png?raw=true "Positional attention network")

## Interpretability of results

Attention allows us to understand its predictions :

![Image not found](images/attention-plot.png?raw=true "Weights of various words in our attention model")

This plot is further explained in the Deep Model readme and final project report.

## Content

* Deep model : jupyter-notebooks for learning a deep Recurrent neural network or attention network (https://arxiv.org/abs/1706.03762). Our deep models has a context of size 1 (for training speed purposes), only looking at the previous and current sentence to predict sarcasm on the current sentence.
* Linear Model : jupyter-notebooks for learning linear models (SVM, Logistic Regression) with classifc statistical NLP feaeturization process.
* Preprocessing : Preprocess the southpark dataset and Reddit sarcasm dataset.
* Reports : pdf of project proposal and final report.

## Install
* Python 2.7, PyTorch v0.3.1, jupyter-notebook
* Download : https://www.kaggle.com/tovarischsukhov/southparklines/data southpark dataset.
* Download : http://nlp.cs.princeton.edu/SARC/2.0/ sarcasm dataset.
