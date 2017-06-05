#!/usr/bin/python

import sys
import csv

cpu_path=sys.argv[1]+"cpu_after.csv"
ram_path=sys.argv[1]+"ram_after.csv"
perc_path=sys.argv[1]+"perc.csv"

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

def gen_per(step, res_min, res_max, *list):
	result=[]
	i=res_min
	sum_=0.0
	while i<=res_max:
		result_i=[0.0]*2
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

		result_i[0]=i #/float(res_max)
		result_i[1]=total_time/len(list)
		result.append(result_i)
		i=i+step

	return result

#least squares method section

#cpu
per_cpu=gen_per(1, cpu_min+1, cpu_max, *res_cpu)
#ram
per_ram=gen_per(10, ram_min+1, ram_max, *res_ram)

#linear function
def cal_linear(*list):
	sum_xy=0.0
	sum_x=0.0
	sum_y=0.0
	sum_x2=0.0
	n=len(list)

	for item in list:
		sum_xy=sum_xy+item[0]*item[1]
		sum_x=sum_x+item[0]
		sum_y=sum_y+item[1]
		sum_x2=sum_x2+item[0]**2

	a=(n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x**2)
	b=(sum_y*sum_x2-sum_x*sum_xy)/(n*sum_x2-sum_x**2)

	result=[0.0, 0.0]
	result[0]=a
	result[1]=b

	return result

with open(perc_path, "wb") as f:
	writer = csv.writer(f)
	writer.writerows(per_cpu)

print cal_linear(*per_cpu)
print cal_linear(*per_ram)

pr_rs = cal_linear(*per_cpu)
alpha=0.0
print (0.70+alpha-pr_rs[1])/pr_rs[0]
print (0.75+alpha-pr_rs[1])/pr_rs[0]
print (0.80+alpha-pr_rs[1])/pr_rs[0]
print (0.85+alpha-pr_rs[1])/pr_rs[0]
print (0.9+alpha-pr_rs[1])/pr_rs[0]