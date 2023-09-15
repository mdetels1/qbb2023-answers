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

print(Together)
