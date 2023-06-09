import datetime
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))
def nearesttime(items, pivot):
    
    temperature= nearest(items['temperature'] ,pivot)
    moment=items[items['temperature']  >= temperature-0.00000000000001]
    moment=moment[moment['temperature']  <= temperature+0.00000000000001]
    moment = moment.reset_index()
    moment= moment.loc[0]['index']
    moment=items.loc[moment]['sampling_moment']
   
    return moment
def latesttime(items, pivot):
     
     temperature= nearest(items['temperature'] ,pivot)
     moment=items[items['temperature']  >= temperature-0.00000000000001]
     moment=moment[moment['temperature']  <= temperature+0.00000000000001]
     moment = moment.reset_index()
     moment= moment.loc[-1]['index']
     moment=items.loc[moment]['sampling_moment']
    
     return moment   
    

source= "../rearangeddata/new 9-05/pandas-timeseries.pkl"
ids=  "../rearangeddata/new 9-05/beter-pandas-ids.pkl"
process= "../rearangeddata/new 9-05/process.csv"
savefile = "../rearangeddata/new 9-05/pandas-process.pkl"
settings = "../data/new 9-05/design.csv"
structure="%Y-%m-%d %H:%M"
#read files
dataids= pd.read_pickle(ids)
dataids = dataids.reset_index()

f = open(process,"r")
processpandas = pd.read_csv(process)
settingspandas = pd.read_csv(settings,sep=";")
#get data from pkl
pf = pd.read_pickle(source)
doids=[]
startbps=[]
stopbps=[]
startfps=[]
stopfps=[]
startbs=[]
stopbs=[]


for x in range (len(dataids)):
    try:
        DoughID =  dataids.iloc[x].loc['dough_id']
        sensorid = dataids.iloc[x].loc['Sensor1']
        
        #select right dataset
        
        myquery="dough_id == \"" +str(DoughID)+ "\" and sensor_id == \""+str(sensorid)+"\""
        tem =  pf.query(myquery)
        
        samp = pd.to_datetime(tem['sampling_moment'], format=structure)
        del tem['sampling_moment']
        samp.reset_index(inplace=True,drop=True)
        temps = tem.reset_index()
        temps['sampling_moment'] =samp 
        indexbakeend = int(temps.loc[temps['temperature'].idxmax()]['index'])
        temps= temps.set_index('index')
        
        myquery="dough_id == \"" +str(DoughID)+ "\""
        times =  processpandas.query(myquery)
        times= times.reset_index()  
        
        myquery="dough_id == \"" +str(DoughID)+ "\""
        setting =  settingspandas.query(myquery)
        setting= setting.reset_index()  
        
        
        startbp=datetime.datetime.strptime(times.iloc[0].loc['Bulkproof start'],structure)
        stopbp=datetime.datetime.strptime(times.iloc[0].loc['Bulkproof stop'],structure)
        startfp=datetime.datetime.strptime(times.iloc[0].loc['Finalproof start'],structure)
        stopfp=datetime.datetime.strptime(times.iloc[0].loc['Finalproof stop'],structure)
        startb=datetime.datetime.strptime(times.iloc[0].loc['Bake start'],structure)
        stopb=datetime.datetime.strptime(times.iloc[0].loc['Bake stop'],structure)
        
        
        
        lowertime =  nearest(temps['sampling_moment'],nearest(temps['sampling_moment'],startbp) - datetime.timedelta(minutes=5))
        uppertime = nearest(temps['sampling_moment'],startbp) + datetime.timedelta(minutes=5)
        info =temps[temps['sampling_moment'] >= lowertime]
        info =info[ temps['sampling_moment'] <= uppertime]
        pivot=25
        startbp=nearesttime(info, pivot)
        
        
        lowertime =  nearest(temps['sampling_moment'],stopbp) - datetime.timedelta(minutes=5)
        uppertime = nearest(temps['sampling_moment'],stopbp) + datetime.timedelta(minutes=5)
        info =temps[temps['sampling_moment'] >= lowertime]
        info =info[ temps['sampling_moment'] <= uppertime]
        pivot=setting.iloc[0].loc['PROOF_bulk_temp']
        stopbp= nearesttime(info, pivot)
        
        
        lowertime =  nearest(temps['sampling_moment'],startfp) - datetime.timedelta(minutes=5)
        uppertime = nearest(temps['sampling_moment'],startfp) + datetime.timedelta(minutes=5)
        info =temps[temps['sampling_moment'] >= lowertime]
        info =info[ temps['sampling_moment'] <= uppertime]
        pivot=float(20)
        startfp= nearesttime(info, pivot)
        
        
        lowertime =  nearest(temps['sampling_moment'],stopfp) - datetime.timedelta(minutes=5)
        uppertime = nearest(temps['sampling_moment'],stopfp) + datetime.timedelta(minutes=5)
        info =temps[temps['sampling_moment'] >= lowertime]
        info =info[ temps['sampling_moment'] <= uppertime]
        pivot=setting.iloc[0].loc['PROOF_final_temp']
        stopfp= nearesttime(info, pivot)
        
       
        
        lowertime =  nearest(temps['sampling_moment'],startb) - datetime.timedelta(minutes=5)
        uppertime = nearest(temps['sampling_moment'],startb) + datetime.timedelta(minutes=5)
        info =temps[temps['sampling_moment'] >= lowertime]
        info =info[ temps['sampling_moment'] <= uppertime]
        pivot=setting.iloc[0].loc['PROOF_final_temp']
        startb= latesttime(info, pivot)
        
        
        
        pivot = indexbakeend
        stopb = temps.iloc[pivot].loc['sampling_moment']
        
        
        doids.append(DoughID)
        startbps.append(startbp)
        stopbps.append(stopbp)
        startfps.append(startfp)
        stopfps.append(stopfp)
        startbs.append(startb)
        stopbs.append(stopb) 
        
    except:
           print("faulty DoughID: "+str(DoughID))
        
          
        
    
  
    
dict = {'dough_id':doids,'startbulkproof':startbps,'stopbulkproof':stopbps,'startfinalproof':startfps,'stopfinalproof':stopfps,'startbake':startbs,'stopbake':stopbs}
pandassettings= pd.DataFrame(dict)     
pandassettings.to_pickle(savefile)
    
    
    
