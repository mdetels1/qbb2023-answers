#!/usr/bin/env python

import sys

fname = sys.argv[1]

data = open(fname)

average_list = []
for lines in data:
	fixed_numbers = float(lines.rstrip())
	average_list.append(fixed_numbers)	

print(average_list)

def my_mean(numbers):
	amount = len(numbers)
	total = sum(numbers)
	return total/amount

my_result = my_mean(average_list)
print(my_result)
