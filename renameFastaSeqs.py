#!/usr/bin/python

import sys

fastafile, prefix = sys.argv
input = open(fastafile)
output = open("".join(fastafile.split('.')[:-1]) + prefix + ".fasta", 'w')

count = 1
for line in input:
    if line.startswith('>'):
        output.write('>%s_%d\n' % (prefix, count))
        count += 1
    else:
        output.write(line)
