
# Capstone project for Azure Machine Learning Engineer Nanodegree


In this project we use a public external dataset.
This dataset will be used for training machine learning models on MS Azure. We use 2 different ways for trainining the model:
1.) AutoML
2.) Hyperparameter tuning with Hyperdrive
We compare the performances of the 2 best models of the above methods and we deploy the best model.
In the end we use the end-point which has been created and we test using the service by generating some predictions with some test data.


## Project Set Up and Installation

In Azure ML Studio we are going to use jupyter notebooks for running the AutoML and Hyperdrive trainings.
In order to run the notebooks a compute instance has been used:

## Dataset

### Overview

The dataset used includes data about mobile phones, such as battery, RAM, clock speed, availability of dual sim etc.
In total there are 20 different features about the phones.
The target variable is a price range of the mobile phones.



### Task
The aim is to understand the relationship between the mobile phone features and price range and based on that we want to predict the price range of mobile phones.

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
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
