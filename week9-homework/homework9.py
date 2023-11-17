#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

# # read in data
# counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# # read in metadata
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

genesout = pd.read_csv("outgenes.csv")

fdr = multitest.fdrcorrection(genesout["pval"].fillna(1.0), alpha=0.05, method='indep', is_sorted=False)

genesout["fdr"] = (fdr[1])

genesout.loc[genesout["fdr"] <= 0.1, "Gene"].to_csv("significantgenes.csv")















