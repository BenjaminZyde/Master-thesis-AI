# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:05:28 2023

@author: zydeb
"""

import pandas as pd

source="../rearangeddata/new 3-01/pandas-K_values-finalproof.pkl"
save="../rearangeddata/new 3-01/beter-pandas-K_values-finalproof.pkl"

data= pd.read_pickle(source)
goodid=[]
goodk=[]

for x in range(len(data)):
    k=data.iloc[x].loc['k_values']
    ids=data.iloc[x].loc['dough_id']
    if (k!=1 and k!=99999):
        goodid.append(ids)
        goodk.append(k)
output=pd.DataFrame()
output['dough_id']=goodid
output['k_values']=goodk
output.reset_index(inplace=True, drop=True )
output.to_pickle(save)
