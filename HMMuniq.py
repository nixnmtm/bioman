#!/usr/bin/env python
import fileinput
import os
import re
import shutil
import argparse

parser = argparse.ArgumentParser(description="""
Copy only uniq HMM models (according to CKSUM line) from a source
folder (where model are split, i.e. 1 file => 1 model) to a
destination folder
""")
parser.add_argument("source", help="the folder of split HMMs")
parser.add_argument("destination", help="folder to copy 'dereplicated' HMM")
args = parser.parse_args()

splitHMMpath = args.source
out = args.destination

## verify / create destination folder
if os.path.isdir(out):
    if os.listdir(out):
        raise OSError('Program stopped because given path should be an empty folder')
else: os.mkdir(out)
    

# open the ID file
#with open(CKSMlist, 'r') as CKL:
#    CKLu = set(CKL.readlines())


# ls files in source
for root, dirs, files in os.walk(splitHMMpath):
    f1 = files
    r = root

# add their path
compFiles = [r+'/'+f for f in f1]

# find the good lines and copy to
# destination if found for the first time
CKSMlist = set()
CHK = re.compile('^CKSUM')
for hmmline in fileinput.input(compFiles):
    result = CHK.search(hmmline)
    if result:
        if hmmline not in CKSMlist:
            shutil.copy(fileinput.filename(),out)
            CKSMlist.add(hmmline)
	fileinput.nextfile()

fileinput.close()



