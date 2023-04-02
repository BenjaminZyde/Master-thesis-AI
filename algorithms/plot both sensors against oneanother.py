import datetime
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

source= "../rearangeddata/new 3-01/pandas-timeseries.pkl"
ids=  "../rearangeddata/new 3-01/pandas-ids.pkl"
process= "../rearangeddata/new 3-01/process.csv"
design = "../rearangeddata/new 3-01/pandas-design.pkl"

structure="%Y-%m-%d %H:%M"
#read files

f = open(process,"r")
dataprocess=f.read()
dataprocess=dataprocess.split("\n")
f.close()
del dataprocess[0]
del dataprocess[-1]
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
#select sensorid
sensorid=""
pf = pd.read_pickle(source)
df = pd.read_pickle(design)
dataids= pd.read_pickle(ids)
dataids = dataids.reset_index()
for x in range( len(dataids)):
    DoughID=str(dataids.loc[x]['DoughID'])
    sensorid=str(dataids.loc[x]['Sensor1'])
    sensorid2=str(dataids.loc[x]['Sensor2'])
    
    line_list=[]    
    line_list2=[]
    x_list=[]  
    x_list2=[]
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
        for x in dataprocess:
            x=x.split(",")
            if (x[0]==DoughID):
                proof1starttime= datetime.datetime.strptime(x[1], structure)
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
        #1-3
    except:
        print("error in data")
    myquery="dough_id == \"" +DoughID+ "\" and sensor_id == \""+sensorid2+"\""
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
        for x in dataprocess:
            x=x.split(",")
            if (x[0]==DoughID):
                proof1starttime= datetime.datetime.strptime(x[1], structure)
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
        x_list2.append(info['sampling_moment'].tolist())
        line_list2.append(info['temperature'].tolist())
        
        #proof 2ish
        info =temps[temps['index'] >= indexproof1end]
        info =info[indexproof3start  >= temps['index']]
        x_list2.append(info['sampling_moment'].tolist())
        line_list2.append(info['temperature'].tolist())
        
        #proof 3
        info =temps[temps['index'] >= indexproof3start]
        info =info[indexbakestart >= temps['index']]
        x_list2.append(info['sampling_moment'].tolist())
        line_list2.append(info['temperature'].tolist())
        
        #bake
        info =temps[temps['index'] >= indexbakestart ]
        info =info[indexbakeend  >= temps['index']]
        x_list2.append(info['sampling_moment'].tolist())
        line_list2.append(info['temperature'].tolist())
        
        designdata =  df.query("dough_id == \"" +DoughID+ "\"")
        bulkprooftemp=float(designdata['PROOF_bulk_temp'])
        prooftemp=20
        finalprooftemp=float(designdata['PROOF_final_temp'])
        baketemp=float(designdata['BAKE_upper_temp'])
        #1-3
    except:
        print("error in data")
    try:     
        if (bulkprooftemp==5):
            x1.append(min(line_list[0]))
            y1.append(min(line_list2[0]))
        else:
            x1.append(max(line_list[0]))
            y1.append(max(line_list2[0]))
        x2.append(max(line_list[1]))
        y2.append(max(line_list2[1]))
        if (finalprooftemp==5):
            x3.append(min(line_list[2]))
            y3.append(min(line_list2[2]))
        else:
            x3.append(max(line_list[2]))
            y3.append(max(line_list2[2]))
        x4.append(max(line_list[3]))
        y4.append(max(line_list2[3]))
        
    except:
        print("error in data of DoughID "+DoughID)
try:
    fig, axs = plt.subplots(2, 2)
    
    
    axs[0, 0].scatter(x1,y1)
    axs[0, 0].set_title('proof 1')
    axs[0, 1].scatter(x2,y2)
    axs[0, 1].set_title('proof 2')
    axs[1, 0].scatter(x3,y3)
    axs[1, 0].set_title('proof 3')
    axs[1, 1].scatter(x4,y4)
    axs[1, 1].set_title('bake')
    fig.suptitle('Plot sensor 1 and sensor 2')
    fig.show()
except:
    print("error in plotting")        
