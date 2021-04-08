import pandas as pd
from matplotlib import pyplot as plt

#attr values
DATE = 0
DEPTH = 1
TEMP = 2
COND = 3
DO = 4
TURB = 5
CHL = 6
BATV = 7

#Open txt file and load into buffer
filename = "lakeerie_data.txt"
buffer = [] #raw data used for chart 1
data = [] #data that goes with Option A of assignment, used for chart 2
Ydata = []
Xdata = []


i=0
with open(filename) as fin:
    for line in fin:
        #Since the first two lines in the data.txt are junk we can skip them
        if(i >= 2):
            myline = line.split()
            buffer.append(myline)
        i+=1
#Scroll thru entries, append if do < 2.0 to data 
for entry in buffer:
    i=0
    match = False
    for item in entry:
        if(i==DATE):
            Xdata.append(float(item))
        if(i == DO):
            if(float(item) <= 1.99):
                match = True
                Ydata.append(float(item))
        i+=1
    if(match):
        print(entry)
        data.append(entry)


#Create visualization from entries in buffer and data ENLARGE MATLIBPLOT for better view!
plt.style.use('fivethirtyeight')
plt.title("Amount of entries for when Dissolved O2 < 2 mg/L")
plt.xlabel("Amount")
plt.ylabel("O2 Level mg/L")
bin = [-0.15, -0.10, 0.00, 0.10, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.99]
plt.hist(Ydata, bins=bin)
plt.show()

                