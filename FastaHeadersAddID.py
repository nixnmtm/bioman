#!/usr/bin/python
import string
import sys
import re
import argparse

parser = argparse.ArgumentParser(description="Screen an input file (arg 1) and add from a mapping file (arg2) a value (c2) if valu in c1 is found")
parser.add_argument("infile", help="the file that should be completed")
parser.add_argument("mapfile", help="the mapping table used to add information")
parser.add_argument("-s", "--separator", default="\t", help="the seprator used to add the complement information, default is <tab>")
args = parser.parse_args()


anyfile = args.infile
ListOfIds = args.mapfile
sep = args.separator

try:
	ids=open(ListOfIds, 'r')
except IOError, e:
	print "file not found or unreadable: ",ListOfIds
	pass
	

IDs = ids.readlines()
mappingIndex={}
for couple in IDs:
	c1=couple.split()[0]
	c2=couple.split()[1:]
	# print c1,c2
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
	for mot in (re.findall(r'[\w.:]+',ligne)):
		#print mot
		if mot in mappingIndex:
			print ligne.strip() + sep + " ".join(mappingIndex[mot])
			break
	else: print ligne.strip()

handle.close()


