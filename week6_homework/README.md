## Step 1.1: Compute genotype PCs ##

plink --noweb --vcf genotypes.vcf --pca 10

## Step 2.1 ##
plink --vcf genotypes.vcf --freq 

## Step 3.1 ##
plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out phenotype_gwas_results_CB1908_IC50

plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out phenotype_gwas_results_GS451_IC50

## Step 3.4 ##
CB1908 - rs10876043 DIP2B is the closest to this hit. This protein might be involved in DNA methylation. This could make sense in terms of the lymphocytopenia phenotype because it might be controlling gene expression via DNA methylation (chromatid condensation) and thus the amount of lymphocytes.
GS451 - rs7257475 ZNF826 is the closest to this hit. This gene is involved in the sequence specific binding of RNA polymerase II. So mutations that effect SNF826 would impact transcription.