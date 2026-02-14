# Group 30 Energy Experiment: Measuring the Energy Impact of Different Optimisation Algorithms on Classifier Training

The machine learning notebook (`cifar10-with-cnn-.ipynb`) has been slightly adapted from https://www.kaggle.com/code/roblexnana/cifar10-with-cnn-for-beginer to allow for energy profiling on the training process.

The energy measuraments can be obtained by running the `run.py` file. For now, we simply run training five times, one with each type of optimiser. However, the code already has all the necessary components to be scaled up to ten runs for each type. 

The results from EnergiBridge are stored in respective folders for each optimisation type, and validation and testing results are stored in the `results` folder.