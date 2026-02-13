# Group 30 Energy Experiment: Measuring the Energy Impact of GPU Optimisation on Classifier Training

The machine learning notebook (`mnist-cnn-classification.ipynb`) has been slightly adapted from https://www.kaggle.com/code/merfarukyce/mnist-cnn-classification to allow for energy profiling on the training process.

The energy measuraments can be obtained by running the `run.py` file. For now, we simply run training twice, one with GPU optimisation, and once without. However, the code already has all the necessary components to be scaled up to ten runs for each mode. 

Lastly, please note that the way GPU optimisation is turned on or off is made for MacOS. On different operating systems, this part of the code will likely need to be modified.
