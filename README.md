
# Capstone project for Azure Machine Learning Engineer Nanodegree
## Operationalize an ML model  - predicting mobile prices 

The aim of this project is to build a fully operationalized ML model pipeline in MS Azure. The outcome of the project is a working service - which is ready for consumption: making predictions on new, unseen data points.

In this project we use a public external dataset about mobile phones.
This dataset will be used for training machine learning models on MS Azure. We use 2 different ways for trainining the model:
1.) AutoML
2.) Hyperparameter tuning with Hyperdrive

We compare the performances of the 2 methods and we deploy the best model.
In the end we use the end-point which has been created and we test using the service by generating some predictions with some test data.


## Project Set Up and Installation

In Azure ML Studio we are going to use jupyter notebooks for running the AutoML and Hyperdrive trainings.
In order to run the notebooks a compute instance has been used: STANDARD_DS3_V2 virtual machine

![apr27_compute_instance_notebook](https://user-images.githubusercontent.com/4347923/116284597-8b0c5280-a78d-11eb-962d-cfb066f2e405.JPG)

## Dataset

### Overview

The dataset used includes data about mobile phones, such as battery, RAM, clock speed, availability of dual sim etc.
In total there are 20 different features about the phones.

The target variable is a price range of the mobile phones, which is a number between 0 (=very low price) and 3(=very high price)

The data set is a public data set and available on Kaggle:
https://www.kaggle.com/iabhishekofficial/mobile-price-classification


### Task
The aim is to understand the relationship between the mobile phone features and price range and based on that we want to predict the price range of mobile phones.

Target variable:
The price with value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost).

The features which will be used:

battery_power: Total energy a battery can store in one time measured in mAh

blue: Has bluetooth or nota

clock_speed: Speed at which microprocessor executes instructions

dual_sim: Has dual sim support or not

fc: Front Camera mega pixels

four_g: Has 4G or not

int_memory: Internal Memory in Gigabytes

m_dep: Mobile Depth in cm

mobile_wt: Weight of mobile phone

n_cores: Number of cores of processor

pc: Primary Camera mega pixels

px_height: Pixel Resolution Height

px_width: Pixel Resolution Width

ram: Random Access Memory in Megabytes

sc_h: Screen Height of mobile in cm

sc_w. Screen Width of mobile in cm

talk_time: longest time that a single battery charge will last when you are

three_g: Has 3G or not

touch_screen: Has touch screen or not

wifi: Has wifi or not


### Access

The dataset is accessed directly from my github repo as a csv file.
After reading the csv file we create a Tabular Dataset from the a pandas dataframe.

## Automated ML

The automl_config class includes all the settings of the configuration, which is used for the AutoML machine experiment in Azure.

The settings, which were tuned:
  - experiment_timeout_minutes (=maximum duration of the experiment in minutes before it terminates): 25
  - max_concurrent_iterations (=nr. of iterations which are done parallel): 4
  - task (=type of task): 'Classification'
  - compute_target (=compute target to run the experiment)
  - training_data (=training data to be used)
  - primary metric (=which metric should be used for the performance measuring): 'Accuracy'
  - enable_early_stopping: 'True'
  - n_cross_validations (=nr. of cross validations): 5
  - featurization (= whether featurization should be done automatically): 'auto'

### Results

The run details with the actual status of the AutoML were visible during the run:




The best algorithm found had an accuracy level of 80.04%.

The parameters of the best model with the algorithm "StackEnsamble" are shown below:






## Hyperparameter Tuning

The model chosen was the decision tree algorithm as it is working very well for classification type of problems.

The parameters I selected for hyperparameter search were the following:
- Max_depth
- Min_samples_split
- Max_features

### Results

The best algorithm found had an accuracy level of 77%.

The parameters of the best model:
- Max_features: 16
- Min samples split:4
- Max depth: 50

In the following screenshots you can see the status of the model training by using `RunDetails` widget as well as the best model trained with it's parameters:

![hyperdrive_run_details3_27april](https://user-images.githubusercontent.com/4347923/116284600-8ba4e900-a78d-11eb-8317-5a6ecbe39b7f.JPG)

![hyperdrive_run_details4_27april](https://user-images.githubusercontent.com/4347923/116284603-8c3d7f80-a78d-11eb-8e78-c5a598b1e1d1.JPG)


## Model Deployment

The best performing model was achieved by using the AutoML functionalities of MS Azure.
The best model has been deployed and afterwards the end-point has been tested by sending some test data to it:

![apri_27_deployed_model_healthy](https://user-images.githubusercontent.com/4347923/116284599-8ba4e900-a78d-11eb-8889-79c337848010.JPG)




## Screen Recording
Here is a screen recording of the project in action: https://youtu.be/4Hg7rqpJPWo
The screencast demonstrates:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response


