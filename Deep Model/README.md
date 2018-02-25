## Introduction

Using deep models to predict sarcasm and assess it's generalization capabilities.

Our code include :
* Learning a model on the Reddit anotated dataset.
* Error analysis on the Reddit test set.
![Image not found](../images/linear-models-false-negative.png?raw=true "False Positive example")
* Transfer learning : Computing the probability of each character in South Park to use irony and comparing with our knowledge of the TV show. (Note: Our deep model has more convincing results on the South Park data).
![Image not found](../images/deep-transfer-learning.png?raw=true "South Park irony probability")

## Model :

Our model is made of conditonnal and positional attention modules, further explained in our report :

![Image not found](../images/conditionnal-attention.png?raw=true "Conditionnal Attention")

The full model is :

![Image not found](../images/full-network.png?raw=true "Full model")
