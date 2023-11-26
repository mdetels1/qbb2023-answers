#!/usr/bin/env python

import numpy as np
import sys
from fasta import readFASTA
import pandas as pd

file = sys.argv[1]
methodfile = sys.argv[2]
file_output = sys.argv[4]

def my_function(FASTA_file, scoring_system):
	input_sequences = readFASTA(open(FASTA_file))

	seq1_id, sequence1 = input_sequences[0]
	seq2_id, sequence2 = input_sequences[1]

	scoring = pd.read_csv(scoring_system, delim_whitespace=True)

	return seq1_id, sequence1, seq2_id, sequence2, scoring

sq1_name, sq1, sq2_name, sq2, scoring_matrix = my_function(file, methodfile)

gap_penalty = float(sys.argv[3])

#output = sys.argv[4]
#print(scoring_matrix)

F_matrix = np.zeros((len(sq1)+1, len(sq2)+1))
traceback_matrix = np.zeros((len(sq1)+1, len(sq2)+1), str)

for i in range(len(sq1)+1):
	F_matrix[i,0] = i * gap_penalty
	traceback_matrix[i,0] = "v"

for j in range(len(sq2)+1):
	F_matrix[0,j] = j * gap_penalty
	traceback_matrix[0,j] = "h"

for i in range(1, F_matrix.shape[0]):
	for j in range(1, F_matrix.shape[1]):
		d = F_matrix[i-1, j-1] + scoring_matrix.loc[sq1[i-1],sq2[j-1]]
		h = F_matrix[i, j-1] + gap_penalty
		v = F_matrix[i-1, j] + gap_penalty

		F_matrix[i,j] = max(d, h, v)
		if F_matrix[i,j] == d:
			traceback_matrix[i,j] = "d"
		elif F_matrix[i,j] == h:
			traceback_matrix[i,j] = "h"
		else:
			traceback_matrix[i,j] = "v"



alignment1 = ""
alignment2 = ""
end1 = len(sq1)
end2 = len(sq2)
gap1 = 0
gap2 = 0

while end1 != 0 or end2 != 0:
	if traceback_matrix[end1,end2] == "d":
		alignment1 = sq1[end1] + alignment1
		alignment2 = sq2[end2] + alignment2
		end1 = end1 - 1
		end2 = end2 - 1
	elif traceback_matrix[end1, end2] == "v":
		alignment1 = "_" + alignment1
		end1 = end1 - 1
		gap2 = gap2 + 1
	elif traceback_matrix[end1, end2] == "h":
		alignmenßt2 = "_" + alignment2
		end2 = end2 - 1
		gap1 = gap1 + 1
file_output = open(sys.argv[4], "w")

alignment1_output = "Sequence 1: " + alignment1
alignment2_output = "Sequence 2: " + alignment2
Gap_number1 = "Number of gaps in Sequence 1: " + str(gap1)
Gap_number2 = "Number of gaps in Sequence 2: " + str(gap2)
Alignment_Score = "Score of the alignment: " + str(F_matrix[-1,-1])

file_output.write(
	alignment1_output + "\n" +
	alignment2_output + "\n" +
	Gap_number1 + "\n" + 
	Gap_number2 + "\n" +
	Alignment_Score)
