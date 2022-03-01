# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:45:02 2022

@author: singh-93
"""

import pandas as pd
class load_data:
    def __init__(self,path):
        self.path=path
    def dataload(self):
        """
        This function is used to load data to the main function.
        """
        try:
            data=pd.read_csv(self.path)
            return data
        except Exception as e:
            raise e