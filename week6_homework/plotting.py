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
# CB1908_ADD = []
# for i in CB1908["TEST"].index:
# 	if CB1908["TEST"][i] == "ADD":
# 		CB1908_ADD.append(CB1908["P"][i])

# GS451 = pd.read_csv("phenotype_gwas_results_GS451_IC50.assoc.linear", delim_whitespace=True)
# GS451_ADD = []
# for i in GS451["TEST"].index:
# 	if GS451["TEST"][i] == "ADD":
# 		GS451_ADD.append(GS451["P"][i])

# minuslogpvalueCB1908 = []
# for value in CB1908_ADD:
# 	minuslogpvalueCB1908.append(-np.log10(value))

# minuslogpvalueGS451 = []
# for value in GS451_ADD:
#  	minuslogpvalueGS451.append(-np.log10(value))

# redcb = []
# for i in minuslogpvalueCB1908:
# 	if i > 5:
# 		redcb.append("r")
# 	else:
# 		redcb.append("b")

# redgs = []
# for i in minuslogpvalueGS451:
# 	if i > 5:
# 		redgs.append("r")
# 	else:
# 		redgs.append("b")

# fig, ax = plt.subplots(2)
# ax[0].scatter(range(len(minuslogpvalueCB1908)), minuslogpvalueCB1908, color=redcb)
# ax[1].scatter(range(len(minuslogpvalueGS451)), minuslogpvalueGS451, color=redgs)
# ax[0].set_title("CB1908 Manhattan Plot")
# ax[1].set_title("GS451 Manhattan Plot")
# ax[0].set_xlabel("Chromosome")
# ax[1].set_xlabel("Chromosome")
# ax[0].set_ylabel("minuslogpvalue")
# ax[1].set_ylabel("minuslogpvalue")
# ax[0].hlines(y = 5, xmin=0, xmax=len(minuslogpvalueCB1908), linestyle="dashed")
# ax[1].hlines(y = 5, xmin=0, xmax=len(minuslogpvalueGS451), linestyle="dashed")
# plt.tight_layout()
# plt.savefig("manhattanplot.png")

# min = np.min(CB1908["P"])






index=0
for i in CB1908["P"]:
	if i == min:
		print(index)
	index+=1
#print(CB1908.iloc[[2028444]])

genotyping = pd.read_csv("genotypes.vcf", delimiter = "\t", skiprows = 27)

SNPs = genotyping["ID"]
#print(SNPs)

index = 0
for value in SNPs:
	if value == "rs10876043":
		print(index)
	index+=1

topSNP = (genotyping.iloc[184404, 9:])

wildtype = []
heterozygous = []
homozygous = []

number = 0
for phenotype in topSNP:
	number += 1
	if phenotype == "0/0":
		wildtype.append(number)
	elif phenotype == "0/1":
		heterozygous.append(number)
	elif phenotype == "1/1":
		homozygous.append(number)

WT_IC50 = []
het_IC50 = []
homo_IC50 = []
CB1908_IC50 = pd.read_csv("CB1908_IC50.txt", delim_whitespace=True) 
for i in CB1908_IC50["FID"].index:
	if i in wildtype:
		WT_IC50.append((CB1908_IC50["CB1908_IC50"][i]))
	elif i in heterozygous:
		het_IC50.append((CB1908_IC50["CB1908_IC50"][i]))
	elif i in homozygous:
		homo_IC50.append((CB1908_IC50["CB1908_IC50"][i]))

data = [WT_IC50, het_IC50, homo_IC50]

del data[1][11]
del data[1][28]

print(data)

plt.boxplot(data)
plt.title("rs10876043 Effect on CB1908 IC50")
plt.xlabel("rs10876043 Genotype")
plt.ylabel("CB1908 IC50")
plt.xticks([1,2,3],["Wildtype", "Heterozygous", "Homozygous"])
plt.savefig("EffectSizeBoxPlot.pdf")
