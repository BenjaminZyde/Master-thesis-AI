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


sourcek="../rearangeddata/new 9-05/output-regressor-k.pkl"
source= "../rearangeddata/new 3-01/pandas-finalproof.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"



real = pd.read_pickle(source)
dataid = pd.read_pickle(ids)
data = pd.read_pickle(sourcek)

for x in range(len(data)):
    dough_id=data.iloc[x].loc['dough_id']
    k=data.iloc[x].loc['k']
    kr=data.iloc[x].loc['prediction']
    chosenid =dataid.query("DoughID == \"" +str(dough_id) +"\"")
    sensor=chosenid.iloc[0].loc['Sensor1']
    myquery="id == \"" +str(dough_id)+str(sensor)+ "\""
    temps= real.query(myquery)
    temps.reset_index(inplace=True)
    roomtemp=temps.iloc[0].loc['set_temperature']
    doughtemp=temps.iloc[0].loc['real_temperature']
    timepassed= np.arange(0,len(temps['real_temperature']),1)
    rescaled = func(timepassed,roomtemp,doughtemp,k)
    y=temps['real_temperature']
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress( rescaled,y)
    print("Dough_id:"+ str(dough_id)+" Rsquared: "+str(r_value))
    

   


