#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

# # # read in data
# counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# # # read in metadata
# metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# counts_df_normed = np.log2(counts_df_normed + 1)

# full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

# # # model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
# # # results = model.fit()

# # slope = results.params[1]
# # pval = results.pvalues[1]


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

# results.loc[results["padj"] <= 0.1, "Genes"].to_csv("significantgenesdeseq.csv")


mygenes = pd.read_csv("significantgenes.csv")
ddsgenes = pd.read_csv("significantgenesdeseq.csv")

mygenes_set = set(map(tuple,mygenes.to_numpy()))

ddsgenes_set = set(map(tuple,ddsgenes.to_numpy()))

# find find genes that overlap
overlap = mygenes_set.intersection(ddsgenes_set)
print(len(overlap))

# find genes that are unique to mygenes
mygenes_unique = mygenes_set.difference(ddsgenes_set)
print(len(mygenes_unique))

# find genes that are unique to ddsgenes
ddsgenes_unique = ddsgenes_set.difference(mygenes_set)
print(len(ddsgenes_unique))

jaccardindex = ((len(overlap)) / (len(mygenes_unique)+len(ddsgenes_unique))) * 100


print(jaccardindex)





