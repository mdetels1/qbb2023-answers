#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt

# # read in data
# counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# # # read in metadata
# metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# counts_df_normed = np.log2(counts_df_normed + 1)

# full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

# # # model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
# # results = model.fit()

# slope = results.params[1]
# pval = results.pvalues[1]


# name = ["Gene", "slope", "pval"]
# genes = pd.DataFrame(columns = name)

# genes["Gene"] = full_design_df.columns[0:-3]
# # for i in genes["Gene"]:
# # 	model = smf.ols(formula = 'Q(i) ~ SEX', data=full_design_df)
# # 	results = model.fit()
# # 	genes.loc[i, "slope"] = results.params[1]
# # 	genes.loc[i, "pval"]

# for i in genes.index:
# 	geneName = genes.loc[i, "Gene"]
# 	model = smf.ols(formula = 'Q(geneName) ~ SEX', data=full_design_df)
# 	results = model.fit()
# 	genes.loc[i, "slope"] = results.params[1]
# 	genes.loc[i, "pval"] = results.pvalues[1]

# # print(genes)

# genes.to_csv("outgenes.csv", index = False)

# genesout = pd.read_csv("outgenes.csv")

# fdr = multitest.fdrcorrection(genesout["pval"].fillna(1.0), alpha=0.05, method='indep', is_sorted=False)

# genesout["fdr"] = (fdr[1])

# genesout.loc[genesout["fdr"] <= 0.1, "Gene"].to_csv("significantgenes.csv")

# dds = DeseqDataSet(
#     counts=counts_df,
#     metadata=metadata,
#     design_factors="SEX",
#     n_cpus=4,
# )

# dds.deseq2()
# stat_res = DeseqStats(dds)
# stat_res.summary()
# results = stat_res.results_df

# results = results.rename_axis("Genes").reset_index()
# print(results)

# results.to_csv("resultsdds.csv", index = False)

# results.loc[results["padj"] <= 0.1, "Genes"].to_csv("significantgenesdeseq.csv")


# mygenes = pd.read_csv("significantgenes.csv")
# ddsgenes = pd.read_csv("significantgenesdeseq.csv")

# mygenes_set = set(map(tuple,mygenes.to_numpy()))

# ddsgenes_set = set(map(tuple,ddsgenes.to_numpy()))

# # find find genes that overlap
# overlap = mygenes_set.intersection(ddsgenes_set)
# # print(len(overlap))

# # find genes that are unique to mygenes
# mygenes_unique = mygenes_set.difference(ddsgenes_set)
# # print(len(mygenes_unique))

# # find genes that are unique to ddsgenes
# ddsgenes_unique = ddsgenes_set.difference(mygenes_set)
# # print(len(ddsgenes_unique))

# jaccardindex = ((len(overlap)) / (len(mygenes_unique)+len(ddsgenes_unique))) * 100


# # print(jaccardindex)


# ddsgenes = pd.read_csv("significantgenesdeseq.csv")
resultsdds = pd.read_csv("resultsdds.csv")

# drop all rows with NaN values

clean_resultsdds = resultsdds.dropna()

# find the log2Fold Change
log2foldchange_volcano = clean_resultsdds["log2FoldChange"]

# find the -log10(padj)
padj_resultsdds = clean_resultsdds["padj"]
log10padj_resultsdds = -np.log10(padj_resultsdds)

# find genes that are significant at 10% FDR
morethan10FDR = clean_resultsdds.loc[clean_resultsdds["padj"] <= 0.1]
FDRandlog2fold = morethan10FDR.loc[abs(morethan10FDR["log2FoldChange"]) >=1]


plt.figure()
plt.scatter(log2foldchange_volcano,log10padj_resultsdds, color = "grey", alpha = 0.5)
plt.xlabel("Log Fold Change")
plt.ylabel("-log10(pvalue)")
plt.title("Volcano Plot of ddsgenes")
plt.scatter(FDRandlog2fold["log2FoldChange"], -np.log10(FDRandlog2fold["padj"]), color= "red", alpha = 0.5)
plt.axhline(y=1, color = "grey", linestyle="--")
plt.axvline(x=1, color = "grey", linestyle="--")
plt.axvline(x=-1, color = "grey", linestyle="--")
plt.savefig("Volcanoplot.png")






