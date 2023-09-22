#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#==============#
# Step 1.2 #
#==============#

def simulate_converage(coverage, genome_len, read_len, figname): #creating a function because we will want to run this 3 times

	coverage_arr = np.zeros(genome_len) #array of 0s of the length of whatever we put in as our genome_len
	
	num_reads = int(coverage * genome_len / read_len)

	low = 0 
	high = genome_len - read_len

	start_positions = np.random.randint(low = low, high = high + 1, size = num_reads) #high is exclusive

	for start in start_positions:
		coverage_arr[start: start + read_len] += 1 # += 1 is short hand for x = x+1

	x = np.arange(0, max(coverage_arr)+1)

	sim_0cov = genome_len - np.count_nonzero(coverage_arr) #number of 0 coverage bases
	sim_0cov_pct = sim_0cov/genome_len * 100

	print(f"In the simulation, there are {sim_0cov} bases with 0 coverage")
	print(f"This is {sim_0cov_pct}% of the genome")

	# Get poisson distribution
	y_poisson = stats.poisson.pmf(x, mu = coverage) * genome_len #pmf is probability mass function, probability that this distribution will report that number

	# Get normal distribution
	y_normal = stats.norm.pdf(x, loc = coverage, scale = np.sqrt(coverage)) * genome_len

	fig, ax = plt.subplots()
	ax.hist(coverage_arr, bins = x, align = "left", label = "Simulation")
	ax.plot(x, y_poisson, label = "Poisson")
	ax.plot(x, y_normal, label = "Normal")
	ax.set_xlabel("Coverage (Number of Reads)")
	ax.set_ylabel("Frequency (bp)")
	ax.legend()
	fig.tight_layout()
	fig.savefig(figname)


#simulate_converage(3,1_000_000, 100, 'ex1_3x_cov.png')

#simulate_converage(10,1_000_000, 100, 'ex1_10x_cov.png')

simulate_converage(30, 1_000_000, 100, 'ex1_30x_cov.png')








