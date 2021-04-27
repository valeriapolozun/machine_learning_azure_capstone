import os
import numpy as np
import pandas as pd
import json
import joblib

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'),'model.pkl')
    model = joblib.load(model_path)

def run(data):
    try:
        #data = np.array(json(data))
        data_json=json.loads(data)
        data=pd.DataFrame(data_json)
        result = model.predict(data)
        return result.tolist()
    except Exception as err:
        return str(err)
