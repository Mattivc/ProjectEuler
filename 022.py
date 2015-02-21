"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

from numpy import loadtxt
import os
import string
path = os.path.dirname(__file__)
data = loadtxt(os.path.join(path, "022_data.txt"), delimiter=',', dtype=str)

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
