#!/usr/bin/python

import sys

sub_num=int(sys.argv[1])

comp_res=[]
time_table=[[] for x in range(15)]

#read compute node resource
f=open("./comp/comp_res")
num_node=0
for line in f.readlines():
	line_=[]
	for i in line.split():
		line_.append(i)
	comp_res.append(line_)
	num_node=num_node+1
f.close()

#fill vm to time table

for i in range(0,sub_num):
	vm_path="./resource/s"+str(i)+"/period"
	f=open(vm_path)
	line=f.readlines()
	period_num=int(line[0])
	f.close()
	time_table[period_num].append(i)

print time_table