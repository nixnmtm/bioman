import re
import collections

class FastaRecord:
	"""
	collection of functions intended to process a fasta entry
	as fast as possible
	"""

	def __init__(self, header, sequence):
		self.head = header
		self.seq = sequence.upper()

	def __str__(self):
		return self.head + '\n' + self.seq
#		return "Fasta record: " + self.parseFastaHeader()[0]

	def parseFastaHeader(self):
		""" read a header and return id and descr """
		h = self.head[1:].strip()
		sID = h[:h.find(" ")]
		sDEF= h[h.find(" ")+1:]
		return sID, sDEF

	def seqLen(self):
		return len(self.seq)

	def gc(self):
		return round((100 * ((self.seq.count('G') +
					self.seq.count('C'))) /
				len(self.seq)),
				2)

	def is_nuc(self):
		pass

	
class FastqRecord:
	"""
	collection of functions intended to process a fastq entry
	as fast as possible
	"""

	def __init__(self, header, sequence, qual):
		self.head = header
		self.seq = sequence.upper()
		q = r''
		self.qual = q + qual

	def __str__(self):
		return self.head + '\n' + self.seq + '\n+\n' + self.qual

	def parseFastqHeader(self):
		""" read a header and return id and descr """
		h = self.head[1:].strip()
		sID = h[:h.find(" ")]
		sDEF= h[h.find(" ")+1:]
		return sID, sDEF

	def seqLen(self):
		return len(self.seq)

	def gc(self):
		return round((100 * ((self.seq.count('G') +
					self.seq.count('C'))) /
				len(self.seq)),
				2)

	def is_nuc(self):
		pass


class SeqCollection(collections.OrderedDict):
	"""
	collect seq entries 
	"""
	def __init__(self):
		pass	
	
	
def fasta2dict(fastafile):
	"""
	reads a fasta file and return a dict
	in which keys are sequence IDs, and
	values are a tuple of description and
	actual sequence
	"""
	handle = open(fastafile,'r')

	seqs = collections.OrderedDict()

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


def validateDNA_AA(seq, alphabet='dna'):
    """
    Check that a sequence only contains values from an alphabet

    >>> seq1 = 'acgatGAGGCATTtagcgatgcgatc'       # True for dna and protein
    >>> seq2 = 'FGFAGGAGFGAFFF'                   # False for dna, True for protein
    >>> seq3 = 'acacac '                          # should return False (a space is not a nucleotide)
    >>> validate(seq1, 'dna')
    True
    >>> validate(seq2, 'dna')
    False
    >>> validate(seq2, 'protein')
    True
    >>> validate(seq3, 'dna')
    False

    """
    alphabets = {'dna': re.compile('^[acgtn]*$', re.I), 
             'protein': re.compile('^[acdefghiklmnpqrstvwy]*$', re.I)}

    if alphabets[alphabet].search(seq) is not None:
         return True
    else:
         return False

