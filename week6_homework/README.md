## Step 1.1: Compute genotype PCs ##

plink --noweb --vcf genotypes.vcf --pca 10

## Step 2.1 ##
plink --vcf genotypes.vcf --freq 

## Step 3.1 ##
plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out phenotype_gwas_results_CB1908_IC50

plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out phenotype_gwas_results_GS451_IC50

