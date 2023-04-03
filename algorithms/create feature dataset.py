# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:35:11 2023

@author: zydeb
"""
import datetime
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np


def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

source= "../rearangeddata/new 3-01/pandas-timeseries.pkl"
ids=  "../rearangeddata/new 3-01/beter-pandas-ids.pkl"
process= "../rearangeddata/new 3-01/process.csv"
design = "../rearangeddata/new 3-01/pandas-design.pkl"
bakepandas = "../rearangeddata/new 3-01/pandas-bake.pkl"
bulkproofpandas = "../rearangeddata/new 3-01/pandas-bulkproof.pkl"
finalproofpandas = "../rearangeddata/new 3-01/pandas-finalproof.pkl"


structure="%Y-%m-%d %H:%M"
#read files

f = open(process,"r")
dataprocess=f.read()
dataprocess=dataprocess.split("\n")
f.close()
del dataprocess[0]
del dataprocess[-1]

#select sensorid
sensorid=""
pf = pd.read_pickle(source)
df = pd.read_pickle(design)
dataids= pd.read_pickle(ids)
dataids = dataids.reset_index()

indexbake=[]
indexbulk=[]
indexfinal=[]
settempbake=[]
settempbulk=[]
settempfinal=[]
realtempbake=[]
realtempbulk=[]
realtempfinal=[]
timestampbake=[]
timestampbulk=[]
timestampfinal=[]



for x in range( len(dataids)):
    DoughID=str(dataids.loc[x]['DoughID'])
    sensorid=str(dataids.loc[x]['Sensor1'])
               
    x_list=[]
    line_list=[]    
    
    #get data from pkl
    
    breaddesign =  df.query("dough_id == \"" +DoughID+ "\"")
    baketime=float(breaddesign['BAKE_totaltime'])
    proof3time=float(breaddesign['PROOF_final_time'])
    proof1time=float(breaddesign['PROOF_bulk_time'])
    
    #select right dataset
    myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid+"\""
    temps =  pf.query(myquery)
    temps= temps.reset_index()
    newdata=[]
    try:
        
        #select hottest point
        indexbakeend = int(temps.loc[temps['temperature'].idxmax()]['index'])
        #del temps['temperature']
        #temps['temperature'] =newdata
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
        for y in dataprocess:
            y=y.split(",")
            if (y[0]==DoughID):
                proof1starttime= datetime.datetime.strptime(y[1], structure)
        proof1starttime = nearest(temps['sampling_moment'],proof1starttime)        
        indexproof1start =  temps.query("sampling_moment == \"" + str(proof1starttime) + "\"")
        indexproof1start =    int(indexproof1start.index[0])    
        
        proof1endtime= proof1starttime + datetime.timedelta(hours=proof1time)
        proof1endtime = nearest(temps['sampling_moment'],proof1endtime)
        indexproof1end =  temps.query("sampling_moment == \"" + str(proof1endtime) + "\"")
        indexproof1end =    int(indexproof1end.index[0])
        
        
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
        
                
        designdata =  df.query("dough_id == \"" +DoughID+ "\"")
        bulkprooftemp=float(designdata['PROOF_bulk_temp'])
        prooftemp=20
        finalprooftemp=float(designdata['PROOF_final_temp'])
        baketemp=float(designdata['BAKE_upper_temp'])
        
        
        
        for y in range(len(line_list[0])):  
            indexbulk.append(DoughID+sensorid)
            settempbulk.append(bulkprooftemp)
            realtempbulk.append(line_list[0][x])
            timestampbulk.append(x_list[0][x])
            
        for y in range(len(line_list[2])): 
            indexfinal.append(DoughID+sensorid)
            settempfinal.append(finalprooftemp)         
            realtempfinal.append(line_list[2][x])
            timestampfinal.append(x_list[2][x])
            
        for y in range(len(line_list[3])):
           indexbake.append(DoughID+sensorid)
           settempbake.append(baketemp)
           realtempbake.append(line_list[3][x])
           timestampbake.append(x_list[3][x])  
    except:
        print("error1") 
    sensorid=str(dataids.loc[x]['Sensor2'])
               
    x_list=[]
    line_list=[]    
    
    #get data from pkl
    
    breaddesign =  df.query("dough_id == \"" +DoughID+ "\"")
    baketime=float(breaddesign['BAKE_totaltime'])
    proof3time=float(breaddesign['PROOF_final_time'])
    proof1time=float(breaddesign['PROOF_bulk_time'])
    
    #select right dataset
    myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid+"\""
    temps =  pf.query(myquery)
    temps= temps.reset_index()
    newdata=[]
    try:
        
        #select hottest point
        indexbakeend = int(temps.loc[temps['temperature'].idxmax()]['index'])
        #del temps['temperature']
        #temps['temperature'] =newdata
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
        for y in dataprocess:
            y=y.split(",")
            if (y[0]==DoughID):
                proof1starttime= datetime.datetime.strptime(y[1], structure)
        proof1starttime = nearest(temps['sampling_moment'],proof1starttime)        
        indexproof1start =  temps.query("sampling_moment == \"" + str(proof1starttime) + "\"")
        indexproof1start =    int(indexproof1start.index[0])    
        
        proof1endtime= proof1starttime + datetime.timedelta(hours=proof1time)
        proof1endtime = nearest(temps['sampling_moment'],proof1endtime)
        indexproof1end =  temps.query("sampling_moment == \"" + str(proof1endtime) + "\"")
        indexproof1end =    int(indexproof1end.index[0])
        
        
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
        
                
        designdata =  df.query("dough_id == \"" +DoughID+ "\"")
        bulkprooftemp=float(designdata['PROOF_bulk_temp'])
        prooftemp=20
        finalprooftemp=float(designdata['PROOF_final_temp'])
        baketemp=float(designdata['BAKE_upper_temp'])
        
        
        
        for y in range(len(line_list[0])):  
            indexbulk.append(DoughID+sensorid)
            settempbulk.append(bulkprooftemp)
            realtempbulk.append(line_list[0][x])
            timestampbulk.append(x_list[0][x])
            
        for y in range(len(line_list[2])): 
            indexfinal.append(DoughID+sensorid)
            settempfinal.append(finalprooftemp)         
            realtempfinal.append(line_list[2][x])
            timestampfinal.append(x_list[2][x])
            
        for y in range(len(line_list[3])):
           indexbake.append(DoughID+sensorid)
           settempbake.append(baketemp)
           realtempbake.append(line_list[3][x])
           timestampbake.append(x_list[3][x])  
    except:
        print("error1")
           
    
dict = {'id':indexbake,'set_temperature':settempbake,'real_temperature':realtempbake,'time_stamp':timestampbake}
pandas_bake= pd.DataFrame(dict) 
dict = {'id':indexbulk,'set_temperature':settempbulk,'real_temperature':realtempbulk,'time_stamp':timestampbulk}
pandas_bulkproof = pd.DataFrame(dict) 
dict = {'id':indexfinal,'set_temperature':settempfinal,'real_temperature':realtempfinal,'time_stamp':timestampfinal}
pandas_finalproof = pd.DataFrame(dict)     

  
pandas_bake.to_pickle(bakepandas)
pandas_bulkproof.to_pickle(bulkproofpandas)
pandas_finalproof.to_pickle(finalproofpandas)