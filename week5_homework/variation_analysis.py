#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(data, bi, ax, label, xl, xx, yy):
    ax.hist(data, alpha=0.3, bins=bi)
    ax.set_title(label)
    ax.set_ylabel("Frequency")
    ax.set_xlabel(xl)
    ax.set_xlim(xx, yy)

# info = []
# for line in open("annotated_end.vcf"):
#     if line.startswith('#'):
#         continue
#     fields = line.rstrip('\n').split('\t')
#     info.append(fields[7])

readdepth = []
genotypequal = []
allelefrequency = []
LOF = 0
NMD = 0
for line in open("annotated_end.vcf"):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    info = fields[7].split(';')
    format_names = fields[8].split(":")
    formats = fields[9:]
    #print(formats)
    dp = format_names.index("DP")
    gq = format_names.index("GQ")
    for i in formats:
        if i.split(":")[dp] != '.':
            readdepth.append(int(i.split(":")[dp]))
            genotypequal.append(float(i.split(":")[gq]))
    for i in info:
        if i.startswith("AF="):
            if ',' not in i[3:]:
                allelefrequency.append(float(i[3:]))
    for i in info:
        if "LOF" in i:
            LOF += 1
        if "NMD" in i:
            NMD += 1

categories = ["LOF","NMD"]
values = [LOF, NMD]


fig, ax = plt.subplots(2, 2, figsize=(10,10))
plot_data(readdepth, 700, ax[0,0], "Read Depth Distribution At Variants", "Read Depth", 0, 20)
plot_data(genotypequal, 20, ax[0,1], "Genotype Quality Distribution", "Genotype Quality (GQ)", 0, 175)
plot_data(allelefrequency, 20, ax[1,0], "Allele Frequency Distribution", "Allele Frequency", 0, 1)
ax[1,1].bar(categories, values)
ax[1,1].set_xlabel("Categories")
ax[1,1].set_ylabel("Frequency")
ax[1,1].set_title("Predicted Effects of the Variants")
plt.tight_layout()
plt.savefig("final_plot.pdf")


# # fig, ax = plt.subplots()
# # ax.hist(readdepth)
# # #    ax.plot(x, y_poisson, label = "Poisson")
# # #    ax.plot(x, y_normal, label = "Normal")
# # #    ax.set_xlabel("Coverage (Number of Reads)")
# # #    ax.set_ylabel("Frequency (bp)")
# # #    ax.legend()
# # fig.tight_layout()
# # showplot()
# # #    fig.savefig(figname)
