# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:01:44 2023

@author: zydeb
"""



import matplotlib
import matplotlib.pyplot as plt
import datetime
import statistics


#static data for one doughID
source= "../data/new 3-01/dough_temperatures.csv"
ids= "../rearangeddata/new 3-01/ids.csv"
process= "../rearangeddata/new 3-01/process.csv"
settings= "../rearangeddata/new 3-01/settings.csv"


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
f = open(settings,"r")
datasettings=f.read()
datasettings=datasettings.split("\n")
f.close()
del datasettings[0]
del datasettings[-1]

            
#variables for the tempereature data and x values
line_list = []
tempvalues = []
x_list = []
tempxvalues = []
xvalue=0
stage=1

#get data from csv file
f = open(source,"r")
data=f.read()
data=data.split("\n")




#temp array for timeseries array=[]
differencesproof1=[]
differencesproof3=[]
#delete noncsv values from the csv data
del data[0]
del data[-1]
#extract temp from data
for ids in dataids:
    ids=ids.split(",")
    DoughID=ids[0]
    sensorid=ids[4]
    for x in dataprocess:
        x= x.split(",")
        if (x[0]==DoughID):
            try:
                switch1= datetime.datetime.strptime(x[1], structure)#start proof 1
                switch2= datetime.datetime.strptime(x[2], structure)#stop proof 1
                switch3= datetime.datetime.strptime(x[3], structure)#start proof 3
                switch4= datetime.datetime.strptime(x[4], structure)#end proof 3
                switch5= datetime.datetime.strptime(x[5], structure)#start bake
                switch6= datetime.datetime.strptime(x[6], structure)#end bake
            except:
                print("I broke at line 79 DoughID:"+DoughID)
    for x in datasettings:
        x=x.split(",")
        if (DoughID==x[0]):   
            prooftempi=x[1]
            prooftempii=x[2]
            prooftempiii=x[3]
            proofhumi=x[4]
            proofhumii=x[5]
            proofhumiii=x[6]
            baketemp=x[7]            
    for x in data:
        x= x.split(";")
        if (x[4]==DoughID):
            
            day= datetime.datetime.strptime(x[7], "%Y-%m-%d %H:%M:%S")
            hours = datetime.datetime.strptime(x[8], "%H:%M:%S")
            timevalue= datetime.datetime.strptime(str(day.year)+"-"+str(day.month)+"-"+str(day.day)+" "+str(hours.hour)+":"+str(hours.minute)+":"+str(hours.second), "%Y-%m-%d %H:%M:%S")
            if (sensorid==x[3] or sensorid==""):
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
                        
                        settings=[]
                elif (timevalue>=switch3 and timevalue<=switch4):
                    if (stage==4):
                        stage =6
                        line_list.append(tempvalues)
                        x_list.append(tempxvalues)
                        tempvalues=[]
                        tempxvalues=[]
                        
                        settings=[]
                elif (timevalue>=switch4 and timevalue<=switch5):
                    if (stage==6):
                        stage =0
                        line_list.append(tempvalues)
                        x_list.append(tempxvalues)
                        tempvalues=[]
                        tempxvalues=[]
                        
                        settings=[]
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
                        
                tempvalues.append(float(x[9]))
                tempxvalues.append(timevalue) 
    
       
    #all data collected
    #line_list[1] ==== prooftempi
    #line_list[3] ==== prooftempiii
    try:
        differencesproof1.append(abs(float(max(line_list[1]))-float(prooftempi)))
        differencesproof3.append(abs(float(max(line_list[3]))-float(prooftempiii)))
    except:
        print("some error in data")
    

print("The maximum difference in themperature between settings and real temp for proof 1 is:\n"+ str(max(differencesproof1)) )
print("The minimum difference in themperature between settings and real temp for proof 1 is:\n"+ str(min(differencesproof1)) )
print("The mean difference in themperature between settings and real temp for proof 1 is:\n"+ str(statistics.mean(differencesproof1)) )
print("The maximum difference in themperature between settings and real temp for proof 3 is:\n"+ str(max(differencesproof3)) )
print("The minimum difference in themperature between settings and real temp for proof 3 is:\n"+ str(min(differencesproof3)) )
print("The mean difference in themperature between settings and real temp for proof 3 is:\n"+ str(statistics.mean(differencesproof3)) )