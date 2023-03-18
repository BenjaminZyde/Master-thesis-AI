# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:49:12 2022

@author: zydeb
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
import pandas as pd

#chose valid breadID
DoughID="DO100"
#chose bread 1 or bread 2
bread=2 #1/2

#static data for one doughID
source= "../rearangeddata/new 3-01/pandas-timeseries.pkl"
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
#time for each switch of stage
for x in dataprocess:
    x=x.split(",")
    if (DoughID==x[0]):
        try:
            switch1= datetime.datetime.strptime(x[1], structure)#start proof 1
            switch2= datetime.datetime.strptime(x[2], structure)#stop proof 1
            switch3= datetime.datetime.strptime(x[3], structure)#start proof 3
            switch4= datetime.datetime.strptime(x[4], structure)#end proof 3
            switch5= datetime.datetime.strptime(x[5], structure)#start bake
            switch6= datetime.datetime.strptime(x[6], structure)#end bake
        except:
            print("Invalid times")
if (switch1=="No such dough ID"):  
    raise Exception(switch1)      
#variables for the tempereature data and x values
line_list = []
tempvalues = []
x_list = []
tempxvalues = []
xvalue=0
stage=1
#get data from pkl
pf = pd.read_pickle(source)


#extract temp from data
myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid+"\""
temps =  pf.query(myquery)
for x in range (len(temps)): 
    day= datetime.datetime.strptime(temps['sampling_date'].loc[temps.index[x]], "%Y-%m-%d %H:%M:%S")
    hours = datetime.datetime.strptime(temps['sampling_time'].loc[temps.index[x]], "%H:%M:%S")
    timevalue= datetime.datetime.strptime(str(day.year)+"-"+str(day.month)+"-"+str(day.day)+" "+str(hours.hour)+":"+str(hours.minute)+":"+str(hours.second), "%Y-%m-%d %H:%M:%S")
    if (timevalue<switch1):
        stage=1
    elif (timevalue>=switch1 and timevalue<=switch2):
        if (stage==1):
            stage =2
            line_list.append(tempvalues)
            x_list.append(tempxvalues)
            tempvalues=[]
            tempxvalues=[]
    elif (timevalue>=switch2 and timevalue<=switch3):
        if (stage==2):
            stage =4
            line_list.append(tempvalues)
            x_list.append(tempxvalues)
            tempvalues=[]
            tempxvalues=[]
    elif (timevalue>=switch3 and timevalue<=switch4):
        if (stage==4):
            stage =6
            line_list.append(tempvalues)
            x_list.append(tempxvalues)
            tempvalues=[]
            tempxvalues=[]
    elif (timevalue>=switch4 and timevalue<=switch5):
        if (stage==6):
            stage =0
            line_list.append(tempvalues)
            x_list.append(tempxvalues)
            tempvalues=[]
            tempxvalues=[]
    elif (timevalue>=switch5 and timevalue<=switch6):
        if (stage==0):
            stage =7
            line_list.append(tempvalues)
            x_list.append(tempxvalues)
            tempvalues=[]
            tempxvalues=[]  
    elif (timevalue>switch6):
        if (stage==7):
            stage =8
            line_list.append(tempvalues)
            x_list.append(tempxvalues)
            tempvalues=[]
            tempxvalues=[]                 
                    
                   
    tempvalues.append(temps['temperature'].loc[temps.index[x]])
    tempxvalues.append(timevalue)                 
               
             
        
try:      
    line_list.append(tempvalues)
    x_list.append(tempxvalues)              
                    
            
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xft = matplotlib.dates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(xft)
    
    
    #plot all 4 stages
    ax.plot(x_list[0],line_list[0], color="gray")
    ax.plot(x_list[1],line_list[1], color="r")
    ax.plot(x_list[2],line_list[2], color="b")
    ax.plot(x_list[3],line_list[3], color="g")
    ax.plot(x_list[4],line_list[4], color="gray")
    ax.plot(x_list[5],line_list[5], color="black")
    ax.plot(x_list[6],line_list[6], color="gray")
    fig.legend(['NA','proof1','proof2','proof3','NA','bake','NA'])
    ax.set_xlabel('Time [hh:mm]')
    ax.set_ylabel('temperature [°C]')
    ax.set_title("core temperature bread")
    fig.show()
except:
    print("some error in data")