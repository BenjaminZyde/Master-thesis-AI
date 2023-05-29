# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:48:26 2023

@author: zydeb
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


sourcek = "../rearangeddata/new 3-01/beter-pandas-K_values-finalproof.pkl"
sourcei = "../rearangeddata/new 3-01/ingredients.pkl"

datak = pd.read_pickle(sourcek)
datai = pd.read_pickle(sourcei)
datax= pd.DataFrame()
datay= pd.DataFrame()
k=[]
sourdough=[]
water=[]
for x in range(len(datak)):
    di= datak.iloc[x].loc['dough_id']
    ing= datai.query("dough_id == \"" +str(di) +"\"")
    k.append(datak.iloc[x].loc['k_values'])
    sourdough.append(ing.iloc[0].loc['sourdough'])
    water.append(ing.iloc[0].loc['water'])
    

#datax['sourdough']=sourdough
datax['water']=water
datay['k']=k


X_train, X_test, y_train, y_test = train_test_split(datax, datay, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

y_pred = regressor.predict(X_test)








