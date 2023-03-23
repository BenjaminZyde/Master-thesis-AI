# -*- coding: utf-8 -*-


import matplotlib
import matplotlib.pyplot as plt
import datetime
import tsfresh
import pandas as pd


source= "../data/new 3-01/design.csv"
pickles= "../rearangeddata/new 3-01/pandas-design.pkl"

pf = pd.read_csv(source, sep=';')

del pf['TS_UPDATE']
del pf['USER']
del pf['DoE_id']
del pf['BTno']
del pf['RelWeek']
del pf['RelDay']
del pf['FORM_sourdough_conc']
del pf['FORM_water_conc']
del pf['FORM_water_temp']
del pf['FORM_yeast_conc']
del pf['MIX_phase2_time']
del pf['MIX_intensity']
del pf['MIX_start_wd']
del pf['MIX_start_t']
del pf['PROOF_bulk_start_t']
del pf['PROOF_bulk_end_wd']
del pf['PROOF_bulk_end_t']
del pf['PROOF_final_start_t']
del pf['PROOF_final_end_wd']
del pf['PROOF_final_end_t']
del pf['BAKE_start_t']
del pf['BAKE_end_t']
del pf['BAKE_etage']
del pf['ActWeek']
del pf['ActYear']
del pf['ActDate_start']


pf.to_pickle(pickles)
