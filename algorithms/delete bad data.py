# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:50:09 2023

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

source= "../rearangeddata/new 3-01/pandas-ids.pkl"
pickles= "../rearangeddata/new 3-01/beter-pandas-ids.pkl"

bpf = pd.read_pickle(source)

bpf = bpf.drop(bpf[bpf.DoughID == "DO113"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO114"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO115"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO116"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO117"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO118"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO86"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO67"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO56"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO57"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO58"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO59"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO60"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO61"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO119"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO120"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO121"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO122"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO123"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO124"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO107"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO110"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO111"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO112"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO50"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO51"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO52"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO53"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO54"].index)
bpf = bpf.drop(bpf[bpf.DoughID == "DO55"].index)

bpf.to_pickle(pickles)