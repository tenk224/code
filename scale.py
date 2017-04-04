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

#get min and max
def get_min(*list):
	result=list[0]
	for i in range(1,15):
		if result > list[i]:
			result=list[i]

	return result

def get_max(*list):
	result=list[0]
	for i in range(1,15):
		if result < list[i]:
			result=list[i]

	return result

cpu_max=get_max(*res_cpu)
cpu_min=get_min(*res_cpu)
ram_max=get_max(*res_ram)
ram_min=get_min(*res_ram)

#calculate recommended resource
def cal_rec_res(step, res_min, res_max, *list):
	result=[0.0]*3
	i=res_min
	sum_=0.0
	while i<=res_max:
		total_res=0.0
		total_time=0.0
		p_res=0.0
		p_time=0.0
		p_sum=0.0

		for j in range(0,15):
			if(i>=list[j]):
				total_res=total_res+list[j]
				total_time=total_time+1
			else:
				total_res=total_res+i

		p_res=total_res/(15*i)
		p_time=total_time/15
		p_sum=p_res+p_time

		if (p_sum>sum_ and p_res>p_time):
			sum_=p_sum
			result[0]=i
			result[1]=p_res
			result[2]=p_time

		i=i+step

	return result

result_cpu=cal_rec_res(1, cpu_min, cpu_max, *res_cpu)
result_ram=cal_rec_res(10, ram_min, ram_max, *res_ram)

print result_cpu
print result_ram

#write recommended resource
f = open(rec_path, 'w')
f.write("%i %i" % (result_cpu[0],result_ram[0]))
f.close()