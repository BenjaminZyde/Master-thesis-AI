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

            

#pandas




#extract temp from data

    
#extract features
features_filtered_direct = tsfresh.extract_relevant_features( colum_value='timeseries', column_sort='timeseries')