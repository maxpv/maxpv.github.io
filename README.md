# Data Science and Machine Learning playground

This is a compilation of [Jupyter](jupyter.org) notebooks, where we'll be playing with machine learning, data visualization and data exploration.

You can also find on this repository:
- [Snippets](snippets.md).
- The GoolgleCloud [installation notes](installation.md) for a quick installation of Jupyter+Keras+Tensorflow+... on a GoogleCloud virtual machine.


## Lab
### Adversarial examples ([notebook](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/Adversarial_ResNet50.ipynb))
In this notebook we generate adversarial images and make a frog looks like a plane in the eyes of a pre-trained `ResNet50` model in Keras.

## Real world problems

### Leaves ([notebook](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/leaves.ipynb))
`classification /w sklearn`

Kaggle Challenge proposed in 2017, of [leaf classification](https://www.kaggle.com/c/leaf-classification/data). It's an interesting dataset because there is 16 sample for each of the 99 species with around 200 features per instance. We mainly focused on reducing the dimensionality of the dataset.

### AdTracking Fraud Detection (work in progress)
`classification /w sklearn`

Kaggle Challenge proposed by Talking Data. The objective is to "predict whether a user will download an app after clicking a mobile app advertisement."

### Parkinson Telemonitoring ([work in progress](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/parkinson-telemonitoring.ipynb))
`regression /w sklearn keras`

[Dataset](https://archive.ics.uci.edu/ml/datasets/Parkinsons+Telemonitoring) of voice measurements from 42 people with early-stage Parkinson's disease, built by the University of Oxford in collaboration with 10 medical centers in the US and INtel Corporation.


## Interesting papers

- [Can computers create art ?](https://arxiv.org/abs/1801.04486): interesting parallel between the state of painting when photography rose. How new technologies followed the pattern: initial fear, denial, acceptance, creation of new art forms. The second part of the paper discuss authorship and wether or not AI systems can create art (?).
