# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:48:26 2023

@author: zydeb
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


sourcek  ="../rearangeddata/new 3-01/beter-pandas-K_values-finalproof.pkl"



dataset = pd.read_pickle(sourcek)
