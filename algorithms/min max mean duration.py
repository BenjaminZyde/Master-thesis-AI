# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:03:45 2023

@author: zydeb
"""
import pandas as pd
import datetime

source= "../rearangeddata/new 3-01/pandas-finalproof.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"
save="../rearangeddata/new 3-01/pandas-minmax-finalproof.pkl"

data= pd.read_pickle(source)
dataids= pd.read_pickle(ids)


duration=[]
starttemp=[]
settemp=[]
mins=[]
maxs=[]
means=[]
for x in range(len(ids)):
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
    
    minimum = temps['real_temperature'].min()
    maximum = temps['real_temperature'].max()
    mean = temps['real_temperature'].mean()
    
    
    
    duration.append(timepassed)
    starttemp.append(doughtemp)
    settemp.append(roomtemp)
    mins.append(minimum)
    maxs.append(maximum)
    means.append(mean)
pf = pd.DataFrame()

pf['duration'] = duration
pf['starttemp'] = starttemp
pf['settemp'] = settemp
pf['min'] = mins
pf['max'] = maxs
pf['mean'] = means


pf.to_pickle(save)



