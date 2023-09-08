#!/usr/bin/env python

# Get a starting frequency and a population size
# Input parameters for fuction

# Make a list to store our allele frequencies

# While our allele frequency is between 0 and 1
# 	Get the new allele frequency for next generation
#	By drawing from the binomial distribution
#	(convert number of successes into a frequency)
#	Store or allele frequency in the allele frequency list



# Return a list of allele frequency at each time point
# Number of generations to fixation is the length of your list

import numpy as np
import matplotlib.pyplot as plt


def WF(frequency, population):
	allele_freq = []
	generation = 0
	generation_list = []
	while 1 > frequency > 0:
		successes = np.random.binomial(2*population, frequency)
		frequency = successes/(2*population)
		generation += 1
		allele_freq.append(frequency)
		generation_list.append(generation)
	return [allele_freq, generation_list]

#print(my_result)
#print("number of generations to fixation:", len(my_result))

fig, ax = plt.subplots()
for i in range(30):
	my_result = WF(0.5,1000)
	x_position = my_result[1]
	y_position = my_result[0]
	ax.plot(x_position,y_position)
	#plt.plot(my_result[1], my_result[0])
plt.xlabel("Time (Generations)")
plt.ylabel("Allele Frequency")
plt.title("Allele Frequency of Population Over Generations")
figure = fig.savefig("30 Iterations of Allele Frequency of Population Over Time")
plt.show()