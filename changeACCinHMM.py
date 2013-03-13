#!/usr/bin/env python
# open a HMM file, replace the line "ACC    something" with "ACC       HMMmod_iterator"
# in all files given a path
import string
import re
import argparse
import glob


parser = argparse.ArgumentParser(description="replace the line 'ACC    something' with 'ACC       prefix_iterator in all files given a path'")
parser.add_argument("path", help="the path where the hmm to modify are")
parser.add_argument("-p", "--prefix", default="hmm_", help="the prefix given to the new ACC, default is 'hmm_'")
args = parser.parse_args()


path = args.path
prefix = args.prefix

counter=0
for hmm in glob.glob(path+"/*"):
	counter=counter+1
	rpl='ACC   '+prefix+str(counter)
	with open(hmm, "r") as fhmm:
		lines = fhmm.readlines()
	with open(hmm, "w") as fhmm:
		for line in lines:
			fhmm.write(re.sub(r'ACC.*', rpl, line))
	
