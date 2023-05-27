



doughlink= "../data/new 9-05/dough_link.csv"
breadlink= "../data/new 9-05/bread_link.csv"
doughtemp= "../data/new 9-05/dough_temperatures.csv"

idlink="../rearangeddata/new 9-05/IDs.csv"

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

f = open(doughtemp,"r")
datadoughtemp=f.read()
datadoughtemp=datadoughtemp.split("\n")
f.close()
del datadoughtemp[0]
del datadoughtemp[-1]

f = open(idlink, "w")
f.write("dough_id,BakeTest,MakeID,BakeID,Sensor1,Sensor2,FormID\n")
f.close()  




for x in range(len(datadoughlink)):
    datadoughlink[x]=datadoughlink[x].split(";")
for x in range(len(databreadlink)):
    databreadlink[x]=databreadlink[x].split(";")
for x in range(len(datadoughtemp)):
    datadoughtemp[x]=datadoughtemp[x].split(",")



for x in range(len(datadoughlink)):
    xdata=datadoughlink[x]
    DoughID=""
    FormID=""
    MakeID=""
    BakeTest=""
    BakeID=""
    SensorID1=""
    SensorID2=""
    
    DoughID=xdata[2]
    FormID=xdata[3]
    MakeID=xdata[4]
    
    for y in range(len(databreadlink)):
        ydata=databreadlink[y]
        if (ydata[3]==DoughID):
            BakeTest=ydata[2]
            BakeID=ydata[4]
            for z in range(len(datadoughtemp)):
                zdata=datadoughtemp[z]
                if (zdata[4]==DoughID and SensorID1=="" and SensorID2==""):
                    SensorID1=zdata[3]
                elif(zdata[4]==DoughID and SensorID2=="" and zdata[3]!=SensorID1):
                     SensorID2=zdata[3]
                if (SensorID2!=""):
                    break
    f = open(idlink,"a")
    message= DoughID+","+BakeTest+","+MakeID+","+BakeID+","+SensorID1+","+SensorID2+","+FormID+"\n"
    f.write(message)
    f.close()

