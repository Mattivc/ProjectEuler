"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from math import sqrt

memo = {}

def is_prime(n):
	if n in memo:
		return memo[n]

	if(n < 2):
		memo[n] = False
		return False

	for x in range(2,int(sqrt(n))+1):
		if(n % x == 0):
			memo[n] = False
			return False
	memo[n] = True
	return True

def factorize(n):
	factors = []

	f = 2
	while is_prime(n) == False:
		if(n % f == 0):
			factors.append(f)
			n = int(n/f)
			f = 2
		f += 1

	factors.append(n)
	return factors
		

print(max(factorize(600851475143)))

