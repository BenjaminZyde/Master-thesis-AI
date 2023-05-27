#dataframe creation
#static data for one doughID



import matplotlib
import matplotlib.pyplot as plt
import datetime
import tsfresh
import pandas as pd
import datetime

source= "../data/new 9-05/dough_temperatures.csv"
pickles= "../rearangeddata/new 9-05/pandas-timeseries.pkl"

pf = pd.read_csv(source, sep=',')

del pf['TS_UPDATE']
del pf['USER']
del pf['bt_id']
del pf['request_id']
del pf['BREP']

days=[]
for x in range( len(pf)):
    day= datetime.datetime.strptime(pf['sampling_date'].loc[pf.index[x]], "%m/%d/%Y")
    hours = datetime.datetime.strptime(pf['sampling_time'].loc[pf.index[x]], "%H:%M:%S")
    timevalue= datetime.datetime.strptime(str(day.year)+"-"+str(day.month)+"-"+str(day.day)+" "+str(hours.hour)+":"+str(hours.minute)+":"+str(hours.second), "%Y-%m-%d %H:%M:%S")   
    days.append(timevalue)
del pf['sampling_date']
del pf['sampling_time']

pf['sampling_moment']=days


pf.to_pickle(pickles)