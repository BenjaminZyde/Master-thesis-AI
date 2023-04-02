# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:54:34 2023

@author: zydeb
"""

#dataframe creation
#static data for one doughID



import matplotlib
import matplotlib.pyplot as plt
import datetime
import tsfresh
import pandas as pd
import datetime

source= "../rearangeddata/new 3-01/IDs.csv"
pickles= "../rearangeddata/new 3-01/pandas-ids.pkl"

pf = pd.read_csv(source, sep=',')




pf.to_pickle(pickles)