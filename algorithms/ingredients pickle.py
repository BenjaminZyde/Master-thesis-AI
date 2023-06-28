# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:02:16 2023

@author: zydeb
"""
import pandas as pd

design = "../data/new 9-05/ingredients_conc_perc.csv"
ingredients = "../rearangeddata/new 9-05/ingredients.pkl"
ing=   pd.read_csv(design,delimiter=(";"))

flour=[]
sourdough=[]
ingredient = pd.DataFrame()

ing.dropna(axis=0,subset=['Water'],inplace=True)
for x in range(len(ing)):
    flour.append(float(ing.iloc[x].loc['Flour'])+float(ing.iloc[x].loc['Whole meal flour']))
    sourdough.append(float(ing.iloc[x].loc['Sourdough'])+float(ing.iloc[x].loc['Sourdough blend']))

del ing['Flour']
del ing['Whole meal flour']
del ing['Sourdough']
del ing['Sourdough blend']
ing['Flour']=flour
ing['Sourdough']=sourdough
ingredient.reset_index()


ing.to_pickle(ingredients)