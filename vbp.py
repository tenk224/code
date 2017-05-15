 #!/usr/bin/python

from copy import deepcopy
import sys


sub_num=int(sys.argv[1])

#var
comp_res=[]
comp_res_remain=[]
time_table=[[] for x in range(15)]
vm=[[] for x in range(15)]
allo=[[] for x in range(15)]
cpu_res=0
ram_res=0

#read compute node resource
f=open("./comp/comp_res")
for line in f.readlines():
	line_=[]
	for i in line.split():
		line_.append(i)
	comp_res.append(line_)
f.close()
comp_res_remain=deepcopy(comp_res)

#fill vm to time table
for i in range(0,sub_num):
	vm_path="./resource/s"+str(i)+"/period"
	f=open(vm_path)
	line=f.readlines()
	period_num=int(line[0])
	f.close()
	time_table[period_num].append(i)

#fill vm on the same period to list
for i in range(0,1):
	for j in range(len(time_table[i])):
		vm_temp=[]
		vm_temp.append(time_table[i][j])
		#read rec resource
		rec_res="./resource/s"+str(time_table[i][j])+"/rec"
		f=open(rec_res)
		for line in f.readlines():
			line_=[]
			for k in line.split():
				line_.append(k)
		f.close()

		vm_temp.append(int(line_[0]))
		vm_temp.append(int(line_[1]))
		vm[i].append(vm_temp)

#allocate vm
#0=compute name
#1=cpu resource
#2=ram resource
for i in range(0,1): #period in a week loop
	for k in range(len(comp_res)): #compute node loop
		fit=True
		allo[i].append([]) #add specific compute node allocation info
		allo[i][k].append(comp_res[k][0]) #compute node name
		while(fit==True and len(vm[i])>0): #fit check loop
			fit_count=0
			vm_remain=[0.0, 0.0, 0.0, 0] #vm info to be fit in compute
			vec_remain=0.0 #vector remain
			vec_vm_remain=0.0 #vector remain of current vm

			for j in range(len(vm[i])): #vm in i period loop

				#convert VMj into fraction of COMPUTEk
				vm_temp=[]
				vm_temp.append(vm[i][j][0]) #vm name
				vm_temp.append(vm[i][j][1]/float(comp_res[k][1])) #vm cpu
				vm_temp.append(vm[i][j][2]/float(comp_res[k][2])) #vm ram

				#convert remaining of COMPTEk into fraction
				comp_remain_temp=[]
				comp_remain_temp.append(comp_res_remain[k][0]) #compute name
				comp_remain_temp.append(float(comp_res_remain[k][1])/float(comp_res[k][1])) #compute cpu
				comp_remain_temp.append(float(comp_res_remain[k][2])/float(comp_res[k][2])) #compute ram
				if(float(comp_remain_temp[1])-float(vm_temp[1])<0 or float(comp_remain_temp[2])-float(vm_temp[2])<0):
					fit_count=fit_count+1
				else:
					vec_vm_remain=((float(comp_remain_temp[1])-float(vm_temp[1]))**(2)+(float(comp_remain_temp[2])-float(vm_temp[2]))**(2))**(0.5)
					if(vec_remain<vec_vm_remain):
						vec_remain=vec_vm_remain
						vm_remain[0]=vm_temp[0]
						vm_remain[1]=vm_temp[1]
						vm_remain[2]=vm_temp[2]
						vm_remain[3]=j

			if(fit_count==len(vm[i])):
				fit=False

			if(fit==True):
				#add allocation info
				allo[i][k].append(vm_remain[0])

				#calculate remaining resource
				comp_res_remain[k][1]=float(comp_res_remain[k][1])-float(vm_remain[1])*float(comp_res[k][1])
				comp_res_remain[k][2]=float(comp_res_remain[k][2])-float(vm_remain[2])*float(comp_res[k][2])

				#remove VMj
				del vm[i][vm_remain[3]]

print allo