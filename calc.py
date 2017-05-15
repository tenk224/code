#!/usr/bin/python

import sys
import csv

cpu_path_after=sys.argv[1]+"cpu_after"
ram_path_after=sys.argv[1]+"ram_after"
cpu_path=sys.argv[1]+"cpu.csv"
ram_path=sys.argv[1]+"ram.csv"
rec_path=sys.argv[1]+"rec"

res=sys.argv[2]

#read cpu resource
res_cpu=[]
f=open(cpu_path)
for line in f.readlines():
	res_cpu.append(int(line))
f.close()


#read ram resource
res_ram=[]
f=open(ram_path)
for line in f.readlines():
	res_ram.append(int(line))
f.close()

#get min and max
def get_min(*list):
	result=list[0]
	for i in range(0,len(list)):
		if result > list[i]:
			result=list[i]

	return result

def get_max(*list):
	result=list[0]
	for i in range(0,len(list)):
		if result < list[i]:
			result=list[i]

	return result

cpu_max=get_max(*res_cpu)
cpu_min=get_min(*res_cpu)
ram_max=get_max(*res_ram)
ram_min=get_min(*res_ram)

#calculate recommended resource
def cal_res(step, res_min, res_max, *list):
	result=[0.0]*3
	i=int(res)
	sum_=0.0
	total_res=0.0
	total_time=0.0
	p_res=0.0
	p_time=0.0
	p_sum=0.0
	for j in range(0,len(list)):
		if(i>list[j]):
			total_res=total_res+list[j]
			total_time=total_time+1
		else:
			total_res=total_res+i

	p_res=total_res/(len(list)*i)
	p_time=total_time/len(list)
	p_sum=p_res+p_time

	sum_=p_sum
	result[0]=i
	result[1]=p_res
	result[2]=p_time

	i=i+step

	return result

result_cpu=cal_res(1, cpu_min+1, cpu_max, *res_cpu)
result_ram=cal_res(10, ram_min+1, ram_max, *res_ram)

print len(res_cpu)
print result_cpu
print result_ram