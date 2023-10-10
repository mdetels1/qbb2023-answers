#!/usr/bin/env python

import sys

from LiveCoding import load_bedgraph, bin_array
import numpy
import scipy.stats
import matplotlib.pyplot as plt


def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, out_fname, frag_width, fwd_control, rev_control = sys.argv[1:]
    
    frag_width = int(frag_width)
    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart

    # Load the sample bedgraph data, reusing the function we already wrote
    forward = load_bedgraph(forward_fname, chrom, chromstart, chromend)
    reverse = load_bedgraph(reverse_fname, chrom, chromstart, chromend)

    # Combine tag densities, shifting by our previously found fragment width
    combined = numpy.zeros(chromlen)
    combined[frag_width // 2:] += forward[frag_width // 2:]
    combined[:-(frag_width // 2)] += combined[:-(frag_width // 2)]
    #combined = forward[frag_width // 2:] + reverse[:-(frag_width // 2)]
    #print('bbb')
    #print(combined.shape)

    # Load the control bedgraph data, reusing the function we already wrote
    cont_f = load_bedgraph(fwd_control, chrom, chromstart, chromend)
    cont_r = load_bedgraph(rev_control, chrom, chromstart, chromend)

    # Combine tag densities
    combined_control = cont_f+ cont_r

    # Adjust the control to have the same coverage as our sample
    
    combined_control = combined_control * (numpy.sum(combined)/numpy.sum(combined_control))
    #print(sum(combined_control))

    #print(combined_control.shape)
    
    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base
    binsize = 1000
    background_pos = bin_array(combined_control,binsize)/binsize
    
    #print(background_pos.shape)

    # Find the mean tags/bp and make each background 
    # position the higher of the
    # the binned score and global background score
    high_background = numpy.maximum(background_pos, numpy.mean(combined_control))

    #print(high_background.shape)

    # Score the sample using a binsize that is 
    # twice our fragment size
    # We can reuse the binning function we already wrote
    scored_sample = bin_array(combined,frag_width*2)
    #print(frag_width*2)
    #print(scored_sample.shape)

    # Find the p-value for each position (you can pass 
    # a whole array of values
    # and array of means). Use scipy.stats.poisson 
    # for the distribution.
    # Remember that we're looking for the probability of 
    # seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, 
    # while your sample is
    # per 2 * width bases. You'll need to adjust your 
    # background

    p_vals = 1 - scipy.stats.poisson.cdf(scored_sample, mu = high_background*frag_width*2)
    #print(y_poisson)


    #pmf is probability mass function, probability that this distribution will report that number
    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you don't get a divide by
    # zero error. I suggest using 1e-250

    p_vals = numpy.clip(p_vals, 1e-250, 2)
    p_vals = -(numpy.log10(p_vals))
    print(p_vals)

    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"

    write_wiggle(p_vals, chrom, chromstart, out_fname + ".wig")

    # Write bed file with non-overlapping peaks defined by high-scoring regions 

    write_bed(p_vals, chrom, chromstart, chromend, frag_width, out_fname + ".bed")

def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()


def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()