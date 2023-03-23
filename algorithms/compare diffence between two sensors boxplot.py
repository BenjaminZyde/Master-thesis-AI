import datetime
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

#static data for one doughID
source= "../rearangeddata/new 3-01/pandas-timeseries.pkl"
ids= "../rearangeddata/new 3-01/ids.csv"
process= "../rearangeddata/new 3-01/process.csv"
design= "../rearangeddata/new 3-01/pandas-design.pkl"

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

dif1=[]
dif2=[]
dif3=[]
dif4=[]
#get data from pkl
pf = pd.read_pickle(source)
designframe = pd.read_pickle(design)
for x in dataids:
    x=x.split(",")
    DoughID=x[0]
    if (x[4]!=""):
        sensorid1=x[4]
        sensorid2=x[5]  
        for processdata in dataprocess:
            processdata=processdata.split(",")
            if (DoughID==processdata[0]):
                try:
                    switch1= datetime.datetime.strptime(processdata[1], structure)#start proof 1
                    switch2= datetime.datetime.strptime(processdata[2], structure)#stop proof 1
                    switch3= datetime.datetime.strptime(processdata[3], structure)#start proof 3
                    switch4= datetime.datetime.strptime(processdata[4], structure)#end proof 3
                    switch5= datetime.datetime.strptime(processdata[5], structure)#start bake
                    switch6= datetime.datetime.strptime(processdata[6], structure)#end bake
                except:
                    print("Invalid times")
        
        #variables for the tempereature data and x values
        line_list = []
        tempvalues = []
        x_list = []
        tempxvalues = []
        
        #extract temp from data
        myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid1+"\""
        temps =  pf.query(myquery)
        temps = temps.reset_index()
        line_list0 = list(savgol_filter(temps['temperature'], 50, 5))
        del temps['temperature']
        
        temps['temperature'] = line_list0
        timespandas= pd.DataFrame(x_list)
        for x in range (len(temps)): 
            timevalue= temps.iloc[x]['sampling_moment']
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
        
        
        line_list2 = []
        tempvalues = []
        x_list2 = []
        tempxvalues = []
        xvalue=0
        stage=1
        myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid2+"\""
        temps =  pf.query(myquery)
        temps = temps.reset_index()
        line_list0 = list(savgol_filter(temps['temperature'], 50, 5))
        del temps['temperature']
        temps['temperature'] = line_list0
        timespandas= pd.DataFrame(x_list)
        for x in range (len(temps)): 
            timevalue= temps.iloc[x]['sampling_moment']
            if (timevalue<switch1):
                stage=1
            elif (timevalue>=switch1 and timevalue<=switch2):
                if (stage==1):
                    stage =2
                    line_list2.append(tempvalues)
                    x_list2.append(tempxvalues)
                    tempvalues=[]
                    tempxvalues=[]
            elif (timevalue>=switch2 and timevalue<=switch3):
                if (stage==2):
                    stage =4
                    line_list2.append(tempvalues)
                    x_list2.append(tempxvalues)
                    tempvalues=[]
                    tempxvalues=[]
            elif (timevalue>=switch3 and timevalue<=switch4):
                if (stage==4):
                    stage =6
                    line_list2.append(tempvalues)
                    x_list2.append(tempxvalues)
                    tempvalues=[]
                    tempxvalues=[]
            elif (timevalue>=switch4 and timevalue<=switch5):
                if (stage==6):
                    stage =0
                    line_list2.append(tempvalues)
                    x_list2.append(tempxvalues)
                    tempvalues=[]
                    tempxvalues=[]
            elif (timevalue>=switch5 and timevalue<=switch6):
                if (stage==0):
                    stage =7
                    line_list2.append(tempvalues)
                    x_list2.append(tempxvalues)
                    tempvalues=[]
                    tempxvalues=[]  
            elif (timevalue>switch6):
                if (stage==7):
                    stage =8
                    line_list2.append(tempvalues)
                    x_list2.append(tempxvalues)
                    tempvalues=[]
                    tempxvalues=[]       
            tempvalues.append(temps['temperature'].loc[temps.index[x]])
            tempxvalues.append(timevalue) 
        
        designdata =  designframe.query("dough_id == \"" +DoughID+ "\"")
        bulkprooftemp=float(designdata['PROOF_bulk_temp'])
        prooftemp=20
        finalprooftemp=float(designdata['PROOF_final_temp'])
        baketemp=float(designdata['BAKE_upper_temp'])
        #1-3
        try:       
            if (bulkprooftemp==5):
                dif1.append(abs(min(line_list[1])-float(bulkprooftemp)))
            else:
                dif1.append(abs(max(line_list[1])-float(bulkprooftemp)))
            dif2.append(abs(max(line_list[2])-max(line_list2[2])))
            dif3.append(abs(max(line_list[3])-max(line_list2[3])))
            dif4.append(abs(max(line_list[5])-max(line_list2[5])))
        except:
            print("error in data of DoughID "+DoughID)
try:
    fig, axs = plt.subplots(2, 2)
    
    
    axs[0, 0].boxplot(dif1)
    axs[0, 0].set_title('proof 1')
    axs[0, 1].boxplot(dif2)
    axs[0, 1].set_title('proof 2')
    axs[1, 0].boxplot(dif3)
    axs[1, 0].set_title('proof 3')
    axs[1, 1].boxplot(dif4)
    axs[1, 1].set_title('bake')
    fig.suptitle('Boxplot sensor 1 and sensor 2')
    fig.show()
except:
    print("error in plotting")        