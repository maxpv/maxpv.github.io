You can find on this page:
- Notebooks about [real world problems](https://maxpv.github.io/#real-world-problems).
- [Fun](https://maxpv.github.io/#lab) with fascinating topic of ML.
- Compilation of [papers](https://maxpv.github.io/#interesting-papers) that I found interesting.

And also:
- Code [snippets](snippets.md) (see also [gist](https://gist.github.com/maxpv)).
- The GoolgleCloud [installation notes](installation.md) for a quick installation of Jupyter+Keras+Tensorflow+... on a GoogleCloud virtual machine.

## Lab
#### Adversarial examples ([notebook](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/Adversarial_ResNet50.ipynb))
In this notebook we generate adversarial images and make a frog looks like a plane in the eyes of a pre-trained `ResNet50` model in Keras.

## Problems
#### Leaves ([notebook](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/leaves.ipynb))
`classification` `sklearn` `ensemble` 

Kaggle Challenge submitted in 2017, of [leaf classification](https://www.kaggle.com/c/leaf-classification/data). It's an interesting dataset because there is 16 sample for each of the 99 species with around 200 features per instance. We mainly focused on reducing the dimensionality of the dataset.

#### Binary Sentiment Analysis ([work in progress](https://drive.google.com/file/d/1t7uN2b1trQgY0NmPnBvoa2KAegxXWIC1/view?usp=sharing))
`nlp` `keras` 

This [dataset](https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences) contains sentences labelled as positive or negative. Sentences comes directly from IMDB, Amazon and yelp. We here experiment with bayesian optimisation processes on top of Keras.

#### Fashion MNIST ([notebook](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/Fashion_MNIST.ipynb) )
`classification` `CNN` `Keras`

[Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) is a dataset crafted by Zalando, containing 70,000 gray scale images. Each image has MNIST-like dimensions: 28x28.
"Zalando intends Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits."

#### AdTracking Fraud Detection (in progress)
`classification` `sklearn`

Kaggle Challenge submitted by Talking Data. The objective is to "predict whether a user will download an app after clicking a mobile app advertisement."

#### Parkinson Telemonitoring ([notebook](https://www.kaggle.com/mountainguest/parkinson-telemonitoring-regression-with-keras))

`multi-variate regression` `sklearn` `Keras`

[Dataset](https://archive.ics.uci.edu/ml/datasets/Parkinsons+Telemonitoring) of voice measurements from 42 people with early-stage Parkinson's disease, built by the University of Oxford in collaboration with 10 medical centers in the US and Intel Corporation.

## Interesting papers

###### - [Practical Black-Box Attacks against Machine Learning](https://arxiv.org/abs/1602.02697) (Papernot and al.)
This paper introduces a technique that enables control over a remote deep neural network. No prior knowledge is required excepted the output label for a given input. The main idea here is to create a local substitute neural network trained with a substitute crafted by the adversary. And  use this substitute DNN to craft adversarial examples with (classic) gradient based techniques. They don't design a substitute DNN with a perfect accuracy but rather "approximate the oracle's decision boundaries with few label queries". A small local and unlabelled dataset is created by the adversary. The dataset is labelled by the oracle and augmented locally by a technique named *Jacobian-based Dataset Augmentation*.

###### - [Can computers create art ?](https://arxiv.org/abs/1801.04486) (Aaron Hertzmann)
Interesting parallel between the state of painting when photography rose. How new technologies followed the pattern: initial fear, denial, acceptance, creation of new art forms. The second part of the paper discuss authorship and whether or not AI systems can create art in the future. In this last case the author lies down some requirement to consider an entity as an artist, for instance: sociability. "AI can be granted authorship when we view the AI as a social agent, and it is performing some communication or sharing through the art. [...] as deserving of empathy and ethical consideration in some way."
