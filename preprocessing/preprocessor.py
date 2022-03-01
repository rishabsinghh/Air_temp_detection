# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:59:09 2022

@author: singh-93
"""

import pandas as pd
from pandas_profiling import ProfileReport
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

class preprocessor:
    def __init__(self,data):
        self.data=data
    def get_eda_report(self):
        """
        This Generates an entire report of the data which summarizes the statistics and insight of the data.
        """
        try:
            pf=ProfileReport(self.data)
            pf.to_file('report.html')
            return
        except Exception as e:
            print(e)
    def normalise_data(self,data):
        """
        This function normalises the numerical data which is needed so that all the units are in one scale.
        """
        try:
            ss=StandardScaler()
            data=pd.DataFrame(list(ss.fit_transform(data)),columns=data.columns)
            return data
        except Exception as e:
            print(e)
    def remove_columns(self,columns):
        try:
            data=self.data.drop(columns,axis=1)
            return data
        except Exception as e:
            print(e)
    def encode(self,columns,data):
        try:
            enc=LabelEncoder()
            for x in columns:
                data[x]=enc.fit_transform(data[x])
            return data
        except Exception as e:
            print(e)
            
            
        
   

            
            
            
            
    