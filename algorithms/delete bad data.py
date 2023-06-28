# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:50:09 2023

@author: zydeb
"""

#dataframe creation
#static data for one dough_id



import matplotlib
import matplotlib.pyplot as plt
import datetime
import tsfresh
import pandas as pd
import datetime

source= "../rearangeddata/new 9-05/pandas-ids.pkl"
pickles= "../rearangeddata/new 9-05/beter-pandas-ids.pkl"

bpf = pd.read_pickle(source)

bpf = bpf.drop(bpf[bpf.dough_id == "DO50"].index)
bpf = bpf.drop(bpf[bpf.dough_id  == "DO51"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO52"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO53"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO54"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO55"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO56"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO57"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO58"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO59"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO60"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO61"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO91"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO123"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO124"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO116"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO117"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO118"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO217"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO218"].index)
bpf = bpf.drop(bpf[bpf.dough_id == "DO219"].index)



bpf.to_pickle(pickles)