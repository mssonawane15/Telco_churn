import pickle
import pandas as pd
import json
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

class Telco_Customer_Churn:
    def __init__(self,data):
        self.data = data

    def load(self):
        self.model = pickle.load(open("model.pkl","rb"))
        self.columns = json.load(open("columns.json","r"))
    
    def Predict(self):
        self.load()
        dictionary = {}
        for k,v in self.data.items():
            if v.isdigit():
                dictionary[k] = [int(v)]
            else:
                dictionary[k] = [v]

        test_dataframe = pd.DataFrame(dictionary)  

        result = self.model.predict(test_dataframe)

        return str(result[0])
