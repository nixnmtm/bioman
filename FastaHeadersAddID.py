#!/usr/bin/python
### in a file (arg1) add corresponding ID
### using a mapping file (arg2)

import string
import sys
import re


anyfile = sys.argv[1]
ListOfIds = sys.argv[2]

try:
	ids=open(ListOfIds, 'r')
except IOError, e:
	print "file not found or unreadable: ",ListOfIds
	pass
	

IDs = ids.readlines()
mappingIndex={}
for couple in IDs:
	c1=couple.split()[0]
	c2=couple.split()[1]
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
			print ligne.strip() +"\t"+ mappingIndex[mot]
			break
	else: print ligne.strip()

handle.close()



