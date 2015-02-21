"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

def is_prime(n):
	if(n < 2):
		return False

	for x in range(2,int(sqrt(n))+1):
		if(n % x == 0):
			return False
	return True

sum = 0

for i in range(2, 2000000):
	if(is_prime(i)):
		sum += i

print(sum)
