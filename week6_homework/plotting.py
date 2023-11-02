#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plink = np.loadtxt("plink.eigenvec")

# pca1 = plink[:,2]
# pca2 = plink[:,3]

# fig, ax = plt.subplots()
# ax.scatter(pca1, pca2)
# plt.xlabel("pca1")
# plt.ylabel("pca2")
# plt.title("Genotype PCs")
# fig.tight_layout()
# plt.savefig("GenotypePCs.pdf")


# freq = pd.read_csv("plink.frq", delim_whitespace=True)
# allelefreq = freq["MAF"]

# fig, ax = plt.subplots()
# ax.hist(allelefreq, bins = 80)
# ax.set_xlabel("Frequency")
# ax.set_ylabel("Count")
# plt.title("Allele Frequencies")
# fig.tight_layout()
# fig.savefig("Allelefrequencies.pdf")

CB1908 = pd.read_csv("phenotype_gwas_results_CB1908_IC50.assoc.linear", delim_whitespace=True)
GS451 = pd.read_csv("phenotype_gwas_results_GS451_IC50.assoc.linear", delim_whitespace=True)

minuslogpvalueCB1908 = -np.log10(CB1908["P"])
minuslogpvalueGS451 = -np.log10(GS451["P"])

redcb = []
for i in minuslogpvalueCB1908:
	if i > 5:
		redcb.append("r")
	else:
		redcb.append("b")

redgs = []
for i in minuslogpvalueGS451:
	if i > 5:
		redgs.append("r")
	else:
		redgs.append("b")


fig, ax = plt.subplots(2)
ax[0].scatter(range(len(CB1908["BP"])),minuslogpvalueCB1908, color=redcb)
ax[1].scatter(range(len(GS451["BP"])), minuslogpvalueGS451, color=redgs)
ax[0].set_title("CB1908 Manhattan Plot")
ax[1].set_title("GS451 Manhattan Plot")
ax[0].set_xlabel("Chromosome")
ax[1].set_xlabel("Chromosome")
ax[0].set_ylabel("minuslogpvalue")
ax[1].set_ylabel("minuslogpvalue")
ax[0].hlines(y = 5, xmin=0, xmax=len(CB1908["BP"]), linestyle="dashed")
ax[1].hlines(y = 5, xmin=0, xmax=len(GS451["BP"]), linestyle="dashed")
plt.tight_layout()
fig.savefig("Manhattanplot.pdf")