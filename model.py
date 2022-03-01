# -*- coding: utf-8 -*-

from Data_loader.load_data import load_data
from preprocessing.preprocessor import preprocessor
import pickle
from sklearn.linear_model import LinearRegression
global filename
class model_build:
    def __init__(self,path):
        self.path=path
    def modelbuild(self):
        loader=load_data(self.path)
        df=loader.dataload()
        # print(df)
        pre=preprocessor(df)
        columns=['UDI','Product ID']
        df=pre.remove_columns(columns)
        #pre.get_eda_report()
        numerical_features=[x for x in df.columns if df[x].dtype!='O']
        new_data=pre.normalise_data(df[numerical_features])        
        df[numerical_features]=new_data
        # print(df)
        cat_features=[x for x in df.columns if df[x].dtype=='O']
        df=pre.encode(cat_features,df)
        y=df['Air temperature [K]']
        X=df.drop(['Air temperature [K]'],axis=1)
        model=LinearRegression()
        model.fit(X,y)
        filename = 'linear_regression.sav'
        pickle.dump(model, open(r"C:\Users\singh-93\Desktop\DS Full STack\Projects\Air_temp_detection\Air_temp_detection\models\Linear_Regression"+"\\"+filename, 'wb'))
        
obj1=model_build(r"C:\Users\singh-93\Desktop\DS Full STack\Projects\Air_temp_detection\Air_temp_detection\air_temp.csv")
obj1.modelbuild()
    
    