#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# # read in data
# counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# # read in metadata
# metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# # normalize
# counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# # log
# counts_df_logged = np.log2(counts_df_normed + 1)

# # merge with metadata
# full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

# full_design_df.to_csv("full_design.csv", index = True)

full_design_df = pd.read_csv("full_design.csv", index_col=0)

# for GTEX-113JC

# find logged normalized counts for all genes, excluding the last three (which are sex, age, dthhrdy)

# step11data = full_design_df.loc["GTEX-113JC",:"MT-TP"]
# step11_nozeros = step11data[step11data != 0]
# print(step11_nozeros)

# plt.figure()
# plt.hist(step11_nozeros, bins=20)
# plt.xlabel("Logged Normalized Expression")
# plt.ylabel("Counts")
# plt.savefig("Exercise1.1.png")

# # print(full_design_df)

# Expression of a single gene between sexes
# for gene MXD4 find logged normalized counts

# step12data = full_design_df.loc[:, ["MXD4", "SEX"]]
# malestep12 = step12data[step12data["SEX"] == 1]
# femalestep12 = step12data[step12data["SEX"] == 2]

# plt.figure()
# plt.hist(malestep12["MXD4"], bins=20, color="orange", alpha = 0.25, label="Male")
# plt.hist(femalestep12["MXD4"], bins=20, color="blue", alpha = 0.25, label="Female")
# plt.xlabel("Logged Normalized Expression")
# plt.ylabel("Counts")
# plt.legend()
# plt.savefig("Exercise1.2.png")

# Distribution of subject ages

# Find the subjects in each age category

# Agedata = full_design_df["AGE"].value_counts().sort_index()

# categories = []
# values = []
# for i in Agedata.index:
# 	categories.append(i)
# for i in Agedata:
# 	values.append(i)

# plt.figure()
# plt.bar(categories, values)
# plt.xlabel("Age Categories")
# plt.ylabel("Counts")
# plt.savefig("Exercise1.3.png")

# Sex-stratified expression with age
# Pull out logged normalized counts and age and sex for LPXN

step14data = full_design_df.loc[:,["LPXN", "AGE", "SEX"]].sort_index()
step14data = step14data.groupby(["AGE", "SEX"])["LPXN"].median()
print(step14data)

male_median=[]
female_median=[]
for i in range(len(step14data.index)):
	if step14data.index[i][1] == 1:
		male_median.append(step14data[i])
	if step14data.index[i][1] == 2:
		female_median.append(step14data[i])

print(male_median)
print(female_median)

time = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]

plt.figure()
plt.plot(time, male_median, label = "Male")
plt.plot(time, female_median, label = "Female")
plt.legend()
plt.xlabel("Age Categories")
plt.ylabel("Median Expression")
plt.savefig("Exercise1.4.png")





