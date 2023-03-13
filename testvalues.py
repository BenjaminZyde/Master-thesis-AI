# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:34:59 2023

@author: zydeb
"""

import datetime 

filler= datetime.datetime(2000, 12, 20)

breadlink= "../data/new 3-01/bread_link.csv"
doughlink= "../data/new 3-01/dough_link.csv"



f = open(doughlink,"r")
datadoughlink=f.read()
datadoughlink=datadoughlink.split("\n")
f.close()
del datadoughlink[0]
del datadoughlink[-1]

f = open(breadlink,"r")
databreadlink=f.read()
databreadlink=databreadlink.split("\n")
f.close()
del databreadlink[0]
del databreadlink[-1]



for x in range(len(datadoughlink)):
    datadoughlink[x]=datadoughlink[x].split(";")
for x in range(len(databreadlink)):
    databreadlink[x]=databreadlink[x].split(";")
    DoughID="DO83"
for x in range(len(datadoughlink)):
    xdata=datadoughlink[x] 
    if(DoughID==xdata[2]):
        DoughIDfound=False
        
        bulkproofstart=filler
        bulkproofstop=filler
        finalproofstart=filler
        finalproofstop=filler
        bakestart=filler
        bakestop=filler
        
        try:
            hour= xdata[8].split(":")
            date=xdata[5].split(" ")
            date=date[0].split("-")
        except: 
            hour=["",""]
            date=["","",""]
        try:
            bulkproofstart= datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(hour[0]),int(hour[1])).strftime("%Y-%m-%d %H:%M")
        except:
            bulkproofstart=""
        try:
            hour= xdata[10].split(":")
            date=xdata[9].split(" ")
            date=date[0].split("-")
        except: 
            hour=["",""]
            date=["","",""]
        try:
            bulkproofstop= datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(hour[0]),int(hour[1])).strftime("%Y-%m-%d %H:%M")
        except:
            bulkproofstop=""
        try:
            hour= xdata[11].split(":")
            date=xdata[9].split(" ")
            date=date[0].split("-")
        except: 
            hour=["",""]
            date=["","",""]
        try:
            finalproofstart= datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(hour[0]),int(hour[1])).strftime("%Y-%m-%d %H:%M")
        except:
            finalproofstart=""
        try:
            hour= xdata[13].split(":")
            date=xdata[12].split(" ")
            date=date[0].split("-")
        except: 
            hour=["",""]
            date=["","",""]
        try:
            finalproofstop= datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(hour[0]),int(hour[1])).strftime("%Y-%m-%d %H:%M")
        except:
            finalproofstop=""
        for y in range(len(databreadlink)):
            ydata=databreadlink[y]
            if (ydata[3]==DoughID):
                DoughIDfound=True
                try:
                    hour= ydata[6].split(":")
                    date=ydata[5].split(" ")
                    date=date[0].split("-")
                except: 
                    hour=["",""]
                    date=["","",""]
                try:
                    bakestart= datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(hour[0]),int(hour[1])).strftime("%Y-%m-%d %H:%M")
                except:
                    bakestart=""
                try:
                    hour= ydata[7].split(":")
                except: 
                    hour=["",""]
                try:
                    bakestop= datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(hour[0]),int(hour[1])).strftime("%Y-%m-%d %H:%M")
                except:
                    bakestop=""
                break
        break