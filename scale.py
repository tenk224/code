#!/usr/bin/python

import sys

cpu_path=sys.argv[1]+"cpu"
ram_path=sys.argv[1]+"ram"

#read cpu resource
res_cpu=[]
f=open(cpu_path)
for line in f.readlines():
	for i in line.split():
		res_cpu.append(int(i))
f.close()

#read ram resource
res_ram=[]
f=open(ram_path)
for line in f.readlines():
	for i in line.split():
		res_ram.append(int(i))
f.close()

print res_cpu
print res_ram