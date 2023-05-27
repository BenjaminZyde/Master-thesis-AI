# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:04:13 2023

@author: zydeb
"""
import math
import matplotlib.pyplot as plt
import pandas as pd


save="../rearangeddata/new 3-01/pandas-physics.pkl"

doughtemp=24.463
roomtemp=5
#time in minutes
time=195

temp=[]

time*=60

for x in range(time):
    temp.append(roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-0.0001279*x)))
    
pf =pd.DataFrame(temp)
pd.to_pickle(pf,save)

plt.figure()
plt.plot(temp)
plt.show()
