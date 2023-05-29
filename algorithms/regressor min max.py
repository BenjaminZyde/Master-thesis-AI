# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:43:48 2023

@author: zydeb
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


source = "../rearangeddata/new 3-01/pandas-minmax-finalproof.pkl"


data = pd.read_pickle(source)

datax= pd.DataFrame()
datay= pd.DataFrame()
datax['duration']=data['duration']
datax['starttemp']=data['starttemp']
datax['settemp']=data['settemp']

datay['min']=data['min']
datay['max']=data['max']
datay['mean']=data['mean']


X_train, X_test, y_train, y_test = train_test_split(datax, datay, test_size=0.1, random_state=5)

regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

y_pred = regressor.predict(X_test)








