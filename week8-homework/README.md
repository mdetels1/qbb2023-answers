## Answer to 1.1 ##

Rscript runChicago.R --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text raw/PCHIC_Data/GM_rep1.chinput,raw/PCHIC_Data/GM_rep2.chinput,raw/PCHIC_Data/GM_rep3.chinput output

## Answer to 1.2 ##

Yes, they do make sense to me. Target fragments are enriched in CTCF, H3K4me1, H3K4me3, H3K27ac and H3K9me3 and not enriched in H3K27me3. CTCF is associated with interactions so it makes sense that this is associated with promoter regions. H3K4me1, H3K4me3, and H3K27ac are all associated with euchromatin states which targets should be associated with because they are probably enhancers and stuff like that. H3K9me3 makes less sense because it is constiutive heterochromatin. Finally, the fact that H3K27me3 is not enriched in target regions makes sense because promoters are not going to be bound up in heterochromatin.

## Answer to 2.2 ##
## 1 ##
1646  chr20   44438565  44565593    .      1000.0  34.77  .  black       chr20    44562442  44565593         PCIF1            +       chr20    44438565  44442365        UBE2C            +
1656  chr20   44438565  44607204    .  986.194996  34.29  .  black       chr20    44596299  44607204  FTLP1;ZNF335            +       chr20    44438565  44442365        UBE2C            +
2820  chr21   26837918  26939577    .  978.429681  34.02  .  black       chr21    26837918  26842640        snoU13            +       chr21    26926437  26939577     MIR155HG            +
1647  chr20   44452862  44565593    .  974.690825  33.89  .  black       chr20    44562442  44565593         PCIF1            +       chr20    44452862  44471524  SNX21;TNNC2            +
476   chr20   17660712  17951709    .  973.540408  33.85  .  black       chr20    17946510  17951709    MGME1;SNX5            +       chr20    17660712  17672229        RRBP1            +
578   chr20   24972345  25043735    .  973.252804  33.84  .  black       chr20    24972345  24985047         APMAP            +       chr20    25036380  25043735        ACSS1            +
## 2 ##
2843  chr21   26797667  26939577    .  952.832902  33.13  .  black       chr21    26926437  26939577            MIR155HG            +       chr21    26797667  26799364          .            -
2255  chr20   55957140  56074932    .  928.674144  32.29  .  black       chr20    55957140  55973022  RBM38;RP4-800J21.3            +       chr20    56067414  56074932          .            -
2839  chr21   26790966  26939577    .  838.941616  29.17  .  black       chr21    26926437  26939577            MIR155HG            +       chr21    26790966  26793953          .            -
232   chr20    5585992   5628028    .  830.601093  28.88  .  black       chr20     5585992   5601172              GPCPD1            +       chr20     5625693   5628028          .            -
2840  chr21   26793954  26939577    .  754.385965  26.23  .  black       chr21    26926437  26939577            MIR155HG            +       chr21    26793954  26795680          .            -
279   chr20    5515866   5933156    .  750.071901  26.08  .  black       chr20     5929472   5933156          MCM8;TRMT6            +       chr20     5515866   5523933          .            -

## Answer to Step 2.3 ##
 Does it make sense for this gene to be interacting with enhancers in GM12878? Explain

 MIR155HG - Yes it does make sense for this gene to be interacting with enhancers because GM12878 is a lymphoblastoid cell line meaning that was originally derived from lymphocytes. According to NCBI MIR155HG is a microRNA that is expressed in high levels in lymphoma and in lymph nodes, so it would make sense that they would be interacting with enhancers in the cell line to drive expression.

 GPCPD1 - This also makes sense. GPCPD is most commonly expressed in the bone marrow, which makes some sense because lymphocytes are produced in the bone marrow. Therefore, it could be possible that there is some cross over here. According to NCBI though there is also expression in lymph nodes where lymphocytes gather. Therefore this makes sense why the GM12878 would be expressing this protein.
