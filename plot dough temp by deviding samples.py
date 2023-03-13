# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:49:12 2022

@author: zydeb
"""
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import time
from calendar import timegm

#static data for one doughID
source= "../data/dough_temperatures.csv"
sensorid1="020000007E67A341"
sensorid2="B70000007E6FDD41"
doughid="DO100"

proof1=15
proof2=30
proof3=15
bake=50
samples=4096

switch1=math.floor(proof1*samples*(proof1/samples))
switch2=math.floor((proof1+proof2)*samples*((proof1+proof2)/samples))
switch3=math.floor((proof1+proof2+proof3)*samples*((proof1+proof2+proof3)/samples))

#time for each switch of stage

x1=np.arange(0,switch1,1)       #proof 1
x2=np.arange(switch1,switch2,1) #proof 2
x3=np.arange(switch2,switch3,1) #proof 3
x4=np.arange(switch3,samples,1) #bake

values1=[]
values2=[]
line_list=[]
#get data from csv file
f = open(source,"r")
data=f.read()
data=data.split("\n")

#delete noncsv values from the csv data
del data[0]
del data[-1]
#extract temp from data
for x in data:
    x= x.split(",")
    
    if (x[4]==doughid):
        sensorid = x[3]
        if (sensorid==sensorid1):
            values1.append(float(x[9]))
           
            
           
        
line_list.append(values1[0:switch1])          
line_list.append(values1[switch1:switch2])                
line_list.append(values1[switch2:switch3])         
line_list.append(values1[switch3:samples])  

#plot all 4 stages
plt.plot(x1,line_list[0], color="r")
plt.plot(x2,line_list[1], color="b")
plt.plot(x3,line_list[2], color="g")
plt.plot(x4,line_list[3], color="black")
plt.legend(['proof1','proof2','proof3','bake'])
plt.xlabel('Samplenumber', fontsize=16)
plt.ylabel('temperature [°C]', fontsize=16)

plt.show()