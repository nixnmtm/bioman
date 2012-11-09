import re

class FastRecord:
"""collection of functions intended to process fast(a/q) files
as fast as possible"""

	def __init__(self, id, description, sequence):
		self.id = id
		self.description = description
		self.sequence = sequence

	@classmethod
	def parseFastaHeader(rawFastaHeader):
		""" read a header and return id and descr """
		h = rawFastaHeader[1:].strip()
		sID = h[:h.find(" ")]
		sDEF= h[h.find(" ")+1:]
		return sID, sDEF


def fasta2dict(fastafile):
	"""
		reads a fasta file and return a dict
		in which keys are sequence IDs, and
		values are a tuple of description and
		actual sequence
	"""
	handle = open(fastafile,'r')

	seqs={}

	seq_id = handle.next()
	while (seq_id[0]!=">"):
		seq_id = handle.next()
	while True:
		try:
			seq = handle.next().strip()
			line = handle.next()
			while (line[0]!=">"):
				seq = seq+line.strip()
				line = handle.next()
			sid,sdef = parseFastaHeader(seq_id)
			seqs[sid]=sdef,seq
			seq_id = line # last loop
		except StopIteration:
			break
        # last line
	while (line[0]!=">"):
		seq = seq+line.strip()
	sid,sdef = parseFastaHeader(seq_id)
	seqs[sid]=sdef,seq

	handle.close()
	
	return seqs

def printFastaDict(fasta2dict):
	for i,j in fasta2dict.items():
		print '>' + i + ' ' + j[0] + '\n' + j[1]


def writeFastaDict(fasta2dict,outfile):
	for i,j in fasta2dict.items():
		outfile.write('>' + i + ' ' + j[0] + '\n' + j[1])

def formatseq(seq,linelength):
	"""
	Take a seq (without linebreak) and insert line breaks
	after every linelength element
	"""
        return re.sub("(.{%s})" % linelength, "\\1\n", seq, re.DOTALL)


