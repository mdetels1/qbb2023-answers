#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ONT_fname, bisulfite_fname, normal_fname, tumor_fname, normal_bisulfite, tumor_bisulfite, out_fname = sys.argv[1:8]

def load_data(fname):
    data = []
    for line in open(fname):
        line = line.rstrip().split()
        data.append([
            line[0], int(line[1]), int(line[2]), float(line[3]), int(line[4])])
    return data

# ONT = load_data(ONT_fname)
# bisulfite = load_data(bisulfite_fname)

# ONT_set = set()
# ONT_multi = set()
# for i in range(len(ONT)):
# 	if ONT[i][1] not in ONT_set:
# 		ONT_set.add(ONT[i][1])
# 	else:
# 		ONT_multi.add(ONT[i][1])
# ONT_single = ONT_set.difference(ONT_multi) # unique sites in nanopore

# bisulfite_set = set()
# bisulfite_multi = set()
# for i in range(len(bisulfite)):
# 	if bisulfite[i][1] not in bisulfite_set:
# 		bisulfite_set.add(bisulfite[i][1])
# 	else:
# 		bisulfite_multi.add(bisulfite[i][1])
# bisulfite_single = bisulfite_set.difference(bisulfite_multi) # unique sites in bisulfite

# ONTcompare = ONT_single - bisulfite_single
# bisulfitecompare = bisulfite_single.difference(ONT_single)
# overlappingsitesset = ONT_single.intersection(bisulfite_single)
# totalsites = (len(ONT_single)+len(bisulfite_single))-(len(overlappingsitesset))

# # print(ONTcompare)
# # print(len(ONTcompare))
# # print(len(bisulfitecompare))
# # print(len(overlappingsitesset))
# # print(totalsites)
# # print(len(ONTcompare)/totalsites)
# # print(len(bisulfitecompare)/totalsites)
# # print(len(overlappingsitesset)/totalsites)


# ONT_df = pd.DataFrame(ONT, columns = ["Chromosome", "Start", "End", "PercentMethylated", "ReadCoverage"])
# bisulfite_df = pd.DataFrame(bisulfite, columns = ["Chromosome", "Start", "End", "PercentMethylated", "ReadCoverage"])


# # plt.figure()
# # plt.hist(ONT_df["ReadCoverage"], bins=1000, alpha=0.5, color='blue', label='ONT')
# # plt.hist(bisulfite_df["ReadCoverage"], bins=1500, alpha=0.5, color='red', label='Bisulfite')
# # plt.xlim(0,100)
# # plt.xlabel("Read Coverage")
# # plt.ylabel("Count")
# # plt.title("Distribution of Coverages Across CpG Sites")
# # plt.legend()
# # plt.savefig(out_fname)

# # print(overlappingsites)
# # print(len(overlappingsitesset))

# ONT_list = []
# for i in range(len(ONT_df["Start"])):
# 	if ONT_df["Start"][i] in overlappingsitesset:
# 		ONT_list.append(ONT_df["PercentMethylated"][i])

# bisulfite_list = []
# for i in range(len(bisulfite_df["Start"])):
# 	if bisulfite_df["Start"][i] in overlappingsitesset:
# 		bisulfite_list.append(bisulfite_df["PercentMethylated"][i])

# fig = plt.figure()
# histogram = np.histogram2d(bisulfite_list, ONT_list, bins = 100)[0]
# histogram_transformed = np.log10(histogram + 1)
# plt.xlabel("Bisulfite Methylated Frequency")
# plt.ylabel("Nanopore Methylated Frequency")
# pearson = np.corrcoef(bisulfite_list, ONT_list)[0,1]
# plt.title(f"Methylation Frequency of Nanopore and Bisulfite, R= {pearson:0.3f}")
# plt.imshow(histogram_transformed)
# plt.savefig(out_fname)



normal = load_data(normal_fname)
tumor = load_data(tumor_fname)

normal_set = set()
normal_multi = set()
for i in range(len(normal)):
	if normal[i][1] not in normal_set:
		normal_set.add(normal[i][1])
	else:
		normal_multi.add(normal[i][1])
normal_single = normal_set.difference(normal_multi) 

tumor_set = set()
tumor_multi = set()
for i in range(len(tumor)):
	if tumor[i][1] not in tumor_set:
		tumor_set.add(tumor[i][1])
	else:
		tumor_multi.add(tumor[i][1])
tumor_single = tumor_set.difference(tumor_multi)

normal_df = pd.DataFrame(normal, columns = ["Chromosome", "Start", "End", "PercentMethylated", "ReadCoverage"])
tumor_df = pd.DataFrame(tumor, columns = ["Chromosome", "Start", "End", "PercentMethylated", "ReadCoverage"])

overlapping = normal_single.intersection(tumor_single)

joined = normal_df.merge(tumor_df, on = "Start")

# print(joined)
# print(type(joined))
# print(joined.columns)
joined["difference"] = joined.loc[:, "PercentMethylated_x"] - joined.loc[:, "PercentMethylated_y"]

idx = joined.loc[:, "difference"] != 0
violin = joined.loc[idx, 'difference']


normal_bi = load_data(normal_bisulfite)
tumor_bi = load_data(tumor_bisulfite)

normalbi_set = set()
normalbi_multi = set()
for i in range(len(normal_bi)):
	if normal_bi[i][1] not in normalbi_set:
		normalbi_set.add(normal_bi[i][1])
	else:
		normalbi_multi.add(normal_bi[i][1])
normalbi_single = normalbi_set.difference(normalbi_multi) 

tumorbi_set = set()
tumorbi_multi = set()
for i in range(len(tumor_bi)):
	if tumor_bi[i][1] not in tumorbi_set:
		tumorbi_set.add(tumor_bi[i][1])
	else:
		tumorbi_multi.add(tumor_bi[i][1])
tumorbi_single = tumorbi_set.difference(tumorbi_multi)

normalbi_df = pd.DataFrame(normal_bi, columns = ["Chromosome", "Start", "End", "PercentMethylated", "ReadCoverage"])
tumorbi_df = pd.DataFrame(tumor_bi, columns = ["Chromosome", "Start", "End", "PercentMethylated", "ReadCoverage"])

overlappingbi = normalbi_single.intersection(tumorbi_single)

joinedbi = normalbi_df.merge(tumorbi_df, on = "Start")

# print(joined)
# print(type(joined))
# print(joined.columns)
joinedbi["difference"] = joinedbi.loc[:, "PercentMethylated_x"] - joinedbi.loc[:, "PercentMethylated_y"]

idx_bi = joinedbi.loc[:, "difference"] != 0
violin_bi = joinedbi.loc[idx_bi, 'difference']


fig = plt.figure()
plt.violinplot([violin, violin_bi])
violinJoined = joined.merge(joinedbi, on = "Start")
pearsonnt = np.corrcoef(violinJoined.loc[:, "difference_x"], violinJoined.loc[:, "difference_y"])[0,1]
plt.title(f"Violin Plot of the Thing you Want, R= {pearsonnt:0.3f}")
plt.xticks([1,2], labels = ["ONT", "Bisulfite"])
plt.savefig(out_fname)


