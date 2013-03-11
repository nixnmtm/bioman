#!/usr/bin/python
# output elements in list 1 than are not in list 2

import sys

f1=sys.argv[1]
f2=sys.argv[2]

l1=open(f1)
l2=open(f2)

s1=set(l1.readlines())
s2=set(l2.readlines())

l1.close()
l2.close()

s1.difference_update(s2)
for element in s1:
	print element,

#end of program

