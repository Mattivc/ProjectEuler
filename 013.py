"""
Project Euler Problem 13
========================

Work out the first ten digits of the sum of the following one-hundred
50-digit numbers.

"""

from numpy import loadtxt
import os
path = os.path.dirname(__file__)
data = loadtxt(os.path.join(path,"013_data.txt"), delimiter=' ')

sum = 0
n = 38 # A n value of 39 is sufficient for the rigth answer with this data.
# But a n value of 38 will provide the correct 10 first digits for any set of data.

for number in data: 
      sum += int(number/10**n)

print(str(sum)[:10])
