

import matplotlib
import matplotlib.pyplot as plt
import datetime
import tsfresh
import pandas as pd

#chose bread 1 or bread 2


#static data for one doughID
source= "../rearangeddata/new 3-01/pandas-timeseries.pkl"
ids=  "../rearangeddata/new 3-01/pandas-ids.pkl"
process= "../rearangeddata/new 3-01/process.csv"


structure="%Y-%m-%d %H:%M"
#read files

f = open(process,"r")
dataprocess=f.read()
dataprocess=dataprocess.split("\n")
f.close()
del dataprocess[0]
del dataprocess[-1]
dataids= pd.read_pickle(ids)
dataids = dataids.reset_index()
pf = pd.read_pickle(source)
pf['newindex'] = pf['dough_id']+pf['sensor_id']           
#pf = pf.set_index('newindex')




#extract temp from data

    
#extract features
features_filtered_direct = tsfresh.extract_features(pf, column_id="newindex")