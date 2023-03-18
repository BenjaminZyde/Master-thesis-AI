#dataframe creation
#static data for one doughID



import matplotlib
import matplotlib.pyplot as plt
import datetime
import tsfresh
import pandas as pd


source= "../data/new 3-01/dough_temperatures.csv"
pickles= "../rearangeddata/new 3-01/pandas-timeseries.pkl"

pf = pd.read_csv(source, sep=';')

del pf['TS_UPDATE']
del pf['USER']
del pf['bt_id']
del pf['request_id']
del pf['BREP']


pf.to_pickle(pickles)