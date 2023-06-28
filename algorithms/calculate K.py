# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:31:55 2023

@author: zydeb
"""


import math
import pandas as pd
import datetime
import scipy
import numpy as np


source= "../rearangeddata/new 3-01/pandas-finalproof.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"
save="../rearangeddata/new 3-01/pandas-K_values-finalproof.pkl"

def func(t,rt,dt,k):
    return (rt+((dt-rt)*np.exp(-(k)*t)))

data= pd.read_pickle(source)
dataids= pd.read_pickle(ids)

doughids=[]
kvalue=[]
for x in range(len(dataids)):
    DoughID= dataids.iloc[x].loc['DoughID']
    print(DoughID)
    
    sensor=dataids.iloc[x].loc['Sensor1']
    myquery="id == \"" +str(DoughID)+str(sensor)+ "\""
    temps= data.query(myquery)
    temps.reset_index(inplace=True)
    roomtemp=temps.iloc[0].loc['set_temperature']
    doughtemp=temps.iloc[0].loc['real_temperature']
    timepassed= np.arange(0,len(temps['real_temperature']),1)
    popt, pcov = scipy.optimize.curve_fit(func, timepassed  , temps['real_temperature'],bounds=([roomtemp-0.0000001,doughtemp-0.0000001,0.], [roomtemp+0.0000001,doughtemp+0.0000001,0.1]))
    
    
    doughids.append(DoughID)
    kvalue.append(popt[2])
    
    sensor2=dataids.iloc[x].loc['Sensor2']
    if (isinstance(sensor2, float)):
        break
    else:
        myquery="id == \"" +str(DoughID)+str(sensor)+ "\""
        temps= data.query(myquery)
        temps.reset_index(inplace=True)
        temps= data.query(myquery)
        temps.reset_index(inplace=True)
        roomtemp=temps.iloc[0].loc['set_temperature']
        doughtemp=temps.iloc[0].loc['real_temperature']
        timepassed= np.arange(0,len(temps['real_temperature']),1)
        
        popt, pcov = scipy.optimize.curve_fit(func, timepassed  , temps['real_temperature'],bounds=([roomtemp-0.0000001,doughtemp-0.0000001,0.], [roomtemp+0.0000001,doughtemp+0.0000001,0.1]))
        
        doughids.append(DoughID)
        kvalue.append(popt[2])
    
pf =pd.DataFrame()
pf['dough_id']= doughids
pf['k_values']=kvalue

pf.to_pickle(save)

