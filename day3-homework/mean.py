#!/usr/bin/env python

def my_mean(list):
	amount = len(list)
	total = sum(list)
	return total/amount

my_result = my_mean([1, 2, 3, 4, 5])
print(my_result)
