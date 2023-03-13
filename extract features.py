# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:55:20 2023

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
import tsfresh
import pandas as pd

#chose bread 1 or bread 2
bread=1 #1/2

#static data for one doughID
source= "../data/new 3-01/dough_temperatures.csv"
ids= "../rearangeddata/new 3-01/ids.csv"
process= "../rearangeddata/new 3-01/process.csv"


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

            
#variables for the tempereature data and x values
line_list = []
tempvalues = []
x_list = []
tempxvalues = []

#get data from csv file
f = open(source,"r")
data=f.read()
data=data.split("\n")

#pandas
collums = {'doughid and sensorid':[],'timeseries':[],'timestamp':[]}
df = pd.DataFrame(collums)


#delete noncsv values from the csv data
del data[0]
del data[-1]
#extract temp from data
for ids in dataids:
    ids = ids= ids.split(",")
    DoughID=ids[0]
    sensorid=ids[4]
    for x in data:
        x= x.split(";")
        if (x[4]==DoughID):
            if (sensorid==x[3] or sensorid==""):
                day= datetime.datetime.strptime(x[7], "%Y-%m-%d %H:%M:%S")
                hours = datetime.datetime.strptime(x[8], "%H:%M:%S")
                timevalue= datetime.datetime.strptime(str(day.year)+"-"+str(day.month)+"-"+str(day.day)+" "+str(hours.hour)+":"+str(hours.minute)+":"+str(hours.second), "%Y-%m-%d %H:%M:%S")
                df2 = pd.DataFrame({'doughid and sensorid':[DoughID+sensorid],'timeseries':[float(x[9])],'timestamp':[timevalue]})
                df = pd.concat([df,df2])
    sensorid=ids[5]
    for x in data:
        x= x.split(";")
        if (x[4]==DoughID):
            if (sensorid==x[3] or sensorid==""):
                day= datetime.datetime.strptime(x[7], "%Y-%m-%d %H:%M:%S")
                hours = datetime.datetime.strptime(x[8], "%H:%M:%S")
                timevalue= datetime.datetime.strptime(str(day.year)+"-"+str(day.month)+"-"+str(day.day)+" "+str(hours.hour)+":"+str(hours.minute)+":"+str(hours.second), "%Y-%m-%d %H:%M:%S")
                df2 = pd.DataFrame({'doughid and sensorid':[DoughID+sensorid],'timeseries':[float(x[9])],'timestamp':[timevalue]})
                df = pd.concat([df,df2])
               
    
#extract features
features_filtered_direct = tsfresh.extract_relevant_features(df,column_id='doughid and sensorid', colum_value='timeseries', column_sort='timeseries')