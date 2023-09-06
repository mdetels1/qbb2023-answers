#!/usr/bin/env python
import numpy

#open file with patient data
f = open("inflammation-01.csv", "r")

lines = f.readlines()

#within the range of 200 to 240, looking for positions 0, 9, and -1

#start a empty list
start_coords = []

#for the rows in lines (the file), do the following
for line in lines:
	line = line.rstrip() #strip of anything not of value
	line_list = line.split(",") #this will split the values into individual ones based on commas but they will be strings
	flare_coords = [] #another empty list that you will put all of the for in values from below into
	for flare in line_list: #for all of the values in each of the rows that are lists above, do the following
		flare = int(flare) #make all of the values integers, instead of strings
		flare_coords.append(flare) # add all of the flare values that are now integers to the new empty list flare_coords
	

	start_coords.append(flare_coords) #add all of the flare_coords values to start_coords
	
#patient1 = [] #empty list that will be all of patient 1 flare up numbers
#patient5 = [] #empty list that will be all of patient 5 flare up numbers
#for num in (start_coords[0]): #for all of the numbers in the first row of the data sheet
#	patient1.append(num) #add to patient1 list
#for num2 in (start_coords[4]): #for all of the numbers in the fifth row of the data sheet
#	patient5.append(num2) #add to patient5 list

#index = [] #empty index list

#for i in range(len(patient1)): # for all positions in the range (gives 0, 1, 2, 3, 4 to an end point) of the length (total numbers of values) of patient 1
#	i = patient1[i] - patient5[i] # defining i the position i we are at (0,1,2,3, etc) the number given in patient5 subtracted from the number given in patient1
#	index.append(i) # adding all of these i values defined above to the empty list above, index

#print(index) #print this list

#Above is how I did it the first time, below is more succinct

index = []
for i in range(len(start_coords[1])):
	i = start_coords[5][i] - start_coords[1][i] # start_coords[5][i] means in start_coords position 5 and within that position i (which will cycle through all of the positions)
	index.append(i)

print(index)




