## Introduction

This is a baseline approach to our problem, with classical statistical NLP feaeturization and classification.

Our code include :
* Learning a model on the Reddit anotated dataset.
* Error analysis on the Reddit test set.
![Image not found](../images/linear-models-false-negative.png?raw=true "False Positive example")
* Transfer learning : Computing the probability of each character in South Park to use irony and comparing with our knowledge of the TV show.
![Image not found](../images/linear-models-transfer-learning.png?raw=true "South Park irony probability")

## Features

This directory contains the jupyter-notebooks for training a linear models with various features :
* tf-idf features on various n-gram sizes.
* words lengths, and other common simple features.
* Showcasing the influence of taking into account a larger context when predicting sarcasm.
![Image not found](../images/memory_influence.png?raw=true "Context size vs. accuracy")

## models

Linear models include :
* support vector machine.
* Logistic regression.

Which allows us to have a good baseline model, for comparaison with our deep learning approach.
