# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:49:12 2022

@author: zydeb
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import pandas as pd
from scipy.signal import savgol_filter

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

#chose valid breadID
DoughID="DO138"
#chose bread 1 or bread 2
bread=2 #1/2

#static data for one doughID
source= "../rearangeddata/new 3-01/pandas-timeseries.pkl"
ids= "../rearangeddata/new 3-01/ids.csv"
process= "../rearangeddata/new 3-01/process.csv"
design = "../rearangeddata/new 3-01/pandas-design.pkl"

structure="%Y-%m-%d %H:%M"
#read files
f = open(ids,"r")
dataids=f.read()
dataids=dataids.split("\n")
f.close()
del dataids[0]
del dataids[-1]
f = open(process,"r")
dataprocess=f.read()
dataprocess=dataprocess.split("\n")
f.close()
del dataprocess[0]
del dataprocess[-1]

#select sensorid
sensorid=""
for x in dataids:
    x=x.split(",")
    if (DoughID==x[0]):
        if bread ==1:
            sensorid=x[4]
        else:
            sensorid=x[5]
switch1 ="No such dough ID"        
    

#get data from pkl
pf = pd.read_pickle(source)
df = pd.read_pickle(design)
breaddesign =  df.query("dough_id == \"" +DoughID+ "\"")
baketime=float(breaddesign['BAKE_totaltime'])
proof3time=float(breaddesign['PROOF_final_time'])
proof1time=float(breaddesign['PROOF_bulk_time'])

#select right dataset
myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid+"\""
temps =  pf.query(myquery)
temps= temps.reset_index()
newdata=[]
newdata= savgol_filter(temps['temperature'], 50, 5)

#select hottest point
indexbakeend = int(temps.loc[temps['temperature'].idxmax()]['index'])
del temps['temperature']
temps['temperature'] =newdata
temps = temps.set_index('index')

#select bake start and end time
bakeendtime= temps.loc[indexbakeend]['sampling_moment']
bakestarttime = bakeendtime - datetime.timedelta(minutes=baketime)
bakestarttime = nearest(temps['sampling_moment'],bakestarttime)
indexbakestart =  temps.query("sampling_moment == \"" + str(bakestarttime) + "\"")
indexbakestart =    int(indexbakestart.index[0])

#select proof3 start time
proof3starttime= bakestarttime - datetime.timedelta(hours=proof3time)
proof3starttime = nearest(temps['sampling_moment'],proof3starttime)
indexproof3start =  temps.query("sampling_moment == \"" + str(proof3starttime) + "\"")
indexproof3start =    int(indexproof3start.index[0])

#select proof1 start and end time
for x in dataprocess:
    x=x.split(",")
    if (x[0]==DoughID):
        Ineedyou= datetime.datetime.strptime(x[1], structure)
proof1starttime = nearest(temps['sampling_moment'],Ineedyou)        
indexproof1start =  temps.query("sampling_moment == \"" + str(proof1starttime) + "\"")
indexproof1start =    int(indexproof1start.index[0])    

proof1endtime= proof1starttime + datetime.timedelta(hours=proof1time)
proof1endtime = nearest(temps['sampling_moment'],proof1endtime)
indexproof1end =  temps.query("sampling_moment == \"" + str(proof1endtime) + "\"")
indexproof1end =    int(indexproof1end.index[0])

x_list=[]
line_list=[]
temps=temps.reset_index()

#proof 1
info =temps[temps['index'] >= indexproof1start]
info =info[ temps['index'] <=indexproof1end]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#proof 2ish
info =temps[temps['index'] >= indexproof1end]
info =info[indexproof3start  >= temps['index']]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#proof 3
info =temps[temps['index'] >= indexproof3start]
info =info[indexbakestart >= temps['index']]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())

#bake
info =temps[temps['index'] >= indexbakestart ]
info =info[indexbakeend  >= temps['index']]
x_list.append(info['sampling_moment'].tolist())
line_list.append(info['temperature'].tolist())






try:      
          
                    
            
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xft = matplotlib.dates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(xft)
    
    
    #plot all 3 stages
    ax.plot(x_list[0],line_list[0], color="r")
    ax.plot(x_list[1],line_list[1], color="gray")
    ax.plot(x_list[2],line_list[2], color="g")
    ax.plot(x_list[3],line_list[3], color="b")
    fig.legend(['proof1','proof 2?','proof3','bake'])
    ax.set_xlabel('Time [hh:mm]')
    ax.set_ylabel('temperature [°C]')
    ax.set_title("core temperature bread")
    fig.show()
except:
    print("some error in data")
