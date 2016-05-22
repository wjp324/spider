#!/bin.python
#coding=utf-8
import re

## re rule
size_rule = '[0-9\.]{0,5}寸'
model_rule = '[M,A][a-zA-Z]{0,5}[0-9]{2,8}'
year_rule = '20[0-9]{2}'
cpu_rule = '[i,I][0-9]'

##util
def remove_duplicate(old):
	if len(old) > 1:
		new = []
		for i in range(0,len(old)):
			new.append(old[i].upper())
		old = list(set(new))
		return old
	if len(old) == 1:
		return old
	else:
		old.append("null")
		return old

'''
f = open("test","r")
for line in f.readlines():
	element = line.split("\t")
	size_e_0 = re.findall(r"%s"% size_rule,element[0])
	size_e_4 = re.findall(r"%s"% size_rule,element[4])
	size_e_0.extend(size_e_4)	
	size = list(set(size_e_0))
	size = remove_duplicate(size)
	
	model_e_0 = re.findall(r"%s"% model_rule,element[0])
	model_e_4 = re.findall(r"%s"% model_rule,element[4])
	model_e_0.extend(model_e_4)	
	model = list(set(model_e_0))
	model = remove_duplicate(model)

	year_e_0 = re.findall(r"%s"% year_rule,element[0])
	year_e_4 = re.findall(r"%s"% year_rule,element[4])
	year_e_0.extend(year_e_4)	
	year = list(set(year_e_0))
	year = remove_duplicate(year)

	cpu_e_0 = re.findall(r"%s"% cpu_rule,element[0])
	cpu_e_4 = re.findall(r"%s"% cpu_rule,element[4])
	cpu_e_0.extend(cpu_e_4)	
	cpu = list(set(cpu_e_0))
	cpu = remove_duplicate(cpu)

	print size[0]+"\t"+model[0]+"\t"+year[0]+"\t"+cpu[0]
'''
def parse_ori(element):
	result = []

	size_e_0 = re.findall(r"%s"% size_rule,element[0])
	size_e_4 = re.findall(r"%s"% size_rule,element[4])
	size_e_0.extend(size_e_4)	
	size = list(set(size_e_0))
	size = remove_duplicate(size)
	result.append(size[0])
	
	model_e_0 = re.findall(r"%s"% model_rule,element[0])
	model_e_4 = re.findall(r"%s"% model_rule,element[4])
	model_e_0.extend(model_e_4)	
	model = list(set(model_e_0))
	model = remove_duplicate(model)
	result.append(model[0])

	year_e_0 = re.findall(r"%s"% year_rule,element[0])
	year_e_4 = re.findall(r"%s"% year_rule,element[4])
	year_e_0.extend(year_e_4)	
	year = list(set(year_e_0))
	year = remove_duplicate(year)
	result.append(year[0])

	cpu_e_0 = re.findall(r"%s"% cpu_rule,element[0])
	cpu_e_4 = re.findall(r"%s"% cpu_rule,element[4])
	cpu_e_0.extend(cpu_e_4)	
	cpu = list(set(cpu_e_0))
	cpu = remove_duplicate(cpu)
	result.append(cpu[0])
	
	return result





