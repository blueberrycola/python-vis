
#Open txt file and load into buffer
filename = "lakeerie_data.txt"
buffer = [] #raw data moved to list
data = [] #data that goes with Option A of assignment


i=0
with open(filename) as fin:
    for line in fin:
        #Since the first two lines in the data.txt are junk we can skip them
        if(i >= 2):
            myline = line.split()
            buffer.append(myline)
        i+=1
#Create var for buffer size
i -= 3
SIZE = i
print(buffer[0])
#Go thru buffer