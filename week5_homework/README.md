## EXERCISE 2 ##

Bash Commands:

## Exercise 2.1 ##
freebayes -f sacCer3.fa --genotype-qualities -p 1 A01_09.fastq.sam.bam A01_24.fastq.sam.bam A01_35.fastq.sam.bam A01_63.fastq.sam.bam A01_11.fastq.sam.bam A01_27.fastq.sam.bam A01_39.fastq.sam.bam A01_23.fastq.sam.bam A01_31.fastq.sam.bam A01_62.fastq.sam.bam > variants.vcf
## Exercise 2.2 ##
vcffilter -f "AF > 0.99" variants.vcf > end.vcf
## Exercise 2.3 ##
vcfallelicprimitives -k -g end.vcf > decomposed_end.vcf
## Exercise 2.4 ##
snpEff ann -v R64-1-1.105 decomposed_end.vcf > annotated_end.vcf
head -n 100 annotated_end.vcf > first100lines.vcf



