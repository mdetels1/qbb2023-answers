#!/usr/bin/env python

import sys
import pandas as pd

baitmap, washU, output = sys.argv[1:4]


baitcolumns = ["Chr", "Start", "End", "ID", "Gene"]
bait = pd.read_csv(baitmap, delim_whitespace = True, names = baitcolumns)
outputcolumns = ["Interaction1", "Interaction2", "Strength"]
output = pd.read_csv(washU, delim_whitespace = True, names = outputcolumns)
output[["Chr1", "Start1", "Stop1"]] = output["Interaction1"].str.split(',', expand=True)
output[["Chr2", "Start2", "Stop2"]] = output["Interaction2"].str.split(',', expand=True)
output = output.drop(columns = ["Interaction1", "Interaction2"])
output = output[["Chr1", "Start1", "Stop1", "Chr2", "Start2", "Stop2", "Strength"]]

maxi = max(output["Strength"])

output['Start1'] = output['Start1'].astype('int')
output['Start2'] = output['Start2'].astype('int')

name = ["chrom", "chromStart", "chromEnd", "name", "score", "value", "ex", "color", "sourceChrom", "sourceStart", "sourceEnd", "sourceName", "sourceStrand", "targetChrom", "targetStart", "targetEnd", "targetName", "targetStrand"]
USCS = pd.DataFrame(columns = name)
for i in output.index:
	newRowNumber = USCS.shape[0] + 1
	USCS.loc[newRowNumber, "chrom"]=output.loc[i, "Chr1"]
	USCS.loc[newRowNumber, "chromStart"]=min(output.loc[i, "Start1"], output.loc[i, "Start2"])
	USCS.loc[newRowNumber, "chromEnd"]=max(output.loc[i, "Stop1"], output.loc[i, "Stop2"])
	USCS.loc[newRowNumber, "name"]="."
	USCS.loc[newRowNumber, "score"]=(output.loc[i, "Strength"])/maxi * 1000
	USCS.loc[newRowNumber, "value"]=output.loc[i, "Strength"]
	USCS.loc[newRowNumber, "ex"]="."
	USCS.loc[newRowNumber, "color"]="black"
	if output.loc[i, 'Start1'] in set(bait["Start"]):
		if output.loc[i, 'Start2'] in set(bait["Start"]):
			USCS.loc[newRowNumber, "targetStrand"] = "+"
			USCS.loc[newRowNumber, "sourceStrand"] = "+"
			#print(bait["Start"] == output.loc[i, 'Start2'])
			USCS.loc[newRowNumber, "targetName"] = bait["Gene"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0]
			USCS.loc[newRowNumber, "targetChrom"] = "chr" + str(bait["Chr"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0])
			USCS.loc[newRowNumber, "sourceName"] = bait["Gene"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0]
			USCS.loc[newRowNumber, "sourceChrom"] = "chr" + str(bait["Chr"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0])
			USCS.loc[newRowNumber, "sourceStart"] = bait["Start"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0]
			USCS.loc[newRowNumber, "sourceEnd"] = bait["End"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0]
			USCS.loc[newRowNumber, "targetStart"] = bait["Start"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0]
			USCS.loc[newRowNumber, "targetEnd"] = bait["End"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0]
		else: # start 1 bait, start 2 target
			USCS.loc[newRowNumber, "targetStrand"] = "-"
			USCS.loc[newRowNumber, "sourceStrand"] = "+"
			USCS.loc[newRowNumber, "targetName"] = "."
			USCS.loc[newRowNumber, "targetChrom"] = output["Chr2"][output["Start2"] == output.loc[i, 'Start2']].to_list()[0]
			USCS.loc[newRowNumber, "sourceName"] = bait["Gene"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0]
			USCS.loc[newRowNumber, "sourceChrom"] = "chr" + str(bait["Chr"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0])
			USCS.loc[newRowNumber, "sourceStart"] = bait["Start"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0]
			USCS.loc[newRowNumber, "sourceEnd"] = bait["End"][bait["Start"] == output.loc[i, 'Start1']].to_list()[0]
			USCS.loc[newRowNumber, "targetStart"] = output["Start2"][output["Start2"] == output.loc[i, 'Start2']].to_list()[0]
			USCS.loc[newRowNumber, "targetEnd"] = output["Stop2"][output["Start2"] == output.loc[i, 'Start2']].to_list()[0]
	else: # start 1 target, start 2 bait
		USCS.loc[newRowNumber, "targetStrand"] = "-"
		USCS.loc[newRowNumber, "sourceStrand"] = "+"
		USCS.loc[newRowNumber, "targetName"] = "."
		USCS.loc[newRowNumber, "targetChrom"] = output["Chr1"][output["Start1"] == output.loc[i, 'Start1']].to_list()[0]
		USCS.loc[newRowNumber, "sourceName"] = bait["Gene"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0]
		USCS.loc[newRowNumber, "sourceChrom"] = "chr" + str(bait["Chr"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0])
		USCS.loc[newRowNumber, "sourceStart"] = bait["Start"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0]
		USCS.loc[newRowNumber, "sourceEnd"] = bait["End"][bait["Start"] == output.loc[i, 'Start2']].to_list()[0]			
		USCS.loc[newRowNumber, "targetStart"] = output["Start1"][output["Start1"] == output.loc[i, 'Start1']].to_list()[0]
		USCS.loc[newRowNumber, "targetEnd"] = output["Stop1"][output["Start1"] == output.loc[i, 'Start1']].to_list()[0]

f = open("ucsc.bed" , "w")
f.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full' + "\n")
f.close()

USCS.to_csv("ucsc.bed", sep = '\t', mode="a", index=False)


print(USCS)


# print(nonbait)
# rownames - output.index
# colnames - output.columns

# print(output)


		## 1. chrom: The chromsome of the interaction
		## 2. chromStart: The start position of the interaction (i.e. the start position of the lower of the two fragments)
		## 3. chromEnd: The end position of the interaction (i.e. the end position of the upper of the two fragments)
		## 4. name: You won't need this so you can just use a `.` to mark that it's missing
		## 5. score: An integer score (0-1000) that describes the strength of the interaction. This is set to help with visualiztion. We'll describe below how to generate this.
		## 6. value: The strength of the interaction
		## 7. ex`: You won't need this so you can just use a `.` to mark that it's missing
		## 8. color: Feel free to set a different color, but you can just use `0` to show the interactions in black
		# 9. sourceChrom: The chromosome of the bait fragment
		# 10. sourceStart: The start position of the bait fragment
		# 11. sourceEnd: The end position of the bait fragment
		# 12. sourceName: The name of the bait fragment (i.e. the name of the gene(s) for which the bait fragment is a marker)
		# 13. sourceStrand: The "strand" of the bait fragment. You don't need this, but we recommend setting it to `+` to indicate that this is a bait fragment
		# 14. targetChrom: The chromosome of the target fragment
		# 15. targetStart: The start position of the target fragment
		# 16. targetEnd: The end position of the target fragment
		# 17. targetName: The name of the target fragment. If the target fragment is *also* a bait fragment, this should be the name of the fragment, otherwise you can mark it as empty with a `.`
		# 18. targetStrand: The "strand" of the target fragment. Again, you don't need this, but we recommend setting it to `+` if the target is also a bait fragment, and `-` if it is not. It will help later on.
  
