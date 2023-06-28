# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:07:01 2023

@author: zydeb
"""
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy

def func(t,rt,dt,k):
    return (rt+((dt-rt)*np.exp(-(k)*t)))


sourcek="../rearangeddata/new 3-01/pandas-K_values-finalproof.pkl"
source= "../rearangeddata/new 3-01/pandas-finalproof.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"


phyf = pd.read_pickle(sourcek)
real = pd.read_pickle(source)
dataid = pd.read_pickle(ids)

dough_id="DO112"

chosenid =dataid.query("DoughID == \"" +str(dough_id) +"\"")
sensor=chosenid.iloc[0].loc['Sensor1']
ks=phyf.query("dough_id == \"" +str(dough_id) +"\"")
k=ks.iloc[0].loc['k_values']

myquery="id == \"" +str(dough_id)+str(sensor)+ "\""
temps= real.query(myquery)
temps.reset_index(inplace=True)
roomtemp=temps.iloc[0].loc['set_temperature']
doughtemp=temps.iloc[0].loc['real_temperature']
timepassed= np.arange(0,len(temps['real_temperature']),1)
y=temps['real_temperature']
rescaled = func(timepassed,roomtemp,doughtemp,k)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(y, rescaled)
roomt=[roomtemp]*len(temps['real_temperature'])
print(r_value)
plt.figure()
plt.plot(y)
plt.plot(rescaled)
plt.plot(roomt)
plt.title("Dough_id: "+ str(dough_id))
plt.xlabel('Discrete time')
plt.ylabel('temperature [°C]')
plt.legend(['real','physics','room temperature'])
plt.show()
