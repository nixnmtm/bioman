#!/usr/bin/python
### needs Biopython
### extracts sequences from a fasta file (arg 1)
### whose length is sup or equal to arg 2
### and inf or equal arg3

import string
import sys
from Bio import SeqIO
from StringIO import StringIO

fastafile = sys.argv[1]
inf = int(sys.argv[2])
sup = int(sys.argv[3])

bank=[]

handle = open(fastafile)
for seq_record in SeqIO.parse(handle, "fasta"):
	bank.append(seq_record)

handle.close()

mySubset=[]

for i in bank:
	for j in req:
		if (i.id==j):
			mySubset.append(i)

out_handle = StringIO()
SeqIO.write(mySubset, out_handle, "fasta")
fasta_data = out_handle.getvalue()

print fasta_data


