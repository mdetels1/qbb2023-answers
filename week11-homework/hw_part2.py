#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

print(adata)

fig, ax = plt.subplots()
sc.pl.umap(adata, color=["CD79A","FCER1A","GNLY"], title=["CD79A Expression", "FCER1A Expression", "GNLY Expression"], show=False)
plt.savefig("Exercise3plot.png")



