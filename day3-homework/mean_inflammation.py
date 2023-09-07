#!/usr/bin/env python

import sys

fname = sys.argv[1]

data = open(fname)

def my_mean(numbers):
	amount = len(numbers)
	total = sum(numbers)
	return total/amount

patient_id = 1
average_list = {}
for lines in data:
	fixed_numbers = lines.rstrip()
	fixed_numbers = fixed_numbers.split(",")
	line_list = []
	for numbs in fixed_numbers:
		line_list.append(float(numbs))
	patient_id += 1	
	patient = 'patient' + str(patient_id)
	average_list[patient] = line_list

#print(average_list)	

for key, value in average_list.items():
	print(key, my_mean(value))

