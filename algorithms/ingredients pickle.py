# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:02:16 2023

@author: zydeb
"""
import pandas as pd

design = "../data/new 3-01/design.csv"
ingredients = "../rearangeddata/new 3-01/ingredients.pkl"
datadesign =   pd.read_csv(design,delimiter=(";"))


ingredient = pd.DataFrame()

ingredient['dough_id'] = datadesign['dough_id']
ingredient['sourdough'] = datadesign['FORM_sourdough_conc']
ingredient['water'] = datadesign['FORM_water_conc']



ingredient.dropna(axis=0,subset=['dough_id'],inplace=True)
ingredient.reset_index()


ingredient.to_pickle(ingredients)