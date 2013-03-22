#!/usr/bin/env python
## working from fasta2ktable.py output to format for esom
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="""
Open a kmer tsv (arg 1) (e.g. fasta2ktable output) and format it in a <tab> seperated
U-matrix file (.umx). Moreover, it removes columns which contains 0 only and write row
names and k-mer names in separated files (.seqnames and .kmernames)
""")
parser.add_argument("ktable", help="a ktable file")
parser.add_argument("-s", "--separator", default = "\t", help="the separator to make the output table, default is <tab>")
args = parser.parse_args()

ktable = args.ktable
sep = args.separator

ktable="/home/manu/Projects/Yujie/JC_06.tetra.tsv"
kt = pd.DataFrame.from_csv(ktable, sep='\t', header=0)

## removing columns with 0 only
ktsub = kt[kt.columns[(kt != 0).any()]]

## writing rows in file
with open (ktable+".seqnames", 'w') as frows:
    for row in ktsub.index:
        frows.write(row+"\n")

## writing columns in file
with open (ktable+".kmernames", 'w') as fcols:
    for col in ktsub.columns:
        fcols.write(col+"\n")

## writing the U-matrix
ktsub.to_csv(ktable+".umx",sep=sep, header=False, index=False)


