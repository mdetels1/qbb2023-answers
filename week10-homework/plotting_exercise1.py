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

step11data = full_design_df.loc["GTEX-113JC",:"MT-TP"]
step11_nozeros = step11data[step11data != 0]
print(step11_nozeros)

plt.figure()
plt.hist(step11_nozeros, bins=20)
plt.xlabel("Logged Normalized Expression")
plt.ylabel("Counts")
plt.savefig("Exercise1.1.png")

# print(full_design_df)