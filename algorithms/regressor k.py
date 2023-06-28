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
sourcei = "../rearangeddata/new 9-05/ingredients.pkl"
sourceids= "../rearangeddata/new 3-01/beter-pandas-ids.pkl"
save="../rearangeddata/new 9-05/output-regressor-k.pkl"
dataids= pd.read_pickle(sourceids) 
datak = pd.read_pickle(sourcek)
datai = pd.read_pickle(sourcei)
datax= pd.DataFrame()
datay= pd.DataFrame()
aa=[]   #Ascorbic acid
f=[]    #flour
s=[]    #salt
sd=[]   #sourdough
vg=[]   #vital gluten
w=[]    #water
y=[]    #yeast
k=[]
for x in range(len(dataids)):
    di= dataids.iloc[x].loc['DoughID']
    ing= datai.query("dough_id == \"" +str(di) +"\"")
    ks= datak.query("dough_id == \"" +str(di) +"\"")
    if (len(ing) !=0 and len(ks)!=0):
        k.append(ks.iloc[0].loc['k_values'])
        aa.append(ing.iloc[0].loc['Ascorbic acid'])
        f.append(ing.iloc[0].loc['Flour'])
        s.append(ing.iloc[0].loc['Salt'])
        sd.append(ing.iloc[0].loc['Sourdough'])
        vg.append(ing.iloc[0].loc['Vital gluten'])
        w.append(ing.iloc[0].loc['Water'])
        y.append(ing.iloc[0].loc['Yeast'])
    
    
    
    
    
datax['Ascorbic acid']=aa
datax['Flour']=f
datax['Salt']=s
datax['Sourdough']=sd
datax['Vital gluten']=vg
datax['Water']=w
datax['Yeast']=y
datay['k']=k


X_train, X_test, y_train, y_test = train_test_split(datax, datay, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

y_pred = regressor.predict(X_test)
saveids=[]
for x in y_test.index:
    saveids.append(datak.iloc[x].loc['dough_id'])
output= pd.DataFrame()
output['dough_id']=saveids
y_test.reset_index(inplace=True)
output['k']=y_test['k']
output['prediction']=y_pred
output.to_pickle(save)






