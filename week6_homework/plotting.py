#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plink = np.loadtxt("plink.eigenvec")

pca1 = plink[:,2]
pca2 = plink[:,3]

fig, ax = plt.subplots()
ax.scatter(pca1, pca2)
plt.xlabel("pca1")
plt.ylabel("pca2")
plt.title("Genotype PCs")
fig.tight_layout()
plt.savefig("GenotypePCs.pdf")


freq = pd.read_csv("plink.frq", delim_whitespace=True)
allelefreq = freq["MAF"]

fig, ax = plt.subplots()
ax.hist(allelefreq, bins = 80)
ax.set_xlabel("Frequency")
ax.set_ylabel("Count")
plt.title("Allele Frequencies")
fig.tight_layout()
fig.show()
fig.savefig("Allelefrequencies.pdf")