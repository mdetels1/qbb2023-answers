#!/usr/bin/env python

#You’ll start by exploring the data in aau1043_dnm.csv. First, load this data into a pandas dataframe.
import pandas as pd

df = pd.read_csv("aau1043_dnm.csv")
#print(df)

# You first want to count the number of paternally 
# and maternally inherited DNMs in each proband. 
# Using this dataframe, create a dictionary where 
# the keys are the proband IDs and the value 
# associated with each key is a list of length 2, 
# where the first element in the list is the number 
# of maternally inherited DNMs and the second element 
# in the list is the number of paternally inherited 
# DNMs for that proband. You can ignore DNMs without 
# a specified parent of origin.

Mydict = {}


probandsf=[]
probandsm=[]
for line in df.index:
	if df.loc[line, "Phase_combined"] == "father":
		probandsm.append(df.loc[line, "Proband_id"])
	elif df.loc[line, "Phase_combined"] == "mother":
		probandsf.append(df.loc[line, "Proband_id"])

for i in df.loc[:, "Proband_id"]:
	Mydict[i] = [0,0]

for idnum in probandsf:
	Mydict[idnum][0] += 1

for idnum in probandsm:
	Mydict[idnum][1] += 1


#Use the following code snippet to convert this dictionary
#into a new pandas dataframe (this assumes your dictionary
#from step 1.2 is called deNovoCount):

#deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, 
#orient = 'index', columns = ['maternal_dnm', 
#'paternal_dnm'])

Mydict = pd.DataFrame.from_dict(Mydict, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])


#Now, load the data from aau1043_parental_age.csv into 
#a new pandas dataframe.

df2 = pd.read_csv("aau1043_parental_age.csv")
df2 = df2.set_index('Proband_id')


#You now have two dataframes with complementary 
#information. It would be nice to have all of this in 
#one data structure. Use the pd.concat() function 
#(more here) to combine your dataframe from step 3 with 
#the dataframe you just created in step 4 to create a 
#new merged dataframe.

#NOTE: You will need to specify the axis and join 
#arguments in pd.concat()

Together = pd.concat([Mydict, df2], axis = 1, join = "inner")

#print(Together)

# Using the merged dataframe from the previous section, 
# you will be exploring the relationships between 
# different features of the data. The statsmodels 
# package (more here) is an incredibly useful package 
# for conducting statistical tests and running 
# regressions. As such, it is especially appropriate 
# for the types of questions we’re interested in here. 
# For this assignment, we’ll be using the formula api 
# from statsmodels (more here) to run some regressions 
# between variables in our dataset. You can load this 
# tool into Python with import statsmodels.formula.api
# as smf.

import statsmodels.formula.api as smf

# First, you’re interested in exploring if there’s a 
# relationship between the number of DNMs and parental age. 
# Use matplotlib to plot the following. All plots should 
# be clearly labelled and easily interpretable.

import matplotlib.pyplot as plt

#the count of maternal de novo mutations vs. maternal age 
#(upload as ex2_a.png in your submission directory)
#the count of paternal de novo mutations vs. paternal age 
#(upload as ex2_b.png in your submission directory)

fig, ax = plt.subplots()

ax.set_xlabel("Maternal Age (Year)")
ax.set_ylabel("De novo Mutations (Count)")
ax.set_title("De Novo Mutations vs Age of Female Parents")
plt.tight_layout()

ax.scatter(Together.loc[:, "maternal_dnm"], Together.loc[:, "Mother_age"], color = "pink")

#figure = fig.savefig("ex2_a.png")

#plt.show()

fig, ax = plt.subplots()

ax.set_xlabel("Paternal Age (Year)")
ax.set_ylabel("De novo Mutations (Count)")
ax.set_title("De Novo Mutations vs Age of Male Parents")
plt.tight_layout()

ax.scatter(Together.loc[:, "paternal_dnm"], Together.loc[:, "Father_age"], color = "blue")

#figure = fig.savefig("ex2_b.png")

#plt.show()

# Now that you’ve visualized these relationships, 
# you’re curious whether they’re statistically significant. 
# Perform ordinary least squares using the smf.ols() 
# function to test for an association between maternal 
# age and maternally inherited de novo mutations. In your 
# README.md for this assignment, answer the following 
# questions:

import statsmodels.formula.api as smf
stats = smf.ols(formula = "maternal_dnm ~ 1 + Mother_age", data = Together).fit()
print(stats.summary())

# What is the “size” of this relationship? In your own 
# words, what does this mean? Does this match what you 
# observed in your plots in step 2.1?
# Is this relationship significant? How do you know?
