#!/usr/bin/python

import sys
import random

path=sys.argv[1]
start=1
end=100
res=[0]*135

f = open(path, 'w')
for i in range(0,135):
	f.write("%i\n" % (random.randint(start,end)))
f.close()