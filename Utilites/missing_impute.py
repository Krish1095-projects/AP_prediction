import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time
import time
from sklearn.impute import KNNImputer
class Identifier:
    def __init__(self):
        pass
    def read_data(self,filename):
        try:
            self.path = os.getcwd()
            self.temp_data = pd.read_csv(self.path+self.filename)
            return self.temp_data
        except Exception as e:
            print(e)
    def check_missing_values(self,df):
        self.df = df
        try:
            if isinstance(self.df, pd.DataFrame):
                print("The passed instance is Dataframe")
                print("Identifying missing values")
                time.sleep(1)
                print("The total number of Missing values present is :{}".format(self.df.isnull().sum().sum()))
                return pd.DataFrame(self.df.isnull().sum(),columns=['count'])
        except Exception as e:
            print(e)
    def compute_missing_percentage(self,df):
        self.df = df
        try:
            if isinstance(self.df, pd.DataFrame):
                print("The passed instance is Dataframe")
                print("Identifying missing values percentage")
                time.sleep(5)
                print("computed percentage")
                return pd.DataFrame((self.df.isnull().sum()/len(self.df))*100,columns=['Missing_percentage'])
        except Exception as e:
            print(e)
    def missing_value_treatment(self,df):
        self.df= df
        try:
            if isinstance(self.df, pd.DataFrame):
                self.df = self.df.values
                self.ix = [i for i in range( self.df.shape[1]) if i != 0 and i!=1 and i!=15]
                self.X, self.y =  self.df[:, self.ix],  self.df[:, 15]
                self.imputer = KNNImputer()
                self.imputer.fit(self.X)
                self.Xtrans = self.imputer.transform(self.X)
                print('Missing: %d' % sum(np.isnan(self.Xtrans).flatten()))
                return self.Xtrans
        except Exception as e:
            print(e)
                    