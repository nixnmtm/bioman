#!/usr/bin/env python
# split a HMM file into several pieces of a chosen amount of HMM models

import sys
import re
import argparse

parser = argparse.ArgumentParser(description="Screen a file (arg 1) for words in mapping file (arg2) column 1 and add after a chosen separator (default is <tab>) the text written in the other columns (or null value if nothing)")
parser.add_argument("hmmfile", help="the file that should be completed")
parser.add_argument("-n", "--nb_hmm", default=2000, help="Number of HMM per new file")
args = parser.parse_args()


hmmfile = args.hmmfile
nbhmm = args.nb_hmm

# I don't use the start re but it works
#start=re.compile(r"HMMER3\/b\ \[3\.0\ \|\ March\ 2010\]")

# I use the end instead
end=re.compile(r"//")

filenb=1
nf=0

with open(hmmfile, 'r') as modelFile:
    nbh=0
    while True:
        try:
            line = modelFile.next()
        except StopIteration:
            print filename, " written"
            print "done"
            subModelFile.close()
            break
        if nbh<=nbhmm:
            if nf!=filenb:
               filename=hmm+'.'+str(filenb)
               subModelFile = open(filename, 'w')
               nf=nf+1
            subModelFile.write(line)
            if end.match(line):
                nbh=nbh+1
        else:
            print filename, " written"
            subModelFile.close()
            filenb=filenb+1
            nbh=0

