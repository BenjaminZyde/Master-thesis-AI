# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:11:27 2023

@author: zydeb
"""





bake= "../data/new 9-05/bake.csv"
make= "../data/new 9-05/make.csv"

ids="../rearangeddata/new 9-05/IDs.csv"
process="../rearangeddata/new 9-05/process.csv"

settings="../rearangeddata/new 9-05/settings.csv"



f = open(make,"r")
datamake=f.read()
datamake=datamake.split("\n")
f.close()
del datamake[0]
del datamake[-1]

f = open(bake,"r")
databake=f.read()
databake=databake.split("\n")
f.close()
del databake[0]
del databake[-1]

f = open(ids,"r")
dataids=f.read()
dataids=dataids.split("\n")
f.close()
del dataids[0]
del dataids[-1]

f = open(settings,"w")
f.write("dough ID, proof 1 temp, proof 1 rel hum, proof 2 temp, proof 2 rel hum, proof 3 temp, proof 3 rel hum, bake temp\n")
f.close()

for x in dataids:
    
    prooftempi=0
    prooftempii=0
    prooftempiii=0
    proofhumi=0
    proofhumii=0
    proofhumiii=0
    baketemp=0
    
    x=x.split(",")
    
    doughid=x[0]
    makeid=x[2]
    bakeid=x[3]
    for bake in databake:
        bake=bake.split(";")
        if (bake[2]==bakeid):
            if (bake[3]=="BAKE_temperature_upper"):
                baketemp=int(bake[6])
            for make in datamake:
                make= make.split(";")
                make.append(5)
                make.append(5)
                if (make[2]==makeid):
                    if (make[3]=="PROOF_temperature"):
                        if (make[4]=="2"):
                            prooftempi=make[6]
                        else:
                            prooftempii=make[6]
                    if (make[3]=="PROOF_temp"):    
                        prooftempiii=make[6]
                    if (make[3]=="PROOF_rel_humidity"):
                        if (make[4]=="2"):
                            proofhumi=make[6]
                        elif (make[4]=="4"):
                            proofhumii=make[6]
                        elif(make[4]=="6"):
                            proofhumiii=make[6]
    f = open(settings,"a")
    f.write(str(doughid)+","+str(prooftempi)+","+str(proofhumi)+","+str(prooftempii)+","+str(proofhumii)+","+str(prooftempiii)+","+str(proofhumiii)+","+str(baketemp)+"\n")
    f.close()
                            