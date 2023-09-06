#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

f = open("all_annotated.csv", "r")
transcripts = f.readlines()

trans=[]
for i in transcripts[1:]:
    i = i.rstrip()
    transcripts_list = i.split(",")
    i = transcripts_list[0]
    trans.append(i)

print(trans[0])

#samples = transcripts[0].rstrip().split(",") [2:]
#print(samples)
 

#print(transcripts[0])
#transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
#print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

#Find row with transcript of interest
for i in range(len(transcripts)):
    print(transcripts[i])
    if 'FBtr0073461' in transcripts[i] :
        row = i

 #Find columns with samples of interest
colsf = []
colsm = []
for i in range(len(samples)):
    if "female" in samples[i]:
        colsf.append(i)
    elif "male" in samples[i]:
        colsm.append(i)


 #Subset data of interest
expressionf = data[row, colsf]
expressionm = data[row,colsm]

 #Prepare data
x = samples[colsf]
yf = expressionf
ym = expressionm
ym2 = 2 * np.array(ym)

x = [10, 11, 12, 13, "14A", "14B", "14C", "14D"]

 #Plot data
fig, ax = plt.subplots()
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")
ax.set_xticklabels(x, rotation = 90)
ax.set_title( "SisA" )
plt.tight_layout()
ax.plot( x, yf )
ax.plot( x, ym )
ax.plot( x, ym2 )
fig.savefig( "FBtr0073461.png" )
plt.close( fig )