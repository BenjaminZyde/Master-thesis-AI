# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 20:28:03 2023

@author: zydeb
"""

import pandas as pd
import math
import matplotlib.pyplot as plt
import scipy
import numpy as np

def func(t,rt,dt,k):
    return (rt+((dt-rt)*np.exp(-(k)*t)))


sourcek="../rearangeddata/new 3-01/pandas-K_values-finalproof.pkl"
save="../rearangeddata/new 3-01/beter-pandas-K_values-finalproof.pkl"
source= "../rearangeddata/new 3-01/pandas-finalproof.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"


phyf = pd.read_pickle(sourcek)
real = pd.read_pickle(source)
dataid = pd.read_pickle(ids)
goodid=[]
goodk=[]

for x in range(len(dataid)):
    DoughID= dataid.iloc[x].loc['DoughID']
    sensor=dataid.iloc[x].loc['Sensor1']
    ks=phyf.query("dough_id == \"" +str(DoughID) +"\"")
    k=ks.iloc[0].loc['k_values']
    myquery="id == \"" +str(DoughID)+str(sensor)+ "\""
    temps= real.query(myquery)
    temps.reset_index(inplace=True)
    roomtemp=temps.iloc[0].loc['set_temperature']
    doughtemp=temps.iloc[0].loc['real_temperature']
    timepassed= np.arange(0,len(temps['real_temperature']),1)
    rescaled = func(timepassed,roomtemp,doughtemp,k)
    y=temps['real_temperature']
    if (y.iloc[0]==y.iloc[len(y)-1]):
        goodid.append(DoughID)
        goodk.append(k)
    else:
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress( rescaled,y)
        print("Dough_id:"+ str(DoughID)+" Rsquared: "+str(r_value))
        if (r_value>0.7):
            goodid.append(DoughID)
            goodk.append(k)
output=pd.DataFrame()
output['dough_id']=goodid
output['k_values']=goodk
output.reset_index(inplace=True, drop=True )
output.to_pickle(save)
   


