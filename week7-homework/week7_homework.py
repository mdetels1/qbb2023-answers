#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd

ONT_fname, bisulfite_fname, out_fname = sys.argv[1:4]

def load_data(fname):
    data = []
    for line in open(fname):
        line = line.rstrip().split()
        data.append([
            line[0], int(line[1]), int(line[2]), float(line[3]), int(line[4])])
    return data

ONT = load_data(ONT_fname)
bisulfite = load_data(bisulfite_fname)

ONT_set = set()
ONT_multi = set()
for i in range(len(ONT)):
	if ONT[i][1] not in ONT_set:
		ONT_set.add(ONT[i][1])
	else:
		ONT_multi.add(ONT[i][1])
ONT_single = ONT_set.difference(ONT_multi) # unique sites in nanopore

bisulfite_set = set()
bisulfite_multi = set()
for i in range(len(bisulfite)):
	if bisulfite[i][1] not in bisulfite_set:
		bisulfite_set.add(bisulfite[i][1])
	else:
		bisulfite_multi.add(bisulfite[i][1])
bisulfite_single = bisulfite_set.difference(bisulfite_multi) # unique sites in bisulfite

ONTcompare = ONT_single - bisulfite_single
bisulfitecompare = bisulfite_single.difference(ONT_single)
overlappingsites = (len(ONT_single)+len(bisulfite_single)) - (len(ONTcompare)+len(bisulfitecompare))
totalsites = (len(ONT_single)+len(bisulfite_single))

print(ONTcompare)
print(len(ONTcompare))
print(len(bisulfitecompare))
print(overlappingsites)
print(totalsites)
print(len(ONTcompare)/totalsites)
print(len(bisulfitecompare)/totalsites)
print(overlappingsites/totalsites)