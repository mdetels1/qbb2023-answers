#!/bin/bash

# bwa index sacCer3.fa

# for sample in *.fastq
# do
# 	echo "Aligning sample:" ${sample}
# 	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
# 		sacCer3.fa \
# 		${sample} \
# 		${sample} > ${sample}.sam
# 		#aligning the FASTQ files to the reference genome
# 		# > redirects things to save as a file instead of printing to the screen
# done

# for sam in *.sam
# do
# 	echo "Making SAM files BAM:" ${sam}
# 	samtools sort -o ${sam}.bam -O bam ${sam}
# done

for bam in *.bam
do
	echo "Indexing:" ${bam}
	samtools index ${bam} > ${bam}.bai
done

