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

fig, (ax1, ax2) = plt.subplots(2)

hist_generations = []
for i in range(1000):
	my_result = WF(0.5,150)
	x_position = my_result[1]
	hist_generations.append(len(x_position))
	y_position = my_result[0]
	ax1.plot(x_position,y_position)
	ax1.plot(my_result[1], my_result[0])

ax2.hist(hist_generations)


ax1.set_xlabel("Time (Generations)")
ax1.set_ylabel("Allele Frequency")
ax1.set_title("Allele Frequency of Population Over Generations")
ax2.set_xlabel("Generations")
ax2.set_ylabel("Number of Occurences")
ax2.set_title("Histogram of Generations to Fixation")
plt.tight_layout()
figure = fig.savefig("30_Exercise_2_2.pdf")

plt.show()