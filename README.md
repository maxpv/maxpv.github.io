You can find on this page:
- Notebooks about [real world problems](https://maxpv.github.io/#real-world-problems)
- [Fun](https://maxpv.github.io/#lab) with fascinating topic of ML.
- Compilation of [papers](https://maxpv.github.io/#interesting-papers) that I found interesting.
- Code [snippets](snippets.md).
- The GoolgleCloud [installation notes](installation.md) for a quick installation of Jupyter+Keras+Tensorflow+... on a GoogleCloud virtual machine.

---- 

### Lab
###### - Adversarial examples ([notebook](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/Adversarial_ResNet50.ipynb))
In this notebook we generate adversarial images and make a frog looks like a plane in the eyes of a pre-trained `ResNet50` model in Keras.

----

### Real world problems
###### - Leaves ([notebook](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/leaves.ipynb)) `classification /w sklearn`
Kaggle Challenge proposed in 2017, of [leaf classification](https://www.kaggle.com/c/leaf-classification/data). It's an interesting dataset because there is 16 sample for each of the 99 species with around 200 features per instance. We mainly focused on reducing the dimensionality of the dataset.

###### - AdTracking Fraud Detection (work in progress) `classification /w sklearn`
Kaggle Challenge proposed by Talking Data. The objective is to "predict whether a user will download an app after clicking a mobile app advertisement."

###### - Parkinson Telemonitoring ([work in progress](https://github.com/maxpv/maxpv.github.io/blob/master/notebooks/parkinson-telemonitoring.ipynb)) `regression /w sklearn keras`
[Dataset](https://archive.ics.uci.edu/ml/datasets/Parkinsons+Telemonitoring) of voice measurements from 42 people with early-stage Parkinson's disease, built by the University of Oxford in collaboration with 10 medical centers in the US and INtel Corporation.

----

### Interesting papers

###### - [Practical Black-Box Attacks against Machine Learning](https://arxiv.org/abs/1602.02697) (Papernot and al.)
This paper introduces a technique that enables control over a remote deep neural network. No prior knowledge is required excepted the output label for a given input. The main idea here is to create a local substitute neural network trained with a substitute crafted by the adversary. And  use this substitute DNN to craft adversarial examples with (classic) gradient based techniques. They don't design a substitue DNN with a perfect accuracy but rather "approximate the oracle's decision boundaries with few label queries". A small local and unlabelled dataset is created by the adversary. The dataset is labelled by the oracle and augmented locally by a technique named *Jacobian-based Dataset Augmentation*.

###### - [Can computers create art ?](https://arxiv.org/abs/1801.04486) (Aaron Hertzmann)
Tnteresting parallel between the state of painting when photography rose. How new technologies followed the pattern: initial fear, denial, acceptance, creation of new art forms. The second part of the paper discuss authorship and wether or not AI systems can create art in the future. In this last case the author lies down some requirement to consider an entity as an artist, for instance: sociability. "AI can be granted authorship when we view the AI as a social agent, and it is performing some communication or sharing through the art. [...] as deserving of empathy and ethical consideration in some way."
