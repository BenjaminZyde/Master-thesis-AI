import datetime 

filler= datetime.datetime(2000, 12, 20)

breadlink= "../data/new 9-05/bread_link.csv"
doughlink= "../data/new 9-05/dough_link.csv"

process="../rearangeddata/new 9-05/process.csv"


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

f = open(process, "w")
f.write("dough_id,Bulkproof start,Bulkproof stop,Finalproof start,Finalproof stop,Bake start,Bake stop\n")
f.close()  


for x in range(len(datadoughlink)):
    datadoughlink[x]=datadoughlink[x].split(";")
for x in range(len(databreadlink)):
    databreadlink[x]=databreadlink[x].split(";")
    
for x in range(len(datadoughlink)):
    DoughIDfound=False
    DoughID=""
    bulkproofstart=filler
    bulkproofstop=filler
    finalproofstart=filler
    finalproofstop=filler
    bakestart=filler
    bakestop=filler
    
    xdata=datadoughlink[x]
    
    DoughID=xdata[2]
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
        hour= xdata[13].split(":")
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
        hour= xdata[15].split(":")
        date=xdata[14].split(" ")
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
                
    if (DoughIDfound):
        f = open(process,"a")
        message= DoughID+","+bulkproofstart+","+bulkproofstop+","+finalproofstart+","+finalproofstop+","+bakestart+","+bakestop+"\n"
        f.write(message)
        f.close()
    else:
        f = open(process,"a")
        message= DoughID+",nothing found\n"
        f.write(message)
        f.close()