# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:05:28 2023

@author: zydeb
"""

import pandas as pd

source="../rearangeddata/new 3-01/pandas-K_values-finalproof.pkl"
save="../rearangeddata/new 3-01/beter-pandas-K_values-finalproof.pkl"

data= pd.read_pickle(source)
doids=[]
length= len(data)-1
for x in range(length):
    k=data.iloc[length-x].loc['k_values']
    if (int(k)==1):
        data.drop(index=length-x,axis=0,inplace=True)
    if (int(k)==99999):
        data.drop(index=length-x,axis=0,inplace=True)
        
data.reset_index()
data.to_pickle(save)
