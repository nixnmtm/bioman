#!/usr/bin/env python
# the lines should be grouped by queries (as usual, do sort file.hmm if not)

import string
import re
import argparse
import sys

parser = argparse.ArgumentParser(description="Returns a 'Best Hits' filtered HMM tab output")
parser.add_argument("HMMERres", help="the HMMer tab output")
parser.add_argument("-c", "--column", type=int, default=14, help="default is 14, i.e. the p/ dom score")
parser.add_argument("-s", "--minscore", type=float, default=25, help="the min score required to keep the hit, default is 25")
args = parser.parse_args()

HMMERres = args.HMMERres
col = args.column - 1
minscore = float(args.minscore)

try:
	Hits=open(HMMERres, 'r')
except IOError, e:
	print "HMM output file not found or unreadable: ",HMMERres
	pass
	
bestHit=Hits.readline()
maxscore=float(bestHit.split()[col])
query=bestHit.split()[0]
hits = Hits.readlines()

for hit in hits:
	hitSplit=hit.split()
	curScore=float(hitSplit[col])
	#print minscore, maxscore, curScore
	if curScore >= minscore:
		if query!=hitSplit[0]:
			if float(bestHit.split()[col]) >= minscore :
				print bestHit,
			query=hitSplit[0]
			maxscore=float(0)
			bestHit=hit
		elif maxscore<=float(hitSplit[col]):
			bestHit=hit
			maxscore=float(hitSplit[col])
Hits.close()

