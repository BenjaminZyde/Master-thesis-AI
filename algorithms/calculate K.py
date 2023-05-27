# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:31:55 2023

@author: zydeb
"""


import math
import pandas as pd
import datetime

source= "../rearangeddata/new 3-01/pandas-finalproof.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"
process= "../rearangeddata/new 3-01/pandas-process.pkl"
save="../rearangeddata/new 3-01/pandas-K_values-finalproof.pkl"


data= pd.read_pickle(source)
dataids= pd.read_pickle(ids)
dataprocess= pd.read_pickle(process)

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
    starttime=temps.iloc[0].loc['time_stamp']  
    endtime=temps.iloc[len(temps)-1].loc['time_stamp']  
    timepassed=(endtime-starttime).total_seconds()
    doughtemp=temps.iloc[0].loc['real_temperature']
    doughtempend=temps.iloc[len(temps)-1].loc['real_temperature']
    
    closestk=0
    closesttemp=0
    temp=[]
    for z in range(1,100000,1):
        
        temp = (roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-(z/10000000)*timepassed)))
        if (abs(temp-doughtempend)<=0.001):
            closestk=z
            break
        if (abs(temp-doughtempend)<=abs(closesttemp-doughtempend)):
            closestk=z
            closesttemp=temp       
    doughids.append(DoughID)
    kvalue.append(closestk)
    
    sensor2=dataids.iloc[x].loc['Sensor2']
    if (isinstance(sensor2, float)):
        break
    myquery="id == \"" +str(DoughID)+str(sensor)+ "\""
    temps= data.query(myquery)
    temps.reset_index(inplace=True)
    roomtemp=temps.iloc[0].loc['set_temperature']
    starttime=temps.iloc[0].loc['time_stamp']  
    endtime=temps.iloc[len(temps)-1].loc['time_stamp']  
    timepassed=(endtime-starttime).total_seconds()
    doughtemp=temps.iloc[0].loc['real_temperature']
    doughtempend=temps.iloc[len(temps)-1].loc['real_temperature']
    dif=[]
    closestk=0
    closesttemp=0
    temp=[]
    for z in range(1,100000,1):
        
        temp = (roomtemp+((doughtemp-roomtemp)*math.pow(math.e,-(z/10000000)*timepassed)))
        dif.append(abs(temp-doughtempend))
        if (abs(temp-doughtempend)<=0.0001):
            closestk=z
            break
        if (abs(temp-doughtempend)<=abs(closesttemp-doughtempend)):
            closestk=z
            closesttemp=temp
            
    doughids.append(DoughID)
    kvalue.append(closestk)
    
pf =pd.DataFrame()
pf['doug_id']= doughids
pf['k_values']=kvalue

pf.to_pickle(save)

