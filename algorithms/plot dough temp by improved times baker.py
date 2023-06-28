# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:36:14 2023

@author: zydeb
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:49:12 2022

@author: zydeb
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

#chose valid breadID
DoughID="DO113"
#chose bread 1 or bread 2
bread=1 #1/2

#static data for one doughID
source= "../rearangeddata/new 3-01/pandas-timeseries.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"
process= "../rearangeddata/new 3-01/pandas-process.pkl"


#read files
dataids= pd.read_pickle(ids)

#dataids = dataids.reset_index()
pf = pd.read_pickle(source)
df = pd.read_pickle(process)

#select sensorid

temps =  dataids.query("DoughID== \"" +str(DoughID)+ "\"")
temps.reset_index(inplace=True)
if (len(temps)==0):
    raise Exception ('no such dough id')
    
if (bread ==1):
    sensorid = temps.iloc[0].loc['Sensor1']
else:
    sensorid = temps.iloc[0].loc['Sensor2']     
    



myquery="dough_id == \"" +str(DoughID)+ "\" and sensor_id == \""+str(sensorid)+"\""
temps =  pf.query(myquery)
temps= temps.reset_index()
myquery="dough_id == \"" +str(DoughID)+ "\" "
times =  df.query(myquery)
times= times.reset_index()

x_list=[]
line_list=[]

timeproof1start=times.iloc[0].loc['startbulkproof']
timeproof1end=times.iloc[0].loc['stopbulkproof']
timeproof3start=times.iloc[0].loc['startfinalproof']
timeproof3stop=times.iloc[0].loc['stopfinalproof']
timebakestart =times.iloc[0].loc['startbake']
timebakeend=times.iloc[0].loc['stopbake']


#preproof 1
info =temps[temps['sampling_moment'] < timeproof1start]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#proof 1
info =temps[temps['sampling_moment'] >= timeproof1start]
info =info[ temps['sampling_moment'] <=timeproof1end]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#proof 2ish
info =temps[temps['sampling_moment'] >=timeproof1end]
info =info[timeproof3start  >= temps['sampling_moment']]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#proof 3
info =temps[temps['sampling_moment'] >= timeproof3start]
info =info[timeproof3stop >= temps['sampling_moment']]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#bake
info =temps[temps['sampling_moment'] >= timebakestart ]
info =info[timebakeend  >= temps['sampling_moment']]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#postbake 1
info =temps[temps['sampling_moment'] > timebakeend]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())



try:      
          
                    
            
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xft = matplotlib.dates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(xft)
    
    
    #plot all 3 stages
    ax.plot(x_list[0],line_list[0], color="gray")
    ax.plot(x_list[1],line_list[1], color="r")
    ax.plot(x_list[2],line_list[2], color="gray")
    ax.plot(x_list[3],line_list[3], color="g")
    ax.plot(x_list[4],line_list[4], color="b")
    ax.plot(x_list[5],line_list[5], color="gray")
    fig.legend(['pre','proof 1','proof 2','proof 3','bake','post'])
    ax.set_xlabel('Time [hh:mm]')
    ax.set_ylabel('temperature [°C]')
    ax.set_title("core temperature bread")
    fig.show()
except:
    print("some error in data")
