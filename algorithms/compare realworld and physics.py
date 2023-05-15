# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:07:01 2023

@author: zydeb
"""
import pandas as pd
import math
import matplotlib.pyplot as plt

physics= "../rearangeddata/new 3-01/pandas-physics.pkl"
realworld= "../rearangeddata/new 3-01/pandas-realworld.pkl"


phyf = pd.read_pickle(physics)
reaf = pd.read_pickle(realworld)

scale = len(phyf)/len(reaf)
rescaled=[]
diff=0

for x in range(len(reaf)):
    newx=math.floor(x*scale)
    
    diff+=math.pow(phyf.loc[newx]-reaf.loc[x],2)
    rescaled.append(phyf.loc[newx])

meandiff=diff/len(reaf)
RMS=math.sqrt(meandiff)
print()
plt.figure()
plt.plot(reaf)
plt.plot(rescaled)
plt.legend(['real','physics'])
plt.show()
