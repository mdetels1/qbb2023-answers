#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

def edges(k, sequence):

	graph = set()

	for read in sequence:
		for i in range(len(read)-k-1):
			kmer1 = read[i: i+k]
			kmer2 = read[i+1: i+1+k]
			graph.add(f'{kmer1} --> {kmer2}')

	f = open("edges.txt", "w")

	for edge in graph:
		f.write(edge + "\n")

edges(k=3, sequence=reads)


