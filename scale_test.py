#!/usr/bin/python

import sys
import csv

cpu_path_after=sys.argv[1]+"cpu_after"
ram_path_after=sys.argv[1]+"ram_after"
cpu_path=sys.argv[1]+"cpu.csv"
ram_path=sys.argv[1]+"ram.csv"
rec_path=sys.argv[1]+"rec"

#read cpu resource
res_cpu=[]
f=open(cpu_path)
for line in f.readlines():
	if(int(line)!=0):
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
def cal_rec_res(step, res_min, res_max, *list):
	result=[0.0]*3
	i=res_min
	sub_=1.0
	while i<=res_max:
		total_res=0.0
		total_time=0.0
		p_res=0.0
		p_time=0.0
		p_sub=0.0
		for j in range(0,len(list)):
			if(i>list[j]):
				total_res=total_res+list[j]
				total_time=total_time+1
			else:
				total_res=total_res+i

		p_res=total_res/(len(list)*i)
		p_time=total_time/len(list)
		p_sub=abs(p_res-p_time)

		if (p_sub<sub_):
			sub_=p_sub
			result[0]=i
			result[1]=p_res
			result[2]=p_time

		i=i+step

	return result

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

		result_i[0]=float(i)/float(res_max)
		result_i[1]=total_time/len(list)
		result.append(result_i)
		i=i+step

	return result

result_cpu=cal_rec_res(1, cpu_min+1, cpu_max, *res_cpu)
result_ram=cal_rec_res(10, ram_min+1, ram_max, *res_ram)
# res_cpu_after=[0]*len(res_cpu)
# res_ram_after=[0]*len(res_ram)

# for i in range(0,len(res_cpu_after)):
# 	if(res_cpu[i]<=result_cpu[0]):
# 		res_cpu_after[i]=res_cpu[i]
# 	else:
# 		res_cpu_after[i]=result_cpu[0]

# f = open(cpu_path_after, 'w')
# for i in range(0,len(res_cpu_after)):
# 	f.write("%i  " % (res_cpu_after[i]))
# f.close()

# for i in range(0,len(res_ram_after)):
# 	if(res_ram[i]<=result_ram[0]):
# 		res_ram_after[i]=res_ram[i]
# 	else:
# 		res_ram_after[i]=result_ram[0]

# f = open(ram_path_after, 'w')
# for i in range(0,len(res_ram_after)):
# 	f.write("%i  " % (res_ram_after[i]))
# f.close()


# print result_cpu
# print result_ram

# #least squares method section

# #cpu
# per_cpu=gen_per(1, cpu_min+1, result_cpu[0], *res_cpu_after)
# #ram
# per_ram=gen_per(10, ram_min+1, result_ram[0], *res_ram_after)

# #linear function
# def cal_linear(*list):
# 	sum_xy=0.0
# 	sum_x=0.0
# 	sum_y=0.0
# 	sum_x2=0.0
# 	n=len(list)

# 	for item in list:
# 		sum_xy=sum_xy+item[0]*item[1]
# 		sum_x=sum_x+item[0]
# 		sum_y=sum_y+item[1]
# 		sum_x2=sum_x2+item[0]**2

# 	a=(n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x**2)
# 	b=(sum_y*sum_x2-sum_x*sum_xy)/(n*sum_x2-sum_x**2)

# 	result=[0.0, 0.0]
# 	result[0]=a
# 	result[1]=b

# 	return result


#write recommended resource

print result_cpu

f = open(rec_path, 'w')
f.write("%i %i" % (result_cpu[0],result_ram[0]))
f.close()

# with open("./perc.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(per_ram)