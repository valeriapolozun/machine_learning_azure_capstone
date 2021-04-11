from sklearn.tree import DecisionTreeClassifier
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from argparse import ArgumentParser


#ds = pd.read_csv('data/mobile_price_data.csv')

ds=pd.read_csv("https://raw.githubusercontent.com/valeriapolozun/machine_learning_azure_capstone/803e04124532b8921a0b19d70aa71abaccf74a1f/Mobile_Price_Classification.csv")


x = ds[['battery_power','blue','clock_speed','dual_sim','fc','four_g','int_memory','m_dep','mobile_wt','n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']]
y = ds[['price_range']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

run = Run.get_context()

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--max_depth', type=int, default=None, help="The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.")
    parser.add_argument('--min_samples_split', type=int, default=2, help="The minimum number of samples required to split an internal node")
    parser.add_argument('--max_features', type=int, help="The number of features to consider when looking for the best split:")

    args = parser.parse_args()

    run.log("Max depth:", np.float(args.max_depth))
    run.log("Min samples split:", np.int(args.min_samples_split))
    run.log("Max features:", np.int(args.max_features))

    model = DecisionTreeClassifier(max_depth=args.max_depth, min_samples_split=args.min_samples_split,max_features=args.max_features).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename='outputs/hyper-model.pkl')

if __name__ == '__main__':
    main()