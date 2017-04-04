#!/usr/bin/python

import sys

cpu_path=sys.argv[1]+"cpu"
ram_path=sys.argv[1]+"ram"
rec_path=sys.argv[1]+"rec"

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

def get_max(*list):
	result=list[0]
	for i in range(1,15):
		if result < list[i]:
			result=list[i]

	return result

cpu_max=get_max(*res_cpu)
ram_max=get_max(*res_ram)

#write recommended resource
f = open(rec_path, 'w')
f.write("%i %i" % (cpu_max,ram_max))
f.close()