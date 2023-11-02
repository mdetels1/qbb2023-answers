#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plink = np.loadtxt("plink.eigenvec")

pca1 = plink[:,2]
pca2 = plink[:,3]

fig, ax = plt.subplots()
ax.scatter(pca1, pca2)
plt.xlabel("pca1")
plt.ylabel("pca2")
plt.title("Genotype PCs")
fig.tight_layout()
plt.savefig("GenotypePCs.pdf")
plt.show()


