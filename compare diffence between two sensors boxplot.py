import datetime
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt


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

dif1=[]
dif2=[]
dif3=[]
dif4=[]
for x in dataids:
    x=x.split(",")
    DoughID=x[0]
    if (x[4]!=""):
        sensorid1=x[4]
        sensorid2=x[5]        
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
        myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid1+"\""
        temps =  pf.query(myquery)
        savgol_filter(temps['temperature'], 10, 2)
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
        line_list2 = []
        tempvalues = []
        x_list2 = []
        tempxvalues = []
        xvalue=0
        stage=1
        myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid2+"\""
        temps =  pf.query(myquery)
        savgol_filter(temps['temperature'], 10, 2)
        for x in range (len(temps)): 
            day= datetime.datetime.strptime(temps['sampling_date'].loc[temps.index[x]], "%Y-%m-%d %H:%M:%S")
            hours = datetime.datetime.strptime(temps['sampling_time'].loc[temps.index[x]], "%H:%M:%S")
            timevalue= datetime.datetime.strptime(str(day.year)+"-"+str(day.month)+"-"+str(day.day)+" "+str(hours.hour)+":"+str(hours.minute)+":"+str(hours.second), "%Y-%m-%d %H:%M:%S")
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
        #1-3
        try:
            dif1.append(abs(max(line_list[1])-max(line_list2[1])))
            dif2.append(abs(max(line_list[2])-max(line_list2[2])))
            dif3.append(abs(max(line_list[3])-max(line_list2[3])))
            dif4.append(abs(max(line_list[5])-max(line_list2[5])))
        except:
            print("error in data of DoughID "+DoughID)
try:
    fig = plt.figure()
    
    
    ax1 =fig.add_subplot(2,2,1)
    ax1.plt.boxplot(dif1)
    ax2 =fig.add_subplot(2,2,2)
    ax2.plt.boxplot(dif2)
    ax3 =fig.add_subplot(2,2,3)
    ax3.plt.boxplot(dif3)
    ax4 =fig.add_subplot(2,2,4)
    ax4.plt.boxplot(dif3)
except:
    print("error in plotting")        