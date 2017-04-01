#!/usr/bin/python

import sys
import random

path=sys.argv[1]+"period"

f = open(path, 'w')
f.write("%i" % (random.randint(0,14)))
f.close()