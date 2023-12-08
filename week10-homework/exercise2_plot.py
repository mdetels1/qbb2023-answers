#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
numbats_df = pd.read_csv("numbats.csv")

# # read in australia data
# au = pd.read_csv("au.csv", header = None)

# # Find latitude
# coords = numbats_df.loc[:, ("decimalLatitude", "decimalLongitude")]

# notNaRows = coords.loc[:, "decimalLatitude"].notnull()
# notNaRows2 = coords.loc[:, "decimalLongitude"].notnull()

# coords_noNA = coords.loc[notNaRows & notNaRows2, :]

# # plot australia
# plt.figure()
# plt.scatter(au.iloc[:,1], au.iloc[:,0], s=1)
# plt.scatter(coords_noNA["decimalLongitude"], coords_noNA["decimalLatitude"], color="orange", label="Numbat Locations", s=4)
# plt.legend()
# plt.title("Locations of Numbats in Australia")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.savefig("Locations of Numbats in Australia.png")


# # time of day numbats are seen
# find time of day
# hour = numbats_df["hour"]

# noNahour = hour[hour.notnull()]

# plt.figure()
# plt.hist(noNahour, bins = 24)
# plt.xlabel("Hour of the Day")
# plt.ylabel("Count")
# plt.title("Sightings of Numbats over the Hours of the Day")
# plt.savefig("Numbatsovertheday.png")

# find the months

months=numbats_df["month"]

noNamonths = months[months.notnull()]

monthlist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

finaldata = noNamonths.value_counts().loc[monthlist]

print(finaldata)

plt.figure()
plt.bar(finaldata.index, finaldata)
plt.title("Sightings of Numbats per Month")
plt.xlabel("Months")
plt.ylabel("Number of Sightings")
plt.savefig("SightingsofNumbatsperMonth.png")







