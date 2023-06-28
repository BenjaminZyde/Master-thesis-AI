# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:19:23 2023

@author: zydeb
"""


import pandas as pd
import math
import matplotlib.pyplot as plt


realworld= "../rearangeddata/new 3-01/pandas-realworld.pkl"


reaf = pd.read_pickle(realworld)

doughtemp=24.463
roomtemp=5
#time in minutes
time=195

temp=[]
temp1=[]
temp2=[]
temp3=[]
temp4=[]
time*=60

for x in range(time):
    temp.append(roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-0.0001279*x)))
    temp4.append(roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-0.0001524*x)))
    temp1.append(roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-0.001*x)))
    temp2.append(roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-0.0001*x)))
    temp3.append(roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-0.00001*x)))
    
    
pf =pd.DataFrame(temp)
pf1 =pd.DataFrame(temp1)
pf2 =pd.DataFrame(temp2)
pf3 =pd.DataFrame(temp3)
pf4 =pd.DataFrame(temp4)

scale = len(pf)/len(reaf)
rescaled=[]
rescaled1=[]
rescaled2=[]
rescaled3=[]
rescaled4=[]
diff=0

for x in range(len(reaf)):
    newx=math.floor(x*scale)
    
    diff+=math.pow(pf.loc[newx]-reaf.loc[x],2)
    rescaled.append(pf.loc[newx])
    rescaled1.append(pf1.loc[newx])
    rescaled2.append(pf2.loc[newx])
    rescaled3.append(pf3.loc[newx])
    rescaled4.append(pf4.loc[newx])

meandiff=diff/len(reaf)
RMS=math.sqrt(meandiff)
print()
plt.figure()
plt.plot(reaf)
plt.plot(rescaled)
plt.plot(rescaled1)
plt.plot(rescaled2)
plt.plot(rescaled3)
plt.plot(rescaled4)
plt.legend(['real','k from algorithm','k1','k2','k3','closest'])

plt.xlabel('Discrete time')
plt.ylabel('temperature [°C]')
plt.show()
