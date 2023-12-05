## Answer to 1.1 ##

Rscript runChicago.R --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text raw/PCHIC_Data/GM_rep1.chinput,raw/PCHIC_Data/GM_rep2.chinput,raw/PCHIC_Data/GM_rep3.chinput output

## Answer to 1.2 ##

Yes, they do make sense to me. Target fragments are enriched in CTCF, H3K4me1, H3K4me3, H3K27ac and H3K9me3 and not enriched in H3K27me3. CTCF is associated with interactions so it makes sense that this is associated with promoter regions. H3K4me1, H3K4me3, and H3K27ac are all associated with euchromatin states which targets should be associated with because they are probably enhancers and stuff like that. H3K9me3 makes less sense because it is constiutive heterochromatin. Finally, the fact that H3K27me3 is not enriched in target regions makes sense because promoters are not going to be bound up in heterochromatin.