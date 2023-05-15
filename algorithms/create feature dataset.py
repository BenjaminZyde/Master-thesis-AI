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
process= "../rearangeddata/new 3-01/pandas-process.pkl"
design = "../rearangeddata/new 3-01/pandas-design.pkl"
bakepandas = "../rearangeddata/new 3-01/pandas-bake.pkl"
bulkproofpandas = "../rearangeddata/new 3-01/pandas-bulkproof.pkl"
finalproofpandas = "../rearangeddata/new 3-01/pandas-finalproof.pkl"
#finalproofseries = "../rearangeddata/new 3-01/series-finalproof.pkl"

structure="%Y-%m-%d %H:%M"
#read files

processdata = pd.read_pickle(process)
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
#testerindex=[]
#testertemp=[]


for x in range( len(dataids)):
    DoughID=str(dataids.loc[x]['DoughID'])
    sensorid=str(dataids.loc[x]['Sensor1'])
               
    x_list=[]
    line_list=[]    
    
    
    
    #select right dataset
    myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid+"\""
    temps =  pf.query(myquery)
    temps= temps.reset_index()
    
    myquery="dough_id == \"" +DoughID+ "\" "
    times =  processdata.query(myquery)
    times= times.reset_index()
    
    timeproof1start=times.loc[0]['startbulkproof']
    timeproof1end=times.loc[0]['stopbulkproof']
    timeproof3start=times.loc[0]['startfinalproof']
    timeproof3stop=times.loc[0]['stopfinalproof']
    timebakestart =times.loc[0]['startbake']
    timebakeend=times.loc[0]['stopbake']
    newdata=[]
    try:
        
        
        
        
        temps=temps.reset_index()
        
        #proof 1
        info =temps[temps['sampling_moment'] >= timeproof1start]
        info =info[ temps['sampling_moment'] <=timeproof1end]
        x_list.append(info['sampling_moment'].tolist())
        line_list.append(info['temperature'].tolist())
        
        #proof 2ish
        info =temps[temps['sampling_moment'] >= timeproof1end]
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
        
                
        designdata =  df.query("dough_id == \"" +DoughID+ "\"")
        bulkprooftemp=float(designdata['PROOF_bulk_temp'])
        prooftemp=20
        finalprooftemp=float(designdata['PROOF_final_temp'])
        baketemp=float(designdata['BAKE_upper_temp'])
        
        
        try:
            for y in range(len(line_list[0])):  
                realtempbulk.append(line_list[0][y])
                timestampbulk.append(x_list[0][y])
                indexbulk.append(DoughID+sensorid)
                settempbulk.append(bulkprooftemp)
        except:
            print("error3")    
        try:    
            for y in range(len(line_list[2])): 
                indexfinal.append(DoughID+sensorid)
                settempfinal.append(finalprooftemp)         
                realtempfinal.append(line_list[2][y])
                timestampfinal.append(x_list[2][y])
        except:
            print("error3")
       
        try:     
            for y in range(len(line_list[3])):
               indexbake.append(DoughID+sensorid)
               settempbake.append(baketemp)
               realtempbake.append(line_list[3][y])
               timestampbake.append(x_list[3][y]) 
        except:
            print("error3")
    except:
        print("error1") 
    sensorid=str(dataids.loc[x]['Sensor2'])
               
    x_list=[]
    line_list=[]    
    
    
    
    #select right dataset
    myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid+"\""
    temps =  pf.query(myquery)
    temps= temps.reset_index()
    newdata=[]
    try:
        
        temps=temps.reset_index()
        
        #proof 1
        info =temps[temps['sampling_moment'] >= timeproof1start]
        info =info[ temps['sampling_moment'] <=timeproof1end]
        x_list.append(info['sampling_moment'].tolist())
        line_list.append(info['temperature'].tolist())
        
        #proof 2ish
        info =temps[temps['sampling_moment'] >= timeproof1end]
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
                
        designdata =  df.query("dough_id == \"" +DoughID+ "\"")
        bulkprooftemp=float(designdata['PROOF_bulk_temp'])
        prooftemp=20
        finalprooftemp=float(designdata['PROOF_final_temp'])
        baketemp=float(designdata['BAKE_upper_temp'])
        
        
        try:
            for y in range(len(line_list[0])):
                timestampbulk.append(x_list[0][y]) 
                realtempbulk.append(line_list[0][y])
                settempbulk.append(bulkprooftemp)
                indexbulk.append(DoughID+sensorid)
        except:
            print("error3")  
        try:
            for y in range(len(line_list[2])): 
                indexfinal.append(DoughID+sensorid)
                settempfinal.append(finalprooftemp)         
                realtempfinal.append(line_list[2][y])
                timestampfinal.append(x_list[2][y])
        except:
            print("error3") 
        #testerindex.append(DoughID+sensorid)
        #testertemp.append(finalprooftemp) 
        try:
            for y in range(len(line_list[3])):
               indexbake.append(DoughID+sensorid)
               settempbake.append(baketemp)
               realtempbake.append(line_list[3][y])
               timestampbake.append(x_list[3][y])  
        except:
              print("error3") 
    except:
        print("error2")
           
    
dict = {'id':indexbake,'set_temperature':settempbake,'real_temperature':realtempbake,'time_stamp':timestampbake}
pandas_bake= pd.DataFrame(dict) 
dict = {'id':indexbulk,'set_temperature':settempbulk,'real_temperature':realtempbulk,'time_stamp':timestampbulk}
pandas_bulkproof = pd.DataFrame(dict) 
dict = {'id':indexfinal,'set_temperature':settempfinal,'real_temperature':realtempfinal,'time_stamp':timestampfinal}
pandas_finalproof = pd.DataFrame(dict)     

#testerseries=pd.Series(testertemp)
#testerseries=testerseries.set_axis(testerindex)



  
pandas_bake.to_pickle(bakepandas)
pandas_bulkproof.to_pickle(bulkproofpandas)
pandas_finalproof.to_pickle(finalproofpandas)
#testerseries.to_pickle(finalproofseries)