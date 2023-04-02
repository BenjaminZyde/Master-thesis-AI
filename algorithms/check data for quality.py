# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:09:42 2023

@author: zydeb
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import pandas as pd
from scipy.signal import savgol_filter

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

def getmoments(DoughID,sensorid,df,pf,dataprocess):
    breaddesign =  df.query("dough_id == \"" +DoughID+ "\"")
    baketime=float(breaddesign['BAKE_totaltime'])
    proof3time=float(breaddesign['PROOF_final_time'])
    proof1time=float(breaddesign['PROOF_bulk_time'])

    #select right dataset
    myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid+"\""
    temps =  pf.query(myquery)
    temps= temps.reset_index()
    

    #select hottest point
    indexbakeend = int(temps.loc[temps['temperature'].idxmax()]['index'])
    del temps['temperature']
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
    times=[proof1starttime,proof1endtime,proof3starttime,bakestarttime,bakeendtime]
    return times
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


#get data from pkl
pf = pd.read_pickle(source)
df = pd.read_pickle(design)

good=[]
average=[]
bad=[]
somethingelse=[]
#code
for x in dataids:
    x=x.split(",")
    DoughID=x[0]
    sensorid=x[4]
    if (sensorid !=""):
        times=getmoments(DoughID,sensorid,df,pf,dataprocess)
    sensorid2=x[5]    
    if (sensorid2 !=""):
        times2=getmoments(DoughID,sensorid2,df,pf,dataprocess)
    difference1 = times[2]-times[1]
    difference2 = times2[2]-times2[1]
    limit1=datetime.timedelta(minutes=50)
    limit2= datetime.timedelta(minutes=30)
    limit3= datetime.timedelta(minutes=15)
    limit4= datetime.timedelta(minutes=0)
    if (difference1>=limit1):
        bad.append(DoughID +"-"+ sensorid)
    elif (difference1<limit1 and difference1>=limit2):
        average.append(DoughID +"-"+  sensorid)
    elif (difference1<limit2 and difference1>=limit3):
        good.append(DoughID +"-"+  sensorid)
    elif (difference1<limit3 and difference1>=limit4):
        average.append(DoughID +"-"+  sensorid)
    elif (difference1<=limit4):
        bad.append(DoughID +"-"+  sensorid)
        
        
    if (difference2>=limit1):
        bad.append(DoughID +"-"+ sensorid2)
    elif (difference2<limit1 and difference2>=limit2):
        average.append(DoughID +"-"+  sensorid2)
    elif (difference2<limit2 and difference2>=limit3):
        good.append(DoughID +"-"+  sensorid2)
    elif (difference2<limit3 and difference2>=limit4):
        average.append(DoughID +"-"+  sensorid2)
    elif (difference2<=limit4):
        bad.append(DoughID +"-"+  sensorid2)
    
alldata = len(good) + len(bad) + len(average) + len(somethingelse)
print("Good data")
print("Amount: " + str(len(good)))
print("Percentage: " + str(len(good)/alldata *100))

print("Average data")
print("Amount: " + str(len(average)))
print("Percentage: " + str(len(average)/alldata *100))

print("Bad data")
print("Amount: " +str( len(bad)))
print("Percentage: " + str(len(bad)/alldata *100))

print("other data")
print("Amount: " + str(len(somethingelse)))
print("Percentage: " + str(len(somethingelse)/alldata *100))

datasorted= "../rearangeddata/new 3-01/datasorted.csv"
f = open(datasorted,"w")
f.write("Good \n")
for x in range(len(good)):
    f.write(good[x]+"\n")
f.write("Average \n")
for x in range(len(average)):
    f.write(average[x]+"\n")
f.write("Bad \n")
for x in range(len(bad)):
    f.write(bad[x]+"\n")
f.write("other \n")
for x in range(len(somethingelse)):
    f.write(somethingelse[x]+"\n")
f.close()