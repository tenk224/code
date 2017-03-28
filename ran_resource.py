#!/usr/bin/python

import sys
import random

path=sys.argv[1]
start=int(sys.argv[2])
end=int(sys.argv[3])
res=[0]*15

f = open(path, 'w')
for i in range(0,15):
	f.write("%i  " % (random.randint(start,end)))
f.close()