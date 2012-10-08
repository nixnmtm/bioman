#!/usr/bin/python
### 

import string
import sys
from Bio import SeqIO
from StringIO import StringIO
from operator import itemgetter


fastafile = sys.argv[1]
Nseqs = sys.argv[2]

seqs={}
seqsOrd={}

handle = open(fastafile)
for seq_record in SeqIO.parse(handle, "fasta"):
	seqs[seq_record]=len(seq_record.seq)

handle.close()


seqsOrd = seqs.items()
seqsOrd.sort(key=itemgetter(1),reverse=True)

handle = open(fastafile+".ord."+Nseqs, "w")
for i in seqsOrd[0:int(Nseqs)]:
	SeqIO.write(i[0], handle, "fasta")
handle.close()

	
