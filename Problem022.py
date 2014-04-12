from numpy import loadtxt
import os
import string
path = os.path.dirname(__file__)
data = loadtxt(os.path.join(path, "Problem022_data.txt"), delimiter=',', dtype=str)

for name in data:
	name = name.replace('"',"")

data.sort()

val = 0

def get_name_value(name):
	nameVal = 0
	for i in range(len(name)):
		nameVal += string.ascii_uppercase.find(name[i])+1
	return nameVal

for i in range(len(data)):
	name = data[i]
	val += get_name_value(name) * (i+1)

print(val)