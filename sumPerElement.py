#!/usr/bin/env python
# input file col 1 is a numerci value
# col2 is an ID 

import string
import sys


tabfile = sys.argv[1]

try:
	Hits=open(tabfile, 'r')
except IOError, e:
	print "file not found or unreadable: ",tabfile
	pass
	
bestHit=Hits.readline()
query=bestHit.split()[1]
tot=float(bestHit.split()[0])

hits = Hits.readlines()

for hit in hits:
	hitSplit=hit.split()
	if query!=hitSplit[1]:
		print query, str(tot)[:8]
		query=hitSplit[1]
		tot=float(bestHit.split()[0])
	else:
		tot=tot+float(bestHit.split()[0])
Hits.close()

