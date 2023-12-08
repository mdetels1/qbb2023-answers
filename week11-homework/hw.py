#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

# pre-processing function that computes a neighborhood graph
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

# Leiden clustering
sc.tl.leiden(adata)

# Visualizing clusters
# UMAP
sc.tl.umap(adata, maxiter=900)
#tSNE
sc.tl.tsne(adata)

fig, ax = plt.subplots(ncols=2)
sc.pl.umap(adata, color="leiden", ax = ax[0], title="UMAP", show=False)
sc.pl.tsne(adata, color="leiden", ax = ax[1], title="tSNE", show=False)
fig.tight_layout()
fig.savefig("Exercise1plot.png")