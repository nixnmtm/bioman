#!/usr/bin/env python
# Screen a file (arg 1) for words in mapping file (arg2) column 1
# and add after a chosen separator (default is <tab>) the text written in the
# other columns (or null value if nothing).

import string
import sys
import re
import argparse

parser = argparse.ArgumentParser(description="Screen a file (arg 1) for words in mapping file (arg2) column 1 and add after a chosen separator (default is <tab>) the text written in the other columns (or null value if nothing)")
parser.add_argument("infile", help="the file that should be completed")
parser.add_argument("mapfile", help="the mapping table used to add information")
parser.add_argument("-s", "--separator", default="\t", help="the separator used to add the complement information, default is <tab>")
parser.add_argument("-s2", "--separator2", default=", ", help="the separator used to combine several complement information, default is ', '")
parser.add_argument("-mapsep", "--mapseparator", default=None, help="the separator used in the mapfile, default is whitespace and <tab>")
parser.add_argument("-n", "--null", default="NA", help="the 'null' value, default is 'NA'")
args = parser.parse_args()


anyfile = args.infile
ListOfIds = args.mapfile
sep = args.separator
sep2 = args.separator2
ms = args.mapseparator
if ms != None:
	m=ms.decode('string-escape')
else: m=ms
#print m
navalue = args.null

try:
	ids=open(ListOfIds, 'r')
except IOError, e:
	print "file not found or unreadable: ",ListOfIds
	pass
	

IDs = ids.readlines()
mappingIndex={}
for couple in IDs:
	c=couple.strip()
	c1=c.split(m)[0]
	c2=" ".join(c.split(m)[1:])
	#print c1,"||",c2
	if c1 not in mappingIndex:
		mappingIndex[c1]=c2
	elif mappingIndex[c1]==c2:
		pass
	else:
		mappingIndex[c1]=str(mappingIndex[c1]) +","+c2
		# print c1,mappingIndex[c1]


handle = open(anyfile)
lignes = handle.readlines()

for ligne in lignes:
	description = []
	#for mot in (re.findall(r'[\w.:]+',ligne)):
	for mot in re.split('[|,\t]',ligne.strip()):
	#	print mot
		if mot in mappingIndex:
			if mappingIndex[mot]:
				description.append(str(mappingIndex[mot]))
	if not description:
		description.append(navalue)
	print ligne.strip() + sep + sep2.join(description)

handle.close()



